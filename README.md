# Verify-admin

  

CSR_mongo(https://github.com/tasuku-revol/CSR_mongo) に関連し、ユーザーとsecret等を管理する画面

## DEMO

![スクリーンショット 2022-09-10 15 39 32](https://user-images.githubusercontent.com/74899466/189472401-6d365575-c32c-4f7e-92b5-b9a09757afd4.png)


  

## Environment


* GCP e2-standard-2（開発者のマシン）
* MongoDB shell version v4.0.28

## Usage

* Mongoの起動　
　(https://www.mongodb.com/)

* レポジトリをクローン

  

```bash

git@github.com:tasuku-revol/Verify-Admin.git
cd Verify-admin

```

* 環境変数の設定

```bash

cd notes-server
vim .env

```



```bash

JWT_KEY="hoge"
JWT_KEY_SCEP="hoge"
DB_URL="mongodb://{url}/{db_name}"
SIGNER="hoge@hoge.com"

```
  
DB_URLの形式に注意してください。<br>
例えば、localhost、port番号が27017、DBの名前がnotes_dbの場合、mongodb://localhost:27017/notes_db　となります。

* サーバーの立ち上げ



  

```bash

cd notes-server
npm start

```

  

* クライアントの立ち上げ

  

```bash

cd ~

cd notes-client
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

* 開発段階で管理者の認証情報をDBに手動で登録しています。

  

* APIでのDBの更新を後々開発します。


## TEST 


* レポジトリをクローン

  

```bash

git@github.com:tasuku-revol/Verify-Admin.git
cd Verify-admin

```

* Mongoの起動　(https://www.mongodb.com/)
*  環境変数の設定


```bash

cd notes-server
vim .env

```

テスト用のDB_URLは固定です。下記から変更しないでください。DB_URL以外はお好みに変更していただいても問題ありません。

```bash

JWT_KEY="hoge"
export JWT_KEY
JWT_KEY_SCEP="hoge"
export JWT_KEY_SCEP
DB_URL="mongodb://localhost:27017/notes_db"
export DB_URL
SIGNER="hoge@hoge.com"
export SIGNER
```

```bash

source .env

```

*  サーバー側の起動

```bash

npm start

```

*  テスト環境の構築
```bash

cd ../test
pip install -r requirements.txt
source ../notes-server/.env

```
*  実行
```bash

python3 testNotes-server.py

```
  

## Author

* Tasuku Sasaki

*  株式会社　プロキューブ

* t.sasaki.revol@gmail.com

