# hideme
#picoCTF2023 #FORENSICS #Concurso #DuplicaLaDosis #Insoportable 
## Objetivo
The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye [here](https://artifacts.picoctf.net/c/256/flag.png).
## Solución
Nos encontramos con una imagen de tipo PNG. Al extraer de forma recursiva mediante binwalk podemos obtener un directorio con los archivos extraidos.

```bash
┌──(insoportable㉿kali666)-[~/Descargas/picoCTF/2023/forensics]
└─$ binwalk -Me flag.png 

Scan Time:     2023-03-17 10:10:51
Target File:   /home/insoportable/Descargas/picoCTF/2023/forensics/flag.png
MD5 Checksum:  609a18ee6059c6b3e33ec9c63f69c254
Signatures:    411

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 512 x 504, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed
39739         0x9B3B          Zip archive data, at least v1.0 to extract, name: secret/
39804         0x9B7C          Zip archive data, at least v2.0 to extract, compressed size: 2997, uncompressed size: 3152, name: secret/flag.png
43036         0xA81C          End of Zip archive, footer length: 22


Scan Time:     2023-03-17 10:10:51
Target File:   /home/insoportable/Descargas/picoCTF/2023/forensics/_flag.png.extracted/29
MD5 Checksum:  d41d8cd98f00b204e9800998ecf8427e
Signatures:    411

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------


Scan Time:     2023-03-17 10:10:51
Target File:   /home/insoportable/Descargas/picoCTF/2023/forensics/_flag.png.extracted/secret/flag.png
MD5 Checksum:  9a33c09ff9ff6fb97afcd7fa1eb8577d
Signatures:    411

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 600 x 50, 16-bit grayscale, non-interlaced
134           0x86            Zlib compressed data, best compression


Scan Time:     2023-03-17 10:10:51
Target File:   /home/insoportable/Descargas/picoCTF/2023/forensics/_flag.png.extracted/secret/_flag.png.extracted/86
MD5 Checksum:  c1b5f76ea43a5a373261a1475377972b
Signatures:    411

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------

                                                                         
┌──(insoportable㉿kali666)-[~/Descargas/picoCTF/2023/forensics]
└─$ ls
flag.png  _flag.png.extracted
```

Posterior a eso entramos en el directorio que se nos da  y extraemos el archivo `9B3B.zip`.

```bash
┌──(insoportable㉿kali666)-[~/Descargas/picoCTF/2023/forensics]
└─$ cd _flag.png.extracted 
┌──(insoportable㉿kali666)-[~/…/picoCTF/2023/forensics/_flag.png.extracted]
└─$ ls
29  29.zlib  9B3B.zip  secret
                                                                         
┌──(insoportable㉿kali666)-[~/…/picoCTF/2023/forensics/_flag.png.extracted]
└─$ unzip 9B3B.zip          
Archive:  9B3B.zip
replace secret/flag.png? [y]es, [n]o, [A]ll, [N]one, [r]ename: r
new name: unziped_flag
  inflating: unziped_flag            
                                                                         
┌──(insoportable㉿kali666)-[~/…/picoCTF/2023/forensics/_flag.png.extracted]
└─$ ls
29  29.zlib  9B3B.zip  secret  unziped_flag
                                                                         
┌──(insoportable㉿kali666)-[~/…/picoCTF/2023/forensics/_flag.png.extracted]
└─$ open unziped_flag 
```

![[Pasted image 20230317102516.png]]

En el archivo descomprimido nos encontramos con la bandera.

==picoCTF{Hiddinng_An_Imag3_within_@n_ima9e_85e04ab8}==
## Notas adicionales

## Referencias