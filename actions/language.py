def find_language(latest_message):
    if not latest_message or not latest_message.strip():
        return 'en'
        
    # Check if the message contains Tamil characters (Unicode block: U+0B80 to U+0BFF)
    has_tamil = any(0x0B80 <= ord(char) <= 0x0BFF for char in latest_message)
    if has_tamil:
        return 'ta'
        
    # For all other inputs, default to English
    return 'en'
