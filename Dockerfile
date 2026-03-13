# Dockerfile
FROM python:3.11-slim

# Metadata
LABEL maintainer="tu-email@example.com"
LABEL description="Simple web scraper con Python"

# Directorio de trabajo
WORKDIR /app

# Copiar requirements primero (para cachear layers)
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY scraper.py .

# Crear directorio para output
RUN mkdir -p /app/data

# Variable de entorno por defecto
ENV TARGET_URL=https://example.com

# Ejecutar scraper
CMD ["python", "scraper.py"]
