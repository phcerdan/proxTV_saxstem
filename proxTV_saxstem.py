# Example script showing how to perform a 2D Total-Variation filtering with proxTV
import prox_tv as ptv
import matplotlib.pyplot as plt
import time
import skimage as ski
from skimage import io, color, util
import os

# parse input image
import argparse
import sys
parser = argparse.ArgumentParser(
    description='Denoising using TV from proxTV')
parser.add_argument(
    '-i', '--input',
    required=True,
    help='Input 2D Image ')
parser.add_argument(
    '-l', '--lam',
    required=False,
    type=float,
    default=0.15,
    help='lambda: Regularization factor for TotalVariation')
parser.add_argument(
    '-o', '--output',
    required=False,
    default='',
    help='Save denoised image')
parser.add_argument(
    '--show',
    required=False,
    action='store_true',
    help='Show plot')
args = parser.parse_args(sys.argv[1:])
input = args.input
lam = args.lam
output = args.output
show_flag = args.show
# Load image
X = io.imread(input)
X = ski.img_as_float(X)
X = color.rgb2gray(X)

# Filter using 2D TV-L1
print('Filtering image with 2D TV-L1... lambda:', str(lam))
start = time.time()
F = ptv.tv1_2d(X, lam)
end = time.time()
print('Elapsed time ' + str(end - start))

if show_flag:
    # Plot results
    plt.subplot(1, 2, 1)
    io.imshow(X)
    plt.xlabel('Original')

    plt.subplot(1, 2, 2)
    io.imshow(F)
    plt.xlabel('Filtered')

    plt.show()

if output:
    io.imsave(output, F)
