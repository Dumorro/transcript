#!/usr/bin/env python3

import os
import sys
import whisper
import time
import json
from datetime import datetime

def list_video_files(directory):
    """Lista todos os arquivos de vídeo no diretório."""
    video_extensions = ['.mp4', '.mkv', '.mov', '.avi', '.mpg', '.mpeg', '.wmv']
    video_files = []
    
    for file in os.listdir(directory):
        if any(file.lower().endswith(ext) for ext in video_extensions):
            video_files.append(os.path.join(directory, file))
    
    return video_files

def transcribe_video(model, video_path):
    """Transcreve um arquivo de vídeo usando o Whisper."""
    print(f"Transcrevendo: {os.path.basename(video_path)}")
    start_time = time.time()
    
    # Realizar a transcrição
    result = model.transcribe(video_path)
    
    # Calcular o tempo de processamento
    process_time = time.time() - start_time
    
    # Preparar nome de saída
    base_name = os.path.splitext(video_path)[0]
    
    # Salvar como texto
    with open(f"{base_name}.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write(result["text"])
    
    # Salvar como JSON (inclui timestamps)
    #with open(f"{base_name}.json", "w", encoding="utf-8") as json_file:
    #    json.dump(result, json_file, ensure_ascii=False, indent=2)
    
    print(f"Transcrição concluída em {process_time:.2f} segundos")
    print(f"Arquivos salvos: {base_name}.txt e {base_name}.json")

def main():
    video_dir = "/app/videos"
    
    # Verificar se há arquivos de vídeos disponíveis
    video_files = list_video_files(video_dir)
    
    if not video_files:
        print("Nenhum arquivo de vídeo encontrado em /app/videos")
        print("Formatos suportados: mp4, mkv, mov, avi, mpg, mpeg, wmv")
        sys.exit(1)
    
    # Carregar modelo do Whisper (tamanho médio)
    print("Carregando modelo Whisper...")
    model = whisper.load_model("medium")
    
    # Criar pasta para logs
    log_dir = os.path.join(video_dir, "logs")
    os.makedirs(log_dir, exist_ok=True)
    
    # Iniciar arquivo de log
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"transcription_log_{timestamp}.txt")
    
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"Transcrição iniciada em: {datetime.now()}\n")
        f.write(f"Arquivos para processamento: {len(video_files)}\n\n")
    
    # Processar cada vídeo
    for video_path in video_files:
        try:
            transcribe_video(model, video_path)
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"Sucesso: {os.path.basename(video_path)}\n")
        except Exception as e:
            print(f"Erro ao processar {os.path.basename(video_path)}: {str(e)}")
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"Erro: {os.path.basename(video_path)} - {str(e)}\n")
    
    print("\nProcessamento concluído!")
    print(f"Log salvo em: {log_file}")

if __name__ == "__main__":
    main()