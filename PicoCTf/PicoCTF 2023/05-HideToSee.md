
# Hide To See

## Descripcion

How about some hide and seek heh?Look at this image [here](https://artifacts.picoctf.net/c/239/atbash.jpg).

## Pistas

Download the image and try to extract it.

## Solucion

```bash()
┌──(kali㉿kali)-[~/hacking]
└─$ mkdir HideToSee
                                                                                                                   
┌──(kali㉿kali)-[~/hacking]
└─$ cd HideToSee 
                                                                                                                   
┌──(kali㉿kali)-[~/hacking/HideToSee]
└─$ wget https://artifacts.picoctf.net/c/239/atbash.jpg
--2023-03-28 01:56:41--  https://artifacts.picoctf.net/c/239/atbash.jpg
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 18.160.124.119, 18.160.124.34, 18.160.124.108, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|18.160.124.119|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 51504 (50K) [application/octet-stream]
Saving to: ‘atbash.jpg’

atbash.jpg                   100%[=============================================>]  50.30K  --.-KB/s    in 0.02s   

2023-03-28 01:56:47 (2.56 MB/s) - ‘atbash.jpg’ saved [51504/51504]

                                                                                                                   
┌──(kali㉿kali)-[~/hacking/HideToSee]
└─$ ls
atbash.jpg
                                                                                                                   

┌──(kali㉿kali)-[~/hacking/HideToSee]
└─$ steghide info abash.jpg
steghide: could not open the file "abash.jpg".
                                                                                                                   
┌──(kali㉿kali)-[~/hacking/HideToSee]
└─$ steghide extract -sf atbash.jpg -xf datos.txt
Enter passphrase: 
wrote extracted data to "datos.txt".
                                                                                                                   
┌──(kali㉿kali)-[~/hacking/HideToSee]
└─$ ls
atbash.jpg  datos.txt
                                                                                                                   
┌──(kali㉿kali)-[~/hacking/HideToSee]
└─$ cat datos.txt 
krxlXGU{zgyzhs_xizxp_1u84w779}

```

## Bandera

picoCTF{atbash_crack_1f84d779}

## Notas adicionales

| comando | descripcion |
usamos la pagina de decode para desencriptar la bandera 

## Referencias
https://www.dcode.fr/atbash-cipher
