# rotation
#CRYPTO #picoCTF2023 #Concurso #DuplicaLaDosis #Insoportable
## Objetivo
You will find the flag after decrypting this file Download the encrypted flag [here](https://artifacts.picoctf.net/c/449/encrypted.txt).
## Solución
Nos encontramos con el siguiente contenido dentro del archivo.
```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ cat encrypted.txt 
xqkwKBN{z0bib1wv_l3kzgxb3l_nl5k4283}

```

La contraseña se encuentra rotada por 18 posiciones.
==picoCTF{r0tat1on_d3crypt3d_fd5c4283}==
## Notas adicionales

## Referencias
- Cyberchef https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,18)&input=eHFrd0tCTnt6MGJpYjF3dl9sM2t6Z3hiM2xfbmw1azQyODN9