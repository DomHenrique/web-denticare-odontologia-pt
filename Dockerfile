# Usar uma imagem oficial do Python como base
FROM python:3.13-slim

# Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Definir o diretório de trabalho no container
WORKDIR /app

# Instalar dependências do sistema necessárias para o psycopg e outras libs
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Instalar as dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação
COPY . /app/

# Coletar arquivos estáticos (opcional, dependendo do setup)
# RUN python manage.py collectstatic --noinput

# Expor a porta 8000
EXPOSE 8000

# Comando para rodar a aplicação usando o Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "DentiCareWeb.wsgi:application"]
