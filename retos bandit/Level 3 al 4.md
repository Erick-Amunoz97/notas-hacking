# Bandit Level 3 -> Level 4

## objetivo
The password for the next level is stored in a hidden file in the **inhere** directory.

## Datos de acceso al nivel
**ssh bandit.labs.overthewire.org -p 2220**
bandit3
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
## solucion
```bash()
bandit3@bandit:~$ cd
bandit3@bandit:~$ pwd
/home/bandit3
bandit3@bandit:~$ ls
inhere
bandit3@bandit:~$ cd inhere/
bandit3@bandit:~/inhere$ ls
bandit3@bandit:~/inhere$ ls
bandit3@bandit:~/inhere$ du --all
4       ./.hidden
8       .
bandit3@bandit:~/inhere$ cat ./.hidden
2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe

```

## Notas adicionales
| comando | descripcion
| cat | demuestra el contenido de un archivo 
| ls | demeuestra la lista de contenidos del directorio
|du | demuestra todos los archivos incluyendo los ocultos, ya que duemestra cuanto espacio ocupa cada uno. 
|du --all | escribe el contador para todos los archivos no solo los directorios. 

## Referencias
https://overthewire.org/wargames/bandit/bandit4.html
https://man7.org/linux/man-pages/man1/du.1.html