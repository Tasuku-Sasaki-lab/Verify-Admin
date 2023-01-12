import os
import math
import jwt
import time
import testJwtVerifyHook
import testAdminRoutes
import testDevicesRoutes
import testScepRoutes
import testUserRoutes
import testCertRoutes

def getToken(jwt_key):
    miriSecondNow = time.time()
    nbf = math.floor( miriSecondNow) 
    exp = nbf + 8*60*60 #exp = 8h
    signer = os.environ['SIGNER']
    jwtPayload = {
        "iss": signer,
        "sub": "testuser",
        "exp": exp,
        "nbf": nbf,
        "role":"administrator"
    }
    token_admin = jwt.encode(jwtPayload, jwt_key, algorithm="HS256")
    jwtPayload = {
        "iss": signer,
        "sub": "testuser",
        "exp": exp,
        "nbf": nbf,
        "role":"user"
    }
    token_user = jwt.encode(jwtPayload, jwt_key, algorithm="HS256")
    jwtPayload = {
        "iss": signer,
        "sub": "testuser",
        "exp": exp,
        "nbf": nbf,
        "role":"scepserver"
    }
    token_scepserver = jwt.encode(jwtPayload, jwt_key, algorithm="HS256")
    jwtPayload = {
        "iss": signer,
        "sub": "testuser",
        "exp": exp,
        "nbf": nbf,
        "role":"wrong"
    }
    token_wrong = jwt.encode(jwtPayload, jwt_key, algorithm="HS256")
    return token_admin,token_user,token_scepserver,token_wrong


def main ():
    try: 
        jwt_key = os.environ['JWT_KEY']
    except Exception as e:
        print(e)
        print('環境変数の設定に問題がある可能性があります')
        exit(1)

    token_admin,token_user,token_scepserver,token_wrong= getToken(jwt_key)
    #testJwtVerifyHook.testJwtVerifyHook(token_admin,token_wrong)
    #testAdminRoutes.testAdminRoutes()
    #testDevicesRoutes.testDevicesRoutes(token_admin,token_user,token_scepserver)
    #testScepRoutes.testScepRoutes(token_admin)
    #testuserroutes
    #testcertRoute
    testUserRoutes.testUserRoutes(token_admin,token_user)
    testCertRoutes.testCertRoutes(token_admin)
    print("テストは正常に終了しました。")

if __name__ == '__main__':
    main()
