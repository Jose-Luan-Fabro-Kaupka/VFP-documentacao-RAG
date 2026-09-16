# Cláusulas Scope

Se um comando do Visual FoxPro tem uma cláusula Scope, você pode especificar um intervalo de registros sobre os quais o comando deve atuar.

# Cláusulas

A tabela a seguir descreve as cláusulas que você pode usar para Scope.

| Scope | Descrição |
| --- | --- |
| ALL | Afeta todos os registros na tabela. |
| NEXT nExpr | Afeta o próximo número nExpr de registros começando com o registro atual. No exemplo a seguir, o comando REPLACE atua no registro atual e nos dois registros seguintes: REPLACE status WITH "open" NEXT 3 |
| RECORD nRecordNumber | Afeta somente o número de registro especificado. Observação Diferentemente das outras cláusulas scope, que são relativas ao número de registros na tabela e à posição atual do ponteiro de registro, a cláusula scope RECORD sempre atua no número de registro físico especificado. Portanto, RECORD nRecordNumber não respeita os valores de SET FILTER ou SET DELETED. No exemplo a seguir, o comando REPLACE atua no registro número 5: REPLACE status WITH "open" RECORD 5 |
| REST | Afeta um intervalo de registros começando com o registro atual e terminando com o último registro na tabela. No exemplo a seguir, o comando REPLACE armazena um valor nulo nos registros restantes: REPLACE status WITH .NULL. REST |

Você também pode especificar intervalos de registros usando cláusulas FOR e WHILE. Para obter mais informações, consulte Cláusulas FOR e Cláusulas WHILE.
