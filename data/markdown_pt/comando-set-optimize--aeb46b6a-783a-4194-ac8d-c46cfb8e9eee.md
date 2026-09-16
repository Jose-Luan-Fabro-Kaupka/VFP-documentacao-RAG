# Comando SET OPTIMIZE

Habilita ou desabilita a Rushmore Query Optimization.

```foxpro
SET OPTIMIZE ON | OFF
```

#### Parâmetros
 **ON**
(Padrão) Habilita a otimização Rushmore.
**OFF**
Desabilita a otimização Rushmore.

# Observações

O Visual FoxPro usa uma tecnologia chamada Rushmore Query Optimization para otimizar a recuperação de dados. Comandos de tabela que suportam uma cláusula FOR usam a tecnologia Rushmore para melhorar seu desempenho. Quando você emite um comando que pode ser otimizado, o Rushmore determina quais registros correspondem ao critério FOR. O comando é executado nos registros da tabela que correspondem ao conjunto de registros Rushmore.

Em casos raros, você deve desabilitar a otimização Rushmore. Se um comando que se beneficia da otimização Rushmore modifica as chaves de índice de uma consulta, o conjunto de registros Rushmore pode ficar desatualizado. Você pode desabilitar a otimização Rushmore para garantir que tenha as informações mais atuais da tabela.

Você pode usar SET OPTIMIZE para habilitar ou desabilitar globalmente a tecnologia Rushmore. Todo comando que usa Rushmore tem uma cláusula NOOPTIMIZE que você pode incluir para desabilitar a otimização Rushmore para o comando.

Para obter mais informações, consulte Using Rushmore Query Optimization to Speed Data Access.

A seguir estão os comandos cujo desempenho é otimizado pelo Rushmore:

| Commands | |
| --- | --- |
| AVERAGE | INDEX |
| BLANK | LABEL |
| BROWSE | LIST |
| CALCULATE | LOCATE |
| CHANGE | RECALL |
| COPY TO | REPLACE |
| COPY TO ARRAY | REPLACE FROM ARRAY |
| COUNT | REPORT |
| DELETE | SCAN |
| DISPLAY | SORT |
| EDIT | SUM |
| EXPORT | TOTAL |
