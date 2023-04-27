
# basic-mod1

## Descripcion
We found this weird message being passed around on the servers, we think we have a working decryption scheme.Download the message [here](https://artifacts.picoctf.net/c/129/message.txt).Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)
## Pistas
1. Do you know what `mod 37` means?
2. `mod 37` means modulo 37. It gives the remainder of a number after being divided by 37.
## Solucion
Se nos da el mensaje siguiente:
```bash()┌──(kali㉿kali)-[~/hacking/BasicMod1]
└─$ cat message.txt 
350 63 353 198 114 369 346 184 202 322 94 235 114 110 185 188 225 212 366 374 261 213                                                                                                                     

```
Y se nos deja saber que estos numeros con el modulo 37 nos dan un caracter de tipo ASCII, siendo que del 0-25 es el alfabeto en mayusculas. y del 26-35 son numeros decimales. 
De aqui tomamos mas 22 para los decimales y mas 65 para que nos de las letras en mayuscula todo esto en ASCII, con un char los cambiamos a caracteres y los imprimimos y nos da la bandera. 

```bash()
datos = open('message.txt').read().split()

print(datos)
flag = ''
for n in datos:
        c = int(n) % 37
        if c >= 0 and c <= 25:
                s = chr(c+65)
        elif c >= 26 and c <= 35:
                s = chr(c+22)
        else:
                s = '_'
        flag += s

print("picoCTF{"+flag+"}")
```

```bash()
┌──(kali㉿kali)-[~/hacking/BasicMod1]
└─$ python3 exp.py
['350', '63', '353', '198', '114', '369', '346', '184', '202', '322', '94', '235', '114', '110', '185', '188', '225', '212', '366', '374', '261', '213']
picoCTF{R0UND_N_R0UND_ADD17EC2}

```
## Bandera

picoCTF{R0UND_N_R0UND_ADD17EC2}

## Notas adicionales

| comando | descripcion |
| --- | --- |

## Referencias
