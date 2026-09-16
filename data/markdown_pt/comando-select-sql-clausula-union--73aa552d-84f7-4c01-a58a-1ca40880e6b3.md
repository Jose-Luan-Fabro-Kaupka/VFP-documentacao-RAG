# Comando SELECT - SQL - Cláusula UNION

A cláusula UNION combina os resultados de duas ou mais instruções SQL SELECT em um único conjunto de resultados contendo linhas de todas as consultas na operação UNION.

> **Observação:** Quando uma das colunas é do tipo Memo, General ou Blob, não é permitido realizar uniões de tipos de coluna diferentes.

Para a sintaxe completa, consulte o comando SELECT - SQL.

A sintaxe detalhada para a cláusula UNION é a seguinte:

```foxpro
[UNION [ALL] SELECTCommand]
```

#### Parâmetros
 **[UNION [ALL] SELECTCommand ]**
Especifica outra instrução SELECT. Por padrão, UNION elimina linhas duplicadas do conjunto de resultados combinado.

> **Observação:** A palavra-chave ALL inclui linhas duplicadas no conjunto de resultados combinado.

# Observações

O código a seguir mostra um resumo das principais cláusulas do comando SELECT - SQL:

```foxpro
SELECT Select_List
   FROM Table_List
...[WITH (BUFFERING = lExpr)]
   [WHERE Conditions]
   [GROUP BY Column_List]
   [HAVING Conditions]
   [UNION Clause]
   [ORDER BY Column_List]
   [INTO Clause | TO Clause ]
   [Additional_Display_Options]
```

Para obter mais informações sobre uma cláusula específica do comando SQL SELECT, consulte os seguintes tópicos:
 - Cláusula SELECT
- Cláusula FROM
- Comando SELECT - SQL - Cláusula WITH
- Comando SELECT - SQL - Cláusula WHERE
- Cláusula GROUP BY
- Cláusula HAVING
- Cláusula ORDER BY
- Cláusula INTO ou TO
- Opções de exibição adicionais

Você pode usar a cláusula UNION para simular um outer join. Você pode especificar várias cláusulas UNION; não há limite para o número de cláusulas UNION por instrução SELECT.

O Visual FoxPro suporta conversão implícita de tipos de dados para tipos de dados que a suportam. Para obter mais informações, bem como regras e considerações sobre cláusulas UNION, consulte Considerations for SQL SELECT Statements.
