# Bandit Level -> Level



## objetivo
The password for the next level is stored in the file **data.txt**, which contains base64 encoded data


## Datos de acceso al nivel
**ssh bandit10@bandit.labs.overthewire.org -p 2220**
bandit10
G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s



## solucion
```bash()
bandit10@bandit:~$ ls
data.txt
bandit10@bandit:~$ cat data.txt
VGhlIHBhc3N3b3JkIGlzIDZ6UGV6aUxkUjJSS05kTllGTmI2blZDS3pwaGxYSEJNCg==
bandit10@bandit:~$ echo "hola mundo"
hola mundo
bandit10@bandit:~$ echo "hola mundo" | base64
aG9sYSBtdW5kbwo=
bandit10@bandit:~$ echo -n ^C
bandit10@bandit:~$ echo -n aG9sYSBtdW5kbwo= |base64 -d
hola mundo
bandit10@bandit:~$ base64 -d data.txt
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
```

## Notas adicionales
| comando | descripcion |
| ls | demeuestra la lista de contenidos del directorio |
| cat | demuestra el contenido de un archivo |
| Base64 | es para convertir un texto a una codificacion de base 64 |
| Base64 -d | Decodifica de base64 a texto. |
| echo | es para mostrar una linea de texto/cadena que se pasa como argumento. Este comando es incorporado principalmente en scripts de shelly archivos de tipo bash para generar texto en la pantalla o en un archivo |
| echo -n | Muestra la salida del texto omitiendo la nueva linea despues de ella |



## Referencias
[[https://www.geeksforgeeks.org/practical-applications-ls-command-linux/|Referencia del comando ls]]
[[https://www.geeksforgeeks.org/cat-command-in-linux-with-examples/|Referencia del comando cat]]
[[https://www.geeksforgeeks.org/convert-text-file-strings-into-base64-encoding/|Refefencia del comando Base64]]
[[https://www.geeksforgeeks.org/echo-command-in-linux-with-examples/|Referencia del comando echo]]
[[https://overthewire.org/wargames/bandit/bandit11.html|Referencia del nivel 10 al 11]]


