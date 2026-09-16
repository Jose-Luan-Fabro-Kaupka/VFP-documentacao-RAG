# Controle CheckBox

Cria uma caixa de seleção.

```foxpro
CheckBox
```

# Observações

Você pode usar uma caixa de seleção para alternar entre três estados, True (.T.), False (.F.) e Null (.NULL.). A propriedade Value do CheckBox determina o estado atual da caixa de seleção.

A tabela a seguir ilustra os três estados possíveis que uma caixa de seleção pode ter.

| Exibição | Propriedade Value | Descrição |
| --- | --- | --- |
| 0 ou .F. (Padrão) | Não selecionada. | |
| 1 ou .T. | Selecionada. | |
| 2 ou .NULL. | Selecionada, mas esmaecida. Este estado permite que o usuário da aplicação se recuse a selecionar a caixa de seleção. No entanto, o usuário da aplicação pode limpar e depois selecionar a caixa de seleção. Dica Após interagir com a caixa de seleção, o usuário pode retornar a caixa de seleção ao estado nulo original pressionando CTRL+0. | |

A propriedade Value do CheckBox reflete o tipo de dados da última atribuição. Por exemplo, se você definir a propriedade como True (.T.) ou False (.F.), o tipo é Logical até que você defina a propriedade como um valor Numeric.

Se você definir a propriedade ControlSource do controle CheckBox para um campo lógico em uma tabela, a caixa de seleção é exibida da seguinte forma:
 - Como selecionada quando o valor no registro atual é True (.T.).
- Como não selecionada quando o valor no registro atual é False (.F.).
- Como selecionada, mas esmaecida, se o valor no registro atual é null (.NULL.). Observação Se a propriedade ControlSource é um campo em uma tabela que não aceita valor nulo, pressionar CTRL+0 gera um erro.

Para especificar o texto que aparece ao lado de uma caixa de seleção, use a propriedade Caption. Para especificar uma imagem para uma caixa de seleção, use a propriedade Picture.

Para informações adicionais sobre controles CheckBox, consulte Como: usar caixas de seleção para especificar estados.
