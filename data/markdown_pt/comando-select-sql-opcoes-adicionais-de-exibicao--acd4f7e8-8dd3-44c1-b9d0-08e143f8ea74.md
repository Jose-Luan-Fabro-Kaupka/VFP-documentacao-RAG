# Comando SELECT - SQL - Opções adicionais de exibição

Você pode especificar opções adicionais de exibição para os resultados finais da consulta de uma instrução SQL SELECT.

Para a sintaxe completa, consulte Comando SELECT - SQL.

A sintaxe detalhada das Opções adicionais de exibição é a seguinte:

```foxpro
[PREFERENCE PreferenceName] [NOCONSOLE] [PLAIN] [NOWAIT]
```

#### Parâmetros
 **[PREFERENCE PreferenceName ]**
Salva os atributos e opções da janela Browse para uso posterior quando os resultados da consulta são enviados a uma janela browse. Observação Você pode recuperar preferências a qualquer momento. Os atributos, ou preferências, são salvos indefinidamente no arquivo de recursos FoxUser.dbf. Na primeira vez que você usa a cláusula PREFERENCE em uma instrução SELECT, ela cria a preferência. Emitir uma instrução SELECT posteriormente com o mesmo nome de preferência restaura a janela Browse para esse estado de preferência. Quando a janela Browse é fechada, a preferência é atualizada. Se você fechar uma janela Browse pressionando CTRL+Q ou CTRL+W, as alterações feitas na janela Browse não são salvas no arquivo de recursos.
**[NOCONSOLE]**
Impede a exibição dos resultados da consulta enviados a um arquivo, à impressora ou à janela principal do Visual FoxPro.
**[PLAIN]**
Impede que os cabeçalhos de coluna apareçam na saída da consulta exibida.

> **Observação:** Você pode usar a cláusula PLAIN independentemente de uma cláusula TO estar incluída. Se uma cláusula INTO estiver incluída, o Visual FoxPro ignora a opção PLAIN.
 **[NOWAIT]**
Continua a execução do programa depois que a janela Browse é aberta e os resultados da consulta são direcionados a ela. O programa não aguarda o fechamento da janela Browse, mas continua a execução na linha do programa imediatamente após a instrução SELECT. Observação Se uma cláusula INTO estiver incluída, o Visual FoxPro ignora a opção NOWAIT. Por exemplo, quando você inclui a cláusula TO SCREEN para direcionar a saída à janela principal do Visual FoxPro ou a uma janela definida pelo usuário, a saída pausa quando a janela principal do Visual FoxPro ou a janela definida pelo usuário está cheia de resultados da consulta. Para ver o próximo conjunto de resultados da consulta, pressione uma tecla. No entanto, se você incluir NOWAIT , os resultados da consulta rolam para fora da janela principal do Visual FoxPro ou da janela definida pelo usuário sem pausar para uma tecla.

# Observações

O código a seguir mostra um resumo das cláusulas principais do Comando SELECT - SQL:

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
- Cláusula UNION
- Cláusula ORDER BY
- Cláusula INTO ou TO
- Opções adicionais de exibição
