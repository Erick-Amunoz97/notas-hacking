
# m00nwalk

## Descripcion

Decode this [message](https://jupiter.challenges.picoctf.org/static/fc1edf07742e98a480c6aff7d2546107/message.wav) from the moon.

## Pistas
1. How did pictures from the moon landing get sent back to Earth?
2. What is the CMU mascot?, that might help select a RX option

## Solucion

```bash()
┌──(kali㉿kali)-[~/opt/sstv]
└─$ cd     
                                                                                                                   
┌──(kali㉿kali)-[~]
└─$ cd hacking/m00nwalk 
                                                                                                                   
┌──(kali㉿kali)-[~/hacking/m00nwalk]
└─$ sstv -d message.wav -o result.png
[sstv] Searching for calibration header... Found!    
[sstv] Detected SSTV mode Scottie 1
[sstv] Decoding image...   [#################################################################################] 100%
[sstv] Drawing image data...
[sstv] ...Done!
                                                                                                                   
┌──(kali㉿kali)-[~/hacking/m00nwalk]
└─$ ls    
message.wav  result.png
                                                                                                                   
┌──(kali㉿kali)-[~/hacking/m00nwalk]
└─$ open result.png 

```

## Bandera

picoCTF{beep_boop_im_in_space}

## Notas adicionales

| comando | descripcion |
| --- | --- |


## Referencias
