from pytube import Playlist
import json

v = "https://www.youtube.com/playlist?list="


def download_list(list_id):
    pl = Playlist(v + list_id)
    print(pl.videos)
    for video in pl.videos:
        # print(f"video title : {video.title}")
        first_video = video.streams.first()
        dir_path = ".\\"
        first_video.download(dir_path)
    make_json(pl)


def make_json(pl: Playlist):
    json_dict = dict()
    json_dict['list_id'] = pl.playlist_id
    json_dict['list_name'] = pl.title
    json_dict['videos'] = list()
    video_urls = pl.video_urls
    i = 0
    for video in pl.videos:
        video_info = dict()
        video_info['video_id'] = video.video_id
        video_info['video_title'] = video.title
        video_info['video_url'] = video_urls[i]
        json_dict['videos'].append(video_info)

    with open(pl.playlist_id, "w", encoding='utf-8') as f:
        json.dump(json_dict, f, indent='\t')


playlist = input("플레이리스트 아이디? : ")
download_list(playlist)
