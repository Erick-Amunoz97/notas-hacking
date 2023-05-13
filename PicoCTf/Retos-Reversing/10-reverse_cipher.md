
# reverse_cipher

## Descripcion
We have recovered a [binary](https://jupiter.challenges.picoctf.org/static/48babf8f8c4c6b8baf336680ea5b9ddf/rev) and a [text file](https://jupiter.challenges.picoctf.org/static/48babf8f8c4c6b8baf336680ea5b9ddf/rev_this). Can you reverse the flag.
## Pistas
objdump and Gihdra are some tools that could assist with this
## Solucion
Se nos da un archivo binario y uno de texto que esta cifrado usando el binario. lo abrimos con ghidra para ver el codigo y cambiamos los nombres de unas variables para mejor entender el codigo: 
```bash()
  flagfile = fopen("flag.txt","r");
  flagrev = fopen("rev_this","a");
  if (flagfile == (FILE *)0x0) {
    puts("No flag found, please make sure this is run on the server");
  }
  if (flagrev == (FILE *)0x0) {
    puts("please run this on the server");
  }
  sVar1 = fread(flag,0x18,1,flagfile);
  local_2c = (int)sVar1;
  if ((int)sVar1 < 1) {
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  for (i = 0; i < 8; i = i + 1) {
    rev = flag[i];
    fputc((int)rev,flagrev);
  }
  for (j = 8; (int)j < 0x17; j = j + 1) {
    if ((j & 1) == 0) {
      rev = flag[(int)j] + '\x05';
    }
    else {
      rev = flag[(int)j] + -2;
    }
```
vemos como esta codificada la bandera entonces hacemos el reverso en un archivo python para que nos de la bandera descifrada:
```bash
cifrado = open('rev_this','r').read()
print(cifrado)


flag = ''

for i in range(8,len(cifrado)-1):
        if i & 1 ==0:
                flag += chr(ord(cifrado[i]) - 5)
        else:
                flag += chr(ord(cifrado[i]) +2)

print(flag)

```
Que al ejecutarlo nos da la bandera:
```bash
┌──(kali㉿kali)-[~/notas-hacking/PicoCTf/reversing/Reverse_Cipher]
└─$ python3 exp.py
picoCTF{w1{1wq8/7376j.:}
r3v3rs312528e05
                     
```

## Bandera

picoCTF{r3v3rs312528e05}

## Notas adicionales

| comando | descripcion

## Referencias
