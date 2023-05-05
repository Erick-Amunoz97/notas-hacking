
# Packets Primer

## Descripcion
Download the packet capture file and use packet analysis software to find the flag.

-   [Download packet capture](https://artifacts.picoctf.net/c/195/network-dump.flag.pcap)
## Pistas
Wireshark, if you can install and use it, is probably the most beginner friendly packet analysis software product.
## Solucion
Usamos un wireshark en el paquete y seguimos la stream tcp
y en el primer stream esta la bandera. 
![[Pasted image 20230427183746.png]]
```bash()
```
p i c o C T F { p 4 c k 3 7 _ 5 h 4 r k _ b 9 d 5 3 7 6 5 }
## Bandera

picoCTF{p4ck37_5h4rk_b9d53765}

## Notas adicionales

| comando | descripcion

## Referencias
