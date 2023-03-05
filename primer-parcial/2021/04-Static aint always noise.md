
# Static aint always noise

## Descripcion

Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/static)? This [BASH script](https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/ltdis.sh) might help!

## Pistas

## Solucion

```bash()
foxmcloud97-picoctf@webshell:~$ wget https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/static
--2023-03-05 07:08:53--  https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/static
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 8376 (8.2K) [application/octet-stream]
Saving to: 'static.1'

static.1                     100%[=============================================>]   8.18K  --.-KB/s    in 0s      

2023-03-05 07:08:53 (246 MB/s) - 'static.1' saved [8376/8376]

foxmcloud97-picoctf@webshell:~$ strings static | grep pico
picoCTF{d15a5m_t34s3r_f6c48608}
```

## Bandera

picoCTF{d15a5m_t34s3r_f6c48608}

## Notas adicionales

| comando | descripcion

## Referencias
