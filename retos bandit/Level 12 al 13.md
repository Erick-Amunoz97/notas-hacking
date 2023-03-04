# Bandit Level 12 -> Level 13



## objetivo
The password for the next level is stored in the file **data.txt**, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)

## Datos de acceso al nivel
**ssh bandit12@bandit.labs.overthewire.org -p 2220**
bandit12
JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv


## solucion
```bash()
bandit12@bandit:~$  xxd -r data.txt | file -
/dev/stdin: gzip compressed data, was "data2.bin", last modified: Tue Feb 21 22:02:52 2023, max compression, from Unix
bandit12@bandit:~$ xxd -r data.txt | zcat |file -
/dev/stdin: bzip2 compressed data, block size = 900k
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat |file -
/dev/stdin: POSIX tar archive (GNU)
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat | tar xO | file -
/dev/stdin: POSIX tar archive (GNU)
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat | tar xO | tar xO | file -
/dev/stdin: bzip2 compressed data, block size = 900k
bandit12@bandit:~$  xxd -r data.txt | zcat | bzcat | zcat | tar xO | tar xO | bzcat |file -
/dev/stdin: POSIX tar archive (GNU)
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | file -
/dev/stdin: gzip compressed data, was "data9.bin", last modified: Tue Feb 21 22:02:52 2023, max compression, from Unix
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | zcat | file -
/dev/stdin: ASCII text
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | zcat
The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw

```

## Notas adicionales
| comando | descripcion
| xxd | crea un "hex dump" de un archivo con el input. tambien puede covertir un "hex dump" a su forma binaria original. |
| xxd - r | operacion en reversa:  convierte un "hex dump" a su forma binaria original. |
| file | determina el tipo de archivo |
| zcat | para ahorrar tiempo y visualizar archivos sin descomprimirlos se utiliza el comando “zcat”. |
| bzcat | El comando bzcat mostrará los archivos comprimidos con el comando bzip. |
| tar | significa archivo de tipo "tape", se utiliza para crear "Archives" y extraer los archivos de los "Archives" | 

## Referencias
[[https://www.tutorialspoint.com/unix_commands/xxd.htm|Link del comando xxd]]
[[https://man7.org/linux/man-pages/man1/file.1.html|Referencia del comando file]]
[[https://www.javatpoint.com/linux-bzcat-bzmore|Link del comando bzcat]]
[[https://www.geeksforgeeks.org/tar-command-linux-examples/|Link del comando tar]]
[[https://overthewire.org/wargames/bandit/bandit13.html|Link del nivel 12 al 13]]
