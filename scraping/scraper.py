import aiohttp
import requests
from bs4 import BeautifulSoup

async def fetch_html(url, api_key=None):
    headers = {}
    if api_key:
        headers['x-api-key'] = api_key

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            return await response.text()
        
# async def scrape_similarweb_data(url):
#     html = await fetch_html(f'https://www.similarweb.com/pt/website/{url}')
#     soup = BeautifulSoup(html, 'html.parser')

#     print(soup)

#     data = {
#         'url': url,
#         'ranking': None,
#         'category': None,
#         'change_in_ranking': None,
#         'average_visit_duration': None,
#         'pages_per_visit': None,
#         'bounce_rate': None,
#         'top_countries': None,
#         'gender_distribution': None,
#         'age_distribution': None
#     }
    
#     ranking_elem = soup.find('div', class_='wa-rank-list__item wa-rank-list__item--global')
    
#     if ranking_elem:
#         data['ranking'] = ranking_elem.text.strip()
    
#     category_elem = soup.find('span', class_='category')
#     if category_elem:
#         data['category'] = category_elem.text.strip()
    
#     change_elem = soup.find('span', class_='change-in-ranking')
#     if change_elem:
#         data['change_in_ranking'] = change_elem.text.strip()
    
#     return data
    
async def scrape_similarweb_data(url):
    
    api_key = '364f1390bf3b4055b2559567c2a8ce1b'

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
