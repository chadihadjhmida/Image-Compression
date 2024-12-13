from matplotlib.image import imread
import numpy as np
import matplotlib.pyplot as plt
import os
import pywt

plt.rcParams["figure.figsize"] = [8, 8]
plt.rcParams.update({"font.size": 18})
# change this name the the name of the image you want to applay to if DWT
name = "p.jpg"
A = imread(os.path.join("dog.jpg"))
B = np.mean(A, -1)  # Convert RGB to grayscale

plt.imshow(B, cmap="gray")
plt.axis("off")
plt.show()

## Wavelet Compression
n = 4
w = "db1"
coeffs = pywt.wavedec2(B, wavelet=w, level=n)

coeff_arr, coeff_slices = pywt.coeffs_to_array(coeffs)

Csort = np.sort(np.abs(coeff_arr.reshape(-1)))
keep = 0.05  # change this to as mush you want to keep a Threshold
thresh = Csort[int(np.floor((1 - keep) * len(Csort)))]
ind = np.abs(coeff_arr) > thresh
Cfilt = coeff_arr * ind  # Threshold small indices

coeffs_filt = pywt.array_to_coeffs(Cfilt, coeff_slices, output_format="wavedec2")

# Plot reconstruction
Arecon = pywt.waverec2(coeffs_filt, wavelet=w)
plt.figure()
plt.imshow(Arecon.astype("uint8"), cmap="gray")
plt.axis("off")
plt.title("keep = " + str(keep))
