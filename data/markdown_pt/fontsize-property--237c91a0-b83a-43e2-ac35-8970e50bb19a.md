# FontSize Property

Especifica o tamanho da fonte do texto exibido com um objeto. Disponível no tempo de projeto e tempo de execução.

```foxpro
Object.FontSize[ = nSize]
```

# Valor de Retorno
**nSize**
Especifica o tamanho da fonte em pontos. O tamanho padrão da fonte é de 9 pontos.

Observações

Applies To: CheckBox Control | Column Object | ComboBox Control | CommandButton Control | EditBox Control | Form Object | Grid Control | Header Object | Label Control (Visual FoxPro) | ListBox Control | OptionButton Control | Page Object | _SCREEN System Variable | Spinner Control | TextBox Control (Visual FoxPro)

O valor máximo para nSize é 127 pontos. Há 72 pontos em 1 polegada.

Em geral, você deve alterar a propriedade FontName antes de definir atributos de tamanho e estilo com as propriedades FontSize, FontBold, FontItalic, FontStrikethru e FontUnderline. No entanto, quando você definir fontes TrueType para menor que 8 pontos, você deve definir o tamanho do ponto com a propriedade FontSize, próximo definir a propriedade FontName, e então definir o tamanho novamente com a propriedade FontSize. O ambiente Windows usa uma fonte diferente para fontes TrueType que são menores que 8 pontos.

> **Nota:** As fontes disponíveis variam de acordo com a configuração do sistema e os dispositivos de impressão. Propriedades relacionadas à fonte podem ser definidas apenas para valores para os quais existem fontes.

Veja também
- Propriedades FontBold, FontItalic, FontStrikethru, FontUnderline
- Properties (Visual FoxPro)
- Language Reference (Visual FoxPro)
