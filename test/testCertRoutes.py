from mongo import Mongo
import json
import requests
import datetime
import time
import os
import math
import jwt
from cryptography.x509 import load_pem_x509_certificate

#異常系
#証明書の内容をどこからとってくるか　テスト用の証明書の内容な　文字列として送ればいいか
def testCertRoutes(token_scepserver):
    #仕様変えるかもしれん　ひとまず置いとく
    '''
    url = "http://localhost:5000/api/cert"
    mongo = Mongo("mongodb://localhost:27017","devices_db","devices")
    mongo.deleteMany({"csrGroup" : -1})

    headers = {
        'authorization':"Bearer" + " " + token_scepserver,
        'Content-Type': 'application/json'
    }
    #ここ　文字列で送るかもしれん

    dtAfter = datetime.datetime.now()
    dtBefore = dtAfter + datetime.timedelta(days=-1)
    try:
        with open("testDepot/nssdc.crt")as f:
            pem_cert  = f.read().encode()
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)

    try:
        cert = load_pem_x509_certificate(pem_cert)
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)
    #Certを何処かから取ってくる必要があるのでは
    payload={"Cert":cert,"Name":"TEST","AllowTime":7,"SerialNumber":-1,
    "NotBefore":dtBefore,"NotAfter":dtAfter,"Pem":"test1"} 
    payload =json.dumps(payload)
    '''
    return 0