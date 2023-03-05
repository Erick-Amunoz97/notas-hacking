# Bandit Level -> Level



## objetivo
Good job getting a shell! Now hurry and grab the password for bandit27!

## Datos de acceso al nivel
**ssh bandit26@bandit.labs.overthewire.org -p 2220**
bandit26
c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1


## solucion
```bash
v
:set shell=/bin/bash
:shell
bandit26@bandit:~$ bandit26@bandit:~$ ls
bandit26@bandit:~$: command not found
bandit26@bandit:~$ ls
bandit27-do  text.txt
bandit26@bandit:~$ ./bandit27-do id
uid=11026(bandit26) gid=11026(bandit26) euid=11027(bandit27) groups=11026(bandit26)
bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27
YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS
bandit26@bandit:~$ 
```

## Notas adicionales
| comando | descripcion
| xx | xx el contenido de un archivo 

## Referencias
[[https://overthewire.org/wargames/bandit/bandit27.html|Link del nivel 26 al 27]]

