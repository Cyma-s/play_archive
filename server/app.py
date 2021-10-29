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

@app.route("/get_playlist")
def get_my_playlist():
    # http://localhost:5000/get_my_playlist?id=~~~~~~~~~

    ## 뒤에 id를 가져와서
    ## playlist_download.py 에 있는 코드 불러서
    ## 인터넷에서 한번 가져온다.
    ## 인터넷에서 가져온건 삭제된 것이 비어있다.
    ## 하지만 우리 로컬에 저장되어있는 파일, 삭제된것이 안 비어 있을 수 있다.
    ## 그 리스트를 쭉 만들때
    ## 인터넷에서 이 곡은 삭제되었다. 하지만 우리가 정보를 들고있다를 포함한 정보를 쭉 보내준다.

    pass

@app.route("/backup_playlist")
def backup_playlist():
    pass 

if __name__ == "__main__":
    app.run(host="0.0.0.0")
