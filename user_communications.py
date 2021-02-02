import falcon, json

class UserCommunications:
    
    def on_post(self,req,resp):
        data = json.loads(req.stream.read())
        user = data.get("User")
        tag = data.get("Tag")
        print(user)
        resp.status = falcon.HTTP_201
        print("User: {} with tag: {} online".format(user,tag))
        resp.body = json.dumps({"Recived":"True"})
