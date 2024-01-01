from bottle import Bottle as B,request as D,response,static_file
from pytube import YouTube as E
from pydub import AudioSegment as F
import os
A=B()
@A.route('/')
def C():return'\n<!DOCTYPE html>\n<html lang="en" data-bs-theme="dark">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>YouTube Downloader</title>\n    <script defer src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>\n    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">\n</head>\n<body>\n    <div class="container text-center pt-5">\n        <h1>YouTube Downloader</h1><br>\n        <form method="POST" action="/download">\n            <input class="form-control form-control" placeholder="YouTube video URL" type="text" id="video_url" name="video_url"><br>\n            <button class="btn btn-lg btn-success" type="submit">Download MP3</button>\n        </form>\n    </div>\n</body>\n</html>\n    '
@A.route('/download',method='POST')
def G():
	try:G=D.forms.get('video_url');H=E(G);B=H.streams.filter(only_audio=True).first();A=B.default_filename;C=f"./downloads/{os.path.splitext(A)[0]}.mp3";B.download(output_path='./downloads',filename_prefix='audio_');I=F.from_file(f"./downloads/audio_{A}");I.export(C,format='mp3');os.remove(f"./downloads/audio_{A}");os.startfile(os.path.abspath(C));return f'''
            <!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Downloader</title>
    <script defer src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container text-center pt-5">
        <h1>YouTube Downloader</h1><br>
        <p>Audio downloaded successfully.</p>
        <a href="/">Back</a>
    </div>
</body>
</html>
        '''
	except Exception as J:return f'''
            <!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Downloader</title>
    <script defer src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container text-center pt-5">
        <h1>YouTube Downloader</h1><br>
        <p>Error.</p>
        <a href="/">Back</a>
    </div>
</body>
</html>
        '''
A.run()