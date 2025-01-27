from flask import Flask, request
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})

@app.route("/download", methods=["POST"])
def Download():
    options = {"format": 'best'}
    
    link = request.json
    
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download(link)
    return "video baixado com sucesso!"
    
if __name__ == "__main__":
    app.run(debug=True)