from PIL import Image
import numpy as np

image = Image.open("spider.png")

I = np.array(image)

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
image.show()