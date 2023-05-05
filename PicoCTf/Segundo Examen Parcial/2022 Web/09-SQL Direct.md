
# SQL Direct

## Descripcion
Connect to this PostgreSQL server and find the flag!

Additional details will be available after launching your challenge instance.
## Pistas
what does an SQL database contain?
## Solucion
ocupamos usar postgreSQL para encontrar la bandera dentro del sql. 
Al realizar un query basico obtenemos la bandera: 

```bash()
┌──(kali㉿kali)-[~]
└─$ psql -h saturn.picoctf.net -p 49946 -U postgres pico
Password for user postgres: 
psql (15.1 (Debian 15.1-1), server 15.2 (Debian 15.2-1.pgdg110+1))
Type "help" for help.

pico-# \dt
         List of relations
 Schema | Name  | Type  |  Owner   
--------+-------+-------+----------
 public | flags | table | postgres
(1 row)

pico=# SELECT * FROM flags;
 id | firstname | lastname  |                address                 
----+-----------+-----------+----------------------------------------
  1 | Luke      | Skywalker | picoCTF{L3arN_S0m3_5qL_t0d4Y_73b0678f}
  2 | Leia      | Organa    | Alderaan
  3 | Han       | Solo      | Corellia
(3 rows)


```

## Bandera

picoCTF{L3arN_S0m3_5qL_t0d4Y_73b0678f}

## Notas adicionales

| comando | descripcion

## Referencias
