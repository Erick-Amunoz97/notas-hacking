# Bandit Level 20 -> Level 21



## objetivo

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
| xx | xx el contenido de un archivo 

## Referencias
