import tornado.ioloop
import tornado.web
import json
import os

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    with open('dictionary.json') as f:
      food = json.loads(f.read())
      self.write(food)
      f.close()

def make_app():
  return tornado.web.Application([
      (r"/", MainHandler),
  ])

if __name__ == "__main__":
  app = make_app()
  app.listen(8888)
  tornado.ioloop.IOLoop.current().start()