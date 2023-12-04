from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_transpose(array: np.ndarray) -> np.ndarray:
    """Function that make the transpose operation on the array"""
    height, width = array.shape
    tranpose_array = np.zeros((width, height), dtype=array.dtype)

    for i in range(height):
        for j in range(width):
            tranpose_array[j, i] = array[i, j]
    return tranpose_array


def main():
    """Rotate the image with transpose operation on the pixel data array"""

    try:
        pixel_data = ft_load("animal.jpeg")

        start_x = (100)
        end_x = start_x + 400
        start_y = (450)
        end_y = start_y + 400

        sliced_array = pixel_data[start_x:end_x, start_y:end_y, 0]
        sliced_array_3D = sliced_array[:, :, np.newaxis]

        print(f"The shape of image is: {sliced_array_3D.shape}")
        print(sliced_array_3D)

        tranpose_array = ft_transpose(sliced_array)

        print(f"New shape after Tranpose: {tranpose_array.shape}")
        print(tranpose_array)

        plt.imshow(tranpose_array, cmap='gray')
        plt.axis('on')
        plt.show()
    except Exception as e:
        print(f"Error handling: {str(e)}")
    return


if __name__ == "__main__":
    main()
