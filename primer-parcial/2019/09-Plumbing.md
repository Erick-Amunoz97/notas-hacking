
# Plumbing

## Descripcion

Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to `jupiter.challenges.picoctf.org 4427`.

## Pistas

1. Remember the flag format is picoCTF{XXXX}
2. What's a pipe? No not that kind of pipe... This [kind](http://www.linfo.org/pipes.html)

## Solucion

```bash()
foxmcloud97-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 4427 | grep "pico"
picoCTF{digital_plumb3r_5ea1fbd7}
```

## Bandera

picoCTF{digital_plumb3r_5ea1fbd7}

## Notas adicionales

| comando | descripcion

| nc | El comando Netcat (nc) es una utilidad de línea de comandos para leer y escribir datos entre dos redes informáticas. |
| grep | El filtro grep busca en un archivo un patrón particular de caracteres y muestra todas las líneas que contienen ese patrón. | 

## Referencias
[[https://www.geeksforgeeks.org/grep-command-in-unixlinux/|Link para el comando grep]]
[[https://phoenixnap.com/kb/nc-command#:~:text=The%20Netcat%20(%20nc%20)%20command%20is,%2C%20ncat%20%2C%20and%20others).|Link para el comando nc]]