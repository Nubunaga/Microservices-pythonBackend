import json, falcon, os

class Encryption(object):
    e = int(os.getenv("e"))
    q = int(os.getenv("p"))
    p = int(os.getenv("q"))
    n = q*p
    d = (p-1)*(q-1)
    def __to_hex(self,message):
        return "".join("{:02x}".format(c)for c in message.encode())

    def __to_decimal(self,hex_message):
        return (int(hex_message,16))


    def __encrypt(self,message):
        hex = self.__to_hex(message)
        decimal = self.__to_decimal(hex)
        return pow(decimal,self.e,self.n)

    def on_post(self,req,resp):
        data = json.loads(req.stream.read())
        message_to_encrypt = data.get("message")
        resp.status = falcon.HTTP_201
        resp.body = json.dumps({"hex":self.__encrypt(message_to_encrypt)})