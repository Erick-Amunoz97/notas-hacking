
# WebNet1

## Descripcion

We found this [packet capture](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/capture.pcap) and [key](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/picopico.key). Recover the flag.

## Pistas
1. Try using a tool like Wireshark.
2. How can you decrypt the TLS stream?
## Solucion
hacemos un wire shark junto con la llave proporcionada nos damos cuenta que hay una imagen que se desencripta con la llave. extraemos la imagen, hacemos un strings, y nos da la bandera. 
```bash()
┌──(kali㉿kali)-[~/hacking/WebNet1]
└─$ wireshark capture.pcap                                                                          
 ** (wireshark:2352) 22:37:52.368471 [GUI WARNING] -- FIX Add drag reordering to UAT dialog
ls
^C
                                                                                                                    
┌──(kali㉿kali)-[~/hacking/WebNet1]
└─$ ls
capture.pcap  picopico.key  vulture.jpg
                                                                                                                    
┌──(kali㉿kali)-[~/hacking/WebNet1]
└─$ open vulture.jpg 
                                                                                                                    
┌──(kali㉿kali)-[~/hacking/WebNet1]
└─$ strings vulture.jpg -n15 
picoCTF{honey.roasted.peanuts}
 )/'%'/9339GDG]]}
 )/'%'/9339GDG]]}
%&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
&'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz

```

## Bandera

picoCTF{honey.roasted.peanuts}

## Notas adicionales

| comando | descripcion

## Referencias
