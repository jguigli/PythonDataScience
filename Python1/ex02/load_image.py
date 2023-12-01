from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    """DOC HERE"""

    try:
        img = Image.open(path)
        pixel_data = np.array(img)
        print(f"The shape of image is : {pixel_data.shape}")
    except Exception as e:
        # Handle any errors with a clear error message
        print(f"Error loading the image: {str(e)}")
    return pixel_data
