# chrono
#picoCTF2023 #GeneralSkills  #Concurso #DuplicaLaDosis #Insoportable 
## Objetivo
How to automate tasks to run at intervals on linux servers?
## Solución
Se nos proporciona un host, un puerto, un usuario y una contraseña para conectarnos mediante SSH. Podemos intuir que la bandera de este reto se encuentra relacionada a la los chrontabs, que son archivos que permiten automatizar tareas en el GNU/Linux.
Al conectarnos al servidor nos movemos a la carpeta `etc` y dentro de esta carpeta observamos el archivo llamado `crontab`.

```bash
picoplayer@challenge:~$ cd /etc/
picoplayer@challenge:/etc$ cat crontab
# picoCTF{Sch3DUL7NG_T45K3_L1NUX_d83baed1}
```

==picoCTF{Sch3DUL7NG_T45K3_L1NUX_d83baed1}==

## Notas adicionales

## Referencias