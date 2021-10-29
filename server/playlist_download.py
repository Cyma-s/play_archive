from pytube import Playlist
import json

v = "https://www.youtube.com/playlist?list="


class PlayListInfo:
    def toJSON(self):
        return json.dumps(self, default=lambda o:
        o.__dict__, sort_keys=True, indent=4)


class VideoInfo:
    def toJSON(self):
        return json.dumps(self, default=lambda o:
        o.__dict__, sort_keys=True, indent=4)


def download_list(list_id):
    pl = Playlist(v + list_id)
    print(pl.videos)
    for video in pl.videos:
        # print(f"video title : {video.title}")
        first_video = video.streams.first()
        dir_path = ".\\"
        first_video.download(dir_path, filename_prefix=f"[{video.video_id}")


def get_playlist(pl: Playlist):
    # playlist의 data를 받아와서 json return
    video_urls = pl.video_urls
    json_object = PlayListInfo()
    json_object.list_id = pl.playlist_id
    json_object.list_name = pl.title
    json_object.videos = list()
    i = 0
    for video in pl.videos:
        video_info = VideoInfo()
        video_info.video_id = video.video_id
        video_info.video_title = video.title
        video_info.video_url = video_urls[i]
        video_info.toJSON()
        json_object.videos.append(video_info)
        json_object.toJSON()
        return json_object


def save_json(json_object):
    # json을 local에 저장
    with open(json_object.list_id + ".json", "w", encoding='utf-8') as f:
        json.dump(json_object, f, indent='\t')


def get_json(pl: Playlist):
    # local json 파일 읽기
    with open(pl.playlist_id + ".json", 'r', encoding='utf-8') as f:
        f = f.read()
        data = json.loads(f)
    print(json.dumps(data, indent=4, ensure_ascii=False))


playlist = input("플레이리스트 아이디? : ")
download_list(playlist)
