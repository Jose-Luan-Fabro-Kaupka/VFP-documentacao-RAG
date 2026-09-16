# Propriedades FontBold, FontItalic, FontStrikethru, FontUnderline

Especifica se o texto tem um ou mais dos seguintes estilos: Bold, Italic, Strikethru ou Underline. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.FontBold[ = lExpr]Object.FontItalic
[ = lExpr]Object.FontStrikeThru[ = lExpr]Object.FontUnderline[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações para as propriedades de fonte são: Setting Description True (.T.) O estilo de fonte é bold, italic, strikethru ou underline. False (.F.) (Padrão, exceto para FontBold) O estilo de fonte não é bold, italic, strikethru ou underline.

# Observações

Aplica-se a: CheckBox Control | Column Object | ComboBox Control | CommandButton Control | EditBox Control | Form Object | Grid Control | Header Object | Label Control (Visual FoxPro) | ListBox Control | OptionButton Control | Page Object | _SCREEN System Variable | Spinner Control | TextBox Control (Visual FoxPro)

Em geral, altere a propriedade FontName antes de definir atributos de tamanho e estilo com as propriedades FontSize, FontBold, FontItalic, FontStrikethru e FontUnderline. No entanto, quando você define fontes TrueType para menos de 8 pontos, deve definir o tamanho do ponto com a propriedade FontSize, depois definir a propriedade FontName e então definir o tamanho novamente com a propriedade FontSize. O Windows usa uma fonte diferente para fontes TrueType menores que 8 pontos.

> **Observação:** As fontes disponíveis variam conforme a configuração do sistema, dispositivos de exibição e dispositivos de impressão. Propriedades relacionadas a fontes só podem ser definidas para valores para os quais existem fontes reais.

> **Observação:** A propriedade FontBold não se aplica ao objeto Page.
