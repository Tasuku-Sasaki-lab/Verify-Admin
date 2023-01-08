import sys
from mongo import Mongo
import json
import requests
import datetime
import time
import os
import math
import jwt

def testJwtVerifyHook(token,token_wrong):
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
    
    headers = {
        'authorization':"Bearer"+" " +token_wrong
    }
    try:
        r = requests.get(url, data=data,headers=headers)
        message ='{"statusCode":401,"error":"Unauthorized","message":"You do not have any roles"}'
        if r.text != message:
            print("テストに失敗しました。")
            exit(1)
    except Exception as e:
        print(e)
        print("テスト中にエラーが生じました。")
        exit(1)
 
    return 0

