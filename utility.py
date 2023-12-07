from bs4 import BeautifulSoup, SoupStrainer
from pathlib import Path

# Find unused images

extensions = {'.png', '.gif', '.jpg'}

excluded_images = [
    "android-chrome-192x192.png",
    "android-chrome-512x512.png",
    "apple-touch-icon.png",
    "favicon-16x16.png",
    "favicon-32x32.png"
]


image_links = set()
# Get all of the HTML files from the _site folder
for path in Path('./_site/').rglob('*.html'):
    # Read the data from the file
    data = Path(path).read_text()
    # Parse the HTML
    soup = BeautifulSoup(data, features="html.parser")
    # Get all of the IMG tags
    for link in soup.find_all('img'):
        # Get the IMG Source
        image_link = link.get('src')
        # If it starts with assets
        if image_link.startswith("/assets/"):
            print(f'Image link: {image_link}')
            print(f'Exists: {Path("." + image_link).is_file()}') 
            image_links.add(image_link.replace("/assets/",""))

# Get all of the files in Assets
for path in Path('./assets/').rglob('*.*'):
    # Limit to image files
    if path.suffix in extensions:
        filename = str(path).replace("assets/","")
        if filename not in image_links and filename not in excluded_images:
            print(f"Image: {filename} is not used")