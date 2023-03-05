
# Tab, Tab, Attack

## Descripcion

Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://mercury.picoctf.net/static/fe16c756149cfa85f23e73cd9dbd6a25/Addadshashanammu.zip)

## Pistas

1. After `unzip`ing, this problem can be solved with 11 button-presses...(mostly Tab)...

## Solucion

```bash()
foxmcloud97-picoctf@webshell:~$ wget https://mercury.picoctf.net/static/fe16c756149cfa85f23e73cd9dbd6a25/Addadshashanammu.zip
--2023-03-05 07:12:14--  https://mercury.picoctf.net/static/fe16c756149cfa85f23e73cd9dbd6a25/Addadshashanammu.zip
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 4520 (4.4K) [application/octet-stream]
Saving to: 'Addadshashanammu.zip'

Addadshashanammu.zip         100%[=============================================>]   4.41K  --.-KB/s    in 0s      

2023-03-05 07:12:14 (101 MB/s) - 'Addadshashanammu.zip' saved [4520/4520]

foxmcloud97-picoctf@webshell:~$ unzip Addadshashanammu.zip
Archive:  Addadshashanammu.zip
   creating: Addadshashanammu/
   creating: Addadshashanammu/Almurbalarammi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
  inflating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet  
foxmcloud97-picoctf@webshell:~$ cd Addadshashanammu/
foxmcloud97-picoctf@webshell:~/Addadshashanammu$ cd Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
foxmcloud97-picoctf@webshell:~/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissir
alis/Ularradallaku$ ls
fang-of-haynekhtnamet
foxmcloud97-picoctf@webshell:~/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissir
alis/Ularradallaku$ file fang-of-haynekhtnamet 
fang-of-haynekhtnamet: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=5fffe70019957f0a27a70bb886b2cfb9f9b21d6e, not stripped
foxmcloud97-picoctf@webshell:~/Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissir
alis/Ularradallaku$ ./fang-of-haynekhtnamet 
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_76266e38}
```

## Bandera

picoCTF{l3v3l_up!_t4k3_4_r35t!_76266e38}

## Notas adicionales

| comando | descripcion

## Referencias
