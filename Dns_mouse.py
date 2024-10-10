import requests
import argparse

GREEN = '\033[92m'
RESET = '\033[0m'

def show_header():
    print(f"{GREEN}")
    print("#########################################")
    print("#         Subdir Scanner Tool           #")
    print("#        Criado por: LipeOzzy           #")
    print("#########################################")
    print(f"{RESET}")

# função para escanear os diretórios
def scan_de_diretorios(url, wordlist):
    print(f"[!] inciando a varredura em: {url}\n")
    
    #le a wordlist
    with open(wordlist, 'r') as f:
        diretorios =f.read().splitlines()
    
    #adiciona sobre a url os subdiretorios da wordlist
    for diretorio in diretorios:
        diretorio_url = f"{url}/{diretorio}"
        
        try:
            # envia uma requisição GET para o diretorio
            responde = requests.get(diretorio_url)
            