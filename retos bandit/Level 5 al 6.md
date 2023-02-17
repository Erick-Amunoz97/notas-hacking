# Bandit Level5 -> Level 6

## objetivo
The password for the next level is stored in a file somewhere under the **inhere** directory and has all of the following properties:

-   human-readable
-   1033 bytes in size
-   not executable

## Datos de acceso al nivel
**ssh bandit.labs.overthewire.org -p 2220**
bandit5
lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR

## solucion
```bash()
bandit5@bandit:~$ ls
inhere
bandit5@bandit:~$ cd ./inhere
bandit5@bandit:~/inhere$ ls
maybehere00  maybehere04  maybehere08  maybehere12  maybehere16
maybehere01  maybehere05  maybehere09  maybehere13  maybehere17
maybehere02  maybehere06  maybehere10  maybehere14  maybehere18
maybehere03  maybehere07  maybehere11  maybehere15  maybehere19
bandit5@bandit:~/inhere$ find . -readable -size 1033c -type f
./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU
```

## Notas adicionales
| comando | descripcion
| cat | demuestra el contenido de un archivo 
| ls | demeuestra la lista de contenidos del directorio
| find | usado para buscar archivos en la herarquia del directorio|
|find -readable| nos demuestra los archivos que pueden ser leidos por el usuario actual|
|find -type f| nos demuetra un archivo regular |
|find -size| encuentra un archivo que es menor o mas de o exactamente unidades n de spacio con redondeo hacia arriba. en este caso usamos el sufijo c ya que estabamos buscando en bytes

## Referencias
https://man7.org/linux/man-pages/man1/find.1.html
https://overthewire.org/wargames/bandit/bandit6.html