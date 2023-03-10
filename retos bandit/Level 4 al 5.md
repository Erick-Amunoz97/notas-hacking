# Bandit Level 4-> Level 5

## objetivo
The password for the next level is stored in the only human-readable file in the **inhere** directory. Tip: if your terminal is messed up, try the “reset” command.

## Datos de acceso al nivel
**ssh bandit4@bandit.labs.overthewire.org -p 2220**
bandit4
2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe

## solucion
```bash()
bandit4@bandit:~$ ls
inhere
bandit4@bandit:~$ cd ./inhere
bandit4@bandit:~/inhere$ ls
-file00  -file02  -file04  -file06  -file08
-file01  -file03  -file05  -file07  -file09
bandit4@bandit:~/inhere$ file ./*
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
bandit4@bandit:~/inhere$ cat ./-file07
lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR

```

## Notas adicionales
| comando | descripcion
| cat | demuestra el contenido de un archivo 
| ls | demeuestra la lista de contenidos del directorio
| file | determina el tipo de archivo
|"file ./*"| demuestra el tipo de todos los archivos

## Referencias
[[https://www.geeksforgeeks.org/practical-applications-ls-command-linux/|Referencia del comando ls]]
[[https://www.geeksforgeeks.org/cat-command-in-linux-with-examples/|Referencia del comando cat]]
[[https://man7.org/linux/man-pages/man1/file.1.html|Referencia del comando file]]
[[https://overthewire.org/wargames/bandit/bandit5.html|Link del nivel 4 al 5]]
