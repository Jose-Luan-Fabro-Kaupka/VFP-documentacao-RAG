# WHILE Cláusulas

A cláusula A WHILE faz com que o comando a atue em cada registro, desde que a expressão lógica seja avaliada como verdadeira (.T.). Na primeira vez que a expressão é avaliada como falsa (.F.), o comando the cessa sem tentar nenhum registro restante. Esta expressão é normalmente usada com uma tabela que foi classificada ou indexada nos campos incluídos na expressão WHILE. Por exemplo, o exemplo a seguir navega em uma tabela indexada para localizar o primeiro registro que atende à condição e, em seguida, o comando REPLACE atua nos registros que atendem à condição WHILE.

```foxpro
USE Mytable INDEX street
LOCATE FOR UPPER(street) = "MAIN"
REPLACE street WITH "Maine" WHILE UPPER(street) = "MAIN"
```

Você pode usar as expressões Scope, FOR e WHILE no mesmo comando Visual FoxPro. Por exemplo, os exemplos a seguir armazenam um novo valor no campo `status` de vários registros.

```foxpro
REPLACE ALL status WITH "Active" FOR total > 30 ;
   WHILE expd > {^1998/02/16}
```

Quando você especifica FOR e WHILE, a expressão WHILE tem precedência e a cláusula FOR é usada para filtrar os registros selecionados por WHILE.

A tabela a seguir lista comandos nos quais você pode usar uma cláusula WHILE.
 Comandos que usam cláusulas WHILE
| AVERAGE | COUNT | RECALL |
| --- | --- | --- |
| BLANK | DELETE | REPLACE |
| BROWSE | DISPLAY | REPLACE FROM ARRAY |
| CALCULATE | EXPORT | REPORT |
| CHANGE | LABEL | SCAN ... ENDSCAN |
| COPY TO ARRAY | LIST | SORT |
| COPY TO | LOCATE | SUM |
