# Bandit Level 14 -> Level 15



## objetivo
The password for the next level can be retrieved by submitting the password of the current level to **port 30000 on localhost**.

## Datos de acceso al nivel
**ssh bandit14@bandit.labs.overthewire.org -p 2220**
bandit14


## solucion
```bash()
bandit14@bandit:~$ 
bandit14@bandit:~$ nc localhost 30000
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
Correct!
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt

^C
```

## Notas adicionales
| comando | descripcion
| nc | Netcat es una de las poderosas herramientas de red, herramienta de seguridad o herramienta de monitoreo de red. Actúa como un comando de tipo "cat" en una red. Incluso se considera como una navaja suiza de herramientas de red. Generalmente se utiliza por las siguientes razones:
-   Operaciones relacionadas con TCP, UDP or UNIX-domain sockets
-   Port Scanning
-   Port listening
-   Port redirection
-  Abre conecciones remotas
-   Read/Write de datos a lo largo del network
-   Debugging del network
-   Network daemon testing
-   Simple TCP proxies
-  comando de Socks o HTTP Proxy Command para ssh |

## Referencias
[[https://www.geeksforgeeks.org/practical-uses-of-ncnetcat-command-in-linux/|Link del comando nc]]
[[https://overthewire.org/wargames/bandit/bandit15.html|Link del nivel 14 al 15]]


