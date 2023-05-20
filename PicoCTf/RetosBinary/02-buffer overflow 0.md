
# buffer overflow 0

## Descripcion
Smash the stackLet's start off simple, can you overflow the correct buffer? The program is available [here](https://artifacts.picoctf.net/c/173/vuln). You can view source [here](https://artifacts.picoctf.net/c/173/vuln.c). And connect with it using:`nc saturn.picoctf.net 51532`
## Pistas
1. How can you trigger the flag to print?
2. If you try to do the math by hand, maybe try and add a few more characters. Sometimes there are things you aren't expecting.
3. Run `man gets` and read the BUGS section. How many characters can the program really read?
## Solucion
Se nos da un codigo y al examinarlo vemos que hay una funcion que imprime la bandera: 
```bash()
void sigsegv_handler(int sig) {
  printf("%s\n", flag);
  fflush(stdout);
  exit(1);
}


```
se llama sigsegv y al buscarlo en el internet se nos da que sigsegv significa "Segmentation fault" lo cual es un error en el hardware protegido por la memoria cuando intenta acceder a directorios en la memora que estan o restringidos o simplemente no existen. 

Tambien vemos que hay un get llamado gets() y lee el buf1 que viene siendo la entrada de lo que escriba el usuario. El cual no tiene cuenta de su lngitud asignada, asi que si metemos muchos caracteres quiza lo podamos desbordar y causar la falla de segmentacion.

```bash()
┌──(kali㉿kali)-[~/notas-hacking/PicoCTf/binary/BufferOverflow0]
└─$ nc saturn.picoctf.net 51532
Input: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
picoCTF{ov3rfl0ws_ar3nt_that_bad_90d2bb58}

```

## Bandera

picoCTF{ov3rfl0ws_ar3nt_that_bad_90d2bb58}

## Notas adicionales

| comando | descripcion

## Referencias
