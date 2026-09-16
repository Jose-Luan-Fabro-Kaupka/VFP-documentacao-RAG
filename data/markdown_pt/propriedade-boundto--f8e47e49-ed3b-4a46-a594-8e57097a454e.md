# Propriedade BoundTo

Especifica se a propriedade Value de um combo box ou list box é determinada pelas propriedades List ou ListIndex. Disponível em tempo de design e em tempo de execução.

```foxpro
 [Form.]Control.BoundTo[ = lExpression]
```

# Valor de retorno
 **lExpression**
As configurações da propriedade BoundTo são: Configuração Descrição .T. A propriedade Value é determinada pela propriedade List. .F. (Padrão) A propriedade Value é determinada pelo tipo de dados da variável ou campo especificado na propriedade ControlSource. Se a variável ou campo especificado na configuração da propriedade ControlSource for do tipo caractere, a propriedade Value é determinada pela propriedade List. Se a variável ou campo especificado na configuração da propriedade ControlSource for do tipo numérico, a propriedade Value usa o número de índice da propriedade ListIndex. Esta configuração fornece compatibilidade com o Microsoft Visual FoxPro 3.0 e versões 2.x do FoxPro.

# Observações

Aplica-se a: ComboBox Control | ListBox Control

No Visual FoxPro 3.0, se a propriedade ControlSource de um combo box ou list box for numérica, o valor da propriedade ListIndex do item selecionado é armazenado na variável ou campo ao qual o controle está vinculado. Defina a propriedade BoundTo como true (.T.) para armazenar o valor da propriedade List na variável ou campo ao qual o controle está vinculado.
