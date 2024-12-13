from matplotlib.image import imread
import numpy as np
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams["figure.figsize"] = [12, 8]
plt.rcParams.update({"font.size": 18})

# change the name to the name of the image you want to test the FFT on it
name = "p.jpg"
A = imread(os.path.join(name))
Abw = np.mean(A, -1)  # Convert RGB to grayscale

plt.imshow(Abw, cmap="gray")
plt.axis("off")
plt.show()

## Compute FFT of image using fft2
At = np.fft.fft2(Abw)
F = np.log(np.abs(np.fft.fftshift(At)) + 1)  # Put FFT on log scale
plt.imshow(F, cmap="gray")
plt.axis("off")
plt.show()

## Zero out all small coefficients and inverse transform
Bt = np.sort(np.abs(np.reshape(At, -1)))
keep = 0.05  # change how much you want to keep as threshhold
thresh = Bt[int(np.floor((1 - keep) * len(Bt)))]
ind = np.abs(At) > thresh
Atlow = At * ind
Flow = np.log(np.abs(np.fft.fftshift(Atlow)) + 1)  # Put FFT on log scale

plt.imshow(Flow, cmap="gray")
plt.axis("off")
plt.show()

## Plot Reconstruction
Alow = np.fft.ifft2(Atlow).astype("uint8")

plt.imshow(Alow, cmap="gray")
plt.axis("off")
plt.show()
