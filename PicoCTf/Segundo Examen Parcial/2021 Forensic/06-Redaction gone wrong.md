
# Redaction gone wrong

## Descripcion
Now you DON’T see me.This [report](https://artifacts.picoctf.net/c/84/Financial_Report_for_ABC_Labs.pdf) has some critical data in it, some of which have been redacted correctly, while some were not. Can you find an important key that was not redacted properly?
## Pistas
How can you be sure of the redaction?
## Solucion
Al abrir el archivo .pdf vemos que tiene texto redactado, pero en el mismo dice "just painted over with ms word" refiriendose a que solo pintaron sobre el texto en microsoft word
![[Pasted image 20230427184949.png]]
Al usar un editor de pdf gratuito encontramos la bandera detras de la cinta negra. 
![[Pasted image 20230427184919.png]]
```bash()
```

## Bandera

picoCTF{C4n_Y0u_S33_m3_fully}

## Notas adicionales

| comando | descripcion

## Referencias
