
# Lookey here

## Descripcion
Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it.Download the data [here](https://artifacts.picoctf.net/c/125/anthem.flag.txt).
## Pistas
Download the file and search for the flag based on the known prefix.
## Solucion
Al abrir el archivo resulta que es un archivo de texto demasiado grande para buscar la bandera manualmente. Asi que realizamos un grep y nos da la bandera facilmente.

```bash()                                                                                                                   
┌──(kali㉿kali)-[~/notas-hacking/PicoCTf/forensic/LookeyHere]
└─$ strings anthem.flag.txt | grep pico                    
      we think that the men of picoCTF{gr3p_15_@w3s0m3_58f5c024}
                                                                   
```

## Bandera

picoCTF{gr3p_15_@w3s0m3_58f5c024}

## Notas adicionales

| comando | descripcion

## Referencias
