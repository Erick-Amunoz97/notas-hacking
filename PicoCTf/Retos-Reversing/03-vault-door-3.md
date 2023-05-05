
# vault-door-3

## Descripcion
This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](https://jupiter.challenges.picoctf.org/static/a4018cec1446761cb2e8cce05db925fa/VaultDoor3.java)
## Pistas
Make a table that contains each value of the loop variables and the corresponding buffer index that it writes to.
## Solucion
bajamos el archivo javascript y vemos que hay una variable llamada password. y que se usa un charAt para codificarla. entonces ocupamos usar el mismo codigo pero al reves para decodificar la contraseña y obtener la bandera. para esto usamos el mozilla firefox del kali para usar la consola que tiene integrado. 
```bash()

allow pasting

var password = "jU5t_a_sna_3lpm12g94c_u_4_m7ra41";

var buffer = Array(32);

for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);…
"g"
buffer.join("")
"jU5t_a_s1mpl3_an4gr4m_4_u_c79a21"

```

## Bandera

picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c79a21}

## Notas adicionales

| comando | descripcion

## Referencias
