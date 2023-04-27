
# Mind your Ps and Qs

## Descripcion
In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? [values](https://mercury.picoctf.net/static/3cfeb09681369c26e3f19d886bc1e5d9/values)
## Pistas
Bits are expensive, I used only a little bit over 100 to save money
## Solucion
Obtenemos 3 valores del link proporcionado y nos sugiere el reto que usemos n para obtener p y q.
```bash()
┌──(kali㉿kali)-[~/hacking/MindYourPsAndQs]
└─$ cat values        
Decrypt my super sick RSA:
c: 8533139361076999596208540806559574687666062896040360148742851107661304651861689
n: 769457290801263793712740792519696786147248001937382943813345728685422050738403253
e: 65537                                                                                                                    
```

Ya que n es muy pequeño, lo podemos factorizar y sacar p y q usando una pagina web como herramienta para factorizar.
![[Pasted image 20230427145743.png]]
nos dan dos numeros primos uno de 40 digitos y el otro de 42. estos serian nuestros p y q. Insertamos todos los numeros a python y usamos las formulas para sacar el tn, el d , finalmente el m. 
al final usamos la funcion de `long_to_bytes` para sacar la bandera.


```bash()
┌──(kali㉿kali)-[~]
└─$ python3
Python 3.10.8 (main, Nov  4 2022, 09:21:25) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> c = 8533139361076999596208540806559574687666062896040360148742851107661304651861689
>>> n = 769457290801263793712740792519696786147248001937382943813345728685422050738403253
>>> e = 65537
>>> from Crypto.Util.number import long_to_bytes
>>> from Crypto.Util.number import inverse
>>> 
>>> p = 1617549722683965197900599011412144490161
>>> q = 475693130177488446807040098678772442581573
>>> 
>>> n = p * q
>>> n
769457290801263793712740792519696786147248001937382943813345728685422050738403253
>>> tn = (p-1) * (q-1)
>>> d = inverse(e,tn)
>>> m = pow(c,d,n)
>>> long_to_bytes(m)
b'picoCTF{sma11_N_n0_g0od_45369387}'
>>> 

```

## Bandera

picoCTF{sma11_N_n0_g0od_45369387}

## Notas adicionales

| comando | descripcion |
| --- | --- |

## Referencias
[[http://www.factordb.com/index.php?query=769457290801263793712740792519696786147248001937382943813345728685422050738403253|Pagina para factorizar]]
