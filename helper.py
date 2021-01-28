    
def to_hex(message):
    return "".join("{:02x}".format(c)for c in message.encode())

def to_decimal(hex_message):
    return (int(hex_message,16))

