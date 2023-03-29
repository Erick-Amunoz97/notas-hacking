# Reverse

## Objetivo

Try reversing this file? Can ya?
I forgot the password to this [file](https://artifacts.picoctf.net/c/275/ret). Please find it for me?

## Solución

Se descarga el archivo y se realiza lo siguiente:

```bash
hone@unidad03:~$ strings ret | grep pico
picoCTF{H
Password correct, please see flag: picoCTF{3lf_r3v3r5ing_succe55ful_7851ef7d}
```

Bandera: picoCTF{3lf_r3v3r5ing_succe55ful_7851ef7d}

## Referencias
