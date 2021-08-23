#!/usr/bin/env python3

import os
from PIL import Image

directory = "/supplier-data/images"

for filename in os.listdir(directory):
    if filename.endswith(".tiff"):
        img = Image.open(os.path.join(directory, filename))
        rgb_img = img.convert("RGB").resize((600,400))
        rgb_img.save(directory+filename, "JPEG")
