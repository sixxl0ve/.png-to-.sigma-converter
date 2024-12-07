from PIL import Image
import struct
import matplotlib.pyplot as plt


def open_and_show_sigma(file_path):
    try:
        with open(file_path, "rb") as sigma_file:
            header = sigma_file.read(11)
            width, height, color_mode = struct.unpack("II3s", header)

            if color_mode != b"RGB":
                raise ValueError("Unsupported color mode in .sigma file!")


            pixel_data = sigma_file.read()


            img = Image.frombytes("RGB", (width, height), pixel_data)


            plt.imshow(img)
            plt.axis('off')
            plt.title(f"{file_path} ({width}x{height})")
            plt.show()
    except Exception as e:
        print(f"Error: {e}")



open_and_show_sigma(".sigma file path")
