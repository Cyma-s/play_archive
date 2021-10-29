from pytube import Playlist
import os
import json

v = "https://www.youtube.com/playlist?list="


class PlayListInfo:

    def __init__(self, pl: Playlist = None):
        if pl is None:
            return
        self.list_id = pl.playlist_id
        self.list_name = pl.title
        self.videos = list()

    def toJSON(self):
        return json.dumps(self, default=lambda o:
        o.__dict__, sort_keys=True, indent=4, ensure_ascii=False)

    def fromJson(self, j):
        self.__dict__ = json.loads(j)
        self.videos = [VideoInfo().setDict(x) for x in self.videos]

class VideoInfo:
    def __init__(self, video = None, url = None):
        if video is None or url is None:
            return
        self.video_id = video.video_id
        self.video_title = video.title
        self.video_url = url
        self.is_deleted = False
        self.toJSON()

    def toJSON(self):
        return json.dumps(self, default=lambda o:
        o.__dict__, sort_keys=True, indent=4, ensure_ascii=False)

    def setDict(self, d):
        self.__dict__ = d
        return self


def download_list(list_id):
    pl = Playlist(v + list_id)
    print(pl.videos)
    for video in pl.videos:
        # print(f"video title : {video.title}")
        first_video = video.streams.first()
        dir_path = ".\\"
        first_video.download(dir_path, filename_prefix=f"[{video.video_id}")


def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__


def get_playlist_info_by_id(id):
    pl = Playlist(v + id)
    return get_playlist_info(pl)


def get_playlist_info(pl: Playlist):
    play_list_info = PlayListInfo(pl)

    for video, url in zip(pl.videos, pl.video_urls):
        video_info = VideoInfo(video, url)
        play_list_info.videos.append(video_info)

    return play_list_info


def save_json(json_object):
    # json을 local에 저장
    try:
        if not os.path.exists('.\\playlist'):
            os.makedirs('.\\playlist')
        with open('.\\playlist\\' + json_object.list_id + ".json", "w", encoding='utf-8') as f:
            f.write(json_object.toJSON())
            # json.dump(json_object.toJSON(), f, indent=4)
            # f.write(json.dumps(json_object, ensure_ascii=False, indent='\t'))
    except OSError:
        print('Error: Creating directory')


def get_json(playlist_id):
    # local json 파일 읽기
    try:
        with open('.\\playlist\\'+playlist_id + ".json", 'r', encoding='utf-8') as f:
            f = f.read()
            playlist_info = PlayListInfo()
            playlist_info.fromJson(f)
            # data = json.dumps(data, default=dumper, indent='\t')
            # data = json.dumps(data, indent=4, ensure_ascii=False)
            # print(json.dumps(data, indent=4, ensure_ascii=False))
            return playlist_info
    except Exception as e:
        print("Error so we return none", e)
        return None


def refresh_playlist(playlist_id):
    prev_json = get_json(playlist_id)
    if prev_json is None:
        playlist_init = get_playlist_info_by_id(playlist_id)
        save_json(playlist_init)
        prev_json = playlist_init

    current_playlist = get_playlist_info_by_id(playlist_id)

    # merged_playlist는 current에서 새로 생긴거 + prev에서 있는데 current에는 없는거까지 다 포함해서 있어야 함
    # prev_json에는 1, 2, 3번 정보가 있다.
    # current_json에는 1, 3, 4번 정보가 있다.
    # merged_playlist에는 1,2,3,4 번 정보가 있어야 한다. (번호는 영상 id)

    merged_playlist = get_playlist_info_by_id(playlist_id)
    merged_playlist.videos = list(prev_json.videos)
    prev_id_list = [x.video_id for x in prev_json.videos]
    for current_video in current_playlist.videos:
        if current_video.video_id not in prev_id_list:
            merged_playlist.videos.append(current_video)
    save_json(merged_playlist)


def backup_playlist(playlist_id):
    try:
        with open("./savedVideoInfo/.json", 'r', encoding='utf-8') as f:
            f = f.read()
            data = json.loads(f)
            print(json.dumps(data, indent=4, ensure_ascii=False))
    except:
        data = {
            "ids": [],
            "number": 0
        }
    stored_id = [x for x in data["ids"]]

    playInfo = get_playlist_info_by_id(playlist_id).list_id
    videos = get_playlist_info_by_id(playlist_id).videos

    for index in range(len(playInfo)):
        if playInfo[index] in stored_id:
            # 백업
            print(1/len(playInfo))
        pass

    pass
    # 백업을 해준다.
    # 백업, 한번에 다 하면 너무 많아
    # 그래서, 우리는 1개씩 해줄거다.
    # 이 함수를 호출하면, playlist 에 있는 영상중 백업이 안된 영상 1개를 찾아서 백업을 해줌 (백업이니까 등록시간이 가장 오래된거면 좋을듯?)
    # 그리고, 전체 n개 중에서 m개 백업을 하였습니다. 를 갯수를 반환해줘 (형식은 자유~)


if __name__ == "__main__":
    # playlist = input("플레이리스트 아이디? : ")
    playlist =  "PLk-LmkzFjEgU6fHg-tAK6sm2LKXCJ0Fvr"
    # download_list(playlist)
    refresh_playlist(playlist)
