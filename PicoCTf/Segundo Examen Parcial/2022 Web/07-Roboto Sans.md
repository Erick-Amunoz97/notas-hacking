
# Roboto Sans

## Descripcion
The flag is somewhere on this web application not necessarily on the website. Find it.Check [this](http://saturn.picoctf.net:61304/) out.
## Pistas
no hay
## Solucion
usamos el robots.txt para encontrar la llave pero nos da lo siguiente: 
```bash()
User-agent *
Disallow: /cgi-bin/
Think you have seen your flag or want to keep looking.

ZmxhZzEudHh0;anMvbXlmaW
anMvbXlmaWxlLnR4dA==
svssshjweuiwl;oiho.bsvdaslejg
Disallow: /wp-admin/
```
Al parecer esta en base 64 y despues de varios intentos encontramos la siguiente direccion: js/myfile.txt
al juntarla con la pagina nos da la bandera 
## Bandera

picoCTF{Who_D03sN7_L1k5_90B0T5_718c9043}

## Notas adicionales

| comando | descripcion

## Referencias
