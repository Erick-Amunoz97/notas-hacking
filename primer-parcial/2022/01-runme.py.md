
# runme.py

## Descripcion

Run the `runme.py` script to get the flag. Download the script with your browser or with `wget` in the webshell.[Download runme.py Python script](https://artifacts.picoctf.net/c/86/runme.py)

## Pistas

1. If you have Python on your computer, you can download the script normally and run it. Otherwise, use the `wget` command in the webshell.
2. To use `wget` in the webshell, first right click on the download link and select 'Copy Link' or 'Copy Link Address'
3. Type everything after the dollar sign in the webshell: `$ wget` , then paste the link after the space after `wget` and press enter. This will download the script for you in the webshell so you can run it!
4. Finally, to run the script, type everything after the dollar sign and then press enter: `$ python3 runme.py` You should have the flag now!

## Solucion

```bash()
foxmcloud97-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/86/runme.py
--2023-03-05 07:32:56--  https://artifacts.picoctf.net/c/86/runme.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 108.156.172.74, 108.156.172.120, 108.156.172.6, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|108.156.172.74|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 270 [application/octet-stream]
Saving to: 'runme.py'

runme.py                     100%[=============================================>]     270  --.-KB/s    in 0s      

2023-03-05 07:32:56 (22.5 MB/s) - 'runme.py' saved [270/270]

foxmcloud97-picoctf@webshell:~$ python runme.py 
picoCTF{run_s4n1ty_run}
```

## Bandera

picoCTF{run_s4n1ty_run}

## Notas adicionales

| comando | descripcion


| wget | El comando wget significa web get. El wget es un comando de descarga de archivos no interactivo gratuito. |
| python | corre un script del lenguaje python. |

## Referencias
[[https://www.javatpoint.com/linux-wget#:~:text=Command%20wget%20stands%20for%20web,while%20wget%20finish%20its%20work.|Link para el comando wget]]
[[https://realpython.com/run-python-scripts/#:~:text=To%20run%20Python%20scripts%20with,see%20the%20phrase%20Hello%20World!|Link del comando Python]]
