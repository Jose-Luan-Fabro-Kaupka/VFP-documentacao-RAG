# Função SETFLDSTATE( )

Atribui um valor de estado de modificação ou exclusão de campo a um campo ou registro em uma tabela ou cursor.

```foxpro
SETFLDSTATE(cFieldName | nFieldNumber, nFieldState [, cTableAlias
   | nWorkArea])
```

#### Parâmetros
 **cFieldName | nFieldNumber**
Especifica o nome ou o número do campo para o qual o status de modificação ou exclusão é atribuído. O número do campo nFieldNumber corresponde à posição do campo na estrutura da tabela ou cursor. DISPLAY STRUCTURE ou FIELD( ) pode ser usado para determinar o número de um campo. Para definir o status de exclusão do registro, inclua 0 como número do campo.
**nFieldState**
Especifica um valor para o status de modificação ou exclusão do campo. A tabela a seguir lista o valor de estado de modificação ou exclusão do campo e o status de modificação ou exclusão correspondente: nFieldState Status de modificação ou exclusão 1 O campo não foi modificado ou o status de exclusão não foi alterado. 2 O campo foi modificado ou o status de exclusão foi alterado. 3 O campo em um registro anexado não foi modificado ou o status de exclusão não foi alterado para o registro anexado. 4 O campo em um registro anexado foi modificado ou o status de exclusão foi alterado para o registro anexado.
**cTableAlias**
Especifica o alias da tabela ou cursor no qual o status de modificação ou exclusão é atribuído.
**nWorkArea**
Especifica a área de trabalho da tabela ou cursor no qual o status de modificação ou exclusão é atribuído. O valor de estado de modificação ou exclusão do campo é atribuído para a tabela ou cursor aberta na área de trabalho atualmente selecionada se SETFLDSTATE( ) for emitido sem os argumentos opcionais cTableAlias ou nWorkArea.

# Valor de retorno

Logical

# Observações

O Visual FoxPro usa valores de estado de campo para determinar quais campos em tabelas ou cursores são atualizados. SETFLDSTATE( ) permite controlar quais campos o Visual FoxPro tenta atualizar, independentemente de quais campos foram modificados na tabela ou cursor.

# Exemplo

O exemplo a seguir demonstra como você pode usar SETFLDSTATE( ) para alterar o status do campo. MULTILOCKS é definido como ON, um requisito para bufferização de tabela. A tabela `customer` no banco de dados `testdata` é aberta, e CURSORSETPROP( ) é então usado para definir o modo de bufferização como bufferização otimista de tabela (5).

GETFLDSTATE( ) é emitido para exibir um valor (1) correspondente ao estado não modificado do campo `cust_id` antes de ser modificado. O campo `cust_id` é modificado com REPLACE, e GETFLDSTATE( ) é emitido novamente para exibir um valor (2) correspondente ao estado modificado do campo `cust_id`.

SETFLDSTATE( ) é usado para alterar o status do campo `cust_id` de volta para 1 (não modificado). GETFLDSTATE( ) é emitido novamente e exibe 1, correspondente ao estado do campo `cust_id` atribuído por SETFLDSTATE( ). TABLEREVERT( ) é usado para retornar a tabela ao seu estado original.

```foxpro
CLOSE DATABASES
SET MULTILOCKS ON  && Must be on for table buffering
SET PATH TO (HOME(2) + 'Data\')     && Sets path to database
OPEN DATABASE testdata  && Open testdata database
USE Customer     && Open customer table
= CURSORSETPROP('Buffering', 5, 'customer')  && Enable table buffering
CLEAR
? GETFLDSTATE('cust_id')  && Displays 1, not modified
REPLACE cust_id    WITH '***'  && Changes field contents
? GETFLDSTATE('cust_id')  && Returns 2, field modified
= SETFLDSTATE('cust_id', 1)  && Change the field status
? GETFLDSTATE('cust_id')  && Displays 1, not modified
= TABLEREVERT(.T.)  && Discard all table changes
```
