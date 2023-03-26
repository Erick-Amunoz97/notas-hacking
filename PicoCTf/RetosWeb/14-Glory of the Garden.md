
# Glory of the Garden

## Descripcion

This [garden](https://jupiter.challenges.picoctf.org/static/4153422e18d40363e7ffc7e15a108683/garden.jpg) contains more than it seems.

## Pistas

What is a hex editor?

## Solucion

```bash()
┌──(kali㉿kali)-[~/hacking]
└─$ strings garden.jpg -n 20
Copyright (c) 1998 Hewlett-Packard Company
IEC http://www.iec.ch
IEC http://www.iec.ch
.IEC 61966-2.1 Default RGB colour space - sRGB
.IEC 61966-2.1 Default RGB colour space - sRGB
,Reference Viewing Condition in IEC61966-2.1
,Reference Viewing Condition in IEC61966-2.1
%&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
&'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
Here is a flag "picoCTF{more_than_m33ts_the_3y33dd2eEF5}"

```

## Bandera

picoCTF{more_than_m33ts_the_3y33dd2eEF5}

## Notas adicionales

| comando | descripcion

## Referencias
