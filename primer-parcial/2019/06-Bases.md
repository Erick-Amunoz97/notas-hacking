
# Bases

## Descripcion

What does this `bDNhcm5fdGgzX3IwcDM1` mean? I think it has something to do with bases.

## Pistas

Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

## Solucion

```bash()
foxmcloud97-picoctf@webshell:~$ echo 'bDNhcm5fdGgzX3IwcDM1' | base64 --decode
l3arn_th3_r0p35
foxmcloud97-picoctf@webshell:~$ 
```

## Bandera

picoCTF{l3arn_th3_r0p35}

## Notas adicionales

| comando | descripcion


|base 64 --decode | Esta opción se utiliza para decodificar cualquier dato codificado de la entrada estándar o de cualquier archivo. |
| echo | Echo es una herramienta de comando de Unix/Linux que se utiliza para mostrar líneas de texto o cadenas que se pasan como argumentos en la línea de comando. |
## Referencias
[[https://linuxhint.com/bash_base64_encode_decode/|Link para el comando base64]]
[[https://www.nielit.gov.in/gorakhpur/sites/default/files/Gorakhpur/Alevel_unix_21april20_AKM.pdf|Link para el comando echo]]
