import json, falcon

class Encryption(object):
    e = 65537
    q = 92092076805892533739724722602668675840671093008520241548191914215399824020372076186460768206814914423802230398410980218741906960527104568970225804374404612617736579286959865287226538692911376507934256844456333236362669879347073756238894784951597211105734179388300051579994253565459304743059533646753003894559
    p = 97846775312392801037224396977012615848433199640105786119757047098757998273009741128821931277074555731813289423891389911801250326299324018557072727051765547115514791337578758859803890173153277252326496062476389498019821358465433398338364421624871010292162533041884897182597065662521825095949253625730631876637
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
        print(message_to_encrypt)
        resp.status = falcon.HTTP_201
        resp.body = json.dumps({"hex":self.__encrypt(message_to_encrypt)})