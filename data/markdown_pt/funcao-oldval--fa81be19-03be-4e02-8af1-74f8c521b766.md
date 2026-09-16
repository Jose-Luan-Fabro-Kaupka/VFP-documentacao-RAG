# Função OLDVAL( )

Retorna valores originais de campo para campos que foram modificados, mas não atualizados.

```foxpro
OLDVAL(cExpression [, cTableAlias | nWorkArea])
```

#### Parâmetros
 **cExpression**
Especifica uma expressão cujo valor original OLDVAL( ) retorna de uma tabela ou fonte de dados remota. cExpression é tipicamente um campo ou uma expressão consistindo em um conjunto de campos da tabela ou fonte de dados remota.
**cTableAlias**
Especifica o alias da tabela ou cursor do qual os valores originais de campo são retornados.
**nWorkArea**
Especifica a área de trabalho da tabela ou cursor do qual os valores originais de campo são retornados.

# Valor de retorno

Character, Currency, Date, DateTime, Double, Float, Integer, Logical, Numeric ou Memo

# Observações

OLDVAL( ) retorna valores originais de campo para registros em uma tabela ou cursor do Visual FoxPro que tem buffer de linha ou tabela habilitado com CURSORSETPROP( ).

Se uma tabela em um banco de dados ou um cursor tiver regras de validação, OLDVAL( ) não requer que buffer de linha ou tabela esteja habilitado para retornar valores originais de campo.

Se o ponteiro de registro for movido para um registro diferente quando o buffer de linha estiver habilitado, ou se TABLEUPDATE( ) for emitido para confirmar alterações no registro, ou houver alguma outra ação que cause uma atualização, como encerrar uma transação, os campos são atualizados e os valores originais de campo não estarão mais disponíveis.

O tipo de dados do valor que OLDVAL( ) retorna é determinado pela expressão que você especifica com cExpression.

> **Observação:** OLDVAL( ) pode retornar .NULL., mesmo para um campo declarado como NOT NULL e com SET NULL OFF.

Os valores originais de campo são retornados para a tabela ou cursor aberto na área de trabalho selecionada atualmente se OLDVAL( ) for emitido sem os argumentos opcionais cTableAlias ou nWorkArea.

# Exemplo

O exemplo a seguir demonstra como você pode usar OLDVAL( ) para retornar o valor original de campo de um campo em uma tabela com buffer. Uma tabela chamada `employees` é criada e INSERT – SQL é usado para inserir o valor "Smith" no campo `cLastName`.

MULTILOCKS é definido como ON, um requisito para buffer de tabela. CURSORSETPROP( ) é usado para definir o modo de buffer como buffer de tabela otimista (5).

O valor original do campo `cLastName` (Smith) é exibido e, em seguida, o campo `cLastName` é modificado com REPLACE. O novo valor do campo `cLastName` (Jones) é exibido. O valor original do campo `cLastName` (Smith) é exibido com OLDVAL( ). TABLEUPDATE( ) é então usado para confirmar alterações na tabela. O valor atualizado do campo `cLastName` (Jones) é então exibido.

```foxpro
CLOSE DATABASES
CLEAR
* Create new table and add blank record
CREATE TABLE employee (cLastName C(10))
APPEND BLANK
* Insert initial value
INSERT INTO employee (cLastName) VALUES ("Smith")
* Enable and set table buffering
SET MULTILOCKS ON  && Allow table buffering
=CURSORSETPROP("Buffering", 5, "employee" )  && Enable table buffering
* Display initial value
=MESSAGEBOX("Original cLastName value: "+ cLastName, 0, "Results")
* Change record value and display results
REPLACE cLastName WITH "Jones"
=MESSAGEBOX("Modified cLastName value: "+ cLastName, 0, "Results")
* Store the old value of the field to cTemp variable and display results
cTemp=OLDVAL("cLastName", "employee")
=MESSAGEBOX("Original cLastName value: "+ cTemp, 0, "Results")
* Update table and display final value
=TABLEUPDATE(.T.)
=MESSAGEBOX("Final cLastName value: "+ cLastName, 0, "Results")
* Close and delete example table file
USE
DELETE FILE employee.dbf
```
