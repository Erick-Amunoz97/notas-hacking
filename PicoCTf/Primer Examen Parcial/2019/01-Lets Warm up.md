
# Let's Warm up

## Descripcion

If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?

## Pistas

Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

## Solucion
```bash()
>>> chr(0x70)
'p'
>>> int(0x70)
112
>>> chr(112)
'p'
```


## Bandera

picoCTF{p}

## Notas adicionales

| comando | descripcion | 

| int() | La función python int() es un método incorporado que convierte una cadena o un número en un número entero. |
| chr() | La función Python chr() toma un argumento entero y devuelve la cadena que representa un carácter en ese punto de código. |



## Referencias
[[https://www.digitalocean.com/community/tutorials/python-ord-chr|Link para el comando de python chr()]]
[[https://www.scaler.com/topics/int-python/|Link para el comando de python int()]]