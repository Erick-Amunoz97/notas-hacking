
# MacroHard WeakEdge

## Descripcion

I've hidden a flag in this file. Can you find it? [Forensics is fun.pptm](https://mercury.picoctf.net/static/52da699e0f203321c7c90ab56ea912d8/Forensics%20is%20fun.pptm)

## Pistas
no hay

## Solucion
1. Decomprimimos el archivo y nos da un archivo de tipo .pptm o PowerPoint. con todas sus diapositivas. 
```bash()
┌──(kali㉿kali)-[~/hacking/MacroHardWeakEdge]
└─$ file Forensics\ is\ fun.pptm 
Forensics is fun.pptm: Microsoft PowerPoint 2007+
                                                                                                                   
┌──(kali㉿kali)-[~/hacking/MacroHardWeakEdge]
└─$ ls -la 
total 104
drwxrwx--- 1 root vboxsf      0 Mar 30 23:26  .
drwxrwx--- 1 root vboxsf   4096 Mar 30 23:25  ..
-rwxrwx--- 1 root vboxsf 100093 Mar 23  2021 'Forensics is fun.pptm'
                                                                                                                   
┌──(kali㉿kali)-[~/hacking/MacroHardWeakEdge]
└─$ unzip Forensics\ is\ fun.pptm 
Archive:  Forensics is fun.pptm
  inflating: [Content_Types].xml     
  inflating: _rels/.rels             
  inflating: ppt/presentation.xml    
  inflating: ppt/slides/_rels/slide46.xml.rels  
  inflating: ppt/slides/slide1.xml   
  inflating: ppt/slides/slide2.xml   
.
.
.
.
.

```
2. usando VScode buscamos entre los archivos y encontramos uno llamada "hidden. " Dentro de este archivo hay un texto en base64. lo decodificamos y obtenemos la bandera. 
```bash()
┌──(kali㉿kali)-[~/hacking/MacroHardWeakEdge]
└─$ echo "Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q" | tr -d " " | base64 -d
flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}base64: invalid input
                                                             
```
## Bandera

picoCTF{D1d_u_kn0w_ppts_r_z1p5}

## Notas adicionales

| comando | descripcion

## Referencias
