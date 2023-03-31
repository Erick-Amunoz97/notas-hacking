
# shark on wire 2

## Descripcion

We found this [packet capture](https://jupiter.challenges.picoctf.org/static/b506393b6f9d53b94011df000c534759/capture.pcap). Recover the flag that was pilfered from the network.

## Pistas
no hay

## Solucion
Encontramos la bandera en todos los paquetes cuyo puerto destino sea el 22. en la informacion todos tienen 5000 como puerto origen y va variando en numeros que nos dan letras tipo char. para no hacer cada letra a la vez hacemos un script.
```bash()
from scapy.all import *

packets = rdpcap('capture.pcap')

flag = ''

for p in packets: 
        if UDP in p and p[UDP].dport == 22: 
                if p[UDP].sport > 5000: 
                        flag += chr(p[UDP].sport - 5000)
    
print(flag)

```
2. Ejecutamos el script
```bash()
┌──(kali㉿kali)-[~/hacking/SharkOnWire2]
└─$ python3 exp.py
picoCTF{p1LLf3r3d_data_v1a_st3g0}

```

## Bandera

picoCTF{p1LLf3r3d_data_v1a_st3g0}

## Notas adicionales

| comando | descripcion

## Referencias
