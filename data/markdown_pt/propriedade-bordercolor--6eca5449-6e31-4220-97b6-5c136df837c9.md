# Propriedade BorderColor

Especifica a cor da borda de um objeto. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.BorderColor[ = nColor]
```

# Valor de retorno
 **nColor**
Especifica o valor da cor da borda. A tabela a seguir lista valores de cor típicos: Cor Valores RGB Valor nColor Branco 255, 255, 255 16777215 Preto 0, 0, 0 0 Cinza 192, 192, 192 12632256 Cinza escuro 128, 128, 128 8421504 Vermelho 255, 0, 0 255 Vermelho escuro 128, 0, 0 128 Amarelo 255, 255, 0 65535 Amarelo escuro 128, 128, 0 32896 Verde 0, 255, 0 65280 Verde escuro 0, 128, 0 32768 Ciano 0, 255, 255 16776960 Ciano escuro 0, 128, 128 8421376 Azul 0, 0, 255 16711680 Azul escuro 0, 0, 128 8388608 Magenta 255, 0 ,255 16711935 Magenta escuro 128, 0, 128 8388736

# Observações

Aplica-se a: Controle ComboBox | Controle CommandGroup | Objeto Container | Objeto Control (Visual FoxPro) | Controle EditBox | Controle Image (Visual FoxPro) | Controle Line | Controle ListBox | Controle OptionGroup | Controle PageFrame | Controle Shape | Controle TextBox (Visual FoxPro)

BorderColor se aplica apenas a uma caixa de texto ou caixa de edição quando a propriedade SpecialEffect está definida como 1 - Plain.

Use a função RGB( ) para converter as três cores componentes em um nColor composto.
