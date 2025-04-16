# Container Docker para Transcrição de Vídeos

Este container utiliza o modelo Whisper da OpenAI para transcrever arquivos de vídeo em texto.

## Requisitos
- Docker instalado
- Arquivos de vídeo na pasta correspondente ao seu sistema operacional:
  - Windows: `C:\temp`
  - Linux: `/tmp` ou qualquer outro diretório
  - Mac: `/tmp` ou qualquer outro diretório

## Formatos de vídeo suportados
- MP4 (.mp4)
- MKV (.mkv)
- MOV (.mov)
- AVI (.avi)
- MPG/MPEG (.mpg, .mpeg)
- WMV (.wmv)

## Instruções de uso

### 1. Primeiro, crie os arquivos necessários

Salve o conteúdo do Dockerfile em um arquivo chamado `Dockerfile` e o script Python em um arquivo chamado `transcribe.py` no mesmo diretório.

### 2. Construa a imagem Docker

```bash
docker build -t video-transcriber .
```

### 3. Execute o container

#### Para Windows (usando PowerShell ou CMD):

```bash
docker run --rm -v C:\temp:/app/videos video-transcriber
```

#### Para Linux:

```bash
docker run --rm -v /caminho/para/seus/videos:/app/videos video-transcriber
```

Exemplo usando `/tmp`:
```bash
docker run --rm -v /tmp:/app/videos video-transcriber
```

#### Para Mac:

```bash
docker run --rm -v /caminho/para/seus/videos:/app/videos video-transcriber
```

Exemplo usando pasta do usuário:
```bash
docker run --rm -v ~/Videos:/app/videos video-transcriber
```

### 4. Resultados

Após a execução, para cada arquivo de vídeo processado, serão gerados:
- Um arquivo `.txt` com a transcrição completa do áudio
- Um arquivo `.json` com a transcrição e timestamps detalhados
- Um log do processamento na pasta `logs`

Os arquivos de saída serão salvos no mesmo diretório dos vídeos originais.

## Notas
- O processo de transcrição pode levar tempo, dependendo do tamanho e da quantidade dos vídeos
- O modelo utiliza a versão "medium" do Whisper, que oferece um bom equilíbrio entre precisão e velocidade
- Todo o processamento acontece localmente, os dados não são enviados para a internet
- Se seu sistema tiver GPU disponível, considere modificar o Dockerfile para usar a versão GPU do PyTorch para melhor desempenho

## Solução de problemas

### Problemas de permissão (Linux/Mac)
Se encontrar problemas de permissão ao executar o container, você pode adicionar a opção `--user` seguida do seu ID de usuário e grupo:

```bash
docker run --rm --user $(id -u):$(id -g) -v /caminho/para/seus/videos:/app/videos video-transcriber
```

### Vídeos não são detectados
Verifique se os vídeos estão em um dos formatos suportados e se o caminho do volume foi mapeado corretamente.