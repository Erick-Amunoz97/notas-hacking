# Bandit Level 9 -> Level 10

## objetivo

The password for the next level is stored in the file **data.txt** in one of the few human-readable strings, preceded by several ‘=’ characters.

## Datos de acceso al nivel
**ssh bandit9@bandit.labs.overthewire.org -p 2220**
bandit9
EN632PlfYiZbn3PhVK3XOGSlNInNE00t

## solucion
```bash()
bandit9@bandit:~$ ls
data.txt
bandit9@bandit:~$ file data.txt
data.txt: data
bandit9@bandit:~$ strings data.txt | grep ==
f========== theM
========== password
========== is
========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
bandit9@bandit:~$ 

```

## Notas adicionales
| ls | demeuestra la lista de contenidos del directorio |
| grep | es un filtro que busca un patron de caracteres dentro de un archivo, y nos demuestra todas las lineas que contengan ese patron |
| file | determina el tipo de archivo |
| strings | se utiliza para devolver los caracteres de tipo string a los archivos. Se enfoca principalmente en determinar el contenido y extraer texto de los archivos binarios(archivo que no es de texto) |



## Referencias
[[https://www.google.com/search?q=eng+to+spa&rlz=1C1VDKB_enUS932US932&oq=eng+to+spa&aqs=chrome.0.69i59l2j46i131i199i433i465j0i131i433i512l3j0i131i433j0i10i433j0i131i433.856j0j7&sourceid=chrome&ie=UTF-8|Referencia de Comando strings]]
[[https://www.geeksforgeeks.org/practical-applications-ls-command-linux/|Referencia del comando ls]]
[[https://www.geeksforgeeks.org/grep-command-in-unixlinux/|Referencia de comando grep]]
[[https://man7.org/linux/man-pages/man1/file.1.html|Referencia del comando file]]
[[https://overthewire.org/wargames/bandit/bandit10.html|Referencia del nivel 9 al 10]]


