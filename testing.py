import requests
import re
import uuid
from bs4 import BeautifulSoup
from moviepy.editor import VideoFileClip



def TiktokDownloadAudio():
    def extract_video_id(url):
        pattern = r'/video/(\d+)'
        match = re.search(pattern, url)
        if match:
            return match.group(1)
        else:
            return None
    def download_video(url, filename):
        with open(filename, 'wb') as f:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                f.write(response.content)
                print("generate link ")
            else:
                print("Gagal mengenerate ")

    url = input("Masukan Link : ")
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    current_url = response.url
    IdVideo = extract_video_id(current_url)
    random_filename = str(uuid.uuid4()) + ".mp4"
    url_video = f"https://www.tikwm.com/video/media/play/{IdVideo}.mp4"
    download_video(url_video, random_filename)
    audio_filename = random_filename.split('.')[0] + ".mp3"
    video = VideoFileClip(random_filename)
    audio = video.audio
    audio.write_audiofile(audio_filename)
    video.close()
    import os
    os.remove(random_filename)
    return audio_filename
audio_file = TiktokDownloadAudio()
print("Download audio berhasil....")
