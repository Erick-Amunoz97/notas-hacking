
# Pixelated

## Descripcion
I have these 2 images, can you make a flag out of them? [scrambled1.png](https://mercury.picoctf.net/static/c9593d1d2ac9d850da95bffe0ac3b6c6/scrambled1.png) [scrambled2.png](https://mercury.picoctf.net/static/c9593d1d2ac9d850da95bffe0ac3b6c6/scrambled2.png)
## Pistas
1. [https://en.wikipedia.org/wiki/Visual_cryptography](https://en.wikipedia.org/wiki/Visual_cryptography)
2. Think of different ways you can "stack" images
## Solucion
Las dos imagenes son usadas para una encriptacion visual. Al investigar nos da que las dos imagenes se tienen que amontonar una encima de la otra para poder ver el codigo oculto. 
Al ver las dos imagenes pareceria que no tienen sentido pero el reto es encontrar que si lo tienen: 
![[scrambled1.png]]

![[scrambled2.png]]

La herramienta que usaremos para este reto se llama stegsolve.
con este programa podemos unir las dos imagenes de varias maneras y la que resulta en la bandera es la manera de `ADD`. Ya con esto obtenemos la bandera.
![[Pasted image 20230427153010.png]]
```bash()
```

## Bandera

picoCTF{da8fcef8}

## Notas adicionales

| comando | descripcion |
| --- | --- |

## Referencias
