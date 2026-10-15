import threading
import time

saldo = 1000

def sacar(valor):
    global saldo

    saldo_atual = saldo
    time.sleep(0.01)
    saldo = saldo_atual - valor

threads = []

for i in range(10):
    t = threading.Thread(target=sacar, args=(50,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Saldo esperado: 500")
print("Saldo obtido:", saldo)

#Resposta
Saldo esperado: 500
Saldo obtido: 950


#protegendo com lock
import threading
import time

saldo = 1000
lock = threading.Lock()

def sacar(valor):
    global saldo

    with lock:
        saldo_atual = saldo
        time.sleep(0.01)
        saldo = saldo_atual - valor

threads = []


print("Saldo esperado: 500")
print("Saldo obtido:", saldo)


#resposta
Saldo esperado: 500
Saldo obtido: 1000
