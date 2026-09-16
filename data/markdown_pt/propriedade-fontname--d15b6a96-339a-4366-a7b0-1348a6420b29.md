# Propriedade FontName

Especifica o nome da fonte usada para exibir texto. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.FontName[ = cName]
```

# Valor de retorno
 **cName**
Especifica o nome da fonte. O padrão é Arial.

# Observações

Aplica-se a: CheckBox Control | Column Object | ComboBox Control | CommandButton Control | EditBox Control | Form Object | Grid Control | Header Object | Label Control (Visual FoxPro) | ListBox Control | OptionButton Control | Page Object | _SCREEN System Variable | Spinner Control | TextBox Control (Visual FoxPro)

A configuração padrão da propriedade FontSize é 9 pontos. As fontes disponíveis variam de acordo com a configuração do seu sistema. Propriedades relacionadas a fonte só podem ser definidas para valores para os quais fontes existem. Em tempo de design, uma lista de fontes disponíveis é exibida quando você seleciona a propriedade FontName na janela Properties e clica na seta para baixo à direita da caixa Property Settings.

Em geral, altere FontName antes de definir atributos de tamanho e estilo com as propriedades FontSize, FontBold, FontItalic, FontStrikethru e FontUnderline.
