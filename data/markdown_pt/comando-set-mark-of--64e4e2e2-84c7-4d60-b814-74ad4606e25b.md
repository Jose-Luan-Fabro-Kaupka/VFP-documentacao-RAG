# Comando SET MARK OF

Exibe ou limpa o caractere de marca para títulos de menu ou itens de menu. Existem várias versões da sintaxe.

```foxpro
SET MARK OF MENU MenuBarName TO lExpression1
SET MARK OF POPUP MenuName1 TO lExpression2
SET MARK OF BAR nMenuItemNumber OF MenuName2 TO lExpression3
```

#### Parâmetros
 **MENU MenuBarName TO lExpression1**
Especifica o nome da barra de menu para a qual exibir ou limpar o caractere de marca. O parâmetro lExpression1 especifica uma expressão lógica a ser avaliada para determinar se o caractere de marca deve ser exibido ou limpo para cada título de menu na barra de menu. Se lExpression1 for avaliada como True (.T.), o caractere de marca é exibido ao lado de cada título de menu. Se lExpression1 for avaliada como False (.F.), o caractere de marca é limpo de cada nome de menu.
**POPUP MenuName1 TO lExpression2**
Especifica o nome do menu para o qual exibir ou limpar o caractere de marca. O parâmetro lExpression2 especifica uma expressão lógica a ser avaliada para determinar se os caracteres de marca devem ser exibidos ou limpos para todos os itens de menu. Se lExpression2 for avaliada como True (.T.), os caracteres de marca são exibidos. Se lExpression2 for avaliada como False (.F.), os caracteres de marca são limpos.
**BAR nMenuItemNumber OF MenuName2 TO lExpression3**
Especifica o número do item de menu e o nome do menu que contém o item de menu para o qual exibir ou limpar o caractere de marca. O parâmetro lExpression3 especifica uma expressão lógica a ser avaliada para determinar se o caractere de marca deve ser exibido ou limpo para o item de menu. Se lExpression3 for avaliada como True (.T.), o caractere de marca é exibido. Se lExpression3 for avaliada como False (.F.), o caractere de marca é limpo.

# Observações

O caractere de marca é sempre um sinal de verificação. Você não pode especificar um caractere de marca para títulos de menu ou itens de menu.

Você não pode marcar itens de menu criados com qualquer uma das cláusulas PROMPT, como FIELD, FILES ou STRUCTURE, para o comando DEFINE POPUP.

Para determinar se um título de menu tem um caractere de marca exibido, use MRKPAD( ). Para obter mais informações, MRKBAR( ) Function. Para determinar se um item de menu tem um caractere de marca exibido, use MRKBAR( ). Para obter mais informações, consulte MRKPAD( ) Function.

Para um exemplo que usa SET MARK OF, consulte CNTBAR( ) Function.
