from flask import Flask, render_template, request, redirect, url_for
import yt_dlp
import os

app = Flask(__name__)
CARPETA_DESCARGAS = "descargas"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/preview", methods=["POST"])
def preview():
    url = request.form.get("url")

    opciones = {"quiet": True, "skip_download": True}
    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            info = ydl.extract_info(url, download=False)
    except Exception as e:
        return render_template("index.html", error=f"No se pudo procesar el link: {e}")

    datos = {
        "titulo": info.get("title"),
        "miniatura": info.get("thumbnail"),
        "duracion": info.get("duration"),
        "canal": info.get("uploader"),
        "url": url,
    }
    return render_template("index.html", datos=datos)

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url")

    opciones = {
        "format": "bestaudio/best",
        "outtmpl": f"{CARPETA_DESCARGAS}/%(title)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "noplaylist": True,
        "quiet": True,
    }


    with yt_dlp.YoutubeDL(opciones) as ydl:
        info = ydl.extract_info(url, download=True)
        titulo = info.get("title")

    ruta = os.path.abspath(f"{CARPETA_DESCARGAS}/{titulo}.mp3")
    return render_template("resultado.html", titulo=titulo, ruta=ruta)

if __name__ == "__main__":
    os.makedirs(CARPETA_DESCARGAS, exist_ok=True)
    app.run(debug=True)