# Bandit Level 2 -> Level 3




## objetivo
The password for the next level is stored in a file called **-** located in the home directory

## Datos de acceso al nivel
**ssh bandit.labs.overthewire.org -p 2220**
bandit2
rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgziL


## solucion
```bash()
bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ cat 'spaces in this filename'
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
bandit2@bandit:~$ 


```

## Notas adicionales
| comando | descripcion
| cat | demuestra el contenido de un archivo 
| ls | demeuestra la lista de contenidos del directorio

## Referencias
https://overthewire.org/wargames/bandit/bandit3.html
