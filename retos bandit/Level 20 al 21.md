# Bandit Level 20 -> Level 21



## objetivo
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

## Datos de acceso al nivel
**ssh bandit20@bandit.labs.overthewire.org -p 2220**
bandit20
VxCazJaVykI6W36BkBU0mJTCM8rR95XT


## solucion
```bash()
bandit20@bandit:~$ nc -lnvp 2020 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT &
[1] 2289870
bandit20@bandit:~$ Listening on 0.0.0.0 2020
./suconnect 2020
Connection received on 127.0.0.1 44188
Read: VxCazJaVykI6W36BkBU0mJTCM8rR95XT
Password matches, sending next password
NvEJF7oVjkddltPSrdKEFOllh9V1IBcq
[1]+  Done                    nc -lnvp 2020 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT
bandit20@bandit:~$ exit
```

## Notas adicionales
| comando | descripcion
| nc | Netcat es una de las poderosas herramientas de red, herramienta de seguridad o herramienta de monitoreo de red. Actúa como un comando de tipo "cat" en una red. Incluso se considera como una navaja suiza de herramientas de red. |

## Referencias
[[https://www.geeksforgeeks.org/practical-uses-of-ncnetcat-command-in-linux/|Link del comando nc]]