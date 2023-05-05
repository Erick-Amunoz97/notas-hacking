
# Static aint always noise

## Descripcion

Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/static)? This [BASH script](https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/ltdis.sh) might help!

## Pistas

## Solucion

```bash()
foxmcloud97-picoctf@webshell:~$ wget https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/static
--2023-03-05 07:08:53--  https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/static
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 8376 (8.2K) [application/octet-stream]
Saving to: 'static.1'

static.1                     100%[=============================================>]   8.18K  --.-KB/s    in 0s      

2023-03-05 07:08:53 (246 MB/s) - 'static.1' saved [8376/8376]

foxmcloud97-picoctf@webshell:~$ strings static | grep pico
picoCTF{d15a5m_t34s3r_f6c48608}
```

## Bandera

picoCTF{d15a5m_t34s3r_f6c48608}

## Notas adicionales

| comando | descripcion

| wget | El comando wget significa web get. El wget es un comando de descarga de archivos no interactivo gratuito. |
| strings | El comando de strings de Linux se utiliza para devolver los caracteres de cadena a los archivos. |
| grep | El filtro grep busca en un archivo un patrón particular de caracteres y muestra todas las líneas que contienen ese patrón. | 


## Referencias
[[https://www.javatpoint.com/linux-wget#:~:text=Command%20wget%20stands%20for%20web,while%20wget%20finish%20its%20work.|Link para el comando wget]]
[[https://www.javatpoint.com/linux-strings-command#:~:text=Linux%20strings%20command%20is%20used,text%20from%20an%20executable%20file.|Link para el comando strings]]
[[https://www.geeksforgeeks.org/grep-command-in-unixlinux/|Link para el comando grep]]