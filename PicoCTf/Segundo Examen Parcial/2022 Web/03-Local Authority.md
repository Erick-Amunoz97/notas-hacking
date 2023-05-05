
# Local Authority

## Descripcion
Can you get the flag?Go to this [website](http://saturn.picoctf.net:51108/) and see what you can discover.
## Pistas
How is the password checked on this website?
## Solucion
Intentamos entrar con una contraseña y usario cualquiera y obviamante no nos dejo. pero en la segunda pagina volvemos a inspeccionar y vemos que tiene una funcion muy  primitiva para encontrar la contraseña :
```bash()
function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )
```
de aqui solo ingresamos los datos y nos da la bandera.

## Bandera

picoCTF{j5_15_7r4n5p4r3n7_05df90c8}

## Notas adicionales

| comando | descripcion

## Referencias
