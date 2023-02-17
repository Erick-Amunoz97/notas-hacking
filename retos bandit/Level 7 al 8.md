# Bandit Level 7-> Level 8

## objetivo
The password for the next level is stored in the file **data.txt** next to the word **millionth**

## Datos de acceso al nivel
**ssh bandit7@bandit.labs.overthewire.org -p 2220**
bandit7
z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S

## solucion
```bash()
bandit7@bandit:~$ ls
data.txt
bandit7@bandit:~$ wc data.txt
  98567  197133 4184396 data.txt
bandit7@bandit:~$ grep -i "millionth" data.txt
millionth       TESKZC0XvTetK0S9xNwm25STk5iWrBvP

```

## Notas adicionales
| comando | descripcion|
| wc | wc significa "word count" es decir el numero de palabras. Se usa principalmente para el proposito de contar. Nos deja saber el **numero de lineas, numero de palabras y el numero de bytes y caracteres** dentro de el archivo especificado|
| grep | es un filtro que busca un patron de caracteres dentro de un archivo, y nos demuestra todas las lineas que contengan ese patron.
| grep -i | ignora si la palabra tiene mayusculas o minusculas e incluye todas las palabras que sean iguales sin importar lo anterior mencionado.
| cat | demuestra el contenido de un archivo 
| ls | demeuestra la lista de contenidos del directorio
## Referencias
[[https://www.geeksforgeeks.org/practical-applications-ls-command-linux/|Referencia del comando ls]]
[[https://www.geeksforgeeks.org/cat-command-in-linux-with-examples/|Referencia del comando cat]]
[[https://www.geeksforgeeks.org/grep-command-in-unixlinux/|Referencia de comando grep]]
[[https://www.geeksforgeeks.org/wc-command-linux-examples/|Referencia de Comando wc]]
[[https://overthewire.org/wargames/bandit/bandit8.html|Link del nivel 7 al 8]]


