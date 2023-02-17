# Bandit Level 1 -> Level 2




## objetivo
The password for the next level is stored in a file called **-** located in the home directory

## Datos de acceso al nivel
** ssh bandit1@bandit.labs.overthewire.org -p 2220
**
bandit1
NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL


## solucion
```bash()
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ cat -
^C
bandit1@bandit:~$ cat ./-
rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi
bandit1@bandit:~$ pwd
/home/bandit1
bandit1@bandit:~$ cat /home/bandit1/-
rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi
```

## Notas adicionales
| comando | descripcion
| cat | demuestra el contenido de un archivo 
| ls | demeuestra la lista de contenidos del directorio

## Referencias
[[https://www.geeksforgeeks.org/practical-applications-ls-command-linux/|Referencia del comando ls]]
[[https://www.geeksforgeeks.org/cat-command-in-linux-with-examples/|Referencia del comando cat]]
[[https://overthewire.org/wargames/bandit/bandit2.html|Link del nivel 1 al 2]]


