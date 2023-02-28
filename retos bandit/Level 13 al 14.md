# Bandit Level -> Level



## objetivo
The password for the next level is stored in **/etc/bandit_pass/bandit14 and can only be read by user bandit14**. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. **Note:** **localhost** is a hostname that refers to the machine you are working on

## Datos de acceso al nivel
**ssh bandit13@bandit.labs.overthewire.org -p 2220**
bandit13
wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw


## solucion
```bash()
bandit14@bandit:~$ ls
bandit14@bandit:~$ file
Usage: file [-bcCdEhikLlNnprsSvzZ0] [--apple] [--extension] [--mime-encoding]
            [--mime-type] [-e <testname>] [-F <separator>]  [-f <namefile>]
            [-m <magicfiles>] [-P <parameter=value>] [--exclude-quiet]
            <file> ...
       file -C [-m <magicfiles>]
       file [--help]
bandit14@bandit:~$ file /*
/bin:        symbolic link to usr/bin
/boot:       directory
/dev:        directory
/drifter:    directory
/etc:        directory
/formulaone: directory
/home:       directory
/krypton:    directory
/lib:        symbolic link to usr/lib
/lib32:      symbolic link to usr/lib32
/lib64:      symbolic link to usr/lib64
/libx32:     symbolic link to usr/libx32
/lost+found: directory
/media:      directory
/mnt:        directory
/opt:        directory
/proc:       directory
/root:       directory
/run:        directory
/sbin:       symbolic link to usr/sbin
/snap:       directory
/srv:        directory
/sys:        directory
/tmp:        sticky, directory
/usr:        directory
/var:        directory
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
bandit14@bandit:~$ exit
logout
Connection to localhost closed.
bandit13@bandit:~$ exit
logout
Connection to bandit.labs.overthewire.org closed.
```

## Notas adicionales
| comando | descripcion
| xx | xx el contenido de un archivo 

## Referencias
