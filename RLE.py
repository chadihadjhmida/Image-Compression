"""We will  start by importing necesary packages"""

import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image, ImageOps
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


name = "p.jpg"  # change this name to the name of the image you want to applay to it RLE (make sure it is in the same rep ans main.py)
img = Image.open("p.jpg")
w, h = img.size
# img = img.resize((w,h))
img = ImageOps.grayscale(img)  # for simplisity of the code
W, H = img.size
img_ar = np.array(img)


def run_length_encode(ar):
    i = 0
    s = ""
    while i < len(ar):
        c = 0
        el = ar[i]
        while i < len(ar) and abs(ar[i] - el) <= 10:
            c += 1
            i += 1

        el_bin = "{0:08b}".format(el)
        c_bin = "{0:08b}".format(c)
        s = s + el_bin + c_bin
    return s


def compress_image(img_ar, filename):
    file = open(filename, "w")
    W, H = img_ar.shape
    bits = 0
    for row in img_ar:
        l = run_length_encode(row) + "\n"
        bits += len(l)
        file.write(l)
    file.close()
    orig_bits = W * H * 8
    print("========== COMPRESSION SUCCESSFULLY DONE =========")
    print("COMPRESSED IMAGEFILE NAME : ", filename)
    print(
        "ORIGINAL SIZE OF IMAGE IN BITS (WxHx8)",
        orig_bits,
        " WHICH IS : ",
        orig_bits / 8000,
        " KB",
    )
    print(
        "AFTER RLE COMPRESSION SIZE IN BITS ", bits, " WHICH IS : ", bits / 8000, " KB"
    )
    print("COMPRESSION PERCENTAGE : ", ((orig_bits - bits) / orig_bits) * 100, "%")


compress_image(img_ar, "encode.txt")


def decode(filename):
    file = open(filename, "r+")
    extract = file.read().split("\n")
    ar = []
    for li in extract:
        for i in range(0, len(li), 16):
            el = li[i : i + 8]
            cnt = li[i + 8 : i + 16]
            el = int(el, 2)
            cnt = int(cnt, 2)
            ar = ar + cnt * [el]
    # print(ar)
    file.close()
    new_img = np.array(ar)
    new_img = np.reshape(new_img, (W, H))
    plt.imshow(new_img, cmap="gray")
    plt.axis("off")
    plt.show()


new_img = decode("encode.txt")
