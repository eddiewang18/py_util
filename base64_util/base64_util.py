import base64

def decode_base64(encoded_str: str) -> str:
    """
    Decodes a Base64 encoded string.

    Parameters:
    encoded_str (str): The Base64 encoded string to decode.

    Returns:
    str: The decoded string.
    """
    # 將 Base64 編碼的字串解碼為 bytes
    decoded_bytes = base64.b64decode(encoded_str)
    
    # 將 bytes 轉換為字串
    decoded_str = decoded_bytes.decode('utf-8')
    
    return decoded_str