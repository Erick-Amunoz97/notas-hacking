
# Need For Speed

## Descripcion
The name of the game is [speed](https://www.youtube.com/watch?v=8piqd2BWeGI). Are you quick enough to solve this problem and keep it above 50 mph? [need-for-speed](https://jupiter.challenges.picoctf.org/static/f9abc386dfb1309e687344783f208b20/need-for-speed).
## Pistas
1. What is the final key?
## Solucion
Se nos da un programa que al correrlo intenta crear una llave pero no hay suficiente tiempo ya que el programa tiene un temporizador y truena: 

```bash()
┌──(kali㉿kali)-[~/notas-hacking/PicoCTf/reversing/NeedForSpeed]
└─$ ./need-for-speed 
Keep this thing over 50 mph!
============================

Creating key...
Not fast enough. BOOM!


```
Entonces hacemos un "dump" de memoria en formato intel y nos da lo siguiente: 
```bash()
┌──(kali㉿kali)-[~/notas-hacking/PicoCTf/reversing/NeedForSpeed]
└─$ objdump -D need-for-speed -M intel | grep '<main>:' -A20
000000000000091a <main>:
 91a:   55                      push   rbp
 91b:   48 89 e5                mov    rbp,rsp
 91e:   48 83 ec 10             sub    rsp,0x10
 922:   89 7d fc                mov    DWORD PTR [rbp-0x4],edi
 925:   48 89 75 f0             mov    QWORD PTR [rbp-0x10],rsi
 929:   b8 00 00 00 00          mov    eax,0x0
 92e:   e8 a5 ff ff ff          call   8d8 <header>
 933:   b8 00 00 00 00          mov    eax,0x0
 938:   e8 f2 fe ff ff          call   82f <set_timer>
 93d:   b8 00 00 00 00          mov    eax,0x0
 942:   e8 36 ff ff ff          call   87d <get_key>
 947:   b8 00 00 00 00          mov    eax,0x0
 94c:   e8 5b ff ff ff          call   8ac <print_flag>
 951:   b8 00 00 00 00          mov    eax,0x0
 956:   c9                      leave
 957:   c3                      ret
 958:   0f 1f 84 00 00 00 00    nop    DWORD PTR [rax+rax*1+0x0]
 95f:   00 

0000000000000960 <__libc_csu_init>:

```
Esto nos demuestra el programa con sus funciones en ensamblador, hay una fucion de temporizador, una para obtener la llave, otra para obtener la bandera. De aqui usamos GDB para poder llamar las funciones individualmente y saltarnos el temporizador:
```bash()
(gdb) info functions
All defined functions:

Non-debugging symbols:
0x00000000000005d8  _init
0x0000000000000600  putchar@plt
0x0000000000000610  puts@plt
0x0000000000000620  alarm@plt
0x0000000000000630  __sysv_signal@plt
0x0000000000000640  exit@plt
0x0000000000000650  __cxa_finalize@plt
0x0000000000000660  _start
0x0000000000000690  deregister_tm_clones
0x00000000000006d0  register_tm_clones
0x0000000000000720  __do_global_dtors_aux
0x0000000000000760  frame_dummy
0x000000000000076a  decrypt_flag
0x00000000000007f1  calculate_key
0x000000000000080e  alarm_handler
0x000000000000082f  set_timer
0x000000000000087d  get_key
0x00000000000008ac  print_flag
0x00000000000008d8  header
0x000000000000091a  main
0x0000000000000960  __libc_csu_init
0x00000000000009d0  __libc_csu_fini
0x00000000000009d4  _fini
(gdb) set disasembly-flavor intel
No symbol table is loaded.  Use the "file" command.
(gdb) set disassembly-flavor intel
(gdb) disassemble
No frame selected.
(gdb) disassemble main
Dump of assembler code for function main:
   0x000000000000091a <+0>:     push   rbp
   0x000000000000091b <+1>:     mov    rbp,rsp
   0x000000000000091e <+4>:     sub    rsp,0x10
   0x0000000000000922 <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x0000000000000925 <+11>:    mov    QWORD PTR [rbp-0x10],rsi
   0x0000000000000929 <+15>:    mov    eax,0x0
   0x000000000000092e <+20>:    call   0x8d8 <header>
   0x0000000000000933 <+25>:    mov    eax,0x0
   0x0000000000000938 <+30>:    call   0x82f <set_timer>
   0x000000000000093d <+35>:    mov    eax,0x0
   0x0000000000000942 <+40>:    call   0x87d <get_key>
   0x0000000000000947 <+45>:    mov    eax,0x0
   0x000000000000094c <+50>:    call   0x8ac <print_flag>
   0x0000000000000951 <+55>:    mov    eax,0x0
   0x0000000000000956 <+60>:    leave
   0x0000000000000957 <+61>:    ret
End of assembler dump.
(gdb) break main
Breakpoint 1 at 0x91e
(gdb) info breakpoints
Num     Type           Disp Enb Address            What
1       breakpoint     keep y   0x000000000000091e <main+4>
(gdb) run 
Starting program: /home/kali/notas-hacking/PicoCTf/reversing/NeedForSpeed/need-for-speed 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x000055555540091e in main ()
(gdb) disassemble main
Dump of assembler code for function main:
   0x000055555540091a <+0>:     push   rbp
   0x000055555540091b <+1>:     mov    rbp,rsp
=> 0x000055555540091e <+4>:     sub    rsp,0x10
   0x0000555555400922 <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x0000555555400925 <+11>:    mov    QWORD PTR [rbp-0x10],rsi
   0x0000555555400929 <+15>:    mov    eax,0x0
   0x000055555540092e <+20>:    call   0x5555554008d8 <header>
   0x0000555555400933 <+25>:    mov    eax,0x0
   0x0000555555400938 <+30>:    call   0x55555540082f <set_timer>
   0x000055555540093d <+35>:    mov    eax,0x0
   0x0000555555400942 <+40>:    call   0x55555540087d <get_key>
   0x0000555555400947 <+45>:    mov    eax,0x0
   0x000055555540094c <+50>:    call   0x5555554008ac <print_flag>
   0x0000555555400951 <+55>:    mov    eax,0x0
   0x0000555555400956 <+60>:    leave
   0x0000555555400957 <+61>:    ret
End of assembler dump.
(gdb) call (int) get_key()
Creating key...
Finished
$1 = 9
(gdb) call (int) print_flag()
Printing flag:
PICOCTF{Good job keeping bus #190ca38b speeding along!}
$2 = 56
(gdb) 
```
Y asi obtenemos la bandera, la cual esta en un formato un poco diferente a lo normal. 
## Bandera

PICOCTF{Good job keeping bus #190ca38b speeding along!}

## Notas adicionales

| comando | descripcion

## Referencias