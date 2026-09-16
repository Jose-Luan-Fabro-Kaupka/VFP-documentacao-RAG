# Função GETFLDSTATE( )

Retorna um valor numérico que indica se um campo em uma tabela ou cursor foi modificado ou se um registro foi acrescentado, ou se o status de exclusão do registro atual foi alterado.

```foxpro
GETFLDSTATE(cFieldName | nFieldNumber [, cTableAlias | nWorkArea])
```

#### Parâmetros
 **cFieldName | nFieldNumber**
Especifica o nome do campo ou o número do campo para o qual o status de modificação é retornado. O número do campo nFieldNumber corresponde à posição do campo na estrutura da tabela ou cursor. DISPLAY STRUCTURE ou FIELD( ) podem ser usados para determinar o número de um campo. Você pode especificar –1 para nFieldNumber para retornar uma cadeia de caracteres composta pelos valores de status de exclusão e modificação de todos os campos na tabela ou cursor. Por exemplo, se uma tabela tem cinco campos e apenas o primeiro campo foi alterado, GETFLDSTATE( ) retorna 121111. O 1 na primeira posição indica que o status de exclusão não foi alterado. Você também pode incluir 0 para nFieldNumber para determinar se o status de exclusão do registro atual foi alterado desde que a tabela ou cursor foi aberta. Observação O uso de GETFLDSTATE() determina apenas se o status de exclusão do registro atual foi alterado. Por exemplo, se você marcar um registro para exclusão e depois recuperá-lo, GETFLDSTATE() indica que o status de exclusão foi alterado, mesmo que o status de exclusão do registro tenha retornado ao estado original. Use DELETED() para determinar o status de exclusão atual de um registro.
**cTableAlias**
Especifica o alias da tabela ou cursor para o qual o status de modificação do campo ou exclusão do registro é retornado.
**nWorkArea**
Especifica a área de trabalho da tabela ou cursor para o qual o status de modificação do campo ou exclusão do registro é retornado. Se você não especificar um alias ou área de trabalho, GETFLDSTATE( ) retorna um valor para um campo na tabela ou cursor atualmente selecionada.

# Valor de retorno

Numérico, Caractere ou .NULL.

# Observações

A tabela a seguir lista os valores de retorno de caractere e o status de modificação ou exclusão correspondente.

| Valor de retorno | Status de modificação ou exclusão |
| --- | --- |
| 1 | O campo não foi modificado ou o status de exclusão não foi alterado. |
| 2 | O campo foi modificado ou o status de exclusão foi alterado. |
| 3 | O campo em um registro acrescentado não foi modificado ou o status de exclusão não foi alterado para o registro acrescentado. |
| 4 | O campo em um registro acrescentado foi modificado ou o status de exclusão foi alterado para o registro acrescentado. |
| .NULL. | Em EOF( ) |

O buffer de linha ou tabela deve primeiro ser habilitado com CURSORSETPROP( ) para que GETFLDSTATE( ) opere em tabelas locais.

O status de modificação ou exclusão é retornado para a tabela ou cursor aberta na área de trabalho atualmente selecionada se GETFLDSTATE( ) for emitido sem os argumentos opcionais cTableAlias ou nWorkArea.

Qualquer alteração em um campo fará GETFLDSTATE() retornar um valor indicando que o campo foi modificado, seja a alteração explícita ou implícita. Um exemplo de modificação explícita seria incluir o campo em um comando REPLACE ou INSERT INTO. Uma modificação implícita ocorre em um campo que tem um valor padrão quando qualquer comando que adiciona um novo registro é emitido.

# Exemplo 1

O exemplo a seguir demonstra como você pode usar GETFLDSTATE( ) para determinar se o conteúdo de um campo foi alterado. MULTILOCKS é definido como ON, um requisito para buffer de tabela. A tabela `customer` no banco de dados `testdata` é aberta, e CURSORSETPROP( ) é usado para definir o modo de buffer como buffer de tabela otimista (5).

GETFLDSTATE( ) é emitido para exibir um valor (1) correspondente ao estado não modificado do campo `cust_id` antes de ser modificado. O campo `cust_id` é modificado com REPLACE, e GETFLDSTATE( ) é emitido novamente para exibir um valor (2) correspondente ao estado modificado do campo `cust_id`. TABLEREVERT( ) é usado para retornar a tabela ao estado original, e GETFLDSTATE( ) é emitido novamente para exibir um valor (1) correspondente ao estado original do campo `cust_id`.

```foxpro
CLOSE DATABASES
CLEAR
SET MULTILOCKS ON         && Allow table buffering
OPEN DATABASE (HOME(2) + 'data\testdata')
USE Customer             && Open customer table
=CURSORSETPROP("Buffering",5,"customer")  && Enable table buffering
* Get field state on original cust_id field and display state
nState=GETFLDSTATE("cust_id")
DO DisplayState WITH nState, "Original"
* Change field contents and display state
REPLACE cust_id    WITH "***"
nState=GETFLDSTATE("cust_id")
DO DisplayState WITH nState, "After Replace"
* Discard table changes and display state
= TABLEREVERT(.T.)        && Discard all table changes
nState=GETFLDSTATE("cust_id")
DO DisplayState WITH nState, "After Revert"
PROCEDURE DisplayState
PARAMETER nState,cOperation
DO CASE
   CASE nState=1
      =MESSAGEBOX("Field has not been modified",0,cOperation)
   OTHERWISE
      =MESSAGEBOX("Field has been modified",0,cOperation)
ENDCASE
```

# Exemplo 2

O exemplo a seguir mostra a diferença de comportamento entre campos com e sem valores padrão.

```foxpro
SET MULTILOCKS ON
CREATE DATABASE example
CREATE TABLE customer (cust_id C(6),state C(2) DEFAULT "FL")
CLOSE TABLES
USE customer
=CURSORSETPROP("Buffering",5,"customer")
APPEND BLANK
?GETFLDSTATE("cust_id")     && Returns 3, field in an appended record has
                            && not been modified.
?GETFLDSTATE("state")    && Returns 4, field in an appended record has
                         && been modified.
```
