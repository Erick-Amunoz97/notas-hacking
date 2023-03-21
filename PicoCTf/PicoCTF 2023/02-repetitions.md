
# repetitions

## Descripcion

Can you make sense of this file?Download the file [here](https://artifacts.picoctf.net/c/295/enc_flag).

## Pistas

Multiple decoding is always good.

## Solucion
se resuelve decodificandolo con base64 seis veces. aqui usamos la herramienta de cyberchef.
```bash()
foxmcloud97-picoctf@webshell:~$ cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d  
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_dbc4340a}
```

## Bandera

picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_dbc4340a}

## Notas adicionales

| comando | descripcion

## Referencias
