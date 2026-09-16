# Variável de sistema _TALLY

Contém o número de registros processados pelo comando de tabela executado mais recentemente.

```foxpro
_TALLY = nRecords
```

#### Parâmetros
 **nRecords**
Contém um valor numérico que indica o número de registros processados pelo comando de tabela executado mais recentemente. Ao iniciar o Visual FoxPro, _TALLY é definido como zero (0).

# Observações

Certos comandos de processamento de tabelas retornam informações sobre seu status durante a execução. Quando tal comando termina de executar, exibe o número de registros processados se o comando SET TALK estiver definido como ON. Se o comando for executado em views e tabelas locais, armazena esse número na variável de sistema _TALLY.

O comando INSERT - SQL altera _TALLY se um comando SQL SELECT for usado para especificar os dados a inserir.

A tabela a seguir lista os comandos e funções que retornam informações de status e armazenam o número de registros processados em _TALLY somente quando executados em tabelas e views locais.

| APPEND FROM Command | REINDEX Command |
| --- | --- |
| AVERAGE Command | REPLACE Command |
| CALCULATE Command | REQUERY( ) Function |
| COPY TO Command | SELECT - SQL Command |
| COUNT Command | SUM Command |
| DELETE Command | SORT Command |
| DELETE - SQL Command | TOTAL Command |
| INDEX Command | UPDATE Command |
| INSERT - SQL Command (Used with SELECT) | UPDATE – SQL Command |
| PACK Command | |

# Exemplo

O exemplo a seguir retorna o número de clientes dos EUA de uma tabela Customer usando o comando SQL SELECT e armazena automaticamente em _TALLY. O comando ? exibe o valor armazenado em _TALLY.

```foxpro
SELECT * FROM customer ;
   WHERE country = 'USA' ;
   INTO CURSOR temp
? _TALLY
```

Para mais informações, consulte ? | ?? Command.
