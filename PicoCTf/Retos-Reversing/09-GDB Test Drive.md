
# GDB Test Drive

## Descripcion
Can you get the flag?Download this [binary](https://artifacts.picoctf.net/c/86/gdbme).Here's the test drive instructions:

-   `$ chmod +x gdbme`
-   `$ gdb gdbme`
-   `(gdb) layout asm`
-   `(gdb) break *(main+99)`
-   `(gdb) run`
-   `(gdb) jump *(main+104)`
## Pistas
no hay
## Solucion
El reto consiste en una prueba del funcionamiento de GDB. Al usar todos los comandos se nos da la bandera. 

```bash

(gdb) run
Starting program: /home/kali/notas-hacking/PicoCTf/reversing/GDBTestDrive/gdbme 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x000055555555532a in main ()
(gdb) jump *(main+104)
Continuing at 0x55555555532f.
picoCTF{d3bugg3r_dr1v3_72bd8355}
[Inferior 1 (process 5423) exited normally]
(gdb) 

```

## Bandera

picoCTF{d3bugg3r_dr1v3_72bd8355}

## Notas adicionales

| comando | descripcion

## Referencias
