# Bandit Level 11 -> Level 12



## objetivo

The password for the next level is stored in the file **data.txt**, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

## Datos de acceso al nivel
**ssh bandit11@bandit.labs.overthewire.org -p 2220**
bandit11
6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM


## solucion
```bash()
bandit11@bandit:~$ ls
data.txt
bandit11@bandit:~$ cat data.txt
Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi
bandit11@bandit:~$ cat data.txt | tr [a-zA-Z] [n-za-mN-ZA-M]
The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv
bandit11@bandit:~$ exit
```

## Notas adicionales
| comando | descripcion
| cat | demuestra el contenido de un archivo |
| ls | demeuestra la lista de contenidos del directorio|
| tr | commando de tipo UNIX usado para traducir o borrrar caracteres |

## Referencias
[[https://www.geeksforgeeks.org/practical-applications-ls-command-linux/|Referencia del comando ls]]
[[https://www.geeksforgeeks.org/cat-command-in-linux-with-examples/|Referencia del comando cat]]
[[https://www.geeksforgeeks.org/tr-command-in-unix-linux-with-examples/|Link del comando tr]]
[[https://overthewire.org/wargames/bandit/bandit12.html|Link del nivel 11 al 12]]

