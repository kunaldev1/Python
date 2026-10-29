import os
from io import BytesIO

from PIL import Image
from rembg import remove


def remove_background(input_path, output_path):
    if not os.path.isfile(input_path):
        print(f"Error: The file '{input_path}' does not exist.")
        return

    try:
        input_image = Image.open(input_path)
        output = remove(input_image)

        # Ensure output is an Image object
        if isinstance(output, (bytes, bytearray, memoryview)):
            output = Image.open(BytesIO(bytes(output))).copy()
        elif not isinstance(output, Image.Image):
            output = Image.fromarray(output)

        output.save(output_path)
        print(f"Background removed and saved to {output_path}")
    except Exception as e:  # noqa: BLE001
        print(f"Error removing background: {e}")


if __name__ == "__main__":
    input_path = "Bleach.jpg"
    output_path = "output_image.png"
    remove_background(input_path, output_path)
