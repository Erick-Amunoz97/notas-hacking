# Bandit Level 16 -> Level 17



## objetivo
The credentials for the next level can be retrieved by submitting the password of the current level to **a port on localhost in the range 31000 to 32000**. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

## Datos de acceso al nivel
**ssh bandit16@bandit.labs.overthewire.org -p 2220**
bandit16
JQttfApK4SeyHwDlI9SXGR50qclOAil1


## solucion
```bash()
bandit16@bandit:~$ nmap -p 31000-32000 localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2023-02-28 17:30 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00015s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.50 seconds
bandit16@bandit:~$  openssl s_client -connect localhost:31790
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = localhost
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = localhost
verify error:num=10:certificate has expired
notAfter=Feb 24 22:59:05 2023 GMT
verify return:1
depth=0 CN = localhost
notAfter=Feb 24 22:59:05 2023 GMT
verify return:1
---
Certificate chain
 0 s:CN = localhost
   i:CN = localhost
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA1
   v:NotBefore: Feb 24 22:58:05 2023 GMT; NotAfter: Feb 24 22:59:05 2023 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDCzCCAfOgAwIBAgIEXaCVVzANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjMwMjI0MjI1ODA1WhcNMjMwMjI0MjI1OTA1WjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDP
cZ+PR+x7nAI6TVhZvc6x5//nXHJUZnIv2kf6x8SOY5al5BV8I5njUSVQef9fQNE2
JlBdoYNJ65jgzYWrVqPCObCqrPsHZHf8pMD/iElYUcD5u/qtNReuVPfeYefxCvBg
Cy0MltMiLGskDn3rDSwCRWNB2jr9+jQYa7rIGDyWCAq4WH/IsWtF6tan25Bqe6tp
LIMJhuAH56EjZ0biNJ3aOgsWHwqS1bBdMzURABvR+PZc0mikWaNjb2R0d8v0gJTf
qz0qkea6IstFSfwEu2FdslmDZ8PWlIwexw3erL+Ae0L2mFhdf3g1nkUARl8R0Bbe
L9/rtYsV7dF3KG7CFJbbAgMBAAGjZTBjMBQGA1UdEQQNMAuCCWxvY2FsaG9zdDBL
BglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0ZWQgYnkgTmNhdC4g
U2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3DQEBBQUAA4IBAQBH
HpXhIirw6+X3VNmrtXw7HjpriGDA1UTjP2yfeu2YuLIm83iUpz3HuiiwsfJJX9HY
VeDQnJjgMekib2qbq99OHkz+4jFKpw0zR7wTa9K8fifkrQHW/KJOVg1fmJCyFl+j
LF06QYp5f8yA+I2ICGKuNSXd3NvYEVh0tWVXemx/oXqQLHUFBjWNcyBDfCnfZIfe
jhHPhGj/9DuJJWx1lBEOIFHrfOj2uge0R5YZvU0kEm3IQ6iabWM2JF8MHOWWYX8s
wXL4aeNo+K4lnz3wjqnRfSClTwTo9zvaaq+Ym8UxPx3w7SmAU3CXbLh/ukYR6xYp
YEsSAXuYvKkxrTvey2Ik
-----END CERTIFICATE-----
subject=CN = localhost
issuer=CN = localhost
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1339 bytes and written 373 bytes
Verification error: certificate has expired
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 2048 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 10 (certificate has expired)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: E0F6B770372FE0D06E63A660B1F080B9BEF670A1C5A0AFF6034B19162B25B8ED
    Session-ID-ctx: 
    Resumption PSK: 71DA01104BB9A12F83B7BB4565CE77764A47D8D139B3BBC39E9E02608C3161D2895FB7B4C5C070FF2CC59D5958F1A9A1
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 70 f2 f5 0a f4 da 59 2b-66 40 bc 3c 8d 67 67 76   p.....Y+f@.<.ggv
    0010 - 11 6d 51 0a 12 53 cb 16-c1 e0 57 ee b3 ce ae 1d   .mQ..S....W.....
    0020 - 5c 98 41 6e b2 cf 0b c3-f4 bd 7c af 62 2d 17 22   \.An......|.b-."
    0030 - 22 14 35 90 9f 81 f0 64-a4 3c ed ea 50 69 f4 a3   ".5....d.<..Pi..
    0040 - 78 e2 bd 40 ac 8f a6 30-12 d7 ab d3 fc c4 61 ad   x..@...0......a.
    0050 - 43 c6 4f 00 9a 24 f8 96-f7 a7 ce d6 4f d2 6f d6   C.O..$......O.o.
    0060 - 27 2e 2b 1e 4b 82 82 04-01 f2 c2 58 cf 29 23 57   '.+.K......X.)#W
    0070 - aa eb 21 1f 32 d5 b0 b4-28 ee 51 64 ff 18 e0 4b   ..!.2...(.Qd...K
    0080 - 1e 16 d8 b9 0e c1 f8 ff-da b3 7d 3a d0 d0 0e 82   ..........}:....
    0090 - a2 ea 1c 8d 9f 70 6e 81-43 a8 dd cd 8e fb 88 f9   .....pn.C.......
    00a0 - fe 45 32 5f 64 31 13 ea-1b 83 31 79 f0 be ad 42   .E2_d1....1y...B
    00b0 - c1 ae b8 5f be a8 91 41-2a f3 29 2b 0c 47 e3 e0   ..._...A*.)+.G..
    00c0 - 0e fc ba 6f 92 db e8 99-36 bd 72 99 6e a9 0b 82   ...o....6.r.n...

    Start Time: 1677605439
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 7A82442EB892A758B712E3ADCD2FDF9E0C6039DF1F48E273946DA260CC970A40
    Session-ID-ctx: 
    Resumption PSK: 430BC5C548BE147671770A28E6804ED98F1DA06B135C75D8662D5DA2A5C5DB919D241296FAD446042E04D24C47C2B53F
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 70 f2 f5 0a f4 da 59 2b-66 40 bc 3c 8d 67 67 76   p.....Y+f@.<.ggv
    0010 - b4 37 ce d0 ac c0 aa ca-89 c7 0f c2 75 dd 39 44   .7..........u.9D
    0020 - ec 68 7c c9 b4 14 c6 6b-20 27 cb 00 c6 28 0b ff   .h|....k '...(..
    0030 - 9b 27 20 3e 00 ff 16 29-26 72 c3 35 0a 1a 0d 6f   .' >...)&r.5...o
    0040 - 41 8e 61 ff b8 38 74 32-6f 4c a6 7c b4 a8 74 9b   A.a..8t2oL.|..t.
    0050 - 05 d1 1f 22 de bc 58 13-38 f4 0b 7a 1e 1d e8 ac   ..."..X.8..z....
    0060 - 9c 92 6c c1 4d ed 3f 03-75 f3 52 87 e5 62 3c 95   ..l.M.?.u.R..b<.
    0070 - 04 1e ab 8a 9c d7 da 56-d7 93 ba aa 72 fc ed 00   .......V....r...
    0080 - 37 10 d6 56 3b 4a 65 1a-7d 55 1e bb 99 bd 62 92   7..V;Je.}U....b.
    0090 - ee 79 0c 8f f5 33 ce 71-8d 80 3e ce 91 d8 84 c3   .y...3.q..>.....
    00a0 - 11 87 43 a8 08 fe 6b 59-18 cb b8 21 18 1c ae e8   ..C...kY...!....
    00b0 - cc 0c 72 3a c9 2d ae bc-74 3a f2 9c 01 de 8e d9   ..r:.-..t:......
    00c0 - 91 71 05 ba 9e ad 6b 90-50 9f b9 6f 9a d5 d6 c8   .q....k.P..o....

    Start Time: 1677605439
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
JQttfApK4SeyHwDlI9SXGR50qclOAil1
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----

closed
bandit16@bandit:~$ exit
logout
Connection to bandit.labs.overthewire.org closed.
    
┌──(kali㉿kali)-[~]
└─$ chmod 600 llave.txt                                             
    
┌──(kali㉿kali)-[~]
└─$ ssh -i llave.txt bandit17@bandit.labs.overthewire.org -p 2220  
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames


      ,----..            ,----,          .---.
     /   /   \         ,/   .`|         /. ./|
    /   .     :      ,`   .'  :     .--'.  ' ;
   .   /   ;.  \   ;    ;     /    /__./ \ : |
  .   ;   /  ` ; .'___,/    ,' .--'.  '   \' .
  ;   |  ; \ ; | |    :     | /___/ \ |    ' '
  |   :  | ; | ' ;    |.';  ; ;   \  \;      :
  .   |  ' ' ' : `----'  |  |  \   ;  `      |
  '   ;  \; /  |     '   :  ;   .   \    .\  ;
   \   \  ',  /      |   |  '    \   \   ' \ |
    ;   :    /       '   :  |     :   '  |--"
     \   \ .'        ;   |.'       \   \ ;
  www. `---` ver     '---' he       '---" ire.org


Welcome to OverTheWire!

If you find any problems, please report them to the #wargames channel on
discord or IRC.

--[ Playing the games ]--

  This machine might hold several wargames.
  If you are playing "somegame", then:

    * USERNAMES are somegame0, somegame1, ...
    * Most LEVELS are stored in /somegame/.
    * PASSWORDS for each level are stored in /etc/somegame_pass/.

  Write-access to homedirectories is disabled. It is advised to create a
  working directory with a hard-to-guess name in /tmp/.  You can use the
  command "mktemp -d" in order to generate a random and hard to guess
  directory in /tmp/.  Read-access to both /tmp/ is disabled and to /proc
  restricted so that users cannot snoop on eachother. Files and directories
  with easily guessable or short names will be periodically deleted! The /tmp
  directory is regularly wiped.
  Please play nice:

    * don't leave orphan processes running
    * don't leave exploit-files laying around
    * don't annoy other players
    * don't post passwords or spoilers
    * again, DONT POST SPOILERS!
      This includes writeups of your solution on your blog or website!

--[ Tips ]--

  This machine has a 64bit processor and many security-features enabled
  by default, although ASLR has been switched off.  The following
  compiler flags might be interesting:

    -m32                    compile for 32bit
    -fno-stack-protector    disable ProPolice
    -Wl,-z,norelro          disable relro

  In addition, the execstack tool can be used to flag the stack as
  executable on ELF binaries.

  Finally, network-access is limited for most levels by a local
  firewall.

--[ Tools ]--

 For your convenience we have installed a few useful tools which you can find
 in the following locations:

    * gef (https://github.com/hugsy/gef) in /opt/gef/
    * pwndbg (https://github.com/pwndbg/pwndbg) in /opt/pwndbg/
    * peda (https://github.com/longld/peda.git) in /opt/peda/
    * gdbinit (https://github.com/gdbinit/Gdbinit) in /opt/gdbinit/
    * pwntools (https://github.com/Gallopsled/pwntools)
    * radare2 (http://www.radare.org/)

 Both python2 and python3 are installed.

--[ More information ]--

  For more information regarding individual wargames, visit
  http://www.overthewire.org/wargames/

  For support, questions or comments, contact us on discord or IRC.

  Enjoy your stay!

bandit17@bandit:~$ cat /etc/bandit_pass/bandit17
VwOSWtCA7lRKkTfbr2IDh6awj9RNZM5e
bandit17@bandit:~$ exit

```

## Notas adicionales
| comando | descripcion
| xx | xx el contenido de un archivo 

## Referencias
