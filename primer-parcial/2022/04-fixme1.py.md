
# fixme1.py

## Descripcion

Fix the syntax error in this Python script to print the flag.[Download Python script](https://artifacts.picoctf.net/c/37/fixme1.py)

## Pistas

1. Indentation is very meaningful in Python
2. To view the file in the webshell, do: `$ nano fixme1.py`
3. To exit `nano`, press Ctrl and x and follow the on-screen prompts.
4. The `str_xor` function does not need to be reverse engineered for this challenge.

## Solucion

```bash()
foxmcloud97-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/37/fixme1.py
--2023-03-05 07:49:01--  https://artifacts.picoctf.net/c/37/fixme1.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 108.156.172.74, 108.156.172.120, 108.156.172.42, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|108.156.172.74|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 837 [application/octet-stream]
Saving to: 'fixme1.py'

fixme1.py                    100%[=============================================>]     837  --.-KB/s    in 0s      

2023-03-05 07:49:02 (278 MB/s) - 'fixme1.py' saved [837/837]

foxmcloud97-picoctf@webshell:~$ python fixme1.py 
  File "/home/foxmcloud97-picoctf/fixme1.py", line 20
    print('That is correct! Here\'s your flag: ' + flag)
IndentationError: unexpected indent
foxmcloud97-picoctf@webshell:~$ nano fixme1.py 
foxmcloud97-picoctf@webshell:~$ python fixme1.py 
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_6a476c8f}
```

## Bandera

picoCTF{1nd3nt1ty_cr1515_6a476c8f}

## Notas adicionales

| comando | descripcion
| wget | El comando wget significa web get. El wget es un comando de descarga de archivos no interactivo gratuito. |
| python | corre un script del lenguaje python. |
| nano | abre una nueva ventana del editor y puede comenzar a editar el archivo. |

## Referencias
[[https://realpython.com/run-python-scripts/#:~:text=To%20run%20Python%20scripts%20with,see%20the%20phrase%20Hello%20World!|Link del comando Python]]
[[https://www.javatpoint.com/linux-wget#:~:text=Command%20wget%20stands%20for%20web,while%20wget%20finish%20its%20work.|Link para el comando wget]]
[[https://linuxize.com/post/how-to-use-nano-text-editor/|Link para el comando nano]]
