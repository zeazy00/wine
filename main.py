import argparse
import datetime
import collections
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape

FOUNDATION_YEAR = 1920

if __name__ in "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--path",
        help="Specifying the path for the product file")
    args = parser.parse_args(default="wine.xlsx")

    products = pandas.read_excel(
        file_path,
        sheet_name='Лист1',
        na_values=['N/A', 'NA'], 
        keep_default_na=False).to_dict(orient='records')
    sorted_products = collections.defaultdict(list)
    for product in products:
        sorted_products[product['Категория']].append(product)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    
    template = env.get_template('template.html')
    rendered_page = template.render(
        age=datetime.datetime.now().year - FOUNDATION_YEAR,
        products=sorted_products
    )
    template = env.get_template('template.html')

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()