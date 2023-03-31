
# tunn3l_v1s10n

## Descripcion

We found this [file](https://mercury.picoctf.net/static/06a5e4ab22ba52cd66a038d51a6cc07b/tunn3l_v1s10n). Recover the flag.

## Pistas
1. Weird that it won't display right...
## Solucion
1. El archivo viene sin extension. Entonces le hacemos un xxd para ver el tipo y sale que es de tipo bmp.
```bash()
┌──(kali㉿kali)-[~/hacking/tunn3lV1s10n]
└─$ file tunn3l_v1s10n 
tunn3l_v1s10n: data
                                                                                                                    
┌──(kali㉿kali)-[~/hacking/tunn3lV1s10n]
└─$ xxd tunn3l_v1s10n | head
00000000: 424d 8e26 2c00 0000 0000 bad0 0000 bad0  BM.&,...........
00000010: 0000 6e04 0000 3201 0000 0100 1800 0000  ..n...2.........
00000020: 0000 5826 2c00 2516 0000 2516 0000 0000  ..X&,.%...%.....
00000030: 0000 0000 0000 231a 1727 1e1b 2920 1d2a  ......#..'..) .*
00000040: 211e 261d 1a31 2825 352c 2933 2a27 382f  !.&..1(%5,)3*'8/
00000050: 2c2f 2623 332a 262d 2420 3b32 2e32 2925  ,/&#3*&-$ ;2.2)%
00000060: 3027 2333 2a26 382c 2836 2b27 392d 2b2f  0'#3*&8,(6+'9-+/
00000070: 2623 1d12 0e23 1711 2916 0e55 3d31 9776  &#...#..)..U=1.v
00000080: 668b 6652 996d 569e 7058 9e6f 549c 6f54  f.fR.mV.pX.oT.oT
00000090: ab7e 63ba 8c6d bd8a 69c8 9771 c193 71c1  .~c..m..i..q..q.


```
2. usamos un mv para darle la extension de .bmp

```bash()
┌──(kali㉿kali)-[~/hacking/tunn3lV1s10n]
└─$ mv tunn3l_v1s10n tunn3l_v1s10n.bmp

```
3. usamos el hexeditor para arreglarlo y poder abrirlo pero al abrirlo por primera vez vemos que no es la imagen completa. Entonces le damos mas espacio y asi vemos la imagen completa y nos da la bandera.
```bash()
                                                                                                                    
┌──(kali㉿kali)-[~/hacking/tunn3lV1s10n]
└─$ exiftool tunn3l_v1s10n.bmp 
ExifTool Version Number         : 12.49
File Name                       : tunn3l_v1s10n.bmp
Directory                       : .
File Size                       : 2.9 MB
File Modification Date/Time     : 2023:03:30 23:09:28-04:00
File Access Date/Time           : 2023:03:30 23:09:28-04:00
File Inode Change Date/Time     : 2023:03:30 23:09:28-04:00
File Permissions                : -rwxrwx---
File Type                       : BMP
File Type Extension             : bmp
MIME Type                       : image/bmp
BMP Version                     : Windows V3
Image Width                     : 1134
Image Height                    : 320
Planes                          : 1
Bit Depth                       : 24
Compression                     : None
Image Length                    : 2893400
Pixels Per Meter X              : 5669
Pixels Per Meter Y              : 5669
Num Colors                      : Use BitDepth
Num Important Colors            : All
Image Size                      : 1134x320
Megapixels                      : 0.363
                                                                                                                    
┌──(kali㉿kali)-[~/hacking/tunn3lV1s10n]
└─$ open tunn3l_v1s10n.bmp
                                                                                                                    
┌──(kali㉿kali)-[~/hacking/tunn3lV1s10n]
└─$ hexeditor tunn3l_v1s10n.bmp
                                                                                                                    
┌──(kali㉿kali)-[~/hacking/tunn3lV1s10n]
└─$ open tunn3l_v1s10n.bmp     
                                                                                                                    
┌──(kali㉿kali)-[~/hacking/tunn3lV1s10n]
└─$ open tunn3l_v1s10n.bmp

```
## Bandera

picoCTF{qu1t3_a_v13w_2020}

## Notas adicionales

| comando | descripcion

## Referencias
