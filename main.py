from lxml import etree, html
import requests
import os

path = "html"

html_files = []
for root, directories, files in os.walk(path):
    for file in files:
        if '.html' in file:
            html_files.append(os.path.join(root, file))

for html in html_files:
    print("Processing: " + html)
    parser = etree.HTMLParser()
    tree = etree.parse(html, parser)
    photo_block_items = tree.xpath("""/html/body/div[3]/div/div[2]/div/a""")

    for pbi in photo_block_items:
        url = "http://ondonnedesnouvelles.com/" + pbi.attrib['href']
        basename = os.path.basename(url)
        yyyymmdd = os.path.splitext(os.path.basename(html))[0]
        filename = "photos/" + yyyymmdd + "-" + basename
        print("Saving:     " + url + " as " + filename)
        photo = requests.get(url)
        open(filename, 'wb').write(photo.content)
