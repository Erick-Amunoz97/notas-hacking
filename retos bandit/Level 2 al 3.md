# Bandit Level 2 -> Level 3

## objetivo
The password for the next level is stored in a file called **spaces in this filename** located in the home directory

## Datos de acceso al nivel
**ssh bandit2@bandit.labs.overthewire.org -p 2220**
bandit2
rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi


## solucion
```bash()
bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ cat 'spaces in this filename'
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
```

## Notas adicionales
| comando | descripcion
| cat | demuestra el contenido de un archivo 
| ls | demeuestra la lista de contenidos del directorio

## Referencias
[[https://www.geeksforgeeks.org/practical-applications-ls-command-linux/|Referencia del comando ls]]
[[https://www.geeksforgeeks.org/cat-command-in-linux-with-examples/|Referencia del comando cat]]
[[https://overthewire.org/wargames/bandit/bandit3.html|Link de nivel 2 al 3]]

