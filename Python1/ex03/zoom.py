from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def main():
    """Zoom the image with slicing operation on the pixel data array"""

    try:
        pixel_data = ft_load("animal.jpeg")
        print(pixel_data)

        start_x = (100)
        end_x = start_x + 400
        start_y = (450)
        end_y = start_y + 400

        sliced_array = pixel_data[start_x:end_x, start_y:end_y, 0]
        sliced_array = sliced_array[:, :, np.newaxis]

        print(f"New shape after slicing: {sliced_array.shape}")
        print(sliced_array)

        plt.imshow(sliced_array, cmap='gray')
        plt.axis('on')
        plt.show()
    except Exception as e:
        print(f"Error handling: {str(e)}")
    return


if __name__ == "__main__":
    main()
