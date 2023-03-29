# MatchTheRegex
#picoCTF2023 #WEB_EXPLOITATION  #Concurso #DuplicaLaDosis #Insoportable 
## Objetivo
How about trying to match a regular expression

Additional details will be available after launching your challenge instance.
## Solución
Se nos proporciona una pagina web con código HTML y JavaScript que hace lo siguiente.
1. Define una página web con un encabezado y un formulario.
2. El formulario tiene un campo de entrada de texto donde el usuario puede escribir un texto.
3. Cuadno el usuario hace click en el botón `SUBMIT`, se ejecuta la funcion `send_request()` en JavaScript.
4. La función `send_request()` toma el valor del campo de entrada de texto, construye una URL con ese valor como parámetro de consulta (`/flag?input=valor_del_campo`), y envía una solicitud HTTP a esa URL utilizando la función `fetch()`.
5. Cuando la respuesta del servidor llega, se convierte en texto (`res.text()`), se analiza como JSON (`JSON.parse(res)`), y se muestra una alerta con el valor de la propiedad `flag` de la respuesta JSON (`alert(res_json.flag)`).
El objetivo de este reto es coincidir con la expresión regular señalada dentro del código JavaScript.

```javascript
function send_request() {
		let val = document.getElementById("name").value;
		// ^p.....F!?
		fetch(`/flag?input=${val}`)
			.then(res => res.text())
			.then(res => {
				const res_json = JSON.parse(res);
				alert(res_json.flag)
				return false;
			})
		return false;
	}
```

La expresión regular `^p.....F!?` encajaría con una cadena de texto que comienza con la letra "p", seguida de exactamente 5 caracteres cualesquiera (excepto salto de línea), y termina con la letra "F" seguida opcionalmente por un signo de exclamación "!".
En este caso la cadena utilizada fue: `"pabcdeF!"`.

==picoCTF{succ3ssfully_matchtheregex_08c310c6}==
## Notas adicionales

## Referencias