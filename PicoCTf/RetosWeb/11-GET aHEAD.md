
# GET aHEAD

## Descripcion

Find the flag being held on this server to get ahead of the competition [http://mercury.picoctf.net:53554/](http://mercury.picoctf.net:53554/)

## Pistas

1. Maybe you have more than 2 choices
2. Check out tools like Burpsuite to modify your requests and look at the responses

## Solucion

```bash()
foxmcloud97-picoctf@webshell:~$ curl -I HEAD -i http://mercury.picoctf.net:53554/index.php 
curl: (6) Could not resolve host: HEAD
HTTP/1.1 200 OK
flag: picoCTF{r3j3ct_th3_du4l1ty_2e5ba39f}
Content-type: text/html; charset=UTF-8

foxmcloud97-picoctf@webshell:~$ 
```

## Bandera

picoCTF{r3j3ct_th3_du4l1ty_2e5ba39f}

## Notas adicionales

| comando | descripcion

## Referencias
