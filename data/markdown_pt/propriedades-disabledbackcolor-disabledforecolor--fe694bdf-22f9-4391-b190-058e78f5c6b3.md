# Propriedades DisabledBackColor, DisabledForeColor

Especificam as cores de fundo e de primeiro plano para um controle desabilitado. Leitura/gravação em tempo de design e em tempo de execução. Há duas versões da sintaxe para cada propriedade.

```foxpro
Control.DisabledBackColor[ = nColor]
```

```foxpro
Control.DisabledBackColor = RGB(nRedValue, nGreenValue, nBlueValue)
```

```foxpro
Control.DisabledForeColor[ = nColor]
```

```foxpro
Control.DisabledForeColor = RGB(nRedValue, nGreenValue, nBlueValue)
```

# Valor de retorno
 **nColor**
Especifica um único número para representar a cor.
**nRedValue, nGreenValue, nBlueValue**
Especificam três intensidades de cor separadas que compõem a cor de primeiro plano ou de fundo do controle. Você deve usar a função RGB( ) com esses valores para consolidar os três componentes de cor em um número.

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandButton Control | EditBox Control | Label Control (Visual FoxPro) | ListBox Control | OptionButton Control | Spinner Control | TextBox Control (Visual FoxPro)

A cor que você especifica é mesclada com cinza.

> **Observação:** Na janela Properties, você pode clicar duas vezes em qualquer uma das propriedades de cor para exibir a caixa de diálogo Color. Você pode escolher ou definir cores nessa caixa de diálogo. As intensidades de vermelho, verde e azul que correspondem à cor escolhida tornam-se as configurações dessas propriedades depois que você fecha a caixa de diálogo Color.

As configurações de cor, ou Temas, do sistema operacional definem as configurações de cor padrão para as propriedades DisabledBackColor e DisabledForeColor.

Se a propriedade Themes estiver definida como True (.T.), definir o valor da propriedade DisabledBackColor produz uma sobreposição de transparência de 35% sobre o botão com tema. Isso produz um efeito de colorização.
