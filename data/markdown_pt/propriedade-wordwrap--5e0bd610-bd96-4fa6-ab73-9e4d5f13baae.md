# Propriedade WordWrap

Especifica se o texto é exibido em uma única linha ou em várias linhas dentro de um controle ou objeto. Disponível em tempo de design e em tempo de execução. Há duas versões da sintaxe.

```foxpro
[Form.]Control.WordWrap [= lExpr]
Grid.Column.Header.WordWrap [= lExpr]
```

# Valor de retorno
 **lExpr**
Especifica um valor lógico que indica se o texto é exibido em várias linhas no controle ou objeto. A tabela a seguir lista os valores de lExpr para controles CheckBox , CommandButton , Label e OptionButton. lExpr Description False (.F.) O texto é exibido em uma única linha e aparece truncado se o texto não se ajustar ao controle. (Padrão) True (.T.) O texto é exibido em várias linhas para se ajustar ao controle. Observação Quando a propriedade WordWrap é True (.T.) para check boxes e option buttons, a propriedade PicturePosition determina a posição das imagens nos controles. Para obter mais informações, consulte PicturePosition Property . A tabela a seguir lista os valores de lExpr para objetos Header em colunas de grade. lExpr Description False (.F.) O texto é exibido em uma única linha e aparece truncado se o texto não se ajustar ao cabeçalho. (Padrão) True (.T.) O texto é exibido em várias linhas e se ajusta ao limite da coluna. No entanto, o texto aparece truncado se você não ajustar a altura do cabeçalho para se ajustar ao texto. Dica Para alterar a altura do cabeçalho, altere a propriedade Grid HeaderHeight. Para obter mais informações, consulte HeaderHeight Property .

# Observações

Aplica-se a: CheckBox Control | CommandButton Control | Header Object | Label Control (Visual FoxPro) | OptionButton Control

Para controles CheckBox, CommandButton, Label e OptionButton, WordWrap especifica se o texto especificado pela propriedade Caption do controle é exibido em uma única linha ou em várias linhas para se ajustar ao controle. Para check boxes, command buttons e option buttons, o texto sempre aparece centralizado verticalmente no controle. Para labels, o texto aparece na parte superior.

> **Dica:** A propriedade AutoSize do controle determina se o controle é redimensionado automaticamente para se ajustar ao seu conteúdo. Para redimensionar o controle automaticamente, defina a propriedade AutoSize do controle como True (.T.). Caso contrário, pode ser necessário ajustar a altura do controle para acomodar várias linhas de texto.

Para check boxes, option buttons e cabeçalhos, a propriedade Alignment determina o alinhamento do texto. Para obter mais informações, consulte Alignment Property.

Para objetos Header de coluna em grades, WordWrap especifica se o texto especificado pela propriedade Caption do cabeçalho se ajusta ao limite da coluna.

> **Observação:** A propriedade WordWrap respeita apenas os caracteres CHR(10) (retorno de carro) e CHR(13)+CHR(10) (alimentação de linha e retorno de carro) para quebra manual de texto.
