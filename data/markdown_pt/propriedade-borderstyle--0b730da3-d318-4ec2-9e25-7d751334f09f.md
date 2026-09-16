# Propriedade BorderStyle

Especifica o estilo da borda de um objeto. Disponível em tempo de design e de execução.

```foxpro
Object.BorderStyle[ = nStyle]
```

# Valor de retorno
**nStyle**
Para um controle CommandGroup, ComboBox, EditBox, Image, Label, OptionGroup, Spinner ou TextBox, as configurações da propriedade BorderStyle são: Configuração Descrição 0 Nenhuma. Padrão para os controles Image e Label. 1 Fixa simples. Padrão para os controles CommandGroup, EditBox, OptionGroup e TextBox. Para uma linha ou forma, as configurações da propriedade BorderStyle são: Configuração Descrição 0 Transparente 1 (Padrão) Sólida. A borda externa é a borda externa do controle Shape. 2 Tracejada 3 Pontilhada 4 Traço-ponto 5 Traço-ponto-ponto 6 Sólida interna Para um objeto Form, as configurações da propriedade BorderStyle são: Configuração Descrição 0 Sem borda 1 Fixa simples 2 Caixa de diálogo fixa 3 (Padrão) Redimensionável

# Observações

Aplica-se a: controle ComboBox | controle CommandGroup | controle EditBox | objeto Form | controle Image (Visual FoxPro) | controle Label (Visual FoxPro) | controle Line | controle OptionGroup | variável de sistema _SCREEN | controle Shape | controle TextBox (Visual FoxPro) | controle Spinner

Se a configuração da propriedade BorderWidth for maior que 1, uma borda sólida será desenhada independentemente da configuração de BorderStyle. Se BorderWidth for definida como 1, BorderStyle produzirá os efeitos descritos nas tabelas acima.
