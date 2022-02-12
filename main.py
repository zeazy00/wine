import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

FOUNDATION_YEAR = 1920

if __name__ in "__main__":
	env = Environment(
		loader=FileSystemLoader('.'),
		autoescape=select_autoescape(['html'])
	)
	template = env.get_template('template.html')

	rendered_page = template.render(
		working_years=datetime.datetime.now().year - FOUNDATION_YEAR
	)
	template = env.get_template('template.html')

	with open('index.html', 'w', encoding="utf8") as file:
		file.write(rendered_page)
	
	server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
	server.serve_forever()