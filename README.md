# SRS Product Display System

A Jinja2-templated HTML display system for showcasing SRS (Stanford Research Systems) products on a 1024 x 600 px 7" tablet.

## Files Included

1. **template.html** - Jinja2 HTML template with product display layout
2. **products.csv** - Product data in CSV format
3. **generate.py** - Python script to render the template with CSV data
4. **product_display.html** - Generated HTML output (ready to use)

## Product Data Structure

The CSV file contains the following columns:

The CSV file contains the following columns:

- `product_pn` - Product part number (e.g., SR542)
- `category` - Product category for grouping and navigation
- `product_name` - Full product name (e.g., Precision Optical Chopper)
- `bullet_1` - First feature/specification
- `bullet_2` - Second feature/specification
- `bullet_3` - Third feature/specification
- `datasheet_link` - URL to product datasheet PDF
- `manual_link` - URL to product manual PDF
- `product_page_url` - URL to product page (card click destination)
- `price` - Product price (formatted as $X,XXX)
- `thumbnail` - Filename of product image (placed in images/ folder)

## Products Included

All 9 requested SRS products:

1. **DC215** - DC Voltage/Current Source
2. **CS580** - Voltage Controlled Current Source
3. **DC205** - Precision DC Voltage Source
4. **SR865A** - 4 MHz Lock-in Amplifier
5. **SR2124A** - Dual Phase Analog Lock-in Amplifier
6. **SR542** - Precision Optical Chopper
7. **LDC501** - Laser Diode Controller
8. **SR446** - 400 MHz Preamplifier
9. **SR560** - Low Noise Voltage Preamplifier

## Usage

### Option 1: Use Pre-Generated HTML
Simply open `product_display.html` in a browser on your 7" tablet.

### Option 2: Regenerate from Template

1. Edit `products.csv` to modify product data
2. Run the generation script:
   ```bash
   python3 generate.py
   ```
3. Open the newly generated `product_display.html`

## Category Navigation

The display includes a dropdown menu in the header that lets you quickly jump to any product category. Categories are automatically extracted from the CSV and products are sorted by category, then by part number.

**To add/modify categories:**
1. Edit the `category` column in `products.csv`
2. Run `generate.py` to rebuild the HTML
3. The dropdown menu and category headers update automatically

## Adding Product Images

1. Create an `images/` folder in the same directory as the HTML file
2. Place product thumbnail images in this folder
3. Update the `thumbnail` column in `products.csv` with the image filename

## Display Specifications

- **Screen Resolution**: 1024 x 600 pixels
- **Layout**: Scrollable card-based design
- **Design**: Modern dark theme with cyan accents
- **Features**:
  - **Category Navigation** - Dropdown menu to jump to product categories
  - **Automatic Sorting** - Products grouped by category
  - **Category Headers** - Visual separators between product groups
  - Clickable product cards (click anywhere to visit product page)
  - Product images (200x150px display area)
  - Product name and part number
  - Three bullet-point features
  - Direct links to datasheets and manuals (with event propagation stopping)
  - Pricing information
  - Smooth hover effects and scrolling
  - Custom scrollbar

## Customization

### Modify the Template
Edit `template.html` to change:
- Colors and styling (CSS section)
- Layout structure
- Card design
- Header/footer

### Update Product Data
Edit `products.csv` to:
- Add new products (add rows)
- Modify existing products (edit cells)
- Remove products (delete rows)

### Change Display Size
To adapt for different screen sizes, modify the CSS in `template.html`:
```css
body {
    width: 1024px;  /* Change width */
    height: 600px;  /* Change height */
}
```

## Technical Notes

- Uses Jinja2 templating for dynamic content
- No external dependencies required for viewing HTML
- Links point to actual SRS documentation URLs
- Product data scraped from thinksrs.com (February 2026)
- Prices are approximate U.S. list prices

## Browser Compatibility

Works with all modern browsers:
- Chrome/Edge
- Firefox
- Safari

Optimized for tablet display with touch-friendly spacing and hover effects.
