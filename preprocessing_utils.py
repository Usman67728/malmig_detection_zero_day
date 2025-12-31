import numpy as np
from PIL import Image
import os

def binary_to_image(file_path, target_width=None):
    """
    Converts a raw binary file into a 2D grayscale NumPy array.
    This demonstrates the initial feature engineering step for 
    Malimg and MALEVIS dataset processing.
    """
    try:
        with open(file_path, 'rb') as f:
            # Read binary data as 8-bit integers
            raw_data = np.frombuffer(f.read(), dtype=np.uint8)
        
        if len(raw_data) == 0:
            return None

        # Heuristic-based width selection if not specified
        if target_width is None:
            size_kb = len(raw_data) / 1024
            if size_kb < 10: target_width = 32
            elif size_kb < 30: target_width = 64
            elif size_kb < 100: target_width = 128
            elif size_kb < 200: target_width = 256
            elif size_kb < 500: target_width = 384
            elif size_kb < 1000: target_width = 512
            else: target_width = 1024

        # Calculate height and truncate/pad data to fit a rectangular matrix
        height = len(raw_data) // target_width
        image_data = raw_data[:height * target_width].reshape((height, target_width))
        
        return image_data

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def normalize_feature_map(image_array):
    """
    Performs min-max normalization to prep the data for 
    CNN input layers.
    """
    if image_array is None: return None
    return (image_array - np.min(image_array)) / (np.max(image_array) - np.min(image_array))

# Placeholder for Anomaly Scoring Logic
def calculate_anomaly_score(latent_vector, cluster_centroids):
    """
    Implements a distance-based anomaly score for Zero-Shot detection.
    (Conceptual Implementation)
    """
    distances = [np.linalg.norm(latent_vector - c) for c in cluster_centroids]
    return min(distances)