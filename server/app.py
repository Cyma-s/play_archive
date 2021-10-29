from flask import Flask
from flask import Response

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world"

@app.route("/melody")
def my_melody():
    my_res = Response("my_melody")

    # Access-Control-Allow-Origin추가: '*'는 모든 사이트를 추가한다는 뜻.
    my_res.headers["Access-Control-Allow-Origin"] = "*"

    ## 특정 사이트를 추가하려면 아래처럼 * 대신 넣으면 됨
    # my_res.headers["Access-Control-Allow-Origin"] = 'https://www.coding-groot.tistory.com/'

    return my_res

if __name__ == "__main__":
    app.run(host="0.0.0.0")
