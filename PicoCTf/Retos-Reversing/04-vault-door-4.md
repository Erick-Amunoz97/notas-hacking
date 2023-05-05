
# vault-door-4

## Descripcion
This vault uses ASCII encoding for the password. The source code for this vault is here: [VaultDoor4.java](https://jupiter.challenges.picoctf.org/static/834acd392e0964a41f05790655a994b9/VaultDoor4.java)
## Pistas
1. Use a search engine to find an "ASCII table".
2. You will also need to know the difference between octal, decimal, and hexadecimal numbers.
## Solucion
la pista nos dice que hay que saber diferenciar entre octal,decimal , hexadecimal lo cual nos dice que la bandera estara en varios codigos. 
al bajar el javascript y analizarlo encontramos una parte que esta codificada en estas bases anteriormente mencionadas: 

```bash()
    byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 0146, 064 ,
            'a' , '8' , 'c' , 'd' , '8' , 'f' , '7' , 'e' ,

```
vamos a usar la consola de nuevo para cambiar todo este codigo a ASCII. 
```bash()
String.fromCharCode(106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 0146, 064 ) + ['a' , '8' , 'c' , 'd' , '8' , 'f' , '7' , 'e'].join("");
"jU5t_4_bUnCh_0f_bYt3s_f4a8cd8f7e"
```
 Y lo podemos comprobar corriendo el programa e ingresando la bandera como la contraseña:
 ```bash()
                                                                                                                     
┌──(kali㉿kali)-[~/notas-hacking/PicoCTf/reversing/VaultDoor4]
└─$ java VaultDoor4.java
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
Enter vault password: picoCTF{jU5t_4_bUnCh_0f_bYt3s_f4a8cd8f7e}
Access granted.

```
## Bandera

picoCTF{jU5t_4_bUnCh_0f_bYt3s_f4a8cd8f7e}

## Notas adicionales

| comando | descripcion

## Referencias
