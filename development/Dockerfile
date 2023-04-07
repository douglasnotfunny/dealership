# Use uma imagem base do Python 3.10, adaptando a versão e variante conforme necessário
FROM python:3.10-slim

# Configuração do diretório de trabalho no container
WORKDIR /app

# Copie os arquivos de requisitos do projeto Flask para o container
COPY requirements.txt .

# Instale as dependências do projeto Flask
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante dos arquivos do projeto para o container
COPY . .

# Exponha a porta que o aplicativo Flask irá usar
EXPOSE 5000

# Inicialize o aplicativo Flask
CMD ["python", "app.py"]
