# YouTube Audio Downloader

Script en Python para descargar audio de YouTube y convertirlo a MP3 usando `yt-dlp` y `ffmpeg`.

## Requisitos

- Python 3.10+
- ffmpeg instalado y agregado al PATH

## Instalación

1. Clona el repositorio
```bash
   git clone https://github.com/Juan-419/TU-REPO.git
   cd TU-REPO
```

2. Crea y activa un entorno virtual
```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1   # Windows
   source venv/bin/activate      # Linux/Mac
```

3. Instala las dependencias
```bash
   pip install -r requirements.txt
```

4. Instala ffmpeg
   - Windows: `choco install ffmpeg`
   - Linux: `sudo apt install ffmpeg`

## Uso

```bash
python descargaryt.py
```

Pega el link del video de YouTube cuando se solicite. El MP3 quedará en la carpeta `descargas/`.

## Nota

Este proyecto es para uso personal con contenido propio o con licencias que permitan su descarga. Respeta los términos de servicio de YouTube y los derechos de autor del contenido.