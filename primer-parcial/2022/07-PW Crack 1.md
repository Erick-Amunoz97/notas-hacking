
# PW Crack 1

## Descripcion

Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/53/level1.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/53/level1.flag.txt.enc) in the same directory too.

## Pistas

1. To view the file in the webshell, do: `$ nano level1.py`
2. To exit `nano`, press Ctrl and x and follow the on-screen prompts.
3. The `str_xor` function does not need to be reverse engineered for this challenge.

## Solucion

```bash()
foxmcloud97-picoctf@webshell:~$ ls
Addadshashanammu      README.txt  codebook.txt  file       fixme2.py    flag      static    strings    warm
Addadshashanammu.zip  code.py     convertme.py  fixme1.py  fixme2.py.1  runme.py  static.1  strings.1
foxmcloud97-picoctf@webshell:~$ cd Addadshashanammu/
foxmcloud97-picoctf@webshell:~/Addadshashanammu$ ls
Almurbalarammi  code.py  codebook.txt
foxmcloud97-picoctf@webshell:~/Addadshashanammu$ wget https://artifacts.picoctf.net/c/53/level1.py
--2023-03-05 08:02:14--  https://artifacts.picoctf.net/c/53/level1.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 108.156.172.74, 108.156.172.6, 108.156.172.120, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|108.156.172.74|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 876 [application/octet-stream]
Saving to: 'level1.py'

level1.py                    100%[=============================================>]     876  --.-KB/s    in 0s      

2023-03-05 08:02:14 (289 MB/s) - 'level1.py' saved [876/876]

foxmcloud97-picoctf@webshell:~/Addadshashanammu$ wget https://artifacts.picoctf.net/c/53/level1.flag.txt.enc
--2023-03-05 08:02:25--  https://artifacts.picoctf.net/c/53/level1.flag.txt.enc
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 108.156.172.6, 108.156.172.42, 108.156.172.120, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|108.156.172.6|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 30 [application/octet-stream]
Saving to: 'level1.flag.txt.enc'

level1.flag.txt.enc          100%[=============================================>]      30  --.-KB/s    in 0s      

2023-03-05 08:02:25 (6.73 MB/s) - 'level1.flag.txt.enc' saved [30/30]

foxmcloud97-picoctf@webshell:~/Addadshashanammu$ ls
Almurbalarammi  code.py  codebook.txt  level1.flag.txt.enc  level1.py
foxmcloud97-picoctf@webshell:~/Addadshashanammu$ python level1.py 
Please enter correct password for flag: d
That password is incorrect           
foxmcloud97-picoctf@webshell:~/Addadshashanammu$ nano level1.py       
foxmcloud97-picoctf@webshell:~/Addadshashanammu$ python level1.py 
Please enter correct password for flag: 8713
Welcome back... your flag, user:
picoCTF{545h_r1ng1ng_1b2fd683}
```

## Bandera

picoCTF{545h_r1ng1ng_1b2fd683}

## Notas adicionales

| comando | descripcion

## Referencias
