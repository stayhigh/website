import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write('Hello, WebApp World!')


app = webapp2.WSGIApplication([('/', MainPage)])

""" Old code:
def main():
  run_wsgi_app(app)

if __name__ == '__main__':
  main()
"""
