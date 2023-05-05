
# Secrets

## Descripcion
We have several pages hidden. Can you find the one with the flag?The website is running [here](http://saturn.picoctf.net:65352/).
## Pistas
folders folders folders
## Solucion
La bandera la encontramos dentro del codigo de cada pagina usando el ctrl-u. Asi vamos viendo el codigo fuente y nos damos cuenta de archivos ocultos dentro de la pagina :

```bash()<!-- css -->

<link href="[secret/assets/index.css](http://saturn.picoctf.net:65352/secret/assets/index.css)" rel="stylesheet" />

</head>

<body>
```
primero encontramos este directorio llamado secret lo cual nos lleva a otra pagina secreta que contiene una pista mas

despues en la siguiente encontramos el /hidden
```bash
<html>

<head>

<title></title>

<link rel="stylesheet" href="[hidden/file.css](http://saturn.picoctf.net:65352/secret/hidden/file.css)" />

</head>
```

y finalmente encontramos el /superhidden que nos da la bandera al ingresar a esa pagina: 
```bash()
required

/>

<input type="hidden" name="db" value="superhidden/xdfgwd.html" />

  

<input

type="submit"

value="Login"
```

## Bandera

picoCTF{succ3ss_@h3n1c@10n_790d2615}

## Notas adicionales

| comando | descripcion

## Referencias
