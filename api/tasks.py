from celery import shared_task
from .models import Task
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@shared_task
def scrape_coin_data(task_id, coins):
    """
    Scrape coin data for the given list of coins.

    Args:
        task_id (int): The ID of the task.
        coins (list): List of coins to scrape data for.

    Returns:
        dict: Dictionary containing the results of the scraping task.
    """
    task = Task.objects.get(pk=task_id)
    task.status = 'IN_PROGRESS'

    task.save()

    try:
        # Call the scrape_data function to scrape coin data
        scraped = scrape_data(coins)
    except Exception as e:
        # If an exception occurs, update the task status to 'FAILED' and save the error message
        task.status = 'FAILED'
        task.result = {'error': str(e)}
        task.save()
        return {'error': str(e)}
    
    results = {'job_id': str(task_id), 'tasks': [scraped]}

    task.status = 'COMPLETED'
    task.result = results
    task.save()
    return results

def scrape_data(coins):
    """
    Scrapes coin data from a website using Selenium.

    Args:
        coins (list): List of coins to scrape data for.

    Returns:
        list: List of dictionaries containing scraped data for each coin.
    """
    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 5) # Wait for 5 secs for elements to load
    driver.get("https://coinmarketcap.com/currencies/duko/")
    time.sleep(3)

    results = []

    for coin in coins:
        output = {}
        coin_data = {"coin": coin, "output": output}
        
        # Click on the search bar
        search = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div[2]/section/div/nav/div/div[2]/div[1]")))
        time.sleep(1)
        search.click()
        time.sleep(2)

        # Enter the coin name in the search bar
        inp = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div[2]/section/div/div[3]/div/div[1]/div[1]/div[2]/input")))
        inp.send_keys(coin)
        time.sleep(1)
        
        # Click on the first search result
        first_href_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div[2]/section/div/div[3]/div/div[2]/div[2]/div[1]/a")))
        driver.get(first_href_element.get_attribute("href"))
        
        # Scrape price
        price_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/section/div/div[2]/span")))
        price = price_element.text.replace('$', '').strip()
        output["price"] = price
        
        # Scrape price change
        price_change_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/section/div/div[2]/div/div/p")
        price_change = price_change_element.text.split('%')[0].strip()
        output["price_change"] = price_change
        
        # Scrape market cap
        market_cap_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[1]/div[1]/dd")
        market_cap = market_cap_element.text.rsplit('$',1)[1].replace(',','').strip()
        output["market_cap"] = market_cap
        
        # Scrape market cap rank
        market_cap_rank_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[1]/div[2]/div/span")
        market_cap_rank = market_cap_rank_element.text.replace('#', '').strip()
        output["market_cap_rank"] = market_cap_rank
        
        # Scrape volume
        volume_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[2]/div[1]/dd")
        volume = volume_element.text.rsplit('$',1)[1].replace(',','').strip()
        output["volume"] = volume
        
        # Scrape volume rank
        volume_rank_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[2]/div[2]/div/span")
        volume_rank = volume_rank_element.text.replace('#', '').strip()
        output["volume_rank"] = volume_rank
        
        # Scrape volume change
        volume_change_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[3]/div/dd")
        volume_change = volume_change_element.text.split('%')[0].strip()
        output["volume_change"] = volume_change
        
        # Scrape circulating supply
        circulating_supply_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[4]/div/dd")
        circulating_supply = circulating_supply_element.text.split('\n')[0].split(' ')[0].replace(',','').strip()
        output["circulating_supply"] = circulating_supply
        
        # Scrape total supply
        total_supply_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[5]/div/dd")
        total_supply = total_supply_element.text.split('\n')[0].split(' ')[0].replace(',','').strip()
        output["total_supply"] = total_supply
        
        # Scrape diluted market cap
        diluted_market_cap_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[7]/div/dd")
        diluted_market_cap = diluted_market_cap_element.text.replace('$', '').replace(',','').strip()
        output["diluted_market_cap"] = diluted_market_cap
        
        # Scrape contracts
        contracts_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[1]/div[2]/div")
        contracts = contracts_element.find_elements(By.XPATH, "./*")
        contract_list = []
        for contract in contracts:
            contract_name = contract.find_element(By.CLASS_NAME, "chain-name").text.split(':')[0].lower().strip()
            contract_link = contract.find_element(By.CLASS_NAME, "chain-name").get_attribute("href").rsplit('/', 1)[1]
            contract_list.append({"name": contract_name, "address": contract_link})
        
        output["contracts"] = contract_list
        
        # Scrape official links
        official_links_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[2]/div[2]/div")
        official_links = official_links_element.find_elements(By.XPATH, "./*")
        official_links_list = []
        for link in official_links:
            link_name = link.find_element(By.XPATH, ".//a").text.lower().strip()
            link_url = link.find_element(By.XPATH, ".//a").get_attribute("href")
            official_links_list.append({"name": link_name, "link": link_url})
        
        output["official_links"] = official_links_list
        
        # Scrape social links
        social_links_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[3]/div[2]/div")
        social_links = social_links_element.find_elements(By.XPATH, "./*")
        social_links_list = []
        for link in social_links:
            link_name = link.find_element(By.XPATH, ".//a").text
            if "\n" in link_name:
                link_name = link_name.split("\n")[1]
            link_name = link_name.lower().strip()
            link_url = link.find_element(By.XPATH, ".//a").get_attribute("href")
            social_links_list.append({"name": link_name, "url": link_url})
        
        output["socials"] = social_links_list
        results.append(coin_data)

    driver.quit()
    return results
