import function_pattern_matching as fpm

def to_hex(message):
    if(isinstance(message,str)):
        return "".join("{:02x}".format(c)for c in message.encode())
    else:
        return hex(int(message))[2:]

def to_decimal(hex_message):
    return (int(hex_message,16))
    
def to_ascii(hex_message):
    return  bytearray.fromhex(hex_message).decode("latin-1")
