import os

import pillow_heif
import streamlit as st
from PIL import Image


def convert_heic_to_jpg(input_directory, output_directory):
    for root, _, files in os.walk(input_directory):
        for file in files:
            if file.lower().endswith(".heic"):
                heic_file_path = os.path.join(root, file)
                jpg_file_path = os.path.join(
                    output_directory, os.path.splitext(file)[0] + ".jpg"
                )

                heif_file = pillow_heif.read_heif(heic_file_path)
                image = Image.frombytes(
                    heif_file.mode,
                    heif_file.size,
                    heif_file.data,
                    "raw",
                    heif_file.mode,
                    heif_file.stride,
                )

                image.save(jpg_file_path, "JPEG")
                st.write(f"Converted: {heic_file_path} to {jpg_file_path}")


st.title("HEIC to JPG Converter")

input_directory = st.text_input("Enter the directory containing HEIC files:")
output_directory = st.text_input("Enter the output directory for JPG files:")

if st.button("Convert"):
    if os.path.isdir(input_directory) and os.path.isdir(output_directory):
        convert_heic_to_jpg(input_directory, output_directory)
        st.success("Conversion completed!")
    else:
        st.error("Please provide valid directory paths.")
