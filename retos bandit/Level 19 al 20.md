# Bandit Level 19 -> Level 20



## objetivo
To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

## Datos de acceso al nivel
**ssh bandit19@bandit.labs.overthewire.org -p 2220**
bandit19
awhqfNnAbc1naukrpqDYcF95h7HoMTrC


## solucion
```bash()
bandit19@bandit:~$ ls -la
total 36
drwxr-xr-x  2 root     root      4096 Feb 21 22:03 .
drwxr-xr-x 70 root     root      4096 Feb 21 22:04 ..
-rwsr-x---  1 bandit20 bandit19 14876 Feb 21 22:03 bandit20-do
-rw-r--r--  1 root     root       220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root     root      3771 Jan  6  2022 .bashrc
-rw-r--r--  1 root     root       807 Jan  6  2022 .profile
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
VxCazJaVykI6W36BkBU0mJTCM8rR95XT
bandit19@bandit:~$ exit

```

## Notas adicionales
| comando | descripcion
| cat | demuestra el contenido de un archivo| 
| ls | demeuestra la lista de contenidos del directorio|
|ls -la | usamos un formato de lista mas detallado que no ignora entradas empezando con '.' |

## Referencias
[[https://www.geeksforgeeks.org/practical-applications-ls-command-linux/|Referencia del comando ls]]
[[https://www.geeksforgeeks.org/cat-command-in-linux-with-examples/|Referencia del comando cat]]
[[https://overthewire.org/wargames/bandit/bandit20.html|Link del nivel 19 al 20]]



