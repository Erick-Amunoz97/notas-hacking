# useless
#GeneralSkills #picoCTF2023 #DuplicaLaDosis #Insoportable 
## Objetivo
There's an interesting script in the user's home directory

Additional details will be available after launching your challenge instance.
## Solución
Se nos otorga un un host, un usuario, una contraseña y un puerto para realizar una conexión SSH. Posterior a eso nos encontramos con un archivo que cumple la función de ser una calculadora sencilla.
Dentro del código del archivo se nos indica que leamos el manual del archivo, haciendo esto obtenemos la bandera.

```bash
picoplayer@challenge:~$ man useless 

useless
     useless, — This is a simple calculator script

SYNOPSIS
     useless, [add sub mul div] number1 number2

DESCRIPTION
     Use the useless, macro to make simple calulations like addition,subtrac‐
     tion, multiplication and division.

Examples
     ./useless add 1 2
       This will add 1 and 2 and return 3

     ./useless mul 2 3
       This will return 6 as a product of 2 and 3

     ./useless div 6 3
       This will return 2 as a quotient of 6 and 3

     ./useless sub 6 5
       This will return 1 as a remainder of substraction of 5 from 6

Authors
     This script was designed and developed by Cylab Africa

     picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_7065}
```

==picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_7065}==
## Notas adicionales

## Referencias