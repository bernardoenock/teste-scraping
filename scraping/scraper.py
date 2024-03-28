import aiohttp
from bs4 import BeautifulSoup

async def fetch_html(url):
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
      return await response.text()
    
async def scrape_similarweb_data(url):
  html = await fetch_html(f'https://www.similarweb.com/website/{url}')
  soup = BeautifulSoup(html, 'html.parser')

  data = {}

  data['url'] = url
  data['ranking'] = soup.find('span', class_='ranking').text.strip() if soup.find('span', class_='ranking') else None


  return data
