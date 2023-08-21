import streamlit as st
import zipfile
import io

from heic_converter import convert_heic_to_jpeg


# StreamlitのUI部分
st.title('HEIC to JPEG Converter')

uploaded_files = st.file_uploader("Choose HEIC files", type='heic', accept_multiple_files=True)

selected_images = []

if uploaded_files:
    with st.container():
        for uploaded_file in uploaded_files:
            heic_bytes = uploaded_file.read()
            jpg_bytes = convert_heic_to_jpeg(heic_bytes)
            st.image(jpg_bytes, caption=f'Converted: {uploaded_file.name}', use_column_width=True, output_format='JPEG')

            # チェックボックスを追加して、選択された画像をリストに追加
            if st.checkbox(f'Select {uploaded_file.name} for download'):
                selected_images.append((uploaded_file.name.replace('.heic', '.jpeg'), jpg_bytes))

    # 選択された画像をZIPファイルとしてダウンロード
    if selected_images:
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED, False) as zip_file:
            for file_name, image_bytes in selected_images:
                zip_file.writestr(file_name, image_bytes)
        st.download_button(label="Download Selected Images as ZIP", data=zip_buffer.getvalue(), file_name='converted_images.zip', mime='application/zip')
