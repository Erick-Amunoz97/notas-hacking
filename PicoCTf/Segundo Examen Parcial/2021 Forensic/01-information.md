
# information

## Descripcion
Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/a614a27d4cb251d04c7d2f3f3f76a965/cat.jpg)
## Pistas
1. Look at the details of the file
2. Make sure to submit the flag as picoCTF{XXXXX}
## Solucion
![[cat.jpg]]
Se nos pide ver los detalles de la imagen por lo cual decidi ver la imagen en el hexeditor. Dentro de cual encontre una parte que estaba en base 64. al traducirla sale la bandera. 

![[Pasted image 20230427173527.png]]
```bash()
┌──(kali㉿kali)-[~]
└─$ cd hacking/Information
                                                                                                                   
┌──(kali㉿kali)-[~/hacking/Information]
└─$ hexeditor cat.jpg     
                                                                                                                   
┌──(kali㉿kali)-[~/hacking/Information]
└─$ cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 | base64 -d
cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9: command not found
                                                                                                                   
┌──(kali㉿kali)-[~/hacking/Information]
└─$ echo cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 | base64 -d
picoCTF{the_m3tadata_1s_modified}  
```

## Bandera

picoCTF{the_m3tadata_1s_modified}

## Notas adicionales

| comando | descripcion

## Referencias
