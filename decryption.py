import json,falcon,os

from helper import to_decimal,to_hex,to_ascii
class Decryption(object):
    e = int(os.getenv("e"))
    q = int(os.getenv("p"))
    p = int(os.getenv("q"))
    n = q*p
    d = pow(e,-1,(p-1)*(q-1))

    def __decrypt(self,message):
        m = pow(int(message),self.d,self.n)
        hex = to_hex(m)
        ascii = to_ascii(hex)
        return ascii

    def on_post(self,req,resp):
        data = json.loads(req.stream.read())
        message_to_decrypt = data.get("message")
        resp.status = falcon.HTTP_201
        resp.body = json.dumps({"message":self.__decrypt(message_to_decrypt)})

