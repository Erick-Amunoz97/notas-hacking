
# Obedient Cat

## Descripcion

This file has a flag in plain sight (aka "in-the-clear"). [Download flag](https://mercury.picoctf.net/static/33996e32dce022205a6a36f69aba56f0/flag).

## Pistas

1. Any hints about entering a command into the Terminal (such as the next one), will start with a '$'... everything after the dollar sign will be typed (or copy and pasted) into your Terminal.
2. To get the file accessible in your shell, enter the following in the Terminal prompt: `$ wget https://mercury.picoctf.net/static/33996e32dce022205a6a36f69aba56f0/flag`
3. $ man cat

## Solucion

```bash()
foxmcloud97-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 4427 | grep "pico"
picoCTF{digital_plumb3r_5ea1fbd7}
wget https://mercury.picoctf.net/static/33996e32dce022205a6a36f69aba56f0/flag
^C
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

## Referencias
