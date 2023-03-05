
# Codebook

## Descripcion

Run the Python script `code.py` in the same directory as `codebook.txt`.

-   [Download code.py](https://artifacts.picoctf.net/c/100/code.py)
-   [Download codebook.txt](https://artifacts.picoctf.net/c/100/codebook.txt)

## Pistas

1. On the webshell, use `ls` to see if both files are in the directory you are in
2. The `str_xor` function does not need to be reverse engineered for this challenge.

## Solucion

```bash()
foxmcloud97-picoctf@webshell:~$ ls
Addadshashanammu      README.txt  codebook.txt  file  runme.py  static.1  strings.1
Addadshashanammu.zip  code.py     convertme.py  flag  static    strings   warm
foxmcloud97-picoctf@webshell:~$ cd Addadshashanammu/
foxmcloud97-picoctf@webshell:~/Addadshashanammu$ wget https://artifacts.picoctf.net/c/100/code.py
--2023-03-05 07:41:30--  https://artifacts.picoctf.net/c/100/code.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 108.156.172.42, 108.156.172.120, 108.156.172.74, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|108.156.172.42|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1278 (1.2K) [application/octet-stream]
Saving to: 'code.py'

code.py                      100%[=============================================>]   1.25K  --.-KB/s    in 0s      

2023-03-05 07:41:30 (55.0 MB/s) - 'code.py' saved [1278/1278]

foxmcloud97-picoctf@webshell:~/Addadshashanammu$ ls
Almurbalarammi  code.py
foxmcloud97-picoctf@webshell:~/Addadshashanammu$ wget https://artifacts.picoctf.net/c/100/codebook.txt
--2023-03-05 07:42:06--  https://artifacts.picoctf.net/c/100/codebook.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 108.156.172.120, 108.156.172.42, 108.156.172.74, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|108.156.172.120|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 27 [application/octet-stream]
Saving to: 'codebook.txt'

codebook.txt                 100%[=============================================>]      27  --.-KB/s    in 0s      

2023-03-05 07:42:06 (1.07 MB/s) - 'codebook.txt' saved [27/27]

foxmcloud97-picoctf@webshell:~/Addadshashanammu$ ls
Almurbalarammi  code.py  codebook.txt
foxmcloud97-picoctf@webshell:~/Addadshashanammu$ python code.py 
picoCTF{c0d3b00k_455157_d9aa2df2}
```

## Bandera

picoCTF{c0d3b00k_455157_d9aa2df2}

## Notas adicionales

| comando | descripcion

## Referencias
