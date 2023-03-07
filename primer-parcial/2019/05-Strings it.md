
# Strings it

## Descripcion

Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/fae9ac5267cd6e44124e559b901df177/strings) without running it?

## Pistas

[strings](https://linux.die.net/man/1/strings)

## Solucion

```bash()
foxmcloud97-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/fae9ac5267cd6e44124e559b901df177/strings
--2023-03-02 19:05:35--  https://jupiter.challenges.picoctf.org/static/fae9ac5267cd6e44124e559b901df177/strings
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 776032 (758K) [application/octet-stream]
Saving to: 'strings.1'

strings.1                                                  100%[=======================================================================================================================================>] 757.84K  1.83MB/s    in 0.4s    

2023-03-02 19:05:36 (1.83 MB/s) - 'strings.1' saved [776032/776032]

foxmcloud97-picoctf@webshell:~$ strings strings | grep pico
picoCTF{5tRIng5_1T_7f766a23}
foxmcloud97-picoctf@webshell:~$ 
```

## Bandera

picoCTF{5tRIng5_1T_7f766a23}

## Notas adicionales

| comando | descripcion

| wget | El comando wget significa web get. El wget es un comando de descarga de archivos no interactivo gratuito. |
| strings | El comando de strings de Linux se utiliza para devolver los caracteres de cadena a los archivos. |


## Referencias
[[https://www.javatpoint.com/linux-wget#:~:text=Command%20wget%20stands%20for%20web,while%20wget%20finish%20its%20work.|Link para el comando wget]]
[[https://www.javatpoint.com/linux-strings-command#:~:text=Linux%20strings%20command%20is%20used,text%20from%20an%20executable%20file.|Link para el comando strings]]
[strings](https://linux.die.net/man/1/strings)