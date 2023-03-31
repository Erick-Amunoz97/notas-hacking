
# c0rrupt

## Descripcion

We found this [file](https://jupiter.challenges.picoctf.org/static/ab30fcb7d47364b4190a7d3d40edb551/mystery). Recover the flag.

## Pistas

1. Try fixing the file header

## Solucion
1. usando pngcheck revisamos la integridad del archivo y nos damos cuenta que contiene errores.
```bash()┌──(kali㉿kali)-[~/hacking/c0rrupt]
└─$ pngcheck -v mystery
zlib warning:  different version (expected 1.2.13, using 1.2.11)

File: mystery (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 5669x5669 pixels/meter (144 dpi)
:  invalid chunk length (too large)
ERRORS DETECTED in mystery

```
2. usamos el hexeditor para arreglar el archivo y asi poder abrirlo
```bash()
┌──(kali㉿kali)-[~/hacking/c0rrupt]
└─$ hexeditor mystery  
                                                                                                                   
┌──(kali㉿kali)-[~/hacking/c0rrupt]
└─$ pngcheck -v mystery
zlib warning:  different version (expected 1.2.13, using 1.2.11)

File: mystery (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 5669x5669 pixels/meter (144 dpi)
  chunk IDAT at offset 0x00057, length 65445
    zlib: deflated, 32K window, fast compression
  chunk IDAT at offset 0x10008, length 65524
  chunk IDAT at offset 0x20008, length 65524
  chunk IDAT at offset 0x30008, length 6304
  chunk IEND at offset 0x318b4, length 0
No errors detected in mystery (9 chunks, 96.3% compression).
┌──(kali㉿kali)-[~/hacking/c0rrupt]
└─$ open mystery 

```

## Bandera

picoCTF{c0rrupt10n_1847995}

## Notas adicionales

| comando | descripcion

## Referencias
