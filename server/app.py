import json

from flask import Flask
from flask import Response
from flask import request
from flask_cors import CORS

# (재훈재훈)
import playlist_download as pd
import playlist_download

app = Flask(__name__)
CORS(app)


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
    # (재훈재훈)
    id = request.args.get('id')
    playlist_info = pd.get_playlist_info_by_id(id)

    # 이거 한줄로 끝남
    videoIds = [x.video_id for x in playlist_info.videos]

    localVideos = pd.get_json(id)
    localVideoIds = [x['id'] for x in (localVideos if localVideos is not None else list())]

    return {"live": playlist_info.toJSON(), "local": localVideos}

    videoIds.sort()
    localVideoIds.sort()

    # localVideoIds = ['id1', 'id2', 'id3', 'id4', 'id5', 'id6', 'id7']
    # videoIds = ['id1', 'id2', 'id3', 'id5', 'id7']
    deletedList = []

    for l_id in localVideoIds:
        if not videoIds or videoIds[0] != l_id:
            deletedList.push(l_id)
        else:
            videoIds.pop()

    print(deletedList)
    # (재훈훈끝)

    id = request.args.get('id')

    playlist_download.download_list(id)

    playlist = playlist_download.get_json(id)

    ## 뒤에 id를 가져와서
    ## playlist_download.py 에 있는 코드 불러서
    ## 인터넷에서 한번 가져온다.
    ## 인터넷에서 가져온건 삭제된 것이 비어있다.
    ## 하지만 우리 로컬에 저장되어있는 파일, 삭제된것이 안 비어 있을 수 있다.
    ## 그 리스트를 쭉 만들때
    ## 인터넷에서 이 곡은 삭제되었다. 하지만 우리가 정보를 들고있다를 포함한 정보를 쭉 보내준다.

    return playlist

@app.route("/refresh_playlist")
def refresh_playlist():
    id = request.args.get('id')

    # playlist_download.refresh_playlist(id)

    return "너는 한개의 플레이리스트가 최신으로 되었을거야 " + id


@app.route("/backup_playlist")
def backup_playlist():
    id = request.args.get('id')

    # playlist_download.backup_playlist(id)

    return "너는 한개의 플레이리스트가 백업되었을것이야 " + id


if __name__ == "__main__":
    app.run(host="0.0.0.0")
