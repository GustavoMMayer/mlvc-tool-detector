# Usa a imagem oficial da Ultralytics com Python e suporte a GPU/CPU
FROM ultralytics/ultralytics:latest

# Define o diretório de trabalho dentro do container
WORKDIR /usr/src/app


# Copia os arquivos do seu projeto para o container
COPY . .

# Instala dependências extras se você tiver um arquivo requirements.txt
# RUN pip install -r requirements.txt
