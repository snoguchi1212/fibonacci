# n番目のフィボナッチ数列を返すAPI

## 機能
n番目のフィボナッチ数列を返すAPIです。

## 使用技術
### リポジトリ内
python==3.10  
fastAPI==0.88.0  
pydantic>=1.2.0,<2.0.0  
httpx  
uvicorn
  
### デプロイ先
aws  
gunicorn  
nginx

## 使用方法
1. git cloneしてください
```shell
git clone https://github.com/snoguchi1212/fibonacci
```
2. cdコマンドでfibonacciに移動後、pipでインストールしてください
```shell
cd fibonacci
```
```shell
pip install -r requirements.txt
```
3. テストツールで利用しているpytestの都合上、ペアレントディレクトリの読み込みを行うために以下のコマンドを実行してください
```shell
pip install -e .
```
4. 以下のコマンドでローカルサーバーを立ち上げてください
```shell
uvicorn app.server.main:app --reload
```
5. `127.0.0.1:8000/fib/?n=3`(3のところは110000の整数値で変更自由)でレスポンスを受けることができます。


## ディレクトリ構造
```
.
├── README.md
├── app
│   ├── __init__.py
│   ├── __pycache__
│   ├── model
│   │   └── fibonacci.py
│   └── server
│       └── main.py
├── requirements.txt
├── setup.py
└── tests
    ├── test_model
    │   └── test_fibonacci.py
    └── test_server
        └── test_main.py
```

## 特徴
fastAPIを利用しているのでローカルサーバーを立ち上げて`127.0.0.1:8000/docs#/`にアクセスしていただくと、OpenAPIの形式でAPIドキュメントを見ることができるようになっています。

