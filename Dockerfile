FROM python:3.12-slim

# Instalar ffmpeg
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar e instalar dependencias primero (mejor cacheo)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Crear carpeta de descargas
RUN mkdir -p descargas

EXPOSE 10000

CMD ["gunicorn", "-b", "0.0.0.0:10000", "app:app"]