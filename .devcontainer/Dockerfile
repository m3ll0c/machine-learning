# Mantendo a base com suporte a GPU
FROM tensorflow/tensorflow:latest-gpu

# Evita prompts interativos durante a instalação
ENV DEBIAN_FRONTEND=noninteractive

# Atualiza o sistema e instala dependências básicas de compilação/sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Atualiza o pip e instala as bibliotecas Python
# Nota: Removi o tensorflow pois já vem na imagem base
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
    torch \
    torchvision \
    torchaudio \
    pandas \
    tqdm \
    numpy \
    seaborn \
    matplotlib \
    scikit-learn \
    ipykernel \
    kaggle \
    kagglehub

# Define o diretório de trabalho
WORKDIR /app

# Comando padrão ao iniciar o container
CMD ["bash"]