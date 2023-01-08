from mongo import Mongo
import json
import requests

def testAdminRoutes():
    url = "http://localhost:5000/authenticate"
    mongo = Mongo("mongodb://localhost:27017","devices_db","users")
    data ={"email":"test@jp.com","pass":"abc","role":"administrator"}

    mongo.deleteMany(data)

    headers={}
    payload ={"username":"test@jp.com","password":"abs_wrong","role":"administrator"}
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