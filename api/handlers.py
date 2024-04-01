from aiohttp import web
from scraping.scraper import scrape_similarweb_data, scrape_similarweb_top_rank, scrape_similarweb_general_data_pro
from database.mongodb import save_to_mongodb, get_from_mongodb, get_rank_from_mongodb

async def save_info(request):
  data = await request.json()
  url = data.get('url')
  if not url:
    return web.json_response({'error': 'URL not provided'}, status=400)

  scraped_data = await scrape_similarweb_data(url)
  await save_to_mongodb(scraped_data)

  return web.json_response({'id': str(scraped_data['_id'])}, status=201)

async def save_rank(request):
  scraped_data = await scrape_similarweb_top_rank()
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
    
    return web.json_response(result, status=200, content_type='application/json')

async def get_info_rank(request):
    result = await get_rank_from_mongodb()
    
    if not result:
        return web.json_response({'error': 'Data not found'}, status=404)
    
    return web.json_response(result, status=200, content_type='application/json')

# SIMILARWEB PRO

async def save_info_pro(request):
  data = await request.json()
  url = data.get('url')
  if not url:
    return web.json_response({'error': 'URL not provided'}, status=400)

  scraped_data = await scrape_similarweb_general_data_pro(url)
  await save_to_mongodb(scraped_data)

  return web.json_response({'id': str(scraped_data['_id'])}, status=201)

async def get_info_pro(request):
    data = await request.json()
    url = data.get('url')
    if not url:
        return web.json_response({'error': 'URL not provided'}, status=400)
    
    result = await get_from_mongodb(url)
    
    if not result:
        return web.json_response({'error': 'Data not found'}, status=404)
    
    return web.json_response(result, status=200, content_type='application/json')
 