# Evento BeforeUpdate

Ocorre imediatamente antes da execução de um comando de atualização para um registro.

> **Observação:** Se a atualização em lote for usada, isto é, se a propriedade CursorAdapter BatchUpdateCount for maior que 1, BeforeUpdate não ocorrerá.

```foxpro
PROCEDURE Object.BeforeUpdate
LPARAMETERS cFldState, lForce, nUpdateType, cUpdateInsertCmd, cDeleteCmd
```

#### Parâmetros
 **cFldState**
Especifica os estados dos campos da linha que está sendo processada. Esse é o mesmo valor obtido ao chamar a seguinte função: GETFLDSTATE(-1). Por exemplo, esse valor pode ser uma cadeia de caracteres composta por valores de status de exclusão e edição de todos os campos da tabela ou do cursor. Se uma tabela tiver cinco campos e somente o primeiro campo tiver sido editado, GETFLDSTATE( ) retornará o valor 121111. O número 1 na primeira posição indica que o status de exclusão não foi alterado.
**lForce**
Especifica o valor do parâmetro lForce da função TABLEUPDATE( ).
**nUpdateType**
Especifica um valor numérico na propriedade UpdateType do objeto CursorAdapter gerado. A tabela a seguir lista os valores possíveis para nUpdateType. nUpdateType Descrição 1 Atualiza os dados antigos com os novos. (Padrão) 2 Atualiza os dados excluindo os antigos e inserindo os novos. Alterar esse valor muda o comportamento do registro atual, mas não altera o valor da propriedade. Esse valor é necessário somente se você estiver usando atualização automática.
**cUpdateInsertCmd**
Especifica o valor da propriedade UpdateCmd ou InsertCmd, conforme apropriado. O Visual FoxPro usa o valor desse parâmetro como comando de atualização ou inserção, que pode ser alterado neste evento. Entretanto, se você alterar o parâmetro cUpdateInsertCmd, as propriedades UpdateCmd e InsertCmd não serão alteradas.
**cDeleteCmd**
Especifica que cDeleteCmd estará vazio se o parâmetro nUpdateType estiver definido como 1. Caso contrário, defina cDeleteCmd como o valor da propriedade DeleteCmd. O Visual FoxPro usa o valor de cDeleteCmd como comando de exclusão, que pode ser alterado neste evento. Entretanto, se você alterar o parâmetro cDeleteCmd, o valor da propriedade DeleteCmd não será alterado.

# Observações

Aplica-se a: classe CursorAdapter

Se o código em BeforeUpdate retornar False (.F.), a operação de atualização não ocorrerá.
