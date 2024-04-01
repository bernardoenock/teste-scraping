from aiohttp import web
from .handlers import save_info, get_info, save_rank, get_info_rank, save_info_pro, get_info_pro

def setup_routes(app):
  app.router.add_post('/save_info', save_info)
  app.router.add_get('/get_info', get_info)
  app.router.add_post('/save_rank', save_rank)
  app.router.add_get('/get_info_rank', get_info_rank)
  app.router.add_post('/ save_info_pro',  save_info_pro)
  app.router.add_get('/get_info_pro', get_info_pro)
