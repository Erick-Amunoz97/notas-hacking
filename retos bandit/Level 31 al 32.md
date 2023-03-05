# Bandit Level 31 -> Level 32



## objetivo
There is a git repository at `ssh://bandit31-git@localhost/home/bandit31-git/repo`. The password for the user `bandit31-git` is the same as for the user `bandit31`.

Clone the repository and find the password for the next level.

## Datos de acceso al nivel
**ssh bandit31@bandit.labs.overthewire.org -p 2220**
bandit31
OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt

## solucion
```bash()
bandit31@bandit:~$ mktemp -d
/tmp/tmp.FQyF8ZNmy5
bandit31@bandit:~$ cd /tmp/tmp.FQyF8ZNmy5
bandit31@bandit:/tmp/tmp.FQyF8ZNmy5$ git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit31/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit31/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit31-git@localhost's password: 
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.
bandit31@bandit:/tmp/tmp.FQyF8ZNmy5$ cd repo
bandit31@bandit:/tmp/tmp.FQyF8ZNmy5/repo$ ls
README.md
bandit31@bandit:/tmp/tmp.FQyF8ZNmy5/repo$ cat README.md
This time your task is to push a file to the remote repository.

Details:
    File name: key.txt
    Content: 'May I come in?'
    Branch: master

bandit31@bandit:/tmp/tmp.FQyF8ZNmy5/repo$ git branch
* master
bandit31@bandit:/tmp/tmp.FQyF8ZNmy5/repo$ echo 'May I come in?' > key.txt
bandit31@bandit:/tmp/tmp.FQyF8ZNmy5/repo$ cat key.txt
May I come in?
bandit31@bandit:/tmp/tmp.FQyF8ZNmy5/repo$ git add -f key.txt
bandit31@bandit:/tmp/tmp.FQyF8ZNmy5/repo$ git commit -m "new key.txt"
[master 09a49a0] new key.txt
 1 file changed, 1 insertion(+), 1 deletion(-)
bandit31@bandit:/tmp/tmp.FQyF8ZNmy5/repo$ git push
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit31/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit31/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit31-git@localhost's password: 
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 2 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 538 bytes | 538.00 KiB/s, done.
Total 6 (delta 1), reused 0 (delta 0), pack-reused 0
remote: ### Attempting to validate files... ####
remote: 
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote: 
remote: Well done! Here is the password for the next level:
remote: rmCBvG56y58BXzv98yZGdO7ATVL5dW8y 
remote: 
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote: 
To ssh://localhost:2220/home/bandit31-git/repo
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'ssh://localhost:2220/home/bandit31-git/repo'
bandit31@bandit:/tmp/tmp.FQyF8ZNmy5/repo$   
```

## Notas adicionales
| comando | descripcion
| mktemp | se proporciona para permitir que los scripts de shell utilicen archivos temporales de forma segura. | 
| git clone | copia un repositorio existente a tu repisotirio local. |
| git add | se usa para agregar archivos al repo |
| git commit -m | hace un commit de los archivos que hayamos agregado anteriormente |
| git push | "empuja" los cambios del codigo dentro del repo local hacia el repo no local |
| git log | es una herramienta de utilidad para revisar y leer un historial de todo lo que sucede en un repositorio. Se pueden usar múltiples opciones con un registro de git para hacer que el historial sea más específico. |
| git diff | es un comando Git multiuso que, cuando se ejecuta, ejecuta una función diff en fuentes de datos Git.|
| cat | demuestra el contenido de un archivo |
| ls | demeuestra la lista de contenidos del directorio|
| cd | se usa para cambiar el directorio de trabajo actual (es decir, en el que está trabajando el usuario actual). El "cd" significa "cambiar de directorio". |

## Referencias
[[https://www.javatpoint.com/linux-cd#:~:text=Linux%20cd%20command%20is%20used,commands%20in%20the%20Linux%20terminal.|Link para comando cd]]
[[https://www.tutorialspoint.com/unix_commands/mktemp.htm#:~:text=mktemp%20is%20provided%20to%20allow,for%20an%20attacker%20to%20win.|Link para el comando mktemp]]
[[https://www.geeksforgeeks.org/basic-git-commands-with-examples/|Link de comandos basicos git]]
[[https://www.javatpoint.com/git-log#:~:text=Git%20log%20is%20a%20utility,is%20a%20record%20of%20commits.|Link de git log]]
[[https://www.atlassian.com/git/tutorials/saving-changes/git-diff#:~:text=Diffing%20is%20a%20function%20that,%2C%20branches%2C%20files%20and%20more.|Link de git diff]]
[[https://www.geeksforgeeks.org/practical-applications-ls-command-linux/|Referencia del comando ls]]
[[https://www.geeksforgeeks.org/cat-command-in-linux-with-examples/|Referencia del comando cat]]
[[https://overthewire.org/wargames/bandit/bandit32.html|Link del nivel 31 al 32]]
