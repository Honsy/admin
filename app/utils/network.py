from flask import  jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer ,BadSignature,SignatureExpired
from config import Config
from enum import Enum, unique

APP_SECRET_KEY=Config.SECRET_KEY
MAX_TOKEN_AGE=1800
token_generator = Serializer(APP_SECRET_KEY, expires_in=MAX_TOKEN_AGE)

#Http 逻辑错误码
HttpSuccess = 200 #成功
HttpParamsError = 401 #客户端参数错误
HttpVailateError = 402 #服务端校验错误


class Network():
    # 响应码
    def responseCode(code,data,message):
        return jsonify({'code':code,'data':data,'message':message})

    # 生成Token
    def generate_auth_token(id, expiration=600):
        access_token = token_generator.dumps({"id": id})
        return access_token

    # 验证Token
    @staticmethod
    def verift_auth_token(token):
        s = Serializer(APP_SECRET_KEY)
        try:
            user_auth = token_generator.loads(token)
        except SignatureExpired:
            return None  # expired
        except BadSignature:
            return None  # invalid token

        return user_auth

