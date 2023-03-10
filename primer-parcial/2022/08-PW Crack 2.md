
# PW Crack 2

## Descripcion

Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/16/level2.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/16/level2.flag.txt.enc) in the same directory too.

## Pistas

1. Does that encoding look familiar?
2. The `str_xor` function does not need to be reverse engineered for this challenge.

## Solucion

```bash()
foxmcloud97-picoctf@webshell:~$ ls  
Addadshashanammu      README.txt  codebook.txt  file       fixme2.py    flag      static    strings    warm
Addadshashanammu.zip  code.py     convertme.py  fixme1.py  fixme2.py.1  runme.py  static.1  strings.1
foxmcloud97-picoctf@webshell:~$ cd Addadshashanammu/
foxmcloud97-picoctf@webshell:~/Addadshashanammu$ ls
Almurbalarammi
foxmcloud97-picoctf@webshell:~/Addadshashanammu$ wget https://artifacts.picoctf.net/c/16/level2.py
--2023-03-05 08:09:31--  https://artifacts.picoctf.net/c/16/level2.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 108.156.172.6, 108.156.172.74, 108.156.172.120, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|108.156.172.6|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 914 [application/octet-stream]
Saving to: 'level2.py'

level2.py                    100%[=============================================>]     914  --.-KB/s    in 0s      

2023-03-05 08:09:31 (417 MB/s) - 'level2.py' saved [914/914]

foxmcloud97-picoctf@webshell:~/Addadshashanammu$ wget https://artifacts.picoctf.net/c/16/level2.flag.txt.enc
--2023-03-05 08:09:42--  https://artifacts.picoctf.net/c/16/level2.flag.txt.enc
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 108.156.172.120, 108.156.172.6, 108.156.172.42, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|108.156.172.120|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 31 [application/octet-stream]
Saving to: 'level2.flag.txt.enc'

level2.flag.txt.enc          100%[=============================================>]      31  --.-KB/s    in 0s      

2023-03-05 08:09:42 (12.0 MB/s) - 'level2.flag.txt.enc' saved [31/31]

foxmcloud97-picoctf@webshell:~/Addadshashanammu$ nano level2.py
foxmcloud97-picoctf@webshell:~/Addadshashanammu$ python
Python 3.10.6 (main, Aug 10 2022, 11:40:04) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36)
'de76'
>>> 
foxmcloud97-picoctf@webshell:~/Addadshashanammu$ python level2.py 
Please enter correct password for flag: de76
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_489dea9a}
```

## Bandera

picoCTF{tr45h_51ng1ng_489dea9a}

## Notas adicionales

| comando | descripcion
| ls | El comando ls se utiliza para mostrar una lista de archivos y subdirectorios en el directorio actual. |
| cd | El comando cd de Linux se usa para cambiar el directorio de trabajo actual. |
| wget | El comando wget significa web get. El wget es un comando de descarga de archivos no interactivo gratuito. |
| python | corre un script del lenguaje python. |
| nano | abre una nueva ventana del editor y puede comenzar a editar el archivo. |
| chr() | La función Python chr() toma un argumento entero y devuelve la cadena que representa un carácter en ese punto de código. |

## Referencias
[[https://www.javatpoint.com/linux-wget#:~:text=Command%20wget%20stands%20for%20web,while%20wget%20finish%20its%20work.|Link para el comando wget]]
[[https://www.atatus.com/blog/ls-command-in-linux-with-example/#:~:text=In%20Linux%2C%20the%20command%20%22ls,as%20well%20as%20system%20administrators.|Link para el comando ls]]
[[https://www.javatpoint.com/linux-cd#:~:text=Linux%20cd%20command%20is%20used,commands%20in%20the%20Linux%20terminal.|Link para el comando cd]]
[[https://realpython.com/run-python-scripts/#:~:text=To%20run%20Python%20scripts%20with,see%20the%20phrase%20Hello%20World!|Link del comando Python]]
[[https://www.digitalocean.com/community/tutorials/python-ord-chr|Link para el comando de python chr()]]
