#!/usr/bin/python3

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

    sequence = 1
    for pbi in photo_block_items:
        url = "http://ondonnedesnouvelles.com/" + pbi.attrib['href']

        # Get the basename of the HTML file, aka the date with format YYYYMMDD
        yyyymmdd = os.path.splitext(os.path.basename(html))[0]

        # Construct the photo file name keeping the original extension
        filename = "photos/" + yyyymmdd + "_" + str(sequence).zfill(4) + os.path.splitext(os.path.basename(url))[1]

        print("Saving:     " + url + " as " + filename)
        photo = requests.get(url)
        with open(filename, 'wb') as handler:
            handler.write(photo.content)

        sequence += 1