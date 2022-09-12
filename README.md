# Verify-admin

  

CSR_mongo(https://github.com/tasuku-revol/CSR_mongo) に関連し、ユーザーとsecret等を管理する画面

## DEMO

![スクリーンショット 2022-09-10 15 39 32](https://user-images.githubusercontent.com/74899466/189472401-6d365575-c32c-4f7e-92b5-b9a09757afd4.png)


  

## Environment


* GCP e2-standard-2（開発者のマシン）

## Usage

* レポジトリをクローン

  

```bash

git@github.com:tasuku-revol/Verify-Admin.git
cd Verify-admin

```

  

* サーバーの立ち上げ

  

```bash

cd notes-server
npm init -y
npm install fastify mongoose --save
npm start

```

  

* クライアントの立ち上げ

  

```bash

cd ~

cd notes-client
npm install react-admin @material-ui/core --save
npm start

```

  

* mongoに管理者を手動で登録

  

```bash

mongo

use notes_db

db.admins.insert({"email":"test@com","pass":"hogehoge"})

```

  

（http://localhost:3000/) にアクセス

## Features

### DB構造
 * db : notes_db
 * collection1 : admins
 * collection2 : notes
 
 #### adimins : 
 
```bash
	
	noteSchema = new  Schema({

	email:{type:String,reqiured:true},

	pass:{type:String,reqiured:true}

	});
	
```
	
 #### notes :
 
```bash
	
	noteSchema = new  Schema({

	csrID:{type:Number,reqiured:true},

	csrGroup:{type:Number,reqiured:true},

	CN:{type:String,reqiured:true},

	email:{type:String,reqiured:true},

	secret:{type:String,reqiured:true},

	status:{type:String,reqiured:true},

	expiration_date:{ type:  Date, required:true},

	pem:{type:String}

	});
	
```
	   

### CNに関して
CSRのCNはRFC4514 Distinguished Name string (https://www.ietf.org/rfc/rfc4514.txt) に準拠します。

  

## Note

* 開発段階で管理者の認証情報を手動で登録しています。

  

* DBの構成を後々修正いたします。

  

* JWT検証を後々開発します。

  

* APIでのDBの更新を後々開発します。

  

## Author

* Tasuku Sasaki

*  株式会社　プロキューブ

* t.sasaki.revol@gmail.com

