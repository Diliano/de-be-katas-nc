def counter_intelligence(encrypted_str):
    if not isinstance(encrypted_str, str):
        raise TypeError("Input must be a string")
    
    if not encrypted_str:
        return ""
    
    encrypted_str = encrypted_str.upper()
    
    shift = (ord(encrypted_str[-1]) - ord("X")) % 26

    result = []
    for char in encrypted_str:
        if char.isalpha():
            base = ord("A")
            decrypted_position = ((ord(char) - base) - shift) % 26
            result.append(chr(decrypted_position + base))
        else:
            result.append(char)
    
    return ("").join(result)