import pyheif
from PIL import Image
import io

# HEICをJPEGに変換する関数
def convert_heic_to_jpeg(heic_bytes):
    heif_file = pyheif.read(heic_bytes)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    output = io.BytesIO()
    image.save(output, format='JPEG')
    return output.getvalue()
