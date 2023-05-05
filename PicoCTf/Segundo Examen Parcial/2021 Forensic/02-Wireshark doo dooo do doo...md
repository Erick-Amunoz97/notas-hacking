
# Wireshark doo dooo do doo..

## Descripcion
Can you find the flag? [shark1.pcapng](https://mercury.picoctf.net/static/b44842413a0834f4a3619e5f5e629d05/shark1.pcapng).
## Pistas
no hay
## Solucion
Por el nombre del reto nos da una pista que se requiere la herramienta del wireshark para encontrar la bandera dentro de la imagen. 
![[Pasted image 20230427175249.png]]
al seguir el tcp al final de la "stream 5" hay algo que parece una bandera. 
Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}

Lo tendremos que decodificar y despues de intentar varios metodos encontre que estaba rotado, y al usar el ROT13 nos sale la bandera. 
![[Pasted image 20230427175451.png]]
The flag is picoCTF{p33kab00_1_s33_u_deadbeef}

```bash()
```

## Bandera

picoCTF{p33kab00_1_s33_u_deadbeef}

## Notas adicionales

| comando | descripcion

## Referencias
