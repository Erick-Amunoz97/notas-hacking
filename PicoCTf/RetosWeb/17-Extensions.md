
# Extensions

## Descripcion

This is a really weird text file [TXT](https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt)? Can you find the flag?

## Pistas

1. How do operating systems know what kind of file it is? (It's not just the ending!
2. Make sure to submit the flag as picoCTF{XXXXX}

## Solucion

```bash()

┌──(kali㉿kali)-[~/hacking/Extensions]
└─$ xxd -l 32 flag.txt
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 06a1 0000 0260 0802 0000 0085 ad5e  .......`.......^
                                                                                                                   
┌──(kali㉿kali)-[~/hacking/Extensions]
└─$ hexeditor flag.txt 
                                                                                                                   
┌──(kali㉿kali)-[~/hacking/Extensions]
└─$ mv flag.txt flag.png
                                                                                                                   
┌──(kali㉿kali)-[~/hacking/Extensions]
└─$ open flag.png 

```

## Bandera

picoCTF{now_you_know_about_extensions}

## Notas adicionales

| comando | descripcion

## Referencias
