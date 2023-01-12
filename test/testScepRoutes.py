import sys
from mongo import Mongo
import json
import requests
import datetime
import time
import os
import math
import jwt

def testScepRoutes(token):
    url = "http://localhost:5000/scep"
    mongo = Mongo("mongodb://localhost:27017","devices_db","devices")
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
        message ='{"message":"The common name is not mathched"}'
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