
# Crypto Scraper

This project is a Django-based API that scrapes cryptocurrency data from [CoinMarketCap](https://coinmarketcap.com/). The API is built using Django REST framework, Celery, Requests, and Selenium.

## Project Structure

- *Project Name*: crypto_scraper
- *App Name*: api

## Features

- *Start Scraping API*: Accepts a list of cryptocurrency acronyms, initiates the scraping process, and returns a job ID.
- *Scraping Status API*: Returns the current status and results of the scraping job using the job ID.

## Prerequisites

- Python 3.9+
- Django
- Django REST framework
- Celery
- Redis (for Celery message broker)
- Requests
- Selenium
- WebDriver (e.g., ChromeDriver for Selenium)

## Installation

1. *Clone the Repository*:

   `git clone https://github.com/yourusername/crypto_scraper.git`

3. *Create and Activate a Virtual Environment*:

   `python3 -m venv myenv`
   
    `source myenv/bin/activate`    

5. *Install Dependencies*:

   `pip install -r requirements.txt`
    

7. *Set Up Django*:

   `python manage.py migrate`
   
    `python manage.py createsuperuser`

   `python manage.py runserver`
    

9. *Set Up Celery*:

    Ensure you have Redis running locally. Start the Celery worker:
    
    `celery -A crypto_scraper worker --loglevel=info`
    

## Usage

### Start Scraping API

*Endpoint*: /api/taskmanager/start_scraping/

*Method*: POST

*Payload*:
json
{
    "coins": ["DUKO", "NOT", "GORILLA"]
}


*Response*:
json
{
    "job_id": "<-UUID->"
}


### Scraping Status API

*Endpoint*: /api/taskmanager/scraping_status/<job_id>/

*Method*: GET

*Response*:
json
{
  "job_id": "<UUID>",
  "tasks": [
    {
      "coin": "DUKO",
      "output": {
        "price": 0.003913,
        "price_change": -5.44,
        "market_cap": 37814377,
        "market_cap_rank": 740,
        "volume": 4583151,
        "volume_rank": 627,
        "volume_change": 12.21,
        "circulating_supply": 9663955990,
        "total_supply": 9999609598,
        "diluted_market_cap": 39127766,
        "contracts": [
          {
            "name": "solana",
            "address": "HLptm5e6rTgh4EKgDpYFrnRHbjpkMyVdEeREEa2G7rf9"
          }
        ],
        "official_links": [
          {
            "name": "website",
            "link": "https://dukocoin.com"
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


## How It Works

### Video Demonstration

A live demonstration video showing the scraping process is given below. This video walks through how the scraping is performed using Selenium.

### Screenshots

#### Admin Panel
1. *Admin Dashboard*:
    ![Admin Dashboard](screenshots/admin_dashboard.png)
   
2. *Task List*:
    ![Task List](screenshots/task_list.png)

#### Postman Requests
1. *Start Scraping API Call*:
    ![Start Scraping](screenshots/start_scraping_postman.png)
   
2. *Scraping Status API Call*:
    ![Scraping Status](screenshots/scraping_status_postman.png)

## Implementation Details

### Celery Tasks

- *Start Scraping Task*: Enqueues the scraping job for the provided list of coins.
- *Scraping Task*: Scrapes data for each coin in parallel and updates the task status.

## Running the Project

1. *Run Django Server*:
    
    `python manage.py runserver`
    

2. *Run Celery Worker*:
    
    `celery -A crypto_scraper worker --loglevel=info`
    

Now, you can use Postman or any other API client to test the APIs.

## Conclusion

This project demonstrates the use of Django, Django REST framework, Celery, Requests, and Selenium to create a scalable web scraping API. The provided video and screenshots should help you understand the implementation and functionality of the project.