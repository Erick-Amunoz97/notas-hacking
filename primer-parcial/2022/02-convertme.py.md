
# convertme.py

## Descripcion

Run the Python script and convert the given number from decimal to binary to get the flag.[Download Python script](https://artifacts.picoctf.net/c/32/convertme.py)

## Pistas

1. Look up a decimal to binary number conversion app on the web or use your computer's calculator!
2. The `str_xor` function does not need to be reverse engineered for this challenge.
3. If you have Python on your computer, you can download the script normally and run it. Otherwise, use the `wget` command in the webshell.
4. To use `wget` in the webshell, first right click on the download link and select 'Copy Link' or 'Copy Link Address'
5. Type everything after the dollar sign in the webshell: `$ wget` , then paste the link after the space after `wget` and press enter. This will download the script for you in the webshell so you can run it!
6. Finally, to run the script, type everything after the dollar sign and then press enter: `$ python3 convertme.py`

## Solucion

```bash()
foxmcloud97-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/32/convertme.py
--2023-03-05 07:35:51--  https://artifacts.picoctf.net/c/32/convertme.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 108.156.172.120, 108.156.172.42, 108.156.172.74, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|108.156.172.120|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1189 (1.2K) [application/octet-stream]
Saving to: 'convertme.py'

convertme.py                 100%[=============================================>]   1.16K  --.-KB/s    in 0s      

2023-03-05 07:35:51 (391 MB/s) - 'convertme.py' saved [1189/1189]

foxmcloud97-picoctf@webshell:~$ python convertme.py 
If 49 is in decimal base, what is it in binary base?
Answer: 110001
That is correct! Here's your flag: picoCTF{4ll_y0ur_b4535_722f6b39}
```

## Bandera

picoCTF{4ll_y0ur_b4535_722f6b39}

## Notas adicionales

| comando | descripcion

## Referencias
