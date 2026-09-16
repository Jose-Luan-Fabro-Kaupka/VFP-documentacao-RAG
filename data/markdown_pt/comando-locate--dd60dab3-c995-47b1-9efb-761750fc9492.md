# Comando LOCATE

Pesquisa sequencialmente a tabela pelo primeiro registro que corresponde à expressão lógica especificada.

```foxpro
LOCATE [FOR lExpression1]   [Scope]   [WHILE lExpression2]   [NOOPTIMIZE]
```

#### Parâmetros
 **FOR lExpression1**
Pesquisa sequencialmente a tabela atual pelo primeiro registro que corresponde à expressão lógica lExpression1 . Rushmore Query Optimization optimizes a query created with LOCATE FOR if lExpression1 is an optimizable expression. For best performance, use an optimizable expression in the FOR clause. For more information, see SET OPTIMIZE Command and Using Rushmore Query Optimization to Speed Data Access .
**Scope**
Especifica um intervalo de registros a localizar. Only the records that fall within the range are located. The scope clauses are: ALL, NEXT nRecords , RECORD nRecordNumber , and REST. Commands that include Scope operate only on the table in the active work area. The default scope for LOCATE is ALL records.
**WHILE lExpression2**
Especifica uma condição pela qual os registros são pesquisados enquanto a expressão lógica lExpression2 for avaliada como true (.T.).
**NOOPTIMIZE**
Desabilita a otimização Rushmore Query Optimization do LOCATE. For more information, see SET OPTIMIZE Command and Using Rushmore Query Optimization to Speed Data Access .

# Observações

A tabela não precisa estar indexada.

Se você usar o comando LOCATE sem a expressão FOR, o Visual FoxPro posiciona o ponteiro de registro no primeiro registro lógico. Isso é mais rápido que usar GO TOP quando um filtro está em uso ou quando DELETED está ON.

Se LOCATE encontrar um registro correspondente, você pode usar RECNO( ) para retornar o número do registro correspondente. If a matching record is found, FOUND( ) returns true (.T.), and EOF( ) returns false (.F.). If SET TALK is ON, the record number of the matching record is displayed.

Depois que LOCATE encontra um registro correspondente, você pode emitir CONTINUE para pesquisar o restante da tabela por registros correspondentes adicionais. When CONTINUE is executed, the search process resumes, starting with the record immediately following the matching record. You can issue CONTINUE repeatedly until the end of the scope or the end of the table is reached.

If a match isn't found, RECNO( ) returns the number of records in the table plus 1, FOUND( ) returns false (.F.), and EOF( ) returns true (.T.).

LOCATE e CONTINUE são específicos da área de trabalho atual. If another work area is selected, the original search process can be continued when the original work area is reselected.

# Exemplo

No exemplo a seguir, registros de clientes da Alemanha são localizados. A contagem total é então exibida.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer  && Open Customer table
SET TALK OFF
STORE 0 TO gnCount
LOCATE FOR ALLTRIM(UPPER(customer.country)) = 'GERMANY'
DO WHILE FOUND()
   gnCount = gnCount + 1
   ? company
   CONTINUE
ENDDO
? 'Total companies Germany: '+ LTRIM(STR(gnCount))
```
