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
| xx | xx el contenido de un archivo 

## Referencias
