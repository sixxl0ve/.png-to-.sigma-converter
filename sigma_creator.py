from PIL import Image
import struct


def convert_png_to_sigma(input_path, output_path):
    try:
        with Image.open(input_path) as img:

            img = img.convert("RGB")


            width, height = img.size


            pixel_data = img.tobytes()


            header = struct.pack("II3s", width, height, b"RGB")

            # Write to .sigma file
            with open(output_path, "wb") as sigma_file:
                sigma_file.write(header)
                sigma_file.write(pixel_data)

        print(f"Image successfully converted to {output_path}")
    except Exception as e:
        print(f"Error: {e}")


# Example usage
convert_png_to_sigma("input_image_path", "output_image_path")
