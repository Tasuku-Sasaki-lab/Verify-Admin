from mongo import Mongo
import json
import requests

def testCreate(token_admin,token_user):
    url = "http://localhost:5000/api/users"
    mongo = Mongo("mongodb://localhost:27017","devices_db","users")
    mongo.deleteMany({"pass":"test1"})
    headers = {
        'authorization':"Bearer" + " " + token_user,
        'Content-Type': 'application/json'
    }
    payload={ "email" : "testtest@com", "pass" : "test1", "role" : "administrator" }
    payload =json.dumps(payload)
    try:
        r = requests.post(url,data=payload,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"You cannot access to the users"}'
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
    payload={  "pass" : "test1", "role" : "administrator" }
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
    payload={ "email" : "testtest@com", "role" : "administrator" }
    payload =json.dumps(payload)
    try:
        r = requests.post(url,data=payload,headers=headers)
        message ='{"statusCode":406,"error":"Not Acceptable","message":"Password should not be empty"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    payload={ "email" : "testtest@com", "pass" : "test1" }
    payload =json.dumps(payload)
    try:
        r = requests.post(url,data=payload,headers=headers)
        message ='{"statusCode":406,"error":"Not Acceptable","message":"Role should not be empty"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    payload={ "email" : "testtest@com", "pass":"test1","role" : "administrator" ,"role" : "Worng"}
    payload =json.dumps(payload)
    try:
        r = requests.post(url,data=payload,headers=headers)
        message ='{"statusCode":406,"error":"Not Acceptable","message":"Role malformed"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    payload={ "email" : "testtest@com", "pass":"test1","role" : "administrator" ,"role" : "user"}
    payload =json.dumps(payload)
    try:
        r = requests.post(url,data=payload,headers=headers)
        res = r.json()
        user = mongo.getOne({"pass":"test1"})
        mongo.deleteMany({"pass":"test1"})
        if res['email'] != user['email']:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    return 0

def testFetch(token_admin,token_user):
    url = "http://localhost:5000/api/users"
    mongo = Mongo("mongodb://localhost:27017","devices_db","users")
    mongo.deleteMany({"pass":"test1"})
    headers = {
        'authorization':"Bearer" + " " + token_user,
        'Content-Type': 'application/json'
    }
    try:
        r = requests.get(url,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"You cannot access to the users"}'
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
    '''
    data = { "email" : "testtest@com", "pass":"test1","role" : "administrator" ,"role" : "user"}
    headers = {
        'authorization':"Bearer" + " " + token_admin,
        'Content-Type': 'application/json'
    }
    try:
        mongo.addOne(data)
        r = requests.get(url,headers=headers)
        res_list = r.json()
        mongo.deleteOne({"pass":"test1"})
        if res_list is None:
            print("テストに失敗しました。")
            exit(1)
        res  = res_list[0]
        print(res)
        if res['email'] != 'testtest@com':
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    
    data1 = { "email" : "testtest1@com", "pass":"test1","role" : "administrator" ,"role" : "user"}
    data2 = { "email" : "testtest2@com", "pass":"test1","role" : "administrator" ,"role" : "user"}
    dat3 = { "email" : "testtest3@com", "pass":"test1","role" : "administrator" ,"role" : "user"}
    try:
        mongo.addOne(data1)
        mongo.addOne(data2)
        mongo.addOne(data3)
        r = requests.get(url,headers=headers)
        res_list = r.json()
        if res_list is None:
            print("テストに失敗しました。")
            exit(1)
        if len(res_list)!= 3:
            print("テストに失敗しました。")
            exit(1)
        res = res_list[0]
        if res['email'] != 'testtest1@com':
            print("テストに失敗しました。")
            exit(1)
        res = res_list[2]
        if res['email'] != 'testtest3@com':
            print("テストに失敗しました。")
            exit(1)
        mongo.deleteMany({"pass":"test1"})
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    '''
    return 0

def testGet(token_admin,token_user):
    mongo = Mongo("mongodb://localhost:27017","devices_db","users")
    mongo.deleteMany({"pass":"test1"})

    headers = {
        'authorization':"Bearer" + " " + token_admin,
        'Content-Type': 'application/json'
    }
    url = "http://localhost:5000/api/users/" + "test"
    try:
        r = requests.get(url,headers=headers)
        message='{"statusCode":500,"error":"Internal Server Error","message":"Cast to ObjectId failed for value \\"test\\" (type string) at path \\"_id\\" for model \\"users\\""}'
        if r.text != message:
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
    data = { "email" : "testtest@com", "pass":"test1","role" : "administrator" ,"role" : "user"}
    try:
        mongo.addOne(data)
        user = mongo.getOne({"pass":"test1"})
        _id = str(user['_id'])
        url = "http://localhost:5000/api/users/" + _id
        r = requests.get(url,headers=headers)
        mongo.deleteOne({"pass":"test1"})
        message='{"statusCode":401,"error":"Unauthorized","message":"You cannot access to the user"}'
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
        user = mongo.getOne({"pass":"test1"})
        _id = str(user['_id'])
        url = "http://localhost:5000/api/users/" + _id
        mongo.deleteOne({"pass":"test1"})
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
    data1 = { "email" : "testtest1@com", "pass":"test1","role" : "administrator" ,"role" : "user"}
    data2 = { "email" : "testtest2@com", "pass":"test1","role" : "administrator" ,"role" : "user"}
    data3 = { "email" : "testtest3@com", "pass":"test1","role" : "administrator" ,"role" : "user"}
    try:
        mongo.addOne(data1)
        mongo.addOne(data2)
        mongo.addOne(data3)
        user = mongo.getOne({"email" : "testtest1@com"})
        _id = str(user['_id'])
        url = "http://localhost:5000/api/users/" + _id
        r = requests.get(url,headers=headers)
        mongo.deleteMany({"pass":"test1"})
        res = r.json()
        if res['role'] != "user":
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    return 0

def testUpdate(token_admin,token_user):
    mongo = Mongo("mongodb://localhost:27017","devices_db","users")
    mongo.deleteMany({"pass":"test1"})
    headers = {
        'authorization':"Bearer" + " " + token_user,
        'Content-Type': 'application/json'
    }
    url = "http://localhost:5000/api/users/"
    data={ "email" : "testtest@com", "pass" : "test1", "role" : "administrator" }
    payload =json.dumps(data)
    try:
        r = requests.put(url,data=payload,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"You cannot access to the users"}'
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
        user = mongo.getOne({"pass":"test1"})
        _id = str(user["_id"])
        url = "http://localhost:5000/api/users/" + _id
        mongo.deleteOne({"pass":"test1"})
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
    data={"pass" : "test1", "role" : "administrator" }
    payload =json.dumps(data)
    try:
        mongo.addOne(data)
        user = mongo.getOne({"pass":"test1"})
        _id = str(user["_id"])
        url = "http://localhost:5000/api/users/" + _id
        r = requests.put(url,data=payload,headers=headers)
        message ='{"statusCode":406,"error":"Not Acceptable","message":"Email should not be empty"}'
        if r.text != message:
            mongo.deleteOne({"pass":"test1"})
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    data={ "email" : "testtest@com", "role" : "administrator" }
    payload =json.dumps(data)
    try:
        r = requests.put(url,data=payload,headers=headers)
        message ='{"statusCode":406,"error":"Not Acceptable","message":"Password should not be empty"}'
        if r.text != message:
            mongo.deleteOne({"pass":"test1"})
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    data={ "email" : "testtest@com", "pass" : "test1" }
    payload =json.dumps(data)
    try:
        r = requests.put(url,data=payload,headers=headers)
        message ='{"statusCode":406,"error":"Not Acceptable","message":"Role should not be empty"}'
        if r.text != message:
            mongo.deleteOne({"pass":"test1"})
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    data={ "email" : "testtest@com", "pass":"test1","role" : "Worng"}
    payload =json.dumps(data)
    try:
        r = requests.put(url,data=payload,headers=headers)
        mongo.deleteOne({"pass":"test1"})
        message ='{"statusCode":406,"error":"Not Acceptable","message":"Role malformed"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    data = { "email" : "testtest@com", "pass":"test1","role" : "user"}
    data_to_update = { "email" : "testtest@com", "pass":"test1","role" : "administrator" }
    payload =json.dumps(data_to_update)
    try:
        mongo.addOne(data)
        user = mongo.getOne({"pass":"test1"})
        _id = str(user["_id"])
        url = "http://localhost:5000/api/users/" + _id
        r = requests.put(url,data=payload,headers=headers)
        user_update = mongo.getOne({"pass":"test1"})
        mongo.deleteOne({"pass":"test1"})
        if user_update['role'] != "administrator":
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    return 0

def testDelete(token_admin,token_user):
    mongo = Mongo("mongodb://localhost:27017","devices_db","users")
    mongo.deleteMany({"pass":"test1"})
    headers = {
        'authorization':"Bearer" + " " + token_user,
        'Content-Type': 'application/json'
    }
    data = "63a00891cb2005d2a0ee3f1f"
    payload =json.dumps(data)
    url = "http://localhost:5000/api/users/" + "test"
    try:
        r = requests.delete(url,data=payload,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"You cannot access to the user"}'
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
    url = "http://localhost:5000/api/users/"
    try:
        r = requests.delete(url,data=payload,headers=headers)
        message='{"statusCode":500,"error":"Internal Server Error","message":"Cast to ObjectId failed for value \\"\\" (type string) at path \\"_id\\" for model \\"users\\""}' 
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    url = "http://localhost:5000/api/users/" + data
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
    data = { "email" : "testtest@com", "pass":"test1","role" : "administrator" ,"role" : "user"}
    try:
        mongo.addOne(data)
        user = mongo.getOne({"pass":"test1"})
        _id = str(user['_id'])
        url = "http://localhost:5000/api/users/" + _id
        r = requests.get(url,headers=headers)
        mongo.deleteOne({"pass":"test1"})
        res = r.json()
        if res is None:
            print("テストに失敗しました。")
            exit(1)
        if res['role'] != user['role']:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    return 0

def testDeleteMany(token_admin,token_user):
    mongo = Mongo("mongodb://localhost:27017","devices_db","users")
    mongo.deleteMany({"pass":"test1"})
    headers = {
        'authorization':"Bearer" + " " + token_user,
        'Content-Type': 'application/json'
    }
    data = ["63a00891cb2005d2a0ee3f1f","63a00891cb2005d2a0ee3f1f"]
    payload =json.dumps(data)
    url = "http://localhost:5000/api/users"

    try:
        r = requests.delete(url,data=payload,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"You cannot access to the users"}'
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
        message='{"statusCode":500,"error":"Internal Server Error","message":"Cast to ObjectId failed for value \\"test\\" (type string) at path \\"_id\\" for model \\"users\\""}' 
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
        message='{"statusCode":406,"error":"Not Acceptable","message":"IDs should not be empty"}' 
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    data1 = { "email" : "testtest1@com", "pass":"test1","role" : "administrator" ,"role" : "user"}
    data2 = { "email" : "testtest2@com", "pass":"test1","role" : "administrator" ,"role" : "user"}
    data3 = { "email" : "testtest3@com", "pass":"test1","role" : "administrator" ,"role" : "user"}  
    try:
        mongo.addOne(data1)
        mongo.addOne(data2)
        mongo.addOne(data3)
        user_1 = mongo.getOne({"email" : "testtest1@com"})
        _id_1 = str(user_1['_id'])
        user_2 = mongo.getOne({"email" : "testtest2@com"})
        _id_2 = str(user_2['_id'])
        data=[]
        data.append(_id_1)
        data.append(_id_2)
        payload =json.dumps(data)
        url = "http://localhost:5000/api/users"
        r = requests.delete(url,data=payload,headers=headers)
        device_test_1 = mongo.getOne({"email" : "testtest1@com"})
        device_test_2 = mongo.getOne({"email" : "testtest2@com"})
        if device_test_1:
            mongo.deleteMany({"pass":"test1"})
            print("テストに失敗しました。")
            exit(1)
        if device_test_2:
            mongo.deleteMany({"pass":"test1"})
            print("テストに失敗しました。")
            exit(1)
        if mongo.getOne({"email" : "testtest3@com"}) is None:
            mongo.deleteMany({"pass":"test1"})
            print("テストに失敗しました。")
            exit(1)
        mongo.deleteMany({"csrGroup" : -1})
    except requests.HTTPError as e:
        print(e.status_code)
        print(e.text)
        print("テスト中にエラーが生じました。")
        exit(1)
    return 0

def testUserRoutes(token_admin,token_user):
    testCreate(token_admin,token_user)
    testFetch(token_admin,token_user)
    testGet(token_admin,token_user)
    testUpdate(token_admin,token_user)
    testDelete(token_admin,token_user)
    testDeleteMany(token_admin,token_user)