# Comando BLANK

Limpa dados dos campos especificados no registro atual ou de todos os campos no registro atual quando emitido sem argumentos adicionais.

```foxpro
BLANK [FIELDS FieldList] [DEFAULT [AUTOINC]] [Scope] [FOR lExpression1]
   [WHILE lExpression2] [NOOPTIMIZE] [IN nWorkArea | cTableAlias]
```

#### Parâmetros
 **[FIELDS FieldList ]**
Limpa apenas os campos que você especifica com FieldList. Se você omitir a cláusula FIELDS, todos os campos em um registro são limpos por padrão. Qualquer campo que você especificar em uma área de trabalho não selecionada deve ser precedido pelo alias da área de trabalho. Observação BLANK não limpa dados de campo de um registro em outra área de trabalho relacionada se o ponteiro de registro estiver no final do arquivo na área de trabalho atual. O ponteiro de registro deve estar em um registro na área de trabalho atual para que BLANK atue nos campos no registro relacionado.
**[DEFAULT [AUTOINC]]**
Inicializa os campos especificados com seus valores padrão conforme especificado com a cláusula DEFAULT para tabelas que pertencem a um banco de dados e cursors. Se nenhum campo for especificado, os valores padrão de todos os campos no registro atual são inicializados. DEFAULT não se aplica a tabelas livres. A palavra-chave AUTOINC especifica incluir todos os campos de incremento automático. Se você omitir AUTOINC, os campos de incremento automático permanecem intactos com seus valores originais. Observação Realizar atualizações em campos de incremento automático requer bloquear o cabeçalho da tabela. Se você chamar o comando BLANK com a cláusula DEFAULT AUTOINC com o arquivo de tabela aberto em modo compartilhado, estiver desbloqueado e o comando SET MULTILOCKS estiver definido como OFF, o Visual FoxPro gera um erro.
**Scope**
Especifica um intervalo de registros a limpar. O escopo padrão para BLANK é o registro atual (NEXT 1). Apenas os registros que estão dentro do intervalo são limpos. As cláusulas de escopo são: ALL, NEXT nRecords, RECORD nRecordNumber e REST. Comandos que incluem o parâmetro Scope operam apenas na tabela na área de trabalho ativa. Para obter mais informações sobre cláusulas de escopo, consulte Scope Clauses.
**FOR lExpression1**
Limpa dados de campo em registros para os quais lExpression1 avalia como True (.T.). Rushmore Query Optimization otimiza BLANK FOR se lExpression1 for uma expressão otimizável. Uma discussão sobre Rushmore Query Optimization aparece em Using Rushmore Query Optimization to Speed Data Access.
**WHILE lExpression2**
Especifica uma condição pela qual dados de campo em registros são limpos enquanto a expressão lógica lExpression2 avalia como True (.T.).
**NOOPTIMIZE**
Impede a otimização Rushmore de BLANK. Para obter mais informações, consulte SET OPTIMIZE Command e Using Rushmore Query Optimization to Speed Data Access.
**IN nWorkArea | cTableAlias**
Especifica a área de trabalho ou o alias de tabela afetado pelo comando BLANK. Use esta cláusula para especificar uma área de trabalho ou uma tabela fora da área de trabalho atual.

# Observações

Para determinar se um campo em um registro está em branco, use ISBLANK( ).

Para adicionar um novo registro em branco ao final de uma tabela, use APPEND BLANK.

# Exemplo

O exemplo a seguir abre a tabela `customer` no banco de dados `testdata`. O conteúdo do primeiro registro é exibido. SCATTER é usado para salvar o conteúdo do registro em um array. O registro é limpo com BLANK e o conteúdo do registro é exibido novamente. GATHER é usado para restaurar o conteúdo original do registro e o conteúdo restaurado do registro é exibido novamente.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'data\testdata')
USE customer  && Open customer table
CLEAR
DISPLAY  && Displays the current record
SCATTER TO gaCustomer  && Create array with record contents
BLANK  && Clear the record
DISPLAY  && Displays the blank record
GATHER FROM gaCustomer  && Restore original record contents
DISPLAY  && Display the restored record
```
