import io, base64


def convert_to_base64(img):
    in_mem_file = io.BytesIO()
    img.save(in_mem_file, format="PNG")
    in_mem_file.seek(0)
    img_bytes = in_mem_file.read()
    base64_encoded_result_bytes = base64.b64encode(img_bytes)
    base64_encoded_result_str = base64_encoded_result_bytes.decode('ascii')
    return base64_encoded_result_str
