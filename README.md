# Image Compression Algorithms

This repository contains implementations of both **lossy** and **lossless** image compression algorithms in Python. The project is designed to explore and compare various techniques for image compression while maintaining a focus on preserving image quality.

## Features

### Lossless Compression Algorithms
1. **Huffman Coding**: 
   - Encodes image data using variable-length codes based on frequency of occurrence.
2. **Run-Length Encoding (RLE)**: 
   - Compresses sequences of repeated values by storing the value and its count.

### Lossy Compression Algorithms
1. **Discrete Wavelet Transform (DWT)**: 
   - Reduces image size by decomposing it into frequency components.
2. **Fast Fourier Transform (FFT)**: 
   - Compresses the image by removing less significant frequency components.

## Requirements

- Python 3.8+
- Libraries:
  - `numpy`
  - `opencv-python`
  - `pywavelets`
  - `matplotlib`
