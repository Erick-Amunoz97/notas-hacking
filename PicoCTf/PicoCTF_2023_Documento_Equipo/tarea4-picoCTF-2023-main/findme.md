# findme
#picoCTF2023 #WEB_EXPLOITATION  #Concurso #DuplicaLaDosis #Insoportable 
## Objetivo
Help us test the form by submiting the username as `test` and password as `test!`

Additional details will be available after launching your challenge instance.
## Solución
Nos encontramos con una página web con un primer formulario que nos pide ingresar las credenciales de usuario `test` y contraseña `test!`.
Tras hacer eso se nos es redireccionado a una siguiente página web que nos muestra un código HTML bastante peculiar.
En este código HTML, cuando el usuario escribe un texto en el campo de entrada con el id "keyword" y hace clic en el botón "Go" dentro del formulario con el id "search-form", se llama a la función "search()". Esta función obtiene el elemento "search-result" por su id y lo muestra en la página. Además, establece el contenido del elemento "search-term" con el valor del texto que el usuario escribió en el campo "keyword".
Luego, la función realiza una solicitud al servidor para obtener los resultados relacionados con el valor de la palabra clave que el usuario ingresó en el campo "keyword". Sin embargo, esta parte del código está incompleta, ya que el código actual solo devuelve un valor fijo "Waiting for server's response... lol" en el elemento "search-result" sin realizar ninguna solicitud al servidor.
Entonces la bandera se encuentra cifrada en base64 dentro de los dos URLs anteriores que nos llevan hasta la ultima pagina web.
Siendo estos URLs los siguientes.
- http://saturn.picoctf.net:53197/next-page/id=cGljb0NURntwcm94aWVzX2Fs
- http://saturn.picoctf.net:53197/next-page/id=bF90aGVfd2F5X2RmNDRjOTRjfQ==
Las partes de la bandera se encuentran en después del `=` que se encuentra posterior al id.
Siendo el texto eb base64 el siguiente `cGljb0NURntwcm94aWVzX2FsbF90aGVfd2F5X2RmNDRjOTRjfQ`.
Dandonos la bandera.
===picoCTF{proxies_all_the_way_df44c94c}===
## Notas adicionales

## Referencias