from celery import Celery
import math

app = Celery('tasks', broker='redis://localhost//', backend= 'redis://localhost:6379', include=['calc'])

@app.task()
def raiz_cuadrada(n):
    resultado = (n ** 0.5)
    return resultado

@app.task()
def potencia(n):
    resultado = (n ** 2)
    return resultado

@app.task()
def logaritmo(n):
    resultado = math.log10(n)
    return resultado