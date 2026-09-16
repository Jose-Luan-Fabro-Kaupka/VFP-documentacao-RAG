# Propriedade AllowCellSelection

Especifica se é possível selecionar células individuais em uma grade, por exemplo, você pode usar a propriedade AllowCellSelection para simular uma caixa de lista. Disponível em tempo de design e em tempo de execução.

```foxpro
Grid.AllowCellSelection [= lExpr]
```

# Valor de retorno
 **lExpr**
Especifica se você pode selecionar o conteúdo de uma célula da grade ou apenas a linha inteira. A tabela a seguir lista os valores para lExpr. lExpr Description True (.T.) Especifica que é possível selecionar conteúdo em uma célula da grade (campo). (Padrão) False (.F.) Especifica que é necessário selecionar a linha inteira.

# Observações

Aplica-se a: Grid Control

Selecionar células individuais ou a linha inteira não altera a cor da linha ou célula selecionada.

Quando AllowCellSelection é definida como False (.F.), o seguinte comportamento adicional ocorre:
 - A grade ignora as propriedades SelectedItemForeColor e SelectedItemBackColor. A linha assume uma cor uniforme baseada nas propriedades HighlightBackColor e HighlightForeColor e outras propriedades relacionadas a cores no nível da coluna. Observação Se você não especificar cores para as propriedades de destaque, um contorno retangular aparece ao redor de uma linha selecionada.
- Se a propriedade HighlightStyle estiver definida com um valor maior que 0, o HighlightBackColor padrão é um gradiente 50 por cento mais claro.
- A grade sempre mostra o cursor especificado com a propriedade MousePointer e não exibe um ponteiro de inserção de texto quando dentro de uma célula. Clicar em uma célula seleciona a linha inteira, em vez de definir o foco na célula individual.
- A tabulação entre células é desabilitada, e o comportamento da grade age de forma semelhante a uma grade com uma única coluna.
- Você não pode selecionar uma linha na grade para exclusão clicando na coluna de exclusão, pois essa funcionalidade está desabilitada.
- Colunas ocultas são ignoradas. Você pode visualizar colunas que foram roladas para a esquerda ou direita fora da grade visível usando as teclas LEFT ARROW e RIGHT ARROW ou o mouse e a barra de rolagem horizontal.
- A propriedade ActiveColumn é avaliada como 0; use a propriedade RelativeColumn para obter a coluna correta na grade.
- O método ActivateCell apenas seleciona a linha inteira.
- Todos os eventos são tratados no nível da grade em vez do nível do controle. Por exemplo, clicar duas vezes em uma célula é tratado pelo evento Grid.DblClick. No entanto, eventos e atributos de cabeçalho ainda são suportados. Por exemplo, você pode clicar em um cabeçalho para reordenar o conteúdo da coluna baseado no campo.
- O suporte para Find está desabilitado, assim como comandos do menu Edit, porque definir AllowCellSelection torna a grade somente leitura. No entanto, a propriedade AllowCellSelection não afeta a coluna de marca de exclusão em uma grade.
- Os eventos AfterRowColChange e BeforeRowColChange funcionam apenas para mudança de linha. A propriedade RowColChange sempre retorna um valor de 1 (Row Change).

A propriedade AllowCellSelection suporta todos os controles padrão do Visual FoxPro; no entanto, controles ActiveX incorporados em uma coluna não são suportados.

Se a propriedade AllowCellSelection de uma grade estiver definida como True (.T.), o Visual FoxPro ignora o evento Grid.KeyPress e usa o evento no nível da célula individual.
