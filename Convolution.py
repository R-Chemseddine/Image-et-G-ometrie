from PIL import Image
import numpy as np


def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

image = Image.open("spider.png")

image_w_padding = add_margin(image, 1, 1, 1, 1, 0)

I = np.array(image_w_padding)

image1 = Image.new('L', (len(I), len(I[0])))

I1 = np.array(image1)

m = [[1/9 for i in range(3)]for j in range(3)] 

for i in range(len(I)):
    for j in range(len(I[0])):
        somme = 0
        for k in range(i-1, i+1):
            for l in range(j-1, j+1):
                somme = somme + m[k-i+1][l-j+1] * I[k][l]
        I1[i][j] = int(somme)

image1 = Image.fromarray(I1)

image1.show()
image_w_padding.show()