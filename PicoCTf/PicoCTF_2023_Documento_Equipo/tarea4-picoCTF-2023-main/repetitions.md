# repetitions
#GeneralSkills  #picoCTF2023 #Concurso #DuplicaLaDosis #Insoportable
## Objetivo
Can you make sense of this file? Download the file [here](https://artifacts.picoctf.net/c/295/enc_flag).
## Solución

```bash
┌──(kali㉿kali)-[~/Downloads/picoCTF2023]
└─$ file enc_flag 
enc_flag: ASCII text
                                                                                
┌──(kali㉿kali)-[~/Downloads/picoCTF2023]
└─$ cat enc_flag     
VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVh
RmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNk
MlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVW
VkpEVGxaYVdFMVhSbHBWV0VKVVZGVm9RMlZHV2toa1JrNVZDbUY2UmtkVVZsWnZWVEpHZEdWRlZs
aGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==

```

Se tiene que decodificar de base64 6 veces.

==picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_dbc4340a}==
- Receta cyberchef: https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=Vm1wR1UxRXlSWGxVV0d4VFlteEtWVll3WkZOV2JHeHlWMjFHVjFKdGVEQlViRnBQWVd4S2RGVnNhRnBXVmxVeFdWWmFTMVpXV25WaApSbVJYWld0YWIxZFdXbXRTTWs1eVRsWldXQXBpVlZwVVZtMTBkMVZXWkZkVmEyUnBZbFphV0ZadE5WZFZaM0JwVTBWS2VsZFdVa05rCk1sWlhWbGhvV0dKWVFrOVZiRkpYVTBaa2NWUnVUbGRhTTBKWlZXcEdTMlZXV2tkYVNHUlhDazFzV25wV1YzaGhWbTFLUms1WE9WVlcKVmtwRVZHeGFZVmRGTVZoU2JIQldWMFZLVlZaR1ZtOVJNbFpIVjJ0b2ExSnJOVlpEYlVZMlVtdGtWVlpzV25aV1ZFcEhaRWRXUmxacwphR2tLWWxScmVsWkVSbGRVTWtwelVXeFdUbEpZVGt4RFp6MDlDZz09Cg
## Notas adicionales

## Referencias