# Crypto Scraper 💰

This project is a Django-based API that scrapes cryptocurrency data from [CoinMarketCap](https://coinmarketcap.com/). The API is built using Django REST framework, Celery, Requests, and Selenium.

## Project Structure 📁

- **Project Name**: crypto_scraper
- **App Name**: api

## Features 🚀

- **Start Scraping API**: Accepts a list of cryptocurrency acronyms, initiates the scraping process, and returns a job ID.
- **Scraping Status API**: Returns the current status and results of the scraping job using the job ID.

## Prerequisites 🛠️

- Python 3.9+
- Django
- Django REST framework
- Celery
- Redis (for Celery message broker)
- Requests
- Selenium
- WebDriver (e.g., ChromeDriver for Selenium)

## Installation 🧰

1. **Clone the Repository**:

   `git clone https://github.com/yourusername/crypto_scraper.git`

3. **Create and Activate a Virtual Environment**:

   `python3 -m venv myenv`
   
    `source myenv/bin/activate`    

5. **Install Dependencies**:

   `pip install -r requirements.txt`
    

7. **Set Up Django**:

   `python manage.py migrate`
   
    `python manage.py createsuperuser`

   `python manage.py runserver`
    

9. **Set Up Celery**:

    Ensure you have Redis running locally. Start the Celery worker:
    
    `celery -A crypto_scraper worker --loglevel=info`
    

## Usage 🚀

### Start Scraping API

- **Endpoint**: /api/taskmanager/start_scraping/
- **Method**: POST
- **Payload**:
  ```json
  {
      "coins": ["DUKO", "NOT", "GORILLA"]
  }
  ```

- **Response**:
  ```json
  {
      "job_id": "<-UUID->"
  }
  ```

### Scraping Status API

- **Endpoint**: /api/taskmanager/scraping_status/<job_id>/
- **Method**: GET
- **Response**:
  ```json
  {
    "job_id": "bbf766fc-ad64-4075-8c09-5c4c837ac44a",
    "tasks": [
     {
       "coin": "DUKO",
       "output": {
         "price": "0.005593",
         "price_change": "39.20",
         "market_cap": "54231818",
         "market_cap_rank": "635",
         "volume": "23758115",
         "volume_rank": "225",
         "volume_change": "43.81",
         "circulating_supply": "9663955990",
         "total_supply": "9999609598",
         "diluted_market_cap": "56115426",
         "contracts": [
           {
             "name": "solana",
             "address": "HLptm5e6rTgh4EKgDpYFrnRHbjpkMyVdEeREEa2G7rf9"
           }
         ],
         "official_links": [
           {
             "name": "website",
             "link": "https://dukocoin.com/"
           }
         ],
         "socials": [
           {
             "name": "twitter",
             "url": "https://twitter.com/dukocoin"
           },
           {
             "name": "telegram",
             "url": "https://t.me/+jlScZmFrQ8g2MDg8"
           }
         ]
       }
     },
     ...
    ]
  }
  ```

## How It Works 🔧

### Video Demonstration

A live demonstration video showing the scraping process is given below. This video walks through how the scraping is performed using Selenium.

[Screencast from 2024-06-07 17-26-44.webm](https://github.com/meet244/Crypto_Scraper/assets/83262693/8dd17af6-44a4-4b22-b4a5-014437ab3a1f)

### Screenshots 📸

#### Admin Panel

1. **Admin Dashboard**:
   ![Screenshot from 2024-06-07 18-00-33](https://github.com/meet244/Crypto_Scraper/assets/83262693/b1eda9df-af51-43f3-b8af-89e09ba80080)
   ![Screenshot from 2024-06-07 17-24-51](https://github.com/meet244/Crypto_Scraper/assets/83262693/0c4097dd-06f3-4be7-ba26-d352401485a1)

3. **Task List**:
   ![Screenshot from 2024-06-07 18-00-48](https://github.com/meet244/Crypto_Scraper/assets/83262693/c3b7fc52-a0f4-42a6-89bf-9c0d069e4ab1)

#### Postman Requests

1. **Start Scraping API Call**:
    ![Screenshot from 2024-06-07 17-20-28](https://github.com/meet244/Crypto_Scraper/assets/83262693/5f8e64b4-c7aa-4004-82aa-9df4839c15ee)

2. **Scraping Status API Call**:
   ![Screenshot from 2024-06-07 17-21-33](https://github.com/meet244/Crypto_Scraper/assets/83262693/c7e50ecb-9076-4110-9c91-bdbc752f6503)

## Implementation Details 📝

### Celery Tasks

- **Start Scraping Task**: Enqueues the scraping job for the provided list of coins.
- **Scraping Task**: Scrapes data for each coin in parallel and updates the task status.

## Running the Project 🏃‍♂️

1. **Run Django Server**:
    
    `python manage.py runserver`
    

2. **Run Celery Worker**:
    
    `celery -A crypto_scraper worker --loglevel=info`
    

Now, you can use Postman or any other API client to test the APIs.

## Conclusion 🎉

This project demonstrates the use of Django, Django REST framework, Celery, Requests, and Selenium to create a scalable web scraping API. The provided video and screenshots should help you understand the implementation and functionality of the project.
