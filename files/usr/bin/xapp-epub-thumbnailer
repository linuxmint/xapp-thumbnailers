#!/usr/bin/python3

import os
import sys
import zipfile
from xml.dom import minidom

import XappThumbnailers
thumbnailer = XappThumbnailers.Thumbnailer()

archive = zipfile.ZipFile(thumbnailer.args.input)

# Read the container to find the path of the root file
container = minidom.parseString(archive.open("META-INF/container.xml").read())
root_path = container.getElementsByTagName("rootfile")[0].getAttribute("full-path")

# Parse the root file...
root_file = minidom.parseString(archive.open(root_path).read())

# Find the cover ID if there is one..
cover_id = None
for meta in root_file.getElementsByTagName("meta"):
    if meta.getAttribute("name") == "cover":
        cover_id = meta.getAttribute("content")
        break

# Look for the cover matching the ID, or any item which properties
# is "cover-image"
manifest = root_file.getElementsByTagName("manifest")[0]
cover_path = None
for item in manifest.getElementsByTagName("item"):
    item_id = item.getAttribute("id")
    if cover_id != None and item_id == cover_id:
        cover_path = item.getAttribute("href")
        break
    elif item.getAttribute("properties") == "cover-image":
        cover_path = item.getAttribute("href")
        break

if cover_path != None:
    cover_path = os.path.join(os.path.dirname(root_path), cover_path)
    cover = archive.open(cover_path)
    thumbnailer.save_bytes(cover.read())
    sys.exit(0)

sys.exit(1)
