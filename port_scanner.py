import socket
import argparse
from threading import Thread
from queue import Queue
import threading

# Interface mais amigável com mensagens e opções padrão
def obter_parametros_user_friendly():
    print("Bem-vindo ao Port Scanner!")
    ip = input("Digite o endereço IP ou host que você deseja escanear (ex: 192.168.1.1): ")
    start_port = input("Digite a porta inicial para o escaneamento (pressione Enter para começar na porta 1): ")
    end_port = input("Digite a porta final para o escaneamento (pressione Enter para terminar na porta 1024): ")
    
    # Usar valores padrão caso o usuário não digite nada
    start_port = int(start_port) if start_port.strip() else 1
    end_port = int(end_port) if end_port.strip() else 1024
    
    # Permitir threads configuráveis
    num_threads = input("Digite o número de threads a serem usadas (pressione Enter para usar 10 threads): ")
    num_threads = int(num_threads) if num_threads.strip() else 10
    
    return ip, start_port, end_port, num_threads

# Função para verificar uma única porta TCP
def verificar_porta(ip, porta):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Tempo limite para a conexão
            if s.connect_ex((ip, porta)) == 0:
                return True
    except socket.error:
        pass
    return False

# Função para a thread escanear as portas
def escanear_fila():
    while not portas.empty():
        porta = portas.get()
        if verificar_porta(ip, porta):
            print(f"Porta {porta} está ABERTA")
            with lock:
                portas_abertas.append(porta)
        portas.task_done()

# Obter parâmetros do usuário de forma interativa
ip, start_port, end_port, num_threads = obter_parametros_user_friendly()

# Criar uma fila com as portas a serem escaneadas
portas = Queue()
for porta in range(start_port, end_port + 1):
    portas.put(porta)

# Lista e lock para armazenar portas abertas
portas_abertas = []
lock = threading.Lock()

# Criar as threads
threads = []
for _ in range(num_threads):
    t = Thread(target=escanear_fila)
    threads.append(t)
    t.start()

# Esperar todas as threads terminarem
portas.join()

# Exibe todas as portas abertas
print("Portas abertas:", portas_abertas)
