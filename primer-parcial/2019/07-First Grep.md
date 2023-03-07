
# First Grep

## Descripcion

Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/515f19f3612bfd97cd3f0c0ba32bd864/file)? This would be really tedious to look through manually, something tells me there is a better way.

## Pistas

grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

## Solucion

```bash()
foxmcloud97-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/515f19f3612bfd97cd3f0c0ba32bd864/file
--2023-03-05 05:04:12--  https://jupiter.challenges.picoctf.org/static/515f19f3612bfd97cd3f0c0ba32bd864/file
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 14551 (14K) [application/octet-stream]
Saving to: 'file'

file                                                       100%[=======================================================================================================================================>]  14.21K  --.-KB/s    in 0s      

2023-03-05 05:04:12 (384 MB/s) - 'file' saved [14551/14551]
foxmcloud97-picoctf@webshell:~$ strings file | grep pico
picoCTF{grep_is_good_to_find_things_5af9d829}
```

## Bandera

picoCTF{grep_is_good_to_find_things_5af9d829}

## Notas adicionales

| comando | descripcion

| wget | El comando wget significa web get. El wget es un comando de descarga de archivos no interactivo gratuito. |
| strings | El comando de strings de Linux se utiliza para devolver los caracteres de cadena a los archivos. |
| grep | El filtro grep busca en un archivo un patrón particular de caracteres y muestra todas las líneas que contienen ese patrón. | 

## Referencias
[[https://www.geeksforgeeks.org/grep-command-in-unixlinux/|Link para el comando grep]]
[[https://www.javatpoint.com/linux-wget#:~:text=Command%20wget%20stands%20for%20web,while%20wget%20finish%20its%20work.|Link para el comando wget]]
[[https://www.javatpoint.com/linux-strings-command#:~:text=Linux%20strings%20command%20is%20used,text%20from%20an%20executable%20file.|Link para el comando strings]]

