#テスト用の環境変数を設定　サーバー側　テスト側まとめてやっちゃえ

import sys
from mongo import Mongo
import json
import requests
import datetime
import time
import os
import math
import jwt

def testwrongURL():
    url ="localhost:5000/wrong"
    try:
        r = requests.get(url, data=payload,headers=headers)
        print(r.text)
        message ='{"statusCode":400,"error":"Bad Request","message":"User doesn\'t exit"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)

    return 0

def testAdminjwtVerifyHook(token,token_scep):
    url ="http://localhost:5000"
    data = {
    'foo': 123,
    }
    headers = {
    }
    try:
        r = requests.get(url, data=data,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"Cannot read property \'match\' of undefined"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    headers = {
        'authorization':"djifh"
    }
    try:
        r = requests.get(url, data=data,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"Cannot read property \'0\' of null"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)

    headers = {
        'authorization':"Bearer" + token
    }
    try:
        r = requests.get(url, data=data,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"Cannot read property \'0\' of null"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)

    headers = {
        'authorization':"Bearer" +" "+ token +"=sasa"
    }
    try:
        r = requests.get(url, data=data,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"Cannot read property \'0\' of null"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)

    headers = {
        'authorization':"xBearer" +" "+ token +"=sasa"
    }
    try:
        r = requests.get(url, data=data,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"Cannot read property \'0\' of null"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)
        
    headers = {
        'authorization':"Bearer" +" "+ token +"#"
    }
    try:
        r = requests.get(url, data=data,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"Cannot read property \'0\' of null"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    headers = {
        'authorization':"Bearer"
    }
    try:
        r = requests.get(url, data=data,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"Cannot read property \'0\' of null"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)

    headers = {
        'authorization':"Bearer"+" " +"eyJhbGc"
    }
    try:
        r = requests.get(url, data=data,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"jwt malformed"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)
 
    url ="http://localhost:5000/scep"
    headers = {
    }
    try:
        r = requests.get(url, data=data,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"Cannot read property \'match\' of undefined"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    headers = {
        'authorization':"djifh"
    }
    try:
        r = requests.get(url, data=data,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"Cannot read property \'0\' of null"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)

    headers = {
        'authorization':"Bearer" + token_scep
    }
    try:
        r = requests.get(url, data=data,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"Cannot read property \'0\' of null"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)

    headers = {
        'authorization':"Bearer" +" "+ token_scep +"=sasa"
    }
    try:
        r = requests.get(url, data=data,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"Cannot read property \'0\' of null"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)

    headers = {
        'authorization':"xBearer" +" "+ token_scep +"=sasa"
    }
    try:
        r = requests.get(url, data=data,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"Cannot read property \'0\' of null"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)
        
    headers = {
        'authorization':"Bearer" +" "+ token_scep +"#"
    }
    try:
        r = requests.get(url, data=data,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"Cannot read property \'0\' of null"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    headers = {
        'authorization':"Bearer"
    }
    try:
        r = requests.get(url, data=data,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"Cannot read property \'0\' of null"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)

    headers = {
        'authorization':"Bearer"+" " +"eyJhbGc"
    }
    try:
        r = requests.get(url, data=data,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"jwt malformed"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    return 0

def testadminRoutes():
    url = "http://localhost:5000/authenticate"
    mongo = Mongo("mongodb://localhost:27017","notes_db","admins")
    data ={"email":"test@jp.com","pass":"abc"}

    mongo.deleteMany(data)

    headers={}
    payload ={"username":"test@jp.com","password":"abs_wrong"}
    try:
        r = requests.post(url, data=payload,headers=headers)
        message ='{"statusCode":415,"code":"FST_ERR_CTP_INVALID_MEDIA_TYPE","error":"Unsupported Media Type","message":"Unsupported Media Type: application/x-www-form-urlencoded"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    headers={'Content-Type': 'application/json'}
    try:
        r = requests.post(url, data=payload,headers=headers)
        message ='{"statusCode":400,"error":"Bad Request","message":"Unexpected token e in JSON at position 0"}'
        message_2 ='{"statusCode":400,"error":"Bad Request","message":"Unexpected token u in JSON at position 0"}'
        if r.text != message and r.text!=message_2:
            print("テストに失敗しました。")
            exit(1)
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    payload =json.dumps(payload)
    try:
        r = requests.post(url, data=payload,headers=headers)
        message ='{"statusCode":400,"error":"Bad Request","message":"User doesn\'t exit"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    mongo.addOne(data)
    try:
        r = requests.post(url, data=payload,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"The password is wrong"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)
    mongo.deleteOne(data)
    return 0

def testnoteRoutes(token):
    url = "http://localhost:5000/api/notes"
    mongo = Mongo("mongodb://localhost:27017","notes_db","notes")
    mongo.deleteMany({"csrGroup" : 45})
    tdatetime = datetime.datetime.now()
    tstr = tdatetime.strftime('%Y/%m/%d')
    data={"csrID" : 1,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=US", "secret" : "pass", "pem" : "ewew"} 

    payload={"csrID" : 1,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=US", "secret" : "pass", "pem" : "ewew"} 
    headers = {
        'authorization':"Bearer" + " " + token,
        'Content-Type': 'application/json'
    }

    payload =json.dumps(payload)
    try:
        mongo.addOne(data)
        r = requests.post(url, data=payload,headers=headers)
        mongo.deleteOne(data)
        message ='{"statusCode":409,"error":"Conflict","message":"This CN is already used"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    data={"csrID" : 1,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=USTT", "secret" : "pass", "pem" : "ewew"}     
    try:
        mongo.addOne(data)
        r = requests.post(url, data=payload,headers=headers)
        mongo.deleteOne(data)
        message ='{"statusCode":409,"error":"Conflict","message":"This csrID is already used"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    try:
        r = requests.post(url, data=payload,headers=headers)
        mongo.deleteOne({"csrID" : 1})
        if r.status_code != 201:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)

    headers = {
        'authorization':"Bearer" + " " + token,
        'Content-Type': 'application/json'
    }

    data={"csrID" : 1,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=US", "secret" : "pass", "pem" : "ewew"}
    mongo.addOne(data)    
    data={"csrID" : 2,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=USs", "secret" : "pass", "pem" : "ewew"}     
    mongo.addOne(data)    
    data={"csrID" : 3,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=USss", "secret" : "pass", "pem" : "ewew"}     
    mongo.addOne(data)    
    
    try:
        r = requests.get(url,headers=headers)
        mongo.deleteMany({"csrGroup" : 45})
        if r.status_code != 200:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    url = "http://localhost:5000/api/notes/" + "686568"
    try:
        r = requests.get(url,headers=headers)
        mongo.deleteOne(data)
        message ='{"statusCode":500,"error":"Internal Server Error","message":"Cast to ObjectId failed for value \\"686568\\" (type string) at path \\"_id\\" for model \\"notes\\""}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)

    data={"csrID" : 1,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=US", "secret" : "pass", "pem" : "ewew"}
    mongo.addOne(data)
    note = mongo.getOne({"csrID" : 1})
    url = "http://localhost:5000/api/notes/" + str(note['_id'])
    try:
        r = requests.get(url,headers=headers)
        mongo.deleteOne(data)
        if r.status_code != 200:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    data={"csrID" : 1,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=US", "secret" : "pass", "pem" : "ewew"}
    mongo.addOne(data)
    note = mongo.getOne({"csrID" : 1})
    data={"csrID" : 2,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=S", "secret" : "pass", "pem" : "ewew"}
    mongo.addOne(data)
    _id = str(note['_id'])
    url = "http://localhost:5000/api/notes/" + _id
    try:
        r = requests.get(url,headers=headers)
        mongo.deleteMany({"csrGroup" : 45})
        if r.status_code != 200:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    data={"csrID" : 1,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=US", "secret" : "pass", "pem" : "ewew"}
    mongo.addOne(data)
    note = mongo.getOne({"csrID" : 1})
    _id = str(note['_id'])
    url = "http://localhost:5000/api/notes/" + _id
    payload={"csrID":1,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Expired", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=US", "secret" : "pass", "pem" : "ewew"} 
    payload =json.dumps(payload)

    try:
        r = requests.put(url,data=payload,headers=headers)
        mongo.deleteOne({"csrID" : 1})
        if r.status_code != 200:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    try:
        r = requests.put(url,data=payload,headers=headers)
        message='{"statusCode":500,"error":"Internal Server Error","message":"Cannot read property \'id\' of null"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    mongo.addOne(data)
    note = mongo.getOne({"csrID" : 1})
    _id = str(note['_id'])
    url = "http://localhost:5000/api/notes/" + "edfedeedededededede"
    payload={"csrID":2,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Expired", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=USS", "secret" : "pass", "pem" : "ewew"} 
    payload =json.dumps(payload)
    try:
        r = requests.put(url,data=payload,headers=headers)
        message='{"statusCode":500,"error":"Internal Server Error","message":"Cannot read property \'id\' of null"}'
        mongo.deleteOne(data)
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    mongo.addOne(data)
    note = mongo.getOne({"csrID" : 1})
    _id = str(note['_id'])
    url = "http://localhost:5000/api/notes/" + _id
    payload={"csrID":1,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Expired", "expiration_date" : tstr,  "secret" : "pass", "pem" : "ewew"} 
    payload =json.dumps(payload)
    try:
        r = requests.put(url,data=payload,headers=headers)
        message='{"statusCode":500,"error":"Internal Server Error","message":"Cannot read property \'id\' of null"}'
        mongo.deleteOne(data)
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)

    mongo.addOne(data)
    note = mongo.getOne({"csrID" : 1})
    _id = str(note['_id'])
    url = "http://localhost:5000/api/notes/" + _id
    payload={"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Expired", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=US", "secret" : "pass", "pem" : "ewew"} 
    payload =json.dumps(payload)
    try:
        r = requests.put(url,data=payload,headers=headers)
        message='{"statusCode":500,"error":"Internal Server Error","message":"Cannot read property \'id\' of null"}'
        mongo.deleteOne(data)
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    mongo.addOne(data)
    data_2={"csrID" : 2,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=USS", "secret" : "pass", "pem" : "ewew"}
    mongo.addOne(data_2)
    note = mongo.getOne({"csrID" : 2})
    _id = str(note['_id'])
    url = "http://localhost:5000/api/notes/" + _id
    payload={"csrID" : 1,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Expired", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=US", "secret" : "pass", "pem" : "ewew"} 
    payload =json.dumps(payload)

    try:
        r = requests.put(url,data=payload,headers=headers)
        message='{"statusCode":409,"error":"Conflict","message":"This CN is already used"}'
        mongo.deleteMany({"csrGroup" : 45})
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)

    mongo.addOne(data)
    data_2={"csrID" : 2,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=USS", "secret" : "pass", "pem" : "ewew"}
    mongo.addOne(data_2)
    note = mongo.getOne({"csrID" : 2})
    _id = str(note['_id'])
    url = "http://localhost:5000/api/notes/" + _id
    payload={"csrID" : 1,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Expired", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=USS", "secret" : "pass", "pem" : "ewew"} 
    payload =json.dumps(payload)
    
    try:
        r = requests.put(url,data=payload,headers=headers)
        message='{"statusCode":409,"error":"Conflict","message":"This csrID is already used"}'
        mongo.deleteMany({"csrGroup" : 45})
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)


    url = "http://localhost:5000/api/notes/" +_id
    payload={"id":_id}
    payload =json.dumps(payload)

    try:
        r = requests.delete(url,data=payload,headers=headers)
        message ='{"data":null}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)

    url = "http://localhost:5000/api/notes/" +"abc"
    payload={"id":_id}
    payload =json.dumps(payload)

    try:
        r = requests.delete(url,data=payload,headers=headers)
        message ='{"statusCode":500,"error":"Internal Server Error","message":"Cast to ObjectId failed for value \\"abc\\" (type string) at path \\"_id\\" for model \\"notes\\""}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    data={"csrID" : 1,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=US", "secret" : "pass", "pem" : "ewew"}
    mongo.addOne(data)
    note = mongo.getOne({"csrID" : 1})
    _id = str(note['_id'])
    url = "http://localhost:5000/api/notes/" +_id
    payload={"id":_id}
    payload =json.dumps(payload)
    try:
        r = requests.delete(url,data=payload,headers=headers)
        mongo.deleteOne(data)
        if r.status_code != 200:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    data={"csrID" : 1,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=US", "secret" : "pass", "pem" : "ewew"}
    mongo.addOne(data)
    note = mongo.getOne({"csrID" : 1})
    _id = str(note['_id'])
    url = "http://localhost:5000/api/notes/" +_id
    payload={"id":_id}
    payload =json.dumps(payload)
    data={"csrID" : 2,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=S", "secret" : "pass", "pem" : "ewew"}
    mongo.addOne(data)
    url = "http://localhost:5000/api/notes/" + _id
    try:
        r = requests.delete(url,data=payload,headers=headers)
        mongo.deleteMany({"csrGroup" : 45})
        if r.status_code != 200:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    data={"csrID" : 1,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=US", "secret" : "pass", "pem" : "ewew"}
    mongo.addOne(data)
    note = mongo.getOne({"csrID" : 1})
    _id_1 = str(note['_id'])
    data={"csrID" : 2,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=S", "secret" : "pass", "pem" : "ewew"}
    mongo.addOne(data)
    note = mongo.getOne({"csrID" : 2})
    _id_2 = str(note['_id'])
    data={"csrID" : 3,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=SS", "secret" : "pass", "pem" : "ewew"}
    mongo.addOne(data)
    note = mongo.getOne({"csrID" : 3})
    _id_3 = str(note['_id'])

    url = "http://localhost:5000/api/notes"
    payload=[]
    payload.append(_id)
    payload.append(_id_2)
    payload.append(_id_3)
    payload =json.dumps(payload)
    try:
        r = requests.delete(url,data=payload,headers=headers)
        if r.status_code != 200:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    payload=[]
    payload.append(_id)
    payload =json.dumps(payload)
    try:
        r = requests.delete(url,data=payload,headers=headers)
        message ='[null]'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    payload=[]
    payload.append("abc")
    payload =json.dumps(payload)
    try:
        r = requests.delete(url,data=payload,headers=headers)
        message ='{"statusCode":500,"error":"Internal Server Error","message":"Cast to ObjectId failed for value \\"abc\\" (type string) at path \\"_id\\" for model \\"notes\\""}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)

    return 0
 
def testscepRoutes(token):
    url = "http://localhost:5000/scep"
    mongo = Mongo("mongodb://localhost:27017","notes_db","notes")
    mongo.deleteMany({"csrGroup" : 45})
    tdatetime = datetime.datetime.now()
    tstr = tdatetime.strftime('%Y/%m/%d')
    data={"csrID" : 1,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=US", "secret" : "pass", "pem" : "ewew"} 

    payload={"csrID" : 1,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "Cn" : "CN=TEST1,OU=MDM,O=scep-client,C=US", "Secret" : "pass_wrong", "pem" : "ewew"} 
    headers = {
        'authorization':"Bearer" + " " + token,
        'Content-Type': 'application/json'
    }
    payload =json.dumps(payload)

    try:
        r = requests.post(url, data=payload,headers=headers)
        message ='{"message":"The common name (RFC4514 Distinguished Name string) is not mathched"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    try:
        mongo.addOne(data)
        r = requests.post(url, data=payload,headers=headers)
        message ='{"message":"The challenge password is wrong"}'
        mongo.deleteOne(data)
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    payload={"csrID" : 1,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "Cn" : "CN=TEST1,OU=MDM,O=scep-client,C=US",  "pem" : "ewew"} 
    payload =json.dumps(payload)

    try:
        mongo.addOne(data)
        r = requests.post(url, data=payload,headers=headers)
        message ='{"message":"The challenge password is wrong"}'
        mongo.deleteOne(data)
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)

    payload={"csrID" : 1,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting",  "Cn" : "CN=TEST1,OU=MDM,O=scep-client,C=US", "Secret" : "pass", "pem" : "ewew"} 
    payload =json.dumps(payload)

    try:
        mongo.addOne(data)
        r = requests.post(url, data=payload,headers=headers)
        message ='{"message":"The csr has been expired"}'
        mongo.deleteOne(data)
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    tdatetime += datetime.timedelta(days=1)
    tstr = tdatetime.strftime('%Y/%m/%d')
    data={"csrID" : 1,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "CN" : "CN=TEST1,OU=MDM,O=scep-client,C=US", "secret" : "pass", "pem" : "ewew"} 

    payload={"csrID" : 1,"csrGroup" : 45, "email" : "test@gmail.com", "status" : "Waiting", "expiration_date" : tstr, "Cn" : "CN=TEST1,OU=MDM,O=scep-client,C=US", "Secret" : "pass", "pem" : "ewew"} 
    payload =json.dumps(payload)

    try:
        mongo.addOne(data)
        r = requests.post(url, data=payload,headers=headers)
        mongo.deleteOne(data)
        if r.status_code != 200:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    return 0

def getToken(jwt_key,jwt_key_scep):
    miriSecondNow = time.time()
    nbf = math.floor( miriSecondNow) 
    exp = nbf + 8*60*60 #exp = 8h
    signer = os.environ['SIGNER']
    jwtPayload = {
        "iss": signer,
        "sub": "testuser",
        "exp": exp,
        "nbf": nbf,
    }
    token = jwt.encode(jwtPayload, jwt_key, algorithm="HS256")

    exp = nbf + 10*365*24*60*60 #exp = 10y
    signer = os.environ['SIGNER']
    jwtPayload = {
        "iss": signer,
        "sub": "testuser",
        "exp": exp,
        "nbf": nbf,
    }
    token_scep = jwt.encode(jwtPayload, jwt_key_scep, algorithm="HS256")
    return token,token_scep
    

def main ():
    try: 
        jwt_key = os.environ['JWT_KEY']
        jwt_key_scep = os.environ['JWT_KEY_SCEP']
    except Exception as e:
        print(e)
        print('環境変数の設定に問題がある可能性があります')
        exit(1)

    token,token_scep= getToken(jwt_key,jwt_key_scep)
    testAdminjwtVerifyHook(token,token_scep)
    testadminRoutes()
    testnoteRoutes(token)
    testscepRoutes(token)
    print("テストは正常に終了しました。")

if __name__ == '__main__':
    main()
