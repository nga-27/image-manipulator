import numpy as np
# from skimage import data
import matplotlib.pyplot as plt 
import base64

import base64
from io import BytesIO
from PIL import Image

with open("input/Scan.jpeg", "rb") as f:
    encoded_string = base64.b64encode(f.read())

print(encoded_string)
print(int(encoded_string[2]))

int_data = [int(val) for val in encoded_string]
filtered = [0] * len(int_data)

for i, val in enumerate(int_data):
    if val < 100:
        filtered[i] = 0
    else:
        filtered[i] = 255

# re_coded = base64.b64encode(str(filtered))
re_coded = bytes(str(filtered), 'utf-8')

with open("output/formalized.png", 'wb') as image_file:
    image_file.write(base64.decodebytes(re_coded))
