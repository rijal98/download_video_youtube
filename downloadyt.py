from pytube import YouTube

def download_youtube_video(url, output_path='./'):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if video:
            print(f'Downloading "{yt.title}"...')
            video.download(output_path)
            print('Download complete!')
        else:
            print('Video not found.')
    except Exception as e:
        print(f'Error: {str(e)}')

# Contoh penggunaan:
if __name__ == "__main__":
    video_url = 'https://www.youtube.com/watch?v=rPysfjP_NWg'
    download_youtube_video(video_url)
