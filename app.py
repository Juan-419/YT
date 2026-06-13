import yt_dlp
import os

def descargar_mp3(url, carpeta_salida="descargas"):
    opciones = {
        'format': 'bestaudio/best',
        'outtmpl': f'{carpeta_salida}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True,
        'quiet': False,
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        info = ydl.extract_info(url, download=True)
        titulo = info.get('title', 'archivo')

    ruta_final = os.path.abspath(f"{carpeta_salida}/{titulo}.mp3")
    print("\n" + "="*50)
    print("✅ ¡Descarga completada con éxito!")
    print(f"📁 Archivo guardado en: {ruta_final}")
    print("="*50)

if __name__ == "__main__":
    os.makedirs("descargas", exist_ok=True)
    url = input("Pega el link del video de YouTube: ")
    descargar_mp3(url)
    input("\nPresiona Enter para salir...")