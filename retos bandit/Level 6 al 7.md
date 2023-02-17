# Bandit Level 6 -> Level 7

## objetivo
The password for the next level is stored **somewhere on the server** and has all of the following properties:

-   owned by user bandit7
-   owned by group bandit6
-   33 bytes in size

## Datos de acceso al nivel
**ssh bandit.labs.overthewire.org -p 2220**
bandit6
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU

## solucion
```bash()
bandit6@bandit:~$ ls
bandit6@bandit:~$ cd
bandit6@bandit:~$ cd ..
bandit6@bandit:/home$ ls
bandit0   bandit15  bandit21  bandit27-git  bandit30-git  bandit6    drifter12  drifter5     formulaone2  krypton4
bandit1   bandit16  bandit22  bandit28      bandit31      bandit7    drifter13  drifter6     formulaone3  krypton5
bandit10  bandit17  bandit23  bandit28-git  bandit31-git  bandit8    drifter14  drifter7     formulaone5  krypton6
bandit11  bandit18  bandit24  bandit29      bandit32      bandit9    drifter15  drifter8     formulaone6  krypton7
bandit12  bandit19  bandit25  bandit29-git  bandit33      drifter0   drifter2   drifter9     krypton1     ubuntu
bandit13  bandit2   bandit26  bandit3       bandit4       drifter1   drifter3   formulaone0  krypton2
bandit14  bandit20  bandit27  bandit30      bandit5       drifter10  drifter4   formulaone1  krypton3
bandit6@bandit:/home$ cd ./bandit07
-bash: cd: ./bandit07: No such file or directory
bandit6@bandit:/home$ cd ./bandit7
bandit6@bandit:/home/bandit7$ ls -a
.  ..  .bash_logout  .bashrc  data.txt  .profile
bandit6@bandit:/home/bandit7$ ls -l
total 4088
-rw-r----- 1 bandit8 bandit7 4184396 Jan 11 19:19 data.txt
bandit6@bandit:/home/bandit7$ ls -la
total 4108
drwxr-xr-x  2 root    root       4096 Jan 11 19:19 .
drwxr-xr-x 70 root    root       4096 Jan 11 19:19 ..
-rw-r--r--  1 root    root        220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root    root       3771 Jan  6  2022 .bashrc
-rw-r-----  1 bandit8 bandit7 4184396 Jan 11 19:19 data.txt
-rw-r--r--  1 root    root        807 Jan  6  2022 .profile
bandit6@bandit:/home/bandit7$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:/home/bandit7$ cat /var/lib/dpkg/info/bandit7.password
z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S
```

## Notas adicionales
| comando | descripcion
| ls -l | Nos muestra un formato de lista de archivos mas largo y detallado |
|ls -la | usamos un formato de lista mas detallado que no ignora entradas empezando con '.' |
| find | usado para buscar archivos en la herarquia del directorio|
| find -user | Busca un archivo que pertenece a un usuario usando el nombre del usuario como referencia|
| find -group | busca un archivo que pertenece a un grupo usando el nombre del grupo como referencia|
|find -size| encuentra un archivo que es menor o mas de o exactamente unidades n de spacio con redondeo hacia arriba. en este caso usamos el sufijo c ya que estabamos buscando en bytes|
| cat | demuestra el contenido de un archivo 
| ls | demeuestra la lista de contenidos del directorio

## Referencias
