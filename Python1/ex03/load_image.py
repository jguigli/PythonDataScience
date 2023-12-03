from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    """DOC HERE"""

    try:
        img = Image.open(path)
        pixel_data = np.array(img)
        print(f"The shape of image is : {pixel_data.shape}")
    except Exception as e:
        print(f"Error loading the image: {str(e)}")
        return
    return pixel_data
