from aiohttp import web
from .handlers import save_info, get_info

def setup_routes(app):
  app.router.add_post('/save_info', save_info)
  app.router.add_post('/get_info', get_info)
