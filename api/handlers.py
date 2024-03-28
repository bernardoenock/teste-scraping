from aiohttp import web
from bson import ObjectId
from scraping.scraper import scrape_similarweb_data
from database.mongodb import save_to_mongodb, get_from_mongodb

async def save_info(request):
  data = await request.json()
  url = data.get('url')
  if not url:
    return web.json_response({'error': 'URL not provided'}, status=400)

  scraped_data = await scrape_similarweb_data(url)
  await save_to_mongodb(scraped_data)

  return web.json_response({'id': str(scraped_data['_id'])}, status=201)

async def get_info(request):
    data = await request.json()
    url = data.get('url')
    if not url:
        return web.json_response({'error': 'URL not provided'}, status=400)
    
    result = await get_from_mongodb(url)
    
    if not result:
        return web.json_response({'error': 'Data not found'}, status=404)
    
    if '_id' in result:
        result['_id'] = str(result['_id'])
    
    return web.json_response(result, status=200)
 