from mongo import Mongo
import json
import requests
import datetime

def testCreate(token_admin,token_user,token_scepserver):
    url = "http://localhost:5000/api/devices"
    mongo = Mongo("mongodb://localhost:27017","devices_db","devices")
    mongo.deleteMany({"csrGroup" : -1})

    headers = {
        'authorization':"Bearer" + " " + token_scepserver,
        'Content-Type': 'application/json'
    }
    payload={"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}], "status" : "Waiting",  
    "CN" : "TEST", "secret" : "pass"} 
    payload =json.dumps(payload)
    try:
        r = requests.post(url,data=payload,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"You cannot access to the device"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)

    headers = {
        'authorization':"Bearer" + " " + token_admin,
        'Content-Type': 'application/json'
    }
    payload={"csrGroup" : -1, "email": [], "status" : "Waiting",  
    "CN" : "TEST", "secret" : "pass"} 
    payload =json.dumps(payload)
    try:
        r = requests.post(url,data=payload,headers=headers)
        message ='{"statusCode":406,"error":"Not Acceptable","message":"Email should not be empty"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    payload={"csrGroup" : -1,  "status" : "Waiting",  
    "CN" : "TEST", "secret" : "pass"} 
    payload =json.dumps(payload)
    try:
        r = requests.post(url,data=payload,headers=headers)
        message ='{"statusCode":406,"error":"Not Acceptable","message":"Email should not be empty"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)

    data = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}], "status" : "Waiting",  
    "CN" : "TEST", "secret" : "pass"}
    payload = data
    payload =json.dumps(payload)
    try:
        r = requests.post(url,data=payload,headers=headers)
        message ='{"statusCode":406,"error":"Not Acceptable","message":"Type should not be empty"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    data = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}], "status" : "Waiting",  
    "type":"Wrong","CN" : "TEST", "secret" : "pass"}
    payload = data
    payload =json.dumps(payload)
    try:
        r = requests.post(url,data=payload,headers=headers)
        message ='{"statusCode":406,"error":"Not Acceptable","message":"Type malformed"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    data = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}], "status" : "Wrong",  
    "type":"SE","CN" : "TEST", "secret" : "pass"}
    payload = data
    payload =json.dumps(payload)
    try:
        r = requests.post(url,data=payload,headers=headers)
        message ='{"statusCode":406,"error":"Not Acceptable","message":"Status malformed"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    data = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}], "status" : "Waiting",  
    "type":"SE","secret" : "pass"}
    payload = data
    payload =json.dumps(payload)
    try:
        r = requests.post(url,data=payload,headers=headers)
        message ='{"statusCode":406,"error":"Not Acceptable","message":"CN should not be empty"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)

    data = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}], 
    "type":"SE","status" : "Waiting",  "CN" : "TEST", "secret" : "pass"}
    payload = data
    payload =json.dumps(payload)
    try:
        mongo.addOne(data)
        r = requests.post(url,data=payload,headers=headers)
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
    data = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}],  
    "type":"SE", "CN" : "TEST", "secret" : "pass"}
    payload = data
    payload =json.dumps(payload)
    try:
        r = requests.post(url,data=payload,headers=headers)
        device = mongo.getOne({"csrGroup":-1})
        if device is None:
            print("テストに失敗しました。")
            exit(1)
        if len(device["email"]) != 2:
            print("テストに失敗しました。")
            exit(1)
        if device["email"][0] != data["email"][0]:
            print("テストに失敗しました。")
            exit(1)
        if device["email"][1] != data["email"][1]:
            print("テストに失敗しました。")
            exit(1)
        if device["status"] != "Waiting":
            print("テストに失敗しました。")
            exit(1)
        if device["CN"] != "TEST":
            print("テストに失敗しました。")
            exit(1)
        if device["secret"] != "pass":
            print("テストに失敗しました。")
            exit(1)
        if device["command"] != "./scepclient-linux-amd64 -server-url=undefined -cn TEST -challenge pass -certificate etc/pki/tls/certs/nssdc.crt -private-key /etc/pki/tls/private/nssdc.key":
            print("テストに失敗しました。")
            exit(1)
        mongo.deleteOne({"csrGroup":-1})
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    headers = {
        'authorization':"Bearer" + " " + token_user,
        'Content-Type': 'application/json'
    }
    data = {"csrGroup" : -1, "email": [],  
    "type":"SE", "CN" : "TEST", "secret" : "pass"}
    payload = data
    payload =json.dumps(payload)
    try:
        r = requests.post(url,data=payload,headers=headers)
        device = mongo.getOne({"csrGroup":-1})
        if device is None:
            print("テストに失敗しました。")
            exit(1)
        if len(device["email"]) != 1:
            print("テストに失敗しました。")
            exit(1)
        if device["email"][0] != {"email-children":"testuser"}:
            print("テストに失敗しました。")
            exit(1)
        if device["status"] != "Waiting":
            print("テストに失敗しました。")
            exit(1)
        if device["CN"] != "TEST":
            print("テストに失敗しました。")
            exit(1)
        if device["secret"] != "pass":
            print("テストに失敗しました。")
            exit(1)
        if device["command"] != "./scepclient-linux-amd64 -server-url=undefined -cn TEST -challenge pass -certificate etc/pki/tls/certs/nssdc.crt -private-key /etc/pki/tls/private/nssdc.key":
            print("テストに失敗しました。")
            exit(1)
        mongo.deleteOne({"csrGroup":-1})
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)

    return 0

def testFetch(token_admin,token_user,token_scepserver):
    url = "http://localhost:5000/api/devices"
    mongo = Mongo("mongodb://localhost:27017","devices_db","devices")
    mongo.deleteMany({"csrGroup" : -1})

    headers = {
        'authorization':"Bearer" + " " + token_scepserver,
        'Content-Type': 'application/json'
    }
    try:
        r = requests.get(url,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"You cannot access to the device"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    dt1 = datetime.datetime.now()
    dt3 = dt1 + datetime.timedelta(days=-1)
    data = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}],  
    "status":"Waiting","expiration_date":dt3,"type":"SE", "CN" : "TEST", "secret" : "pass"}
    headers = {
        'authorization':"Bearer" + " " + token_admin,
        'Content-Type': 'application/json'
    }
    try:
        mongo.addOne(data)
        r = requests.get(url,headers=headers)
        responce_list = r.json()
        responce = responce_list[0]
        mongo.deleteOne({"csrGroup" : -1})
        if responce is None:
            print("テストに失敗しました。")
            exit(1)
        if len(responce["email"]) != 2:
            print("テストに失敗しました。")
            exit(1)
        if responce["email"][0] != {"email-children":"test@com"}:
            print("テストに失敗しました。")
            exit(1)
        if responce["email"][1] != {"email-children":"test2@com"}:
            print("テストに失敗しました。")
            exit(1)
        if responce["status"] != "Expired":
            print("テストに失敗しました。")
            exit(1)
        if responce["CN"]!= "TEST":
            print("テストに失敗しました。")
            exit(1)
        if responce["secret"] != "pass":
            print("テストに失敗しました。")
            exit(1)
        mongo.deleteOne({"csrGroup":-1})
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    data1 = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}],  
    "status":"Waiting","expiration_date":dt1,"type":"SE", "CN" : "TEST", "secret" : "pass1"}
    data2 = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}],  
    "status":"Waiting","expiration_date":dt1,"type":"SE", "CN" : "TEST", "secret" : "pass2"}
    data3 = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}],  
    "status":"Waiting","expiration_date":dt3,"type":"SE", "CN" : "TEST", "secret" : "pass3"}

    try:
        mongo.addOne(data1)
        mongo.addOne(data2)
        mongo.addOne(data3)
        r = requests.get(url,headers=headers)
        responce_list = r.json()
        if responce_list is None:
            print("テストに失敗しました。")
            exit(1)
        if len(responce_list)!= 3:
            print("テストに失敗しました。")
            exit(1)
        responce = responce_list[0]
        if responce["status"] != "Waiting":
            print("テストに失敗しました。")
            exit(1)
        responce = responce_list[2]
        if responce["status"] != "Expired":
            print("テストに失敗しました。")
            exit(1)
        mongo.deleteOne({"csrGroup" : -1})
        if responce is None:
            print("テストに失敗しました。")
            exit(1)

        mongo.deleteMany({"csrGroup":-1})
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)

    headers = {
        'authorization':"Bearer" + " " + token_user,
        'Content-Type': 'application/json'
    }
    data = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}],  
    "status":"Waiting","expiration_date":dt1,"type":"SE", "CN" : "TEST", "secret" : "pass"}
    try:
        mongo.addOne(data)
        r = requests.get(url,headers=headers)
        mongo.deleteOne({"csrGroup" : -1})
        responce_list = r.json()
        if responce_list:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    data1 = {"csrGroup" : -1, "email": [{"email-children": "testuser"}, {"email-children": "test2@com"}],  
    "status":"Waiting","expiration_date":dt1,"type":"SE", "CN" : "TEST", "secret" : "pass1"}
    data2 = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}],  
    "status":"Waiting","expiration_date":dt1,"type":"SE", "CN" : "TEST", "secret" : "pass2"}
    data3 = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "testuser"}],  
    "status":"Waiting","expiration_date":dt3,"type":"SE", "CN" : "TEST", "secret" : "pass3"}

    try:
        mongo.addOne(data1)
        mongo.addOne(data2)
        mongo.addOne(data3)
        r = requests.get(url,headers=headers)
        responce_list = r.json()
        if responce_list is None:
            print("テストに失敗しました。")
            exit(1)
        if len(responce_list)!= 2:
            print("テストに失敗しました。")
            exit(1)
        responce = responce_list[0]
        if responce["status"] != "Waiting":
            print("テストに失敗しました。")
            exit(1)
        responce = responce_list[1]
        if responce["status"] != "Expired":
            print("テストに失敗しました。")
            exit(1)
        mongo.deleteOne({"csrGroup" : -1})
        if responce is None:
            print("テストに失敗しました。")
            exit(1)

        mongo.deleteMany({"csrGroup":-1})
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)

    return 0

def testGet(token_admin,token_user,token_scepserver):
    mongo = Mongo("mongodb://localhost:27017","devices_db","devices")
    mongo.deleteMany({"csrGroup" : -1})

    headers = {
        'authorization':"Bearer" + " " + token_scepserver,
        'Content-Type': 'application/json'
    }
    url = "http://localhost:5000/api/devices/" + "test"
    try:
        r = requests.get(url,headers=headers)
        message='{"statusCode":500,"error":"Internal Server Error","message":"Cast to ObjectId failed for value \\"test\\" (type string) at path \\"_id\\" for model \\"devices\\""}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    dt1 = datetime.datetime.now()
    data = {"csrGroup" : -1, "email": [{"email-children": "testuser"}, {"email-children": "test2@com"}],  
    "status":"Waiting","expiration_date":dt1,"type":"SE", "CN" : "TEST", "secret" : "pass"}
    try:
        mongo.addOne(data)
        device = mongo.getOne({"csrGroup" : -1})
        _id = str(device['_id'])
        url = "http://localhost:5000/api/devices/" + _id
        r = requests.get(url,headers=headers)
        mongo.deleteOne({"csrGroup" : -1})
        message='{"statusCode":401,"error":"Unauthorized","message":"You cannot access to the device"}'
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
        device = mongo.getOne({"csrGroup" : -1})
        _id = str(device['_id'])
        url = "http://localhost:5000/api/devices/" + _id
        mongo.deleteOne({"csrGroup" : -1})
        r = requests.get(url,headers=headers)
        message='{"statusCode":406,"error":"Not Acceptable","message":"This ID is wrong"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)

    headers = {
        'authorization':"Bearer" + " " + token_admin,
        'Content-Type': 'application/json'
    }
    data1 = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}],  
    "status":"Waiting","expiration_date":dt1,"type":"SE", "CN" : "TEST", "secret" : "pass1"}
    data2 = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}],  
    "status":"Waiting","expiration_date":dt1,"type":"SE", "CN" : "TEST", "secret" : "pass2"}
    data3 = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "testuser"}],  
    "status":"Waiting","expiration_date":dt1,"type":"SE", "CN" : "TEST", "secret" : "pass3"}

    try:
        mongo.addOne(data1)
        mongo.addOne(data2)
        mongo.addOne(data3)
        device = mongo.getOne({"secret" : "pass1"})
        _id = str(device['_id'])
        url = "http://localhost:5000/api/devices/" + _id
        r = requests.get(url,headers=headers)
        mongo.deleteMany({"csrGroup" : -1})
        responce = r.json()
        if responce["secret"] != "pass1":
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    headers = {
        'authorization':"Bearer" + " " + token_user,
        'Content-Type': 'application/json'
    }
    data1 = {"csrGroup" : -1, "email": [{"email-children": "test@vom"}, {"email-children": "test2@com"}],  
    "status":"Waiting","expiration_date":dt1,"type":"SE", "CN" : "TEST", "secret" : "pass1"}
    data2 = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}],  
    "status":"Waiting","expiration_date":dt1,"type":"SE", "CN" : "TEST", "secret" : "pass2"}
    data3 = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "testuser"}],  
    "status":"Waiting","expiration_date":dt1,"type":"SE", "CN" : "TEST", "secret" : "pass3"}

    try:
        mongo.addOne(data1)
        mongo.addOne(data2)
        mongo.addOne(data3)
        device = mongo.getOne({"secret" : "pass1"})
        _id = str(device['_id'])
        url = "http://localhost:5000/api/devices/" + _id
        r = requests.get(url,headers=headers)
        mongo.deleteMany({"csrGroup" : -1})
        message = '{"statusCode":401,"error":"Unauthorized","message":"You cannot access to the device"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    data1 = {"csrGroup" : -1, "email": [{"email-children": "testuser"}, {"email-children": "test2@com"}],  
    "status":"Waiting","expiration_date":dt1,"type":"SE", "CN" : "TEST", "secret" : "pass1"}
    data2 = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}],  
    "status":"Waiting","expiration_date":dt1,"type":"SE", "CN" : "TEST", "secret" : "pass2"}
    data3 = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "testuser"}],  
    "status":"Waiting","expiration_date":dt1,"type":"SE", "CN" : "TEST", "secret" : "pass3"}

    try:
        mongo.addOne(data1)
        mongo.addOne(data2)
        mongo.addOne(data3)
        device = mongo.getOne({"secret" : "pass1"})
        _id = str(device['_id'])
        url = "http://localhost:5000/api/devices/" + _id
        r = requests.get(url,headers=headers)
        mongo.deleteMany({"csrGroup" : -1})
        response = r.json()
        if responce["secret"] != "pass1":
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    return 0

def testUpdate(token_admin,token_user,token_scepserver):
    mongo = Mongo("mongodb://localhost:27017","devices_db","devices")
    mongo.deleteMany({"csrGroup" : -1})
    headers = {
        'authorization':"Bearer" + " " + token_scepserver,
        'Content-Type': 'application/json'
    }
    data = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}], "status" : "Waiting",  
    "type":"SE","CN" : "TEST", "secret" : "pass"}
    data_to_update = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}], "status" : "Waiting",  
    "type":"SE","CN" : "TEST", "secret" : "pass1"}
    payload =json.dumps(data_to_update)
    try:
        mongo.addOne(data)
        device = mongo.getOne({"csrGroup" : -1})
        _id = str(device["_id"])
        url = "http://localhost:5000/api/devices/" + _id
        r = requests.put(url,data=payload,headers=headers)
        mongo.deleteOne({"csrGroup" : -1})
        message ='{"statusCode":401,"error":"Unauthorized","message":"You cannot access to the device"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)

    headers = {
        'authorization':"Bearer" + " " + token_admin,
        'Content-Type': 'application/json'
    }
    try:
        mongo.addOne(data)
        device = mongo.getOne({"csrGroup" : -1})
        _id = str(device["_id"])
        url = "http://localhost:5000/api/devices/" + _id
        mongo.deleteOne({"csrGroup" : -1})
        r = requests.put(url,data=payload,headers=headers)
        message ='{"statusCode":500,"error":"Internal Server Error","message":"This id is wrong"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)

    data_to_update = {"csrGroup" : -1,  "status" : "Waiting",  
    "type":"SE","CN" : "TEST", "secret" : "pass1"}
    payload =json.dumps(data_to_update)
    try:
        mongo.addOne(data)
        device = mongo.getOne({"csrGroup" : -1})
        _id = str(device["_id"])
        url = "http://localhost:5000/api/devices/" + _id
        r = requests.put(url,data=payload,headers=headers)
        mongo.deleteOne({"csrGroup" : -1})
        message ='{"statusCode":406,"error":"Not Acceptable","message":"Email should not be empty"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    data_to_update = {"csrGroup" : -1,"email":[],  "status" : "Waiting",  
    "type":"SE","CN" : "TEST", "secret" : "pass1"}
    payload =json.dumps(data_to_update)
    try:
        mongo.addOne(data)
        device = mongo.getOne({"csrGroup" : -1})
        _id = str(device["_id"])
        url = "http://localhost:5000/api/devices/" + _id
        r = requests.put(url,data=payload,headers=headers)
        mongo.deleteOne({"csrGroup" : -1})
        message ='{"statusCode":406,"error":"Not Acceptable","message":"Email should not be empty"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)

    data = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}], "status" : "Waiting",  
    "type":"SE","CN" : "TEST", "secret" : "pass"}
    data2 = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}], "status" : "Waiting",  
    "type":"SE","CN" : "TEST2", "secret" : "pass"}
    data_to_update = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}], "status" : "Waiting",  
    "type":"SE","CN" : "TEST2", "secret" : "pass1"}
    payload =json.dumps(data_to_update)
    try:
        mongo.addOne(data)
        mongo.addOne(data2)
        device = mongo.getOne({"csrGroup" : -1})
        _id = str(device["_id"])
        url = "http://localhost:5000/api/devices/" + _id
        r = requests.put(url,data=payload,headers=headers)
        mongo.deleteOne({"csrGroup" : -1})
        message ='{"statusCode":409,"error":"Conflict","message":"This CN is already used"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)

    data = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}], "status" : "Waiting",  
    "type":"SE","CN" : "TEST", "secret" : "pass"}
    data_to_update = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}], "status" : "Waiting",  
    "type":"SE", "secret" : "pass1"}
    payload =json.dumps(data_to_update)
    try:
        mongo.addOne(data)
        device = mongo.getOne({"csrGroup" : -1})
        _id = str(device["_id"])
        url = "http://localhost:5000/api/devices/" + _id
        r = requests.put(url,data=payload,headers=headers)
        mongo.deleteOne({"csrGroup" : -1})
        message ='{"statusCode":406,"error":"Not Acceptable","message":"CN should not be empty"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    data = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}], "status" : "Waiting",  
    "type":"SE","CN" : "TEST", "secret" : "pass"}
    data_to_update = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}], "status" : "Waiting",  
    "type":"SE","CN" : "TEST","secret" : "pass1"}
    payload =json.dumps(data_to_update)
    try:
        mongo.addOne(data)
        device = mongo.getOne({"csrGroup" : -1})
        _id = str(device["_id"])
        url = "http://localhost:5000/api/devices/" + _id
        r = requests.put(url,data=payload,headers=headers)
        device = mongo.getOne({"csrGroup" : -1})
        mongo.deleteMany({"csrGroup" : -1})
        if device["secret"] != "pass1":
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    headers = {
        'authorization':"Bearer" + " " + token_user,
        'Content-Type': 'application/json'
    }

    data = {"csrGroup" : -1, "email": [{"email-children": "testuser"}, {"email-children": "test2@com"}], "status" : "Waiting",  
    "type":"SE","CN" : "TEST", "secret" : "pass"}
    data_to_update = {"csrGroup" : -1, "email": [{"email-children": "testuser"}, {"email-children": "test2@com"}], "status" : "Waiting",  
    "type":"SE", "CN":"TEST","secret" : "pass1"}
    payload =json.dumps(data_to_update)
    try:
        mongo.addOne(data)
        device = mongo.getOne({"csrGroup" : -1})
        _id = str(device["_id"])
        url = "http://localhost:5000/api/devices/" + _id
        r = requests.put(url,data=payload,headers=headers)
        device_update = mongo.getOne({"csrGroup" : -1})
        mongo.deleteOne({"csrGroup" : -1})
        if device_update["secret"] != "pass1":
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    return 0

def testDelete(token_admin,token_user):
    mongo = Mongo("mongodb://localhost:27017","devices_db","devices")
    mongo.deleteMany({"csrGroup" : -1})
    headers = {
        'authorization':"Bearer" + " " + token_user,
        'Content-Type': 'application/json'
    }
    data = "63a00891cb2005d2a0ee3f1f"
    payload =json.dumps(data)
    url = "http://localhost:5000/api/devices/" + "test"
    try:
        r = requests.delete(url,data=payload,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"You cannot access to the device"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
        
    headers = {
        'authorization':"Bearer" + " " + token_admin,
        'Content-Type': 'application/json'
    }
    url = "http://localhost:5000/api/devices/"
    try:
        r = requests.delete(url,data=payload,headers=headers)
        message='{"statusCode":500,"error":"Internal Server Error","message":"Cast to ObjectId failed for value \\"\\" (type string) at path \\"_id\\" for model \\"devices\\""}' 
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    url = "http://localhost:5000/api/devices/" + data
    try:
        r = requests.delete(url,data=payload,headers=headers)
        message='{"statusCode":500,"error":"Internal Server Error","message":"This id is wrong"}' 
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)

    dt1 = datetime.datetime.now()
    data = {"csrGroup" : -1, "email": [{"email-children": "testuser"}, {"email-children": "test2@com"}],  
    "status":"Waiting","expiration_date":dt1,"type":"SE", "CN" : "TEST", "secret" : "pass"}
    mongo.addOne(data)
    device = mongo.getOne({"csrGroup" : -1})
    _id = str(device['_id'])
    url = "http://localhost:5000/api/devices/" + _id
    try:
        r = requests.delete(url,data=payload,headers=headers)
        response = r.json()
        if response is None:
            print("テストに失敗しました。")
            exit(1)
        if response['data']['secret'] != device['secret']:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    return 0

def testDeleteMany(token_admin,token_user):
    mongo = Mongo("mongodb://localhost:27017","devices_db","devices")
    mongo.deleteMany({"csrGroup" : -1})
    headers = {
        'authorization':"Bearer" + " " + token_user,
        'Content-Type': 'application/json'
    }
    data = ["63a00891cb2005d2a0ee3f1f","63a00891cb2005d2a0ee3f1f"]
    payload =json.dumps(data)
    url = "http://localhost:5000/api/devices"

    try:
        r = requests.delete(url,data=payload,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"You cannot access to the device"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
        
    headers = {
        'authorization':"Bearer" + " " + token_admin,
        'Content-Type': 'application/json'
    }
    data=[]
    data.append("test")
    data.append("test2")
    payload =json.dumps(data)

    try:
        r = requests.delete(url,data=payload,headers=headers)
        message='{"statusCode":500,"error":"Internal Server Error","message":"Cast to ObjectId failed for value \\"test\\" (type string) at path \\"_id\\" for model \\"devices\\""}' 
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    data=[]
    payload =json.dumps(data)
    try:
        r = requests.delete(url,data=payload,headers=headers)
        message='{"statusCode":406,"error":"Not Acceptable","message":"Email should not be empty"}' 
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    dt1 = datetime.datetime.now()
    data1 = {"csrGroup" : -1, "email": [{"email-children": "testuser"}, {"email-children": "test2@com"}],  
    "status":"Waiting","expiration_date":dt1,"type":"SE", "CN" : "TEST", "secret" : "pass1"}
    data2 = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "test2@com"}],  
    "status":"Waiting","expiration_date":dt1,"type":"SE", "CN" : "TEST", "secret" : "pass2"}
    data3 = {"csrGroup" : -1, "email": [{"email-children": "test@com"}, {"email-children": "testuser"}],  
    "status":"Waiting","expiration_date":dt1,"type":"SE", "CN" : "TEST", "secret" : "pass3"}

    try:
        mongo.addOne(data1)
        mongo.addOne(data2)
        mongo.addOne(data3)
        device_1 = mongo.getOne({"secret" : "pass1"})
        _id_1 = str(device_1['_id'])
        device_2 = mongo.getOne({"secret" : "pass2"})
        _id_2 = str(device_2['_id'])
        data=[]
        data.append(_id_1)
        data.append(_id_2)
        payload =json.dumps(data)
        url = "http://localhost:5000/api/devices"
        r = requests.delete(url,data=payload,headers=headers)
        device_test_1 = mongo.getOne({"secret" : "pass1"})
        device_test_2 = mongo.getOne({"secret" : "pass2"})
        if device_test_1:
            mongo.deleteMany({"csrGroup" : -1})
            print("テストに失敗しました。")
            exit(1)
        if device_test_2:
            mongo.deleteMany({"csrGroup" : -1})
            print("テストに失敗しました。")
            exit(1)
        if mongo.getOne({"secret" : "pass3"}) is None:
            mongo.deleteMany({"csrGroup" : -1})
            print("テストに失敗しました。")
            exit(1)
        mongo.deleteMany({"csrGroup" : -1})
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    return 0

def testDevicesRoutes(token_admin,token_user,token_scepserver):
    testCreate(token_admin,token_user,token_scepserver)
    testFetch(token_admin,token_user,token_scepserver)
    testGet(token_admin,token_user,token_scepserver)
    testUpdate(token_admin,token_user,token_scepserver)
    print("dssd")
    testDelete(token_admin,token_user)
    print("ds")
    testDeleteMany(token_admin,token_user)
    return 0
