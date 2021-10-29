from pytube import Playlist

v = "https://www.youtube.com/playlist?list="


def download_list(list_id):
    pl = Playlist(v + list_id)
    print(pl.videos)
    for video in pl.videos:
        # print(f"video title : {video.title}")
        first_video = video.streams.first()
        dir_path = "E:\\Youtube\\"
        first_video.download(dir_path)


'''def show_progress(bytes_remaining, video):
    percent = round((1 - bytes_remaining / video.filesize) * 100, 3)
    if percent % 10 < 0.01:
        print('% done...')'''


playlist = input("플레이리스트 아이디? : ")
download_list(playlist)
