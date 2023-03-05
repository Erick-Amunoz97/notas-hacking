
# fixme2.py

## Descripcion

Fix the syntax error in the Python script to print the flag.[Download Python script](https://artifacts.picoctf.net/c/66/fixme2.py)

## Pistas

1. Are equality and assignment the same symbol?
2. To view the file in the webshell, do: `$ nano fixme2.py`
3. To exit `nano`, press Ctrl and x and follow the on-screen prompts.
4. The `str_xor` function does not need to be reverse engineered for this challenge.

## Solucion

```bash()
foxmcloud97-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/66/fixme2.py
--2023-03-05 07:54:39--  https://artifacts.picoctf.net/c/66/fixme2.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 108.156.172.120, 108.156.172.74, 108.156.172.6, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|108.156.172.120|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1029 (1.0K) [application/octet-stream]
Saving to: 'fixme2.py.1'

fixme2.py.1                  100%[=============================================>]   1.00K  --.-KB/s    in 0s      

2023-03-05 07:54:39 (57.0 MB/s) - 'fixme2.py.1' saved [1029/1029]

foxmcloud97-picoctf@webshell:~$ python fixme2.py 
  File "/home/foxmcloud97-picoctf/fixme2.py", line 22
    if flag = "":
       ^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
foxmcloud97-picoctf@webshell:~$ nano fixme2.py
foxmcloud97-picoctf@webshell:~$ python fixme2.py 
That is correct! Here's your flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_4863e11b}
```

## Bandera

picoCTF{3qu4l1ty_n0t_4551gnm3nt_4863e11b}

## Notas adicionales

| comando | descripcion

## Referencias
