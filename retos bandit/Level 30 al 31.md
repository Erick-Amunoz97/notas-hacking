# Bandit Level 30 -> Level 31



## objetivo
There is a git repository at `ssh://bandit30-git@localhost/home/bandit30-git/repo`. The password for the user `bandit30-git` is the same as for the user `bandit30`.

Clone the repository and find the password for the next level.

## Datos de acceso al nivel
**ssh bandit30@bandit.labs.overthewire.org -p 2220**
bandit30
xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS



## solucion
```bash()
bandit30@bandit:~$ mktemp -d
/tmp/tmp.YpCI7Xhb1Y
bandit30@bandit:~$ cd /tmp/tmp.YpCI7Xhb1Y
bandit30@bandit:/tmp/tmp.YpCI7Xhb1Y$ git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit30/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit30/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit30-git@localhost's password: 
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.
bandit30@bandit:/tmp/tmp.YpCI7Xhb1Y$ cd repo
bandit30@bandit:/tmp/tmp.YpCI7Xhb1Y/repo$ ls
README.md
bandit30@bandit:/tmp/tmp.YpCI7Xhb1Y/repo$ cat README.md
just an epmty file... muahaha
bandit30@bandit:/tmp/tmp.YpCI7Xhb1Y/repo$ git log
commit cf552c166d78421e64ddf52f850e680075d216e1 (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:13 2023 +0000

    initial commit of README.md
bandit30@bandit:/tmp/tmp.YpCI7Xhb1Y/repo$ git branch
* master
bandit30@bandit:/tmp/tmp.YpCI7Xhb1Y/repo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
bandit30@bandit:/tmp/tmp.YpCI7Xhb1Y/repo$ git show-ref
cf552c166d78421e64ddf52f850e680075d216e1 refs/heads/master
cf552c166d78421e64ddf52f850e680075d216e1 refs/remotes/origin/HEAD
cf552c166d78421e64ddf52f850e680075d216e1 refs/remotes/origin/master
831aac2e2341f009e40e46392a4f5dd318483019 refs/tags/secret
bandit30@bandit:/tmp/tmp.YpCI7Xhb1Y/repo$ git show 831aac2e2341f009e40e46392a4f5dd318483019
OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt
bandit30@bandit:/tmp/tmp.YpCI7Xhb1Y/repo$ exit
```

## Notas adicionales
| comando | descripcion
| mktemp | se proporciona para permitir que los scripts de shell utilicen archivos temporales de forma segura. | 
| git clone | copia un repositorio existente a tu repisotirio local. |
| git log | es una herramienta de utilidad para revisar y leer un historial de todo lo que sucede en un repositorio. Se pueden usar múltiples opciones con un registro de git para hacer que el historial sea más específico. |
| git branch | es una versión nueva/separada del repositorio principal. |
| cat | demuestra el contenido de un archivo |
| ls | demeuestra la lista de contenidos del directorio|
| cd | se usa para cambiar el directorio de trabajo actual (es decir, en el que está trabajando el usuario actual). El "cd" significa "cambiar de directorio". |

## Referencias
[[https://www.geeksforgeeks.org/basic-git-commands-with-examples/|Link de comandos basicos git]]
[[https://www.javatpoint.com/git-log#:~:text=Git%20log%20is%20a%20utility,is%20a%20record%20of%20commits.|Link de git log]]
[[https://www.w3schools.com/git/git_branch.asp?remote=github|Link del comando git branch]]
[[https://www.geeksforgeeks.org/practical-applications-ls-command-linux/|Referencia del comando ls]]
[[https://www.geeksforgeeks.org/cat-command-in-linux-with-examples/|Referencia del comando cat]]
[[https://www.tutorialspoint.com/unix_commands/mktemp.htm#:~:text=mktemp%20is%20provided%20to%20allow,for%20an%20attacker%20to%20win.|Link para el comando mktemp]]
[[https://www.javatpoint.com/linux-cd#:~:text=Linux%20cd%20command%20is%20used,commands%20in%20the%20Linux%20terminal.|Link para comando cd]]
[[https://overthewire.org/wargames/bandit/bandit31.html|Link para el nivel 30 al 31]]