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
  print(f'\n[>] Verificando {ip}')
  print(f'[>] La IP {ip} es válida y está en la lista')
  main()
  
else:
  print(f'\n[>] Verificando {ip}')
  time.sleep(3)
  print(f'\n[>] La IP {ip} no está en la lista')
  exit()
