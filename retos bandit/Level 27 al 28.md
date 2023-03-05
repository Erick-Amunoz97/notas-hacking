# Bandit Level -> Level



## objetivo
There is a git repository at `ssh://bandit27-git@localhost/home/bandit27-git/repo`. The password for the user `bandit27-git` is the same as for the user `bandit27`.
  
Clone the repository and find the password for the next level.

## Datos de acceso al nivel
**ssh bandit27@bandit.labs.overthewire.org -p 2220**
bandit27
YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS


## solucion
```bash()
bandit27@bandit:~$ mktemp -d
/tmp/tmp.FOU1MdmOpM
bandit27@bandit:~$ cd /tmp/tmp.FOU1MdmOpM
bandit27@bandit:/tmp/tmp.FOU1MdmOpM$ git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? no
Host key verification failed.
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
bandit27@bandit:/tmp/tmp.FOU1MdmOpM$ git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit27/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit27/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit27-git@localhost's password: 
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
bandit27@bandit:/tmp/tmp.FOU1MdmOpM$ ls -la
total 120
drwx------    3 bandit27 bandit27   4096 Feb 28 19:27 .
drwxrwx-wt 3078 root     root     110592 Feb 28 19:28 ..
drwxrwxr-x    3 bandit27 bandit27   4096 Feb 28 19:28 repo
bandit27@bandit:/tmp/tmp.FOU1MdmOpM$ ls
repo
bandit27@bandit:/tmp/tmp.FOU1MdmOpM$ cd repo/
bandit27@bandit:/tmp/tmp.FOU1MdmOpM/repo$ ls
README
bandit27@bandit:/tmp/tmp.FOU1MdmOpM/repo$ cat README
The password to the next level is: AVanL161y9rsbcJIsFHuw35rjaOM19nR
```

## Notas adicionales
| comando | descripcion
| mktemp | se proporciona para permitir que los scripts de shell utilicen archivos temporales de forma segura. | 

## Referencias
[[https://www.tutorialspoint.com/unix_commands/mktemp.htm#:~:text=mktemp%20is%20provided%20to%20allow,for%20an%20attacker%20to%20win.|Link para el comando mktemp]]
[[https://overthewire.org/wargames/bandit/bandit28.html|Link del nivel 27 al 28]]
