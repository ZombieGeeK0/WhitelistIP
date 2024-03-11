# importamos las librerías necesarias 
import requests, time, sys, socket

ip = socket.gethostname()

def exit():
  sys.exit()

def main(): 
  print('\n[>] Hello World\n')  # escribe aquí el código de tu programa 

url = 'https://github.com/ZombieGeeK0/WhitelistIP/list.txt'
request = requests.get(url)
 
whitelist_ip = [ 
  'https://github.com/ZombieGeeK0/WhitelistIP/list.txt'
]
 
if ip in whitelist_ip: # Here we check if the ip of the variable is in our list
  print(f'\n[>] Verificando IP: {ip}')
  time.sleep(3)
  print(f'[>] IP {ip} verificada')
  time.sleep(2)
  main()  # se ejecuta el código
  
else:
  print(f'Verifying IP: {ip}')
  time.sleep(3)
  print('\n [>] No estás en la lista')
  exit()
