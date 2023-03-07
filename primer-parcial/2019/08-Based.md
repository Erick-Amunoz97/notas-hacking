
# Based

## Descripcion

To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with `nc jupiter.challenges.picoctf.org 29956`.

## Pistas

1. I hear python can convert things.
2. It might help to have multiple windows open.

## Solucion

```bash()
foxmcloud97-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 29956
Let us see how data is stored
nurse
Please give the 01101110 01110101 01110010 01110011 01100101 as a word.
...
you have 45 seconds.....

Input:
nurse
Please give me the  143 157 154 157 162 141 144 157 as a word.
Input:
colorado
Please give me the 6e75727365 as a word.
Input:
nurse
You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_b375bb16}
```

## Bandera

picoCTF{learning_about_converting_values_b375bb16}

## Notas adicionales

| comando | descripcion

## Referencias
[[https://phoenixnap.com/kb/nc-command#:~:text=The%20Netcat%20(%20nc%20)%20command%20is,%2C%20ncat%20%2C%20and%20others).|Link para el comando nc]]
[[https://www.rapidtables.com/convert/number/binary-to-ascii.html|Link para convertidor de binario a texto]]
[[http://www.unit-conversion.info/texttools/octal/|Link para convertidor de octal a texto]]
[[http://www.unit-conversion.info/texttools/hexadecimal/|Link para convertidor de hexadecimal a texto]]


