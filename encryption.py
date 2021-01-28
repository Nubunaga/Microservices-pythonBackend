import json, falcon, os
from helper import to_decimal,to_hex
class Encryption(object):
    e = int(os.getenv("e"))
    q = int(os.getenv("p"))
    p = int(os.getenv("q"))
    n = q*p
    d = (p-1)*(q-1)

    def __encrypt(self,message):
        hex = to_hex(message)
        decimal = to_decimal(hex)
        return pow(decimal,self.e,self.n)

    def on_post(self,req,resp):
        data = json.loads(req.stream.read())
        message_to_encrypt = data.get("message")
        resp.status = falcon.HTTP_201
        resp.body = json.dumps({"hex":self.__encrypt(message_to_encrypt)})