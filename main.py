import tornado.ioloop
import tornado.web
import json
import os

# Main handler
class MainHandler(tornado.web.RequestHandler):
  def set_default_headers(self):
      self.set_header("Access-Control-Allow-Origin", "*")
      self.set_header("Access-Control-Allow-Headers", "x-requested-with")
      self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

  # get food items from dictionary.json file
  def get(self):
    with open('dictionary.json') as f:
      food = json.loads(f.read())
      self.write(food)
      f.close()

# make API app with tornado
def make_app():
  return tornado.web.Application([
      (r"/", MainHandler),
  ])

if __name__ == "__main__":
  app = make_app()
  app.listen(8888)
  tornado.ioloop.IOLoop.current().start()