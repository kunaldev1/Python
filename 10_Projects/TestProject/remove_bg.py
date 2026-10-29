"""Remove an image background and save the result as an image file."""

from io import BytesIO
from pathlib import Path

from PIL import Image
from rembg import remove

PROJECT_DIR = Path(__file__).resolve().parent


def remove_background(input_path, output_path):
    """Remove an image background and save the result.

    Args:
        input_path: Source image path.
        output_path: Destination path for the processed image.

    Returns:
        True if the output was saved successfully; otherwise False.
    """
    source_path = Path(input_path)
    destination_path = Path(output_path)

    if not source_path.is_absolute():
        source_path = PROJECT_DIR / source_path
    if not destination_path.is_absolute():
        destination_path = PROJECT_DIR / destination_path

    if not source_path.is_file():
        print(f"Error: input image not found: {source_path}")
        return False

    try:
        with Image.open(source_path) as input_image:
            output = remove(input_image.convert("RGBA"))

        if isinstance(output, (bytes, bytearray, memoryview)):
            with Image.open(BytesIO(bytes(output))) as output_image:
                output_image.load()
                output_image = output_image.copy()
        elif isinstance(output, Image.Image):
            output_image = output.copy()
        else:
            output_image = Image.fromarray(output)

        destination_path.parent.mkdir(parents=True, exist_ok=True)
        output_image.save(destination_path)
        print(f"Background removed and saved to {destination_path}")
        return True
    except (OSError, ValueError, TypeError) as error:
        print(f"Error removing background: {error}")
        return False
    except Exception as error:  # Model/runtime errors can vary by rembg backend.
        print(f"Background-removal model failed: {error}")
        return False


if __name__ == "__main__":
    remove_background("Bleach.jpg", "output_image.png")
