FROM python:3.8

# Installer les dépendances système
RUN apt-get update && apt-get install -y default-mysql-client

# Copier et installer les dépendances de votre application
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copier le code de l'application
COPY . /app

# Définir le répertoire de travail
WORKDIR /app

# Rendre le script wait-for-it.sh exécutable
RUN chmod +x wait-for-it.sh

# Commande par défaut
CMD ["./wait-for-it.sh", "db", "--", "python", "app.py"]
