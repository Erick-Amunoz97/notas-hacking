
# Forbiden Paths

## Descripcion
Here's the [website](http://saturn.picoctf.net:55287/).We know that the website files live in `/usr/share/nginx/html/` and the flag is at `/flag.txt` but the website is filtering absolute file paths. Can you get past the filter to read the flag?
## Pistas
no hay
## Solucion
sabemos que la bandera esta dentro del directorio root de la pagina despues de 4 archivos, y la pagina esta diseñada para leer archivos al darle la direccion entonces introducimos la direccion ../../../../flag.txt
y obtenemos la bandera. 
```bash()
```

## Bandera

picoCTF{7h3_p47h_70_5ucc355_e5a6fcbc}

## Notas adicionales

| comando | descripcion

## Referencias
