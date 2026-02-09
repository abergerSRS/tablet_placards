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
    
    # Try different encodings
    encodings_to_try = ['utf-8-sig', 'utf-8', 'latin-1', 'cp1252']
    
    for encoding in encodings_to_try:
        try:
            with open(csv_file, 'r', encoding=encoding) as f:
                reader = csv.DictReader(f)
                products = list(reader)
                
                if products:
                    # Show what columns we found
                    print(f"Successfully read CSV with {encoding} encoding")
                    print(f"Found columns: {list(products[0].keys())}")
                    return products
        except Exception as e:
            continue
    
    raise Exception(f"Could not read CSV file with any standard encoding")

def render_template(template_file, products, categories):
    """Render Jinja2 template with product data"""
    with open(template_file, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    template = Template(template_content)
    return template.render(products=products, categories=categories)

def main():
    # Load product data from CSV
    try:
        products = load_products('products.csv')
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return
    
    # Sort products by category, then by product_pn
    products.sort(key=lambda x: (x.get('category', ''), x.get('product_pn', '')))
    
    # Extract unique categories in order
    categories = []
    seen = set()
    for product in products:
        cat = product.get('category', '')
        if cat and cat not in seen:
            categories.append(cat)
            seen.add(cat)
    
    # Render template
    html_output = render_template('template.html', products, categories)
    
    # Write output HTML
    with open('product_display.html', 'w', encoding='utf-8') as f:
        f.write(html_output)
    
    print(f"\nGenerated product_display.html with {len(products)} products")
    print(f"Categories: {', '.join(categories)}")
    print("\nProducts included:")
    for product in products:
        print(f"  - {product['product_pn']}: {product['product_name']} ({product.get('category', 'N/A')})")

if __name__ == '__main__':
    main()
