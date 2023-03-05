# Bandit Level -> Level



## objetivo
There is a git repository at `ssh://bandit28-git@localhost/home/bandit28-git/repo`. The password for the user `bandit28-git` is the same as for the user `bandit28`.

Clone the repository and find the password for the next level.

## Datos de acceso al nivel
**ssh bandit28@bandit.labs.overthewire.org -p 2220**
bandit28
AVanL161y9rsbcJIsFHuw35rjaOM19nR

## solucion
```bash()
bandit28@bandit:~$ mktemp -d
/tmp/tmp.glZUrWkxFU
bandit28@bandit:~$ cd /tmp/tmp.glZUrWkxFU
bandit28@bandit:/tmp/tmp.glZUrWkxFU$ git clone ssh://bandit28-git@localhost/home/bandit28-git/repo
Cloning into 'repo'...
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit28/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit28/.ssh/known_hosts).

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

!!! You are trying to log into this SSH server on port 22, which is not intended.

bandit28-git@localhost: Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
bandit28@bandit:/tmp/tmp.glZUrWkxFU$ git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit28/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit28/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit28-git@localhost's password: 
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 9 (delta 2), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (9/9), done.
Resolving deltas: 100% (2/2), done.
bandit28@bandit:/tmp/tmp.glZUrWkxFU$ ls
repo
bandit28@bandit:/tmp/tmp.glZUrWkxFU$ cd repo/
bandit28@bandit:/tmp/tmp.glZUrWkxFU/repo$ ls
README.md
bandit28@bandit:/tmp/tmp.glZUrWkxFU/repo$ cat README.md
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx

bandit28@bandit:/tmp/tmp.glZUrWkxFU/repo$ git log
commit 104db85a904e9691ff22aafe1a96124c88f75afa (HEAD -> master, origin/master, origin/HEAD)
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Feb 21 22:03:10 2023 +0000

    fix info leak

commit 6c3c5e485cc531e5d52c321587ce1103833ab7c3
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Feb 21 22:03:10 2023 +0000

    add missing data

commit cd3b97ef95879ec34df0d6c82f2a96d552f0e56c
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:10 2023 +0000

    initial commit of README.md
bandit28@bandit:/tmp/tmp.glZUrWkxFU/repo$ git diff 104db85a904e9691ff22aafe1a96124c88f75afa 6c3c5e485cc531e5d52c321587ce1103833ab7c3
diff --git a/README.md b/README.md
index 5c6457b..b302105 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for level29 of bandit.
 ## credentials
 
 - username: bandit29
-- password: xxxxxxxxxx
+- password: tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S
 
bandit28@bandit:/tmp/tmp.glZUrWkxFU/repo$ exit
```

## Notas adicionales
| comando | descripcion
| mktemp | se proporciona para permitir que los scripts de shell utilicen archivos temporales de forma segura. | 
| git clone | copia un repositorio existente a tu repisotirio local. |
| git log | es una herramienta de utilidad para revisar y leer un historial de todo lo que sucede en un repositorio. Se pueden usar múltiples opciones con un registro de git para hacer que el historial sea más específico. |
| git diff | es un comando Git multiuso que, cuando se ejecuta, ejecuta una función diff en fuentes de datos Git.|
| cat | demuestra el contenido de un archivo |
| ls | demeuestra la lista de contenidos del directorio|
| cd | se usa para cambiar el directorio de trabajo actual (es decir, en el que está trabajando el usuario actual). El "cd" significa "cambiar de directorio". |
## Referencias
[[https://www.geeksforgeeks.org/basic-git-commands-with-examples/|Link de comandos basicos git]]
[[https://www.javatpoint.com/git-log#:~:text=Git%20log%20is%20a%20utility,is%20a%20record%20of%20commits.|Link de git log]]
[[https://www.atlassian.com/git/tutorials/saving-changes/git-diff#:~:text=Diffing%20is%20a%20function%20that,%2C%20branches%2C%20files%20and%20more.|Link de git diff]]
[[https://www.geeksforgeeks.org/practical-applications-ls-command-linux/|Referencia del comando ls]]
[[https://www.geeksforgeeks.org/cat-command-in-linux-with-examples/|Referencia del comando cat]]
[[https://www.tutorialspoint.com/unix_commands/mktemp.htm#:~:text=mktemp%20is%20provided%20to%20allow,for%20an%20attacker%20to%20win.|Link para el comando mktemp]]
[[https://www.javatpoint.com/linux-cd#:~:text=Linux%20cd%20command%20is%20used,commands%20in%20the%20Linux%20terminal.|Link para comando cd]]
[[https://overthewire.org/wargames/bandit/bandit29.html|Link del nivel 28 al 29]]

