# Bandit Level 29 -> Level 30



## objetivo
There is a git repository at `ssh://bandit29-git@localhost/home/bandit29-git/repo`. The password for the user `bandit29-git` is the same as for the user `bandit29`.

Clone the repository and find the password for the next level.

## Datos de acceso al nivel
**ssh bandit29@bandit.labs.overthewire.org -p 2220**
bandit29
tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S


## solucion
```bash()
bandit29@bandit:~$ mktemp -d
/tmp/tmp.s7WQQOQ1ZW
bandit29@bandit:~$ cd /tmp/tmp.s7WQQOQ1ZW
bandit29@bandit:/tmp/tmp.s7WQQOQ1ZW$ git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit29/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit29/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit29-git@localhost's password: 
remote: Enumerating objects: 16, done.
remote: Counting objects: 100% (16/16), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 16 (delta 2), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (16/16), done.
Resolving deltas: 100% (2/2), done.
bandit29@bandit:/tmp/tmp.s7WQQOQ1ZW$ cd repo
bandit29@bandit:/tmp/tmp.s7WQQOQ1ZW/repo$ ls
README.md
bandit29@bandit:/tmp/tmp.s7WQQOQ1ZW/repo$ cat README.md
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>

bandit29@bandit:/tmp/tmp.s7WQQOQ1ZW/repo$ git log
commit 0afe3501277395fbfa017480925edee3df6e8bb5 (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    fix username

commit c2606dfc0aef7179bf1ccd6cffa9ed19151facb4
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    initial commit of README.md
bandit29@bandit:/tmp/tmp.s7WQQOQ1ZW/repo$ git diff 0afe3501277395fbfa017480925edee3df6e8bb5 c2606dfc0aef7179bf1ccd6cffa9ed19151facb4
diff --git a/README.md b/README.md
index 1af21d3..2da2f39 100644
--- a/README.md
+++ b/README.md
@@ -3,6 +3,6 @@ Some notes for bandit30 of bandit.
 
 ## credentials
 
-- username: bandit30
+- username: bandit29
 - password: <no passwords in production!>
 
bandit29@bandit:/tmp/tmp.s7WQQOQ1ZW/repo$ git branch
* master
bandit29@bandit:/tmp/tmp.s7WQQOQ1ZW/repo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/master
  remotes/origin/sploits-dev
bandit29@bandit:/tmp/tmp.s7WQQOQ1ZW/repo$ git checkout remotes/origin/dev
Note: switching to 'remotes/origin/dev'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at fbbce0e add data needed for development
bandit29@bandit:/tmp/tmp.s7WQQOQ1ZW/repo$ git branch
* (HEAD detached at origin/dev)
  master
bandit29@bandit:/tmp/tmp.s7WQQOQ1ZW/repo$ git log
commit fbbce0ec6c80acb0fdc00ebb4b5228dd868fd799 (HEAD, origin/dev)
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    add data needed for development

commit 925c929e0527f14c189b3d617d2bcc60f019f567
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    add gif2ascii

commit 0afe3501277395fbfa017480925edee3df6e8bb5 (origin/master, origin/HEAD, master)
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    fix username

commit c2606dfc0aef7179bf1ccd6cffa9ed19151facb4
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    initial commit of README.md
bandit29@bandit:/tmp/tmp.s7WQQOQ1ZW/repo$ git show fbbce0ec6c80acb0fdc00ebb4b5228dd868fd799
commit fbbce0ec6c80acb0fdc00ebb4b5228dd868fd799 (HEAD, origin/dev)
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Feb 21 22:03:11 2023 +0000

    add data needed for development

diff --git a/README.md b/README.md
index 1af21d3..a4b1cf1 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for bandit30 of bandit.
 ## credentials
 
 - username: bandit30
-- password: <no passwords in production!>
+- password: xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS
 
bandit29@bandit:/tmp/tmp.s7WQQOQ1ZW/repo$ exit
```

## Notas adicionales
| comando | descripcion
| mktemp | se proporciona para permitir que los scripts de shell utilicen archivos temporales de forma segura. | 
| git clone | copia un repositorio existente a tu repisotirio local. |
| git add | se usa para agregar archivos al repo |
| git commit -m | hace un commit de los archivos que hayamos agregado anteriormente |
| git push | "empuja" los cambios del codigo dentro del repo local hacia el repo no local |
| git log | es una herramienta de utilidad para revisar y leer un historial de todo lo que sucede en un repositorio. Se pueden usar múltiples opciones con un registro de git para hacer que el historial sea más específico. |
| git branch | es una versión nueva/separada del repositorio principal. |
| cat | demuestra el contenido de un archivo |
| ls | demeuestra la lista de contenidos del directorio|
| cd | se usa para cambiar el directorio de trabajo actual (es decir, en el que está trabajando el usuario actual). El "cd" significa "cambiar de directorio". |
## Referencias
[[https://www.geeksforgeeks.org/basic-git-commands-with-examples/|Link de comandos basicos git]]
[[https://www.javatpoint.com/git-log#:~:text=Git%20log%20is%20a%20utility,is%20a%20record%20of%20commits.|Link de git log]]
[[https://www.atlassian.com/git/tutorials/saving-changes/git-diff#:~:text=Diffing%20is%20a%20function%20that,%2C%20branches%2C%20files%20and%20more.|Link de git diff]]
[[https://www.w3schools.com/git/git_branch.asp?remote=github|Link del comando git branch]]
[[https://www.geeksforgeeks.org/practical-applications-ls-command-linux/|Referencia del comando ls]]
[[https://www.geeksforgeeks.org/cat-command-in-linux-with-examples/|Referencia del comando cat]]
[[https://www.tutorialspoint.com/unix_commands/mktemp.htm#:~:text=mktemp%20is%20provided%20to%20allow,for%20an%20attacker%20to%20win.|Link para el comando mktemp]]
[[https://www.javatpoint.com/linux-cd#:~:text=Linux%20cd%20command%20is%20used,commands%20in%20the%20Linux%20terminal.|Link para comando cd]]
[[https://overthewire.org/wargames/bandit/bandit30.html|Link para en nivel 29 al 30]]