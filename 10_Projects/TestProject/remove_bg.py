from io import BytesIO


from PIL import Image
from rembg import remove
import os


def remove_background(input_path, output_path):
    if not os.path.isfile(input_path):
        print(f"Error: The file '{input_path}' does not exist.")
        return

    try:
        input_image = Image.open(input_path)
        output = remove(input_image)

        # Ensure output is an Image object
        if isinstance(output, bytes):
            output = Image.open(BytesIO(output))
        elif isinstance(output, bytearray):
            output = Image.open(BytesIO(output))
        elif isinstance(output, memoryview):
            output = Image.open(BytesIO(bytes(output)))

        output.save(output_path)
        print(f"Background removed and saved to {output_path}")
    except Exception as e:
        print(f"Error removing background: {e}")


if __name__ == "__main__":
    input_path = "Sharingan.jpg"
    output_path = "output_image.png"
    remove_background(input_path, output_path)
