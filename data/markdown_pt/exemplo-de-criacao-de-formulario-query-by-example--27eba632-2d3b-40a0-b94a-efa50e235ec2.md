# Exemplo de criação de formulário Query-By-Example

Arquivo: ...\Samples\Solution\Forms\Qbf.scx

Este exemplo permite pesquisar e filtrar registros na mesma interface em que eles são exibidos.

Quando o usuário escolhe Enter QBF, o código associado ao evento Click de cmdQBFMode inicia uma transação e acrescenta um registro em branco à tabela para armazenar o texto da consulta.

```foxpro
* extract from cmdQBFMode.Click
BEGIN TRANSACTION
APPEND BLANK
THISFORM.Refresh
```

Quando o usuário escolhe Query, o código associado ao evento Click de cmdExecuteQBF desfaz a transação, descartando o novo registro.

Você pode usar transações somente com tabelas contidas em um banco de dados. Para incluir recursos QBF em uma tabela que não esteja em um banco de dados, percorra todos os controles do formulário, salve a configuração antiga de ControlSource e defina ControlSource como uma cadeia vazia. Depois de obter a cadeia de consulta, percorra novamente os controles e restaure as propriedades ControlSource.

O código associado ao evento Click de cmdExecuteQBF também percorre os controles, verifica os valores inseridos pelo usuário e chama o método ParseCondition para montar a cadeia de filtro.

O usuário pode inserir um único valor para correspondência ou uma expressão. Por exemplo, pode inserir um dos valores abaixo na caixa de texto Title:

```foxpro
Sales Manager
!= "Sales Manager"
```

Se o usuário não inserir uma expressão, as aspas não serão necessárias.

# Método ParseCondition

```foxpro
LPARAMETERS cCondition, cControlSource
LOCAL lcRetCondition, lcFieldName
IF TYPE('cCondition') = 'C'
   cCondition = ALLTRIM(cCondition)
ENDIF
lcFieldName = SUBSTRC(cControlSource,(RATC(".",cControlSource)+1))
IF !EMPTY(cCondition) THEN
   IF TYPE('cCondition')$ "CM"
      IF ("<"       $ cCondition OR ;
         "=="    $ cCondition OR ;
         "LIKE"    $ cCondition OR ;
         "<>"    $ cCondition OR ;
         "!="    $ cCondition OR ;
         "#"    $ cCondition OR ;
         "="    $ cCondition OR ;
         ">"    $ cCondition)
           lcRetCondition = lcFieldName + cCondition
      ENDIF
   ENDIF
   IF EMPTY(lcRetCondition)
      DO CASE
         * put quotes around character expressions
         CASE TYPE(cControlSource) $ "CM"
            lcRetCondition = lcFieldName + " = " + CHR(34) + cCondition + CHR(34)
         * put braces around date expressions
         CASE TYPE(cControlSource) $ "DT"
            lcRetCondition = lcFieldName + " = {" + DTOC(cCondition) + "}"
         OTHERWISE
            lcRetCondition = lcFieldName + " = " + STR(cCondition)
      ENDCASE
   ENDIF
ELSE
   lcRetCondition = ""
ENDIF
RETURN lcRetCondition
```
