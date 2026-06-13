# YouTube Audio Downloader

Script en Python para descargar audio de YouTube y convertirlo a MP3.

## Requisitos

- Python 3.10+
- ffmpeg instalado (`choco install ffmpeg`)

## Instalación

1. Clona el repositorio
```bash
   git clone https://github.com/Juan-419/YT.git
   cd YT
```

2. Crea y activa el entorno virtual
```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1
```

3. Instala las dependencias
```bash
   pip install -r requirements.txt
```

## Uso

```bash
python app.py
```

Pega el link del video de YouTube cuando se solicite. El MP3 quedará en la carpeta `descargas/`.