from encryption import Encryption
import falcon, json

class CalculationRSA(object):
    initial_test = [{"rsa":"This is a test!"}]

    def on_get(self,req,resp):
        resp.body = json.dumps(self.initial_test)

    def on_post(self,req,resp):
        data = json.loads(req.stream.read())
        self.initial_test.append(data)
        resp.status = falcon.HTTP_201
        resp.body = json.dumps({"message":"Message added"})
        


api = falcon.API()

calculation_endpoint = CalculationRSA()
encryption_endpoint = Encryption()
api.add_route('/calculations',calculation_endpoint)
api.add_route('/encryptMedia',encryption_endpoint)

