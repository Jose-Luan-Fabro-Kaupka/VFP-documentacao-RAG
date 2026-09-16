# Amostra Desabilitar ou exibir marca de seleção em item de menu

Arquivo: ...\Samples\Solution\Menus\Chkmenu.scx

Esta amostra ilustra a desabilitação dinâmica de itens de menu e a exibição de marcas de seleção ao lado de itens de menu específicos.

O menu nesta amostra foi criado no Menu Designer e é executado quando o formulário é inicializado.

```foxpro
DO chkmenu.mpr
```

Para desabilitar um item de menu, inclua uma expressão que avalie como false (.F.) no comando SET SKIP OF. Por exemplo, a linha de código a seguir no evento InteractiveChange de uma caixa de seleção emite SET SKIP OF com o inverso do valor da caixa de seleção, desabilitando o item de menu quando a caixa de seleção não está marcada.

```foxpro
SET SKIP OF BAR 1 OF checkitems !THIS.Value
```

Para exibir uma marca de seleção ao lado de um item de menu, inclua uma expressão que avalie como true (.T.) após a palavra-chave TO do comando SET MARK OF. Por exemplo, a linha de código a seguir no evento InteractiveChange de uma caixa de seleção emite o comando SET MARK OF com a configuração da propriedade Value da caixa de seleção.

```foxpro
SET MARK OF BAR 1 OF checkitems TO THIS.Value
```
