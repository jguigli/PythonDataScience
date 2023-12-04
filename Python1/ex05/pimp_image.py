from PIL import Image
import numpy as np


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    pixel_data = np.copy(array)
    pixel_data = 255 - pixel_data

    invert_img = Image.fromarray(pixel_data.astype('uint8'))
    invert_img.show()


def ft_red(array) -> np.ndarray:
    """Modify the color of the image received only with red RGB."""
    pixel_data = np.copy(array)
    pixel_data[:, :, 1] = 0
    pixel_data[:, :, 2] = 0

    red_img = Image.fromarray(pixel_data.astype('uint8'))
    red_img.show()


def ft_green(array) -> np.ndarray:
    """Modify the color of the image received only with green RGB."""
    pixel_data = np.copy(array)
    pixel_data[:, :, 0] = 0
    pixel_data[:, :, 2] = 0

    red_img = Image.fromarray(pixel_data.astype('uint8'))
    red_img.show()


def ft_blue(array) -> np.ndarray:
    """Modify the color of the image received only with blue RGB."""
    pixel_data = np.copy(array)
    pixel_data[:, :, 0] = 0
    pixel_data[:, :, 1] = 0

    red_img = Image.fromarray(pixel_data.astype('uint8'))
    red_img.show()


def ft_grey(array) -> np.ndarray:
    """Modify the color of the image received in grey."""
    pixel_data = np.copy(array)
    pixel_data = np.dot(pixel_data[..., :3], [0.299, 0.587, 0.114])

    gray_img = Image.fromarray(pixel_data.astype('uint8'))
    gray_img.show()
