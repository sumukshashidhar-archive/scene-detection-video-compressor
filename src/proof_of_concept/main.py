import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim


def output_cut_video(file_path, cut_file_path):
    
