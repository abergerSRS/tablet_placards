#!/usr/bin/env python3
"""
SRS Product Display Generator
Renders HTML from Jinja2 template using CSV product data
"""

import csv
from jinja2 import Template

def load_products(csv_file):
    """Load product data from CSV file"""
    products = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append(row)
    return products

def render_template(template_file, products):
    """Render Jinja2 template with product data"""
    with open(template_file, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    template = Template(template_content)
    return template.render(products=products)

def main():
    # Load product data from CSV
    products = load_products('products.csv')
    
    # Render template
    html_output = render_template('template.html', products)
    
    # Write output HTML
    with open('product_display.html', 'w', encoding='utf-8') as f:
        f.write(html_output)
    
    print(f"Generated product_display.html with {len(products)} products")
    print("\nProducts included:")
    for product in products:
        print(f"  - {product['product_pn']}: {product['product_name']}")

if __name__ == '__main__':
    main()
