# Bandit Level 8-> Level 9

## objetivo
The password for the next level is stored in the file **data.txt** and is the only line of text that occurs only once


## Datos de acceso al nivel
**ssh bandit8@bandit.labs.overthewire.org -p 2220**
bandit8
TESKZC0XvTetK0S9xNwm25STk5iWrBvP
## solucion
```bash
bandit8@bandit:~$ ls
data.txt
bandit8@bandit:~$  wc data.txt
 1001  1001 33033 data.txt
bandit8@bandit:~$ cat data.txt | sort | uniq -u
EN632PlfYiZbn3PhVK3XOGSlNInNE00t

```

## Notas adicionales

| wc | wc significa "word count" es decir el numero de palabras. Se usa principalmente para el proposito de contar. Nos deja saber el **numero de lineas, numero de palabras y el numero de bytes y caracteres** dentro de el archivo especificado|
|sort | es un comando que ordena los contenidos de un archivo de texto linea por linea|
|uniq | es un a utilidad que reporta o filtra las lineas repetidas dentro de un archivo y las borra dejando solo las lineas unicas|
|uniq -u | Imprime solo las lineas unicas|
| cat | demuestra el contenido de un archivo 
| ls | demeuestra la lista de contenidos del directorio

## Referencias
[[https://www.geeksforgeeks.org/sort-command-linuxunix-examples/|Referencia de Comando Sort]]
[[https://www.geeksforgeeks.org/uniq-command-in-linux-with-examples/|Referencia de Comando uniq]]
[[https://www.geeksforgeeks.org/practical-applications-ls-command-linux/|Referencia del comando ls]]
[[https://www.geeksforgeeks.org/cat-command-in-linux-with-examples/|Referencia del comando cat]]
[[https://www.geeksforgeeks.org/wc-command-linux-examples/|Referencia de Comando wc]]
[[https://overthewire.org/wargames/bandit/bandit9.html|Link del nivel 8 al 9]]

