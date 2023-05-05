
# Enhance!

## Descripcion
Download this image file and find the flag.

-   [Download image file](https://artifacts.picoctf.net/c/100/drawing.flag.svg)
## Pistas
no hay
## Solucion
usando un strings y un grep encontramos algo que parece ser la bandera
```bash()
┌──(kali㉿kali)-[~/notas-hacking/PicoCTf/forensic/Enhance!]
└─$ strings drawing.flag.svg | grep {
         id="tspan3764">F { 3 n h 4 n </tspan><tspan
                                                                                                                   
┌──(kali㉿kali)-[~/notas-hacking/PicoCTf/forensic/Enhance!]
└─$ strings drawing.flag.svg | grep }*
c 3 d _ a a b 7 2 9 d d }</tspan></text>

```
nos dan : 
{ 3 n h 4 n 
c 3 d _ a a b 7 2 9 d d }
y al juntarlos y quitar los espacios nos queda :
``{3nh4nc3d_aab729dd}``

## Bandera

picoCTF{3nh4nc3d_aab729dd}

## Notas adicionales

| comando | descripcion

## Referencias
