# Como: armazenar resultados de consulta em uma tabela, matriz ou cursor

Você pode armazenar os resultados da sua consulta em uma tabela, matriz ou cursor para outros usos, como preencher formulários e imprimir relatórios e etiquetas. Se desejar armazenar os resultados apenas temporariamente, envie os resultados para uma matriz ou cursor. Se desejar armazenar os resultados permanentemente, envie os resultados para uma tabela.

### Para especificar uma tabela como destino
- Use a cláusula INTO da instrução SELECT - SQL para especificar um destino.

O exemplo a seguir mostra uma cláusula INTO para uma tabela:

```foxpro
SELECT * ;
   FROM tastrade!customer ;
   WHERE customer.country = "Canada" ;
   INTO TABLE mytable
```

### Para especificar uma matriz como destino
- Use a cláusula INTO da instrução SELECT - SQL para especificar um destino.

O exemplo a seguir mostra uma cláusula INTO para uma matriz:

```foxpro
SELECT * ;
   FROM tastrade!customer ;
   WHERE customer.country = "Canada" ;
   INTO ARRAY aMyArray
```

### Para especificar um cursor como destino
- Use a cláusula INTO da instrução SELECT - SQL para especificar um destino.

O exemplo a seguir mostra uma cláusula INTO para um cursor chamado `mycursor`:

```foxpro
SELECT * ;
   FROM tastrade!customer ;
   WHERE customer.country = "Canada" ;
   INTO CURSOR mycursor
```

Se você criar uma tabela ou uma matriz, pode usá-la como qualquer outra tabela ou matriz no Visual FoxPro. Se você criar um cursor, pode navegar pelo seu conteúdo. O cursor é aberto na área de trabalho disponível mais baixa. Você pode acessá-lo usando o nome que atribuiu na instrução SELECT - SQL.

Os dois procedimentos a seguir descrevem duas maneiras comuns de incluir resultados de consulta armazenados em tabelas e cursors em uma aplicação.
