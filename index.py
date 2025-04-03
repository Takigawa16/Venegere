def vigenere_cipher(message, keyword, mode='encrypt'):
    """
    Encrypts or decrypts a message using the Vigenère cipher.
    
    Parameters:
    - message: The text to be encrypted or decrypted.
    - keyword: The keyword used for encryption and decryption.
    - mode: 'encrypt' for encryption, 'decrypt' for decryption.
    
    Returns:
    - The encrypted or decrypted text.
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    
    # Convert message and keyword to uppercase and remove spaces
    message = message.replace(' ', '').upper()
    keyword = keyword.upper()
    
    # Repeat the keyword to match the length of the message
    keyword = keyword * (len(message) // len(keyword)) + keyword[:len(message) % len(keyword)]
    
    for i in range(len(message)):
        # Find the position in the alphabet for the message and keyword letters
        msg_pos = alphabet.index(message[i])
        key_pos = alphabet.index(keyword[i])
        
        if mode == 'encrypt':
            # Subtract keyword value from message value (adjusted for your request)
            # Normally, you'd add for encryption, but you asked for subtraction
            new_pos = (msg_pos - key_pos) % 26
        elif mode == 'decrypt':
            # Add message value and keyword value (for decryption, it's the reverse)
            new_pos = (msg_pos + key_pos) % 26
        
        # Append the encrypted/decrypted letter to the result
        result += alphabet[new_pos]
    
    return result

def convert_to_html(text):
    """
    Converts the text into HTML format.
    
    Parameters:
    - text: The text to be converted.
    
    Returns:
    - The text wrapped in HTML tags.
    """
    return f"<p>{text}</p>"

# Example usage
message = "HELLO"
keyword = "KEY"

encrypted = vigenere_cipher(message, keyword, mode='encrypt')
decrypted = vigenere_cipher(encrypted, keyword, mode='decrypt')

encrypted_html = convert_to_html(encrypted)
decrypted_html = convert_to_html(decrypted)

print(f"Encrypted HTML: {encrypted_html}")
print(f"Decrypted HTML: {decrypted_html}")
