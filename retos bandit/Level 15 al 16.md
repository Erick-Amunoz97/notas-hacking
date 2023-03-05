# Bandit Level 15 -> Level 16



## objetivo
The password for the next level can be retrieved by submitting the password of the current level to **port 30001 on localhost** using SSL encryption.

**Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…**

## Datos de acceso al nivel
**ssh bandit15@bandit.labs.overthewire.org -p 2220**
bandit15
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt

## solucion
```bash()
bandit15@bandit:~$ openssl s_client -connect localhost:30001
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = localhost
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = localhost
verify error:num=10:certificate has expired
notAfter=Feb 21 22:03:56 2023 GMT
verify return:1
depth=0 CN = localhost
notAfter=Feb 21 22:03:56 2023 GMT
verify return:1
---
Certificate chain
 0 s:CN = localhost
   i:CN = localhost
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA1
   v:NotBefore: Feb 21 22:02:56 2023 GMT; NotAfter: Feb 21 22:03:56 2023 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDCzCCAfOgAwIBAgIEF3vcjDANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjMwMjIxMjIwMjU2WhcNMjMwMjIxMjIwMzU2WjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCg
1elREdWTbtCZNl7KNMjleNrcG71f9lZhjAfM4x+TDwlPpT+Q9O3V6J687fJdMH85
xfUwcZG0XFCeN1nxnmQadGF/ZHEt0laWmCQfo5LogzgGFcaZWC1a6XZ5ZKv7SRDt
tvPK/CTKwOJD5ZJVEXEk9R8YQ/VbKwZMDc43WD/HKypvBv7fZVbJkKYY75LOby86
7gux29Emhntj5pZyYagYbmonnAiw6447bGTC1d6jilGPhXMzckTI57WGeNdp4ppL
3pXSVDLOU2XJ8Um/L2VIgGTsUk5CwrtzVxyt6I5sKavUhsNGlzqvHI/McgbsnHi8
3LDg9k/Co8F21eZFooVlAgMBAAGjZTBjMBQGA1UdEQQNMAuCCWxvY2FsaG9zdDBL
BglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0ZWQgYnkgTmNhdC4g
U2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3DQEBBQUAA4IBAQBz
lgp6XhMshglRxhxHRg1xHkVYSFSBaS5Adq5OIoE/oetyedTiO2B9MLmNZ9Juu/WK
/+WZFmNdzQ6Iw5ueBz/rmY+DvzTjjd4CPPqeilG5mngceR5nliM9mXkpQlmm3T1a
8JuBrDugrN9BP4IeBTER0pgQcQvsRATrv/SAVFVBhTSvOKFhoYNEdBzaqxclEjD6
bl3UkzNag/S3iLuv24xoQkMmlFC2afaswkG/cQ4p3BuapuZORjbohUOXS24QDl0z
A2RDFNizi42ZVJ8ZW1qbURZ4n/VbIAi7vRHldPKjC8hYAcdvUekB0schBlc1J06Z
phGCgzTVUzJu9yz8uKzO
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
    Session-ID: 41D0F1C9101F960D48626A4BFFB3C880151C6DB21924CA72C170DAA3078DC5DA
    Session-ID-ctx: 
    Resumption PSK: 5F94CAF80C8430BE7FE9524F89D80FAE3033AE2F8BCE0776B89083DCE7F93242E51E5DFC246F16AA304C8D0317F49B6D
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - a5 3d 92 1f d1 78 36 48-bb a6 da 4d 19 13 ee a7   .=...x6H...M....
    0010 - 2e 77 96 a6 c8 00 47 c5-00 45 97 6b 50 49 dd 06   .w....G..E.kPI..
    0020 - a3 fb 5d 06 39 2b 91 1a-2c eb 1f ad 63 57 63 1e   ..].9+..,...cWc.
    0030 - 26 ad 86 35 b1 d6 6b 12-c3 ae be 63 79 4d 49 2d   &..5..k....cyMI-
    0040 - 61 97 09 79 ad ae 6a a4-23 16 9b 70 2a f3 b1 e0   a..y..j.#..p*...
    0050 - 91 93 0d aa 5d 5c 5e 1e-09 5b e1 4d e9 d0 1c cb   ....]\^..[.M....
    0060 - 1a cf 06 08 fd 03 1b 6c-61 b0 22 87 76 62 e8 20   .......la.".vb. 
    0070 - 56 6c 07 04 2a bb 4a 74-97 95 8d f2 d7 7b 1b a9   Vl..*.Jt.....{..
    0080 - 10 b8 c3 b6 7a 0e c3 bc-16 76 17 51 cb 97 ce df   ....z....v.Q....
    0090 - 74 60 eb ff b9 06 e6 d2-1d c9 3e d5 2a 70 b4 17   t`........>.*p..
    00a0 - 1b 1b 9c af fc 95 3d df-db 16 a3 95 07 ec 4e eb   ......=.......N.
    00b0 - a9 2a dc ee bc e5 ee be-e4 00 87 06 49 ec a3 cd   .*..........I...
    00c0 - 38 2e 8d e2 34 50 47 fd-20 4c c7 d7 19 a5 ae 8b   8...4PG. L......

    Start Time: 1677177421
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
    Session-ID: C1E0B3B0B6F7B681786B2B5513B408722094519817382BD2AE4C4CDF843DF8DC
    Session-ID-ctx: 
    Resumption PSK: C757D8CE48C1CD9EF5AD158A20736ED20B8288FD5773BD3FBAE51774EC7F0F3F6026B2932AC559F6C522EB37369BEFCB
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - a5 3d 92 1f d1 78 36 48-bb a6 da 4d 19 13 ee a7   .=...x6H...M....
    0010 - 67 26 22 ab 70 b4 af 09-f4 84 77 54 7d 21 3c c8   g&".p.....wT}!<.
    0020 - 7d 7a 35 0a 33 96 48 12-62 78 3c 8c 70 3c 62 dd   }z5.3.H.bx<.p<b.
    0030 - 80 5e 49 21 69 e3 7b 59-d6 ea e1 72 41 9c 83 90   .^I!i.{Y...rA...
    0040 - 39 4f 50 02 cf 36 c7 32-ba e9 d7 e2 26 6b 0b 7a   9OP..6.2....&k.z
    0050 - 52 d9 9d ff b6 10 8e 00-0c 63 d0 6d 19 f4 dd 63   R........c.m...c
    0060 - 59 68 56 f3 8e 9c e1 ae-be fe 30 3c b7 d5 7e 91   YhV.......0<..~.
    0070 - 1c cc fa c8 cd 3c b3 65-4f 83 e8 05 a6 7b 1a da   .....<.eO....{..
    0080 - c6 ae 58 00 4f ac 1a e8-04 44 0f 7f 6e 9d ea 95   ..X.O....D..n...
    0090 - 0a e9 8d df d3 55 cc 51-f5 fe 09 e1 5b 23 d7 70   .....U.Q....[#.p
    00a0 - 19 ac d7 2d db ba e5 50-0f 97 5b a9 01 56 91 19   ...-...P..[..V..
    00b0 - fd 54 9d 8d 0e 98 52 17-eb ac 6d 78 f6 92 b0 9c   .T....R...mx....
    00c0 - 70 06 21 bd 29 1c 43 24-37 fe 3f f0 22 b6 4b ab   p.!.).C$7.?.".K.

    Start Time: 1677177421
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt         
Correct!
JQttfApK4SeyHwDlI9SXGR50qclOAil1

```

## Notas adicionales
| comando | descripcion
| openssl | una biblioteca de software o conjunto de herramientas de criptografía que hace que la comunicación a través de redes informáticas sea más segura. |
| s_client | implementa un cliente SSL/TLS genérico que se conecta a un host remoto mediante SSL/TLS. Es una herramienta de diagnóstico muy útil para servidores SSL. |

## Referencias
[[https://www.geeksforgeeks.org/practical-uses-of-openssl-command-in-linux/|Link para comando ssl]]
[[https://www.openssl.org/docs/man1.1.1/man1/openssl-s_client.html#:~:text=The%20s_client%20command%20implements%20a,diagnostic%20tool%20for%20SSL%20servers.|Link para comando s_client]]
[[https://overthewire.org/wargames/bandit/bandit16.html|Link del nivel 15 al 16]]
