
# PW Crack 3

## Descripcion

Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/25/level3.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/25/level3.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/25/level3.hash.bin) in the same directory too.There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

## Pistas

1. To view the level3.hash.bin file in the webshell, do: `$ bvi level3.hash.bin`
2. To exit `bvi` type `:q` and press enter.
3. The `str_xor` function does not need to be reverse engineered for this challenge.

## Solucion

```bash()
foxmcloud97-picoctf@webshell:~$ ls
Addadshashanammu      README.txt  codebook.txt  file       fixme2.py    flag      static    strings    warm
Addadshashanammu.zip  code.py     convertme.py  fixme1.py  fixme2.py.1  runme.py  static.1  strings.1
foxmcloud97-picoctf@webshell:~$ cd Addadshashanammu/
foxmcloud97-picoctf@webshell:~/Addadshashanammu$ wget https://artifacts.picoctf.net/c/25/level3.py
--2023-03-05 08:12:46--  https://artifacts.picoctf.net/c/25/level3.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 108.156.172.120, 108.156.172.42, 108.156.172.6, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|108.156.172.120|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1337 (1.3K) [application/octet-stream]
Saving to: 'level3.py'

level3.py                    100%[=============================================>]   1.31K  --.-KB/s    in 0s      

2023-03-05 08:12:46 (375 MB/s) - 'level3.py' saved [1337/1337]

foxmcloud97-picoctf@webshell:~/Addadshashanammu$ wget https://artifacts.picoctf.net/c/25/level3.flag.txt.enc
--2023-03-05 08:12:58--  https://artifacts.picoctf.net/c/25/level3.flag.txt.enc
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 108.156.172.120, 108.156.172.6, 108.156.172.42, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|108.156.172.120|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 31 [application/octet-stream]
Saving to: 'level3.flag.txt.enc'

level3.flag.txt.enc          100%[=============================================>]      31  --.-KB/s    in 0s      

2023-03-05 08:12:58 (15.3 MB/s) - 'level3.flag.txt.enc' saved [31/31]

foxmcloud97-picoctf@webshell:~/Addadshashanammu$ wget https://artifacts.picoctf.net/c/25/level3.hash.bin
--2023-03-05 08:13:14--  https://artifacts.picoctf.net/c/25/level3.hash.bin
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 108.156.172.42, 108.156.172.74, 108.156.172.120, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|108.156.172.42|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 16 [application/octet-stream]
Saving to: 'level3.hash.bin'

level3.hash.bin              100%[=============================================>]      16  --.-KB/s    in 0s      

2023-03-05 08:13:14 (11.2 MB/s) - 'level3.hash.bin' saved [16/16]

foxmcloud97-picoctf@webshell:~/Addadshashanammu$ ls
Almurbalarammi  level3.flag.txt.enc  level3.hash.bin  level3.py
foxmcloud97-picoctf@webshell:~/Addadshashanammu$ bvi level3.hash.bin 

bvi version 1.4.0 Copyright (C) 1996-2014 by Gerhard Buergmann
foxmcloud97-picoctf@webshell:~/Addadshashanammu$ python level3.py
Please enter correct password for flag: 8799
That password is incorrect
foxmcloud97-picoctf@webshell:~/Addadshashanammu$ python level3.py
Please enter correct password for flag: d3ab
That password is incorrect
foxmcloud97-picoctf@webshell:~/Addadshashanammu$ python level3.py
Please enter correct password for flag: 1ea2
Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_6f98a49f}
```

## Bandera

picoCTF{m45h_fl1ng1ng_6f98a49f}

## Notas adicionales

| comando | descripcion
| ls | El comando ls se utiliza para mostrar una lista de archivos y subdirectorios en el directorio actual. |
| cd | El comando cd de Linux se usa para cambiar el directorio de trabajo actual. |
| wget | El comando wget significa web get. El wget es un comando de descarga de archivos no interactivo gratuito. |
| python | corre un script del lenguaje python. |
| nano | abre una nueva ventana del editor y puede comenzar a editar el archivo. |
| bvi | bvi es un editor orientado a visualización para archivos binarios (editor hexadecimal), basado en el editor de texto vi. |

## Referencias
[[https://www.javatpoint.com/linux-wget#:~:text=Command%20wget%20stands%20for%20web,while%20wget%20finish%20its%20work.|Link para el comando wget]]
[[https://www.atatus.com/blog/ls-command-in-linux-with-example/#:~:text=In%20Linux%2C%20the%20command%20%22ls,as%20well%20as%20system%20administrators.|Link para el comando ls]]
[[https://www.javatpoint.com/linux-cd#:~:text=Linux%20cd%20command%20is%20used,commands%20in%20the%20Linux%20terminal.|Link para el comando cd]]
[[https://realpython.com/run-python-scripts/#:~:text=To%20run%20Python%20scripts%20with,see%20the%20phrase%20Hello%20World!|Link del comando Python]]
[[https://bvi.sourceforge.net/|Link para el comando bvi]]
