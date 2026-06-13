from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__)
CARPETA_DESCARGAS = "descargas"
COOKIES_FILE = "cookies.txt"

def get_opciones_base(skip_download=False):
    opciones = {
        "quiet": True,
        "skip_download": skip_download,
        "noplaylist": True,
    }
    if os.path.exists(COOKIES_FILE):
        opciones["cookiefile"] = COOKIES_FILE
    return opciones

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/preview", methods=["POST"])
def preview():
    url = request.form.get("url")

    opciones = get_opciones_base(skip_download=True)

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            info = ydl.extract_info(url, download=False)
    except Exception as e:
        return render_template("index.html", error=f"No se pudo procesar el link: {e}")

    # Convertir duración a minutos:segundos
    duracion_raw = info.get("duration", 0)
    minutos = duracion_raw // 60
    segundos = duracion_raw % 60

    datos = {
        "titulo": info.get("title"),
        "miniatura": info.get("thumbnail"),
        "duracion": f"{minutos}:{segundos:02d}",
        "canal": info.get("uploader"),
        "vistas": f"{info.get('view_count', 0):,}".replace(",", "."),
        "url": url,
    }
    return render_template("index.html", datos=datos)

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url")

    opciones = get_opciones_base()
    opciones.update({
        "format": "bestaudio/best",
        "outtmpl": f"{CARPETA_DESCARGAS}/%(title)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    })

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            info = ydl.extract_info(url, download=True)
            titulo = info.get("title", "audio")
    except Exception as e:
        return render_template("index.html", error=f"Error al descargar: {e}")

    # Buscar el archivo mp3 generado
    ruta_mp3 = None
    for archivo in os.listdir(CARPETA_DESCARGAS):
        if archivo.endswith(".mp3"):
            ruta_mp3 = os.path.join(CARPETA_DESCARGAS, archivo)
            break

    if not ruta_mp3:
        return render_template("index.html", error="No se encontró el archivo MP3 generado.")

    # Enviar el archivo al navegador y borrarlo después
    return send_file(
        ruta_mp3,
        as_attachment=True,
        download_name=f"{titulo}.mp3",
        mimetype="audio/mpeg"
    )

if __name__ == "__main__":
    os.makedirs(CARPETA_DESCARGAS, exist_ok=True)
    app.run(debug=True)