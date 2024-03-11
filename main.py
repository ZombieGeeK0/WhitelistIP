# importamos las librerías necesarias 
import requests, sys, socket

ip = socket.gethostname()

def exit():
  sys.exit()

def main(): 
  print('\n[>] Hello World\n')  # escribe aquí el código de tu programa 

url = 'https://github.com/ZombieGeeK0/WhitelistIP/list.txt'
request = requests.get(url)
 
if ip in request:
  print(f'[>] Verificando {ip}')
  
  
else:
  print(f'Verifying IP: {ip}')
  time.sleep(3)
  print('\n [>] No estás en la lista')
  exit()
