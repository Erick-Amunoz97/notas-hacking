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
bandit6@bandit:/home/bandit7$ file ./*
./data.txt: regular file, no read permission
bandit6@bandit:/home/bandit7$ ls -a
.  ..  .bash_logout  .bashrc  data.txt  .profile
bandit6@bandit:/home/bandit7$ ls --all
.  ..  .bash_logout  .bashrc  data.txt  .profile
bandit6@bandit:/home/bandit7$ cd ./.profile
-bash: cd: ./.profile: Not a directory
bandit6@bandit:/home/bandit7$ cat ./.profile
# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
        . "$HOME/.bashrc"
    fi
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
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
bandit6@bandit:/home/bandit7$ exit
```

## Notas adicionales
| comando | descripcion
| xx | xx el contenido de un archivo 

## Referencias
