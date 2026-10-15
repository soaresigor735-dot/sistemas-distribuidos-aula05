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

#sistema de estoque
import threading
import time

estoque = 5
lock = threading.Lock()

def comprar(cliente):
    global estoque

    with lock:
        if estoque > 0:
            print(cliente, "encontrou", estoque, "unidade(s)")
            time.sleep(0.5)
            estoque -= 1
            print(cliente, "comprou. Restam:", estoque)
        else:
            print(cliente, "não conseguiu comprar: estoque esgotado")
clientes = []

for i in range(1, 9):
    t = threading.Thread(target=comprar, args=(f"Cliente {i}",))
    clientes.append(t)
    t.start()

for t in clientes:
    t.join()

print("Estoque final:", estoque)
#resposta
Cliente 1 encontrou 5 unidade(s)
Cliente 1 comprou. Restam: 4
Cliente 2 encontrou 4 unidade(s)
Cliente 2 comprou. Restam: 3
Cliente 3 encontrou 3 unidade(s)
Cliente 3 comprou. Restam: 2
Cliente 4 encontrou 2 unidade(s)
Cliente 4 comprou. Restam: 1
Cliente 5 encontrou 1 unidade(s)
Cliente 5 comprou. Restam: 0
Cliente 6 não conseguiu comprar: estoque esgotado
Cliente 7 não conseguiu comprar: estoque esgotado
Cliente 8 não conseguiu comprar: estoque esgotado
Estoque final: 0
