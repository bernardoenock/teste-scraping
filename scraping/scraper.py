import os
import requests
import aiohttp
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

async def scrape_similarweb_data(url):
    api_key = API_KEY
    api_url = f"https://api.similarweb.com/v1/similar-rank/{url}/rank?api_key={api_key}"

    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status == 200:
                data = await response.json()
                if isinstance(data, dict):
                    return data
                else:
                    print("Resposta da API do SimilarWeb não está no formato esperado.")
                    return None
            else:
                print("Erro ao solicitar dados do SimilarWeb:", response.status)
                print(response)
                return None


async def scrape_similarweb_top_rank():
    api_key = API_KEY
    api_url = f"https://api.similarweb.com/v1/similar-rank/top-sites?api_key={api_key}&limit={50}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status == 200:
                data = await response.json()
                if isinstance(data, dict):
                    return data
                else:
                    print("Resposta da API do SimilarWeb não está no formato esperado.")
                    return None
            else:
                print("Erro ao solicitar dados do SimilarWeb:", response.status)
                print(response)
                return None
            

# SIMILARWEB PRO

async def scrape_similarweb_general_data_pro(url):
    api_key = API_KEY
    api_url = f"https://api.similarweb.com/v1/website/{url}/general-data/all?api_key={api_key}&format=json"

    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status == 200:
                data = await response.json()
                if isinstance(data, dict):
                    return data
                else:
                    print("Resposta da API do SimilarWeb não está no formato esperado.")
                    return None
            else:
                print("Erro ao solicitar dados do SimilarWeb:", response.status)
                print(response)
                return None

async def scrape_similarweb_traffic_and_engagement_pro(url):
    
    api_key = API_KEY

    api_url = "https://api.similarweb.com/v3/batch/traffic_and_engagement/request-report"

    payload = {
        "metrics": ["all_traffic_visits", "global_rank", "desktop_new_visitors", "mobile_average_visit_duration"],
        "filters": {
            "domains": [url],
            "countries": ["WW"],
            "include_subdomains": True
        },
        "granularity": "monthly",
        "start_date": "2022-06",
        "end_date": "2023-06",
        "response_format": "csv",
        "delivery_method": "download_link"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "api-key": api_key
    }
    
    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Erro ao solicitar dados do SimilarWeb:", response.text)
        return None
