from bs4 import BeautifulSoup, SoupStrainer
from pathlib import Path

# Find unused images

image_links = set()
for path in Path('./_site/').rglob('*.html'):
    data = Path(path).read_text()
    soup = BeautifulSoup(data, features="html.parser")
    for link in soup.find_all('img'):
        image_link = link.get('src')
        if image_link.startswith("/assets/"):
            image_links.add(image_link.replace("/assets/",""))

extensions = {'.png', '.gif', '.jpg'}
for path in Path('./assets/').rglob('*.*'):
    if path.suffix in extensions:
        filename = path.name.replace("assets/","")
        if filename not in image_links:
            print(f"Image {filename} is not used")