
# Permissions

## Descripcion

Can you read files in the root file?

Additional details will be available after launching your challenge instance.

## Pistas

no hay

## Solucion

```bash()
picoplayer@challenge:/$ ls
bin  boot  challenge  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
picoplayer@challenge:/$ cd challenge/
picoplayer@challenge:/challenge$ ls
metadata.json
picoplayer@challenge:/challenge$ cat metadata.json 
{"flag": "picoCTF{uS1ng_v1m_3dit0r_ad091ce1}", "username": "picoplayer", "password": "8nVVw6hmD7"}picoplayer@challenge:/challenge$ Connection to saturn.picoctf.net closed by remote host.
Connection to saturn.picoctf.net closed.
```

## Bandera

picoCTF{uS1ng_v1m_3dit0r_ad091ce1}

## Notas adicionales

| comando | descripcion

## Referencias
