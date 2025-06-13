# Punto de entrada: FastAPI + scheduler
from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from data_inserter import fetch_and_insert

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API corriendo..."}

# Agrega tarea cada X minutos
scheduler = BackgroundScheduler()
scheduler.add_job(fetch_and_insert, 'interval', minutes=1)  
scheduler.start()

