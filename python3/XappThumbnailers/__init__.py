import argparse
import os
import PIL.Image
import PIL.ImageOps
import sys
from io import BytesIO

import gi
gi.require_version('GdkPixbuf', '2.0') 
from gi.repository import GdkPixbuf

class Thumbnailer():

    def __init__(self):
        # Parse arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--input', type=str, required=True)
        parser.add_argument('-o', '--output', type=str, required=True)
        parser.add_argument('-s', '--size', type=int, required=True)
        self.args = parser.parse_args()

        if not os.path.exists(self.args.input):
            print("File not found ", self.args.input)
            sys.exit(1)

    def save_path(self, path):
        if path.endswith(".svg"):
            img = self.svg_to_image(path)
        else:
            try:
                img = PIL.Image.open(path)
            except (PIL.UnidentifiedImageError, FileNotFoundError) as e:
                print("PIL ERROR: ", e)

        if img:
            self.save_pil(img)
            return True

        return False

    def save_bytes(self, data):
        img = PIL.Image.open(BytesIO(data))
        self.save_pil(img)

    def save_pil(self, img):
        # Resize image
        width, height = img.size
        if height >= width:
            percent = self.args.size / float(height)
            wsize = int((float(width) * float(percent)))
            img = img.resize((wsize, self.args.size), PIL.Image.ANTIALIAS)
        else:
            percent = self.args.size / float(width)
            hsize = int((float(height) * float(percent)))
            img = img.resize((self.args.size, hsize), PIL.Image.ANTIALIAS)
        # Rotate image according to its EXIF rotation tag
        try:
            img = PIL.ImageOps.exif_transpose(img)
        except Exception as e:
            print(e)
        img.save(self.args.output, "PNG")

    def svg_to_image(self, path):
        try:
            pixbuf = GdkPixbuf.Pixbuf.new_from_file(path)

            data = pixbuf.get_pixels()

            w = pixbuf.get_width()
            h = pixbuf.get_height()
            stride = pixbuf.get_rowstride()

            mode = "RGB"
            if pixbuf.get_has_alpha():
                mode = "RGBA"

            image = PIL.Image.frombytes(mode, (w, h), data, "raw", mode, stride)
            return image
        except Exception as e:
            print("SVG Error:", e)
