# Propriedade InputMask

Especifica como os usuários inserem dados e como exibi-los em um controle. Disponível em tempo de design e execução.

```foxpro
Control.InputMask[ = cMask]
```

# Valor de retorno
 **cMask**
Especifica configurações para determinar como inserir e exibir dados. Valores possíveis: ! converte letras minúsculas em maiúsculas. # permite dígitos, espaços e sinais, como menos (–). $ exibe o símbolo monetário atual, definido por SET CURRENCY, em posição fixa. $$ exibe um símbolo monetário flutuante junto aos dígitos de um controle spinner ou caixa de texto. , exibe o separador de grupos de dígitos atual definido nas opções regionais do Windows. . exibe o caractere decimal atual definido por SET POINT (o padrão é ponto). 9 permite dígitos e sinais. A permite apenas caracteres alfabéticos. H impede símbolos não hexadecimais na posição. L permite apenas dados lógicos. N permite apenas letras e dígitos. U permite apenas letras e as converte em maiúsculas (A-Z). W permite apenas letras e as converte em minúsculas (a-z). X permite qualquer caractere. Y permite Y, y, N e n para os valores lógicos True (.T.) e False (.F.), respectivamente.

# Observações

Aplica-se a: objeto Column | controle ComboBox | controle Spinner | controle TextBox (Visual FoxPro)

InputMask difere de Format por especificar o comportamento de todo o campo de entrada. Você pode combinar vários códigos Format; no entanto, eles afetam todos os dados no campo de entrada.
