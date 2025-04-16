FROM python:3.10-slim

# Instalar ffmpeg e outras dependências
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Configurar diretório de trabalho
WORKDIR /app

# Instalar dependências Python
RUN pip install --no-cache-dir tqdm numpy
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir openai-whisper

# Criar diretório para arquivos de vídeo
RUN mkdir -p /app/videos

# Adicionar script de transcrição
COPY transcribe.py /app/

# Definir o volume
VOLUME ["/app/videos"]

# Comando para executar o script
ENTRYPOINT ["python", "/app/transcribe.py"]