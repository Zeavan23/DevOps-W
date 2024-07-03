from flask import Flask, request, make_response
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import socket

app = Flask(__name__)

# Configuration de la base de données
DATABASE_URL = 'mysql+pymysql://myuser:mypassword@db/mydb'
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Définir la table access_log
class AccessLog(Base):
    __tablename__ = 'access_log'
    id = Column(Integer, primary_key=True)
    client_ip = Column(String(45))
    server_ip = Column(String(45))
    timestamp = Column(DateTime)

try:
    Base.metadata.create_all(engine)
except Exception as e:
    print(f"Erreur lors de la création des tables : {e}")

# Compteur global
counter = 0

@app.route('/')
def index():
    global counter
    counter += 1

    # Obtenir l'IP du client
    client_ip = request.remote_addr

    # Obtenir l'IP interne du serveur
    server_ip = socket.gethostbyname(socket.gethostname())

    # Définir le cookie
    response = make_response(server_ip)
    response.set_cookie('internal_ip', server_ip, max_age=5 * 60)

    # Enregistrer dans la base de données
    try:
        new_log = AccessLog(client_ip=client_ip, server_ip=server_ip, timestamp=datetime.now())
        session.add(new_log)
        session.commit()
    except Exception as e:
        print(f"Erreur lors de l'enregistrement du log : {e}")

    return response

@app.route('/showcount')
def showcount():
    return str(counter)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8003)
