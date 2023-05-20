
# Obedient Cat

## Descripcion

This file has a flag in plain sight (aka "in-the-clear"). [Download flag](https://mercury.picoctf.net/static/33996e32dce022205a6a36f69aba56f0/flag).

## Pistas

1. Any hints about entering a command into the Terminal (such as the next one), will start with a '$'... everything after the dollar sign will be typed (or copy and pasted) into your Terminal.
2. To get the file accessible in your shell, enter the following in the Terminal prompt: `$ wget https://mercury.picoctf.net/static/33996e32dce022205a6a36f69aba56f0/flag`
3. $ man cat

## Solucion

```bash()
foxmcloud97-picoctf@webshell:~$ wget https://mercury.picoctf.net/static/33996e32dce022205a6a36f69aba56f0/flag
--2023-03-05 06:40:33--  https://mercury.picoctf.net/static/33996e32dce022205a6a36f69aba56f0/flag
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 34 [application/octet-stream]
Saving to: 'flag'

flag                         100%[=============================================>]      34  --.-KB/s    in 0s      

2023-03-05 06:40:33 (14.0 MB/s) - 'flag' saved [34/34]

foxmcloud97-picoctf@webshell:~$ cat flag
picoCTF{s4n1ty_v3r1f13d_2aa22101}
foxmcloud97-picoctf@webshell:~$ 
```

## Bandera

picoCTF{s4n1ty_v3r1f13d_2aa22101}

## Notas adicionales

| comando | descripcion

| cat | El comando cat (concatenar) se usa con mucha frecuencia en Linux. Lee datos del archivo y da su contenido como salida. |
| wget | El comando wget significa web get. El wget es un comando de descarga de archivos no interactivo gratuito. |

## Referencias
[[https://www.geeksforgeeks.org/cat-command-in-linux-with-examples/|Link para el comando cat]]
[[https://www.javatpoint.com/linux-wget#:~:text=Command%20wget%20stands%20for%20web,while%20wget%20finish%20its%20work.|Link para el comando wget]]