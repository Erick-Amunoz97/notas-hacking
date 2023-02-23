# Bandit Level 0 -> Level 1


## objetivo
The password for the next level is stored in a file called **readme** located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

## Datos de acceso al nivel
** ssh bandit0@bandit.labs.overthewire.org -p 2220
**
bandit0
bandit0

## solucion
```bash()
bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ cat readme
NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL


```

## Notas adicionales
| comando | descripcion|
| cat | demuestra el contenido de un archivo 
| ls | demeuestra la lista de contenidos del directorio

## Referencias
[[https://www.geeksforgeeks.org/practical-applications-ls-command-linux/|Referencia del comando ls]]
[[https://www.geeksforgeeks.org/cat-command-in-linux-with-examples/|Referencia del comando cat]]
[[https://overthewire.org/wargames/bandit/bandit1.html|Link del Nivel 0 al 1]]

[[https://overthewire.org/wargames/bandit/bandit1.html|]]

