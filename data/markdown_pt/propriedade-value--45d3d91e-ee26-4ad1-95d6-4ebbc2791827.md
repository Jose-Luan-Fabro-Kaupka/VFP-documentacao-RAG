# Propriedade Value

Especifica o estado atual de um controle. Disponível em tempo de design e em tempo de execução.

```foxpro
[Form.]Control.Value [= nSetting]
```

# Valor de retorno
 **nSetting**
Especifica uma configuração que indica o estado atual do controle. Para controles CommandGroup , ComboBox , EditBox , ListBox , OptionGroup e Spinner, a propriedade Value contém a cadeia de caracteres ou o valor numérico atualmente selecionado no controle. Para um controle TextBox, a propriedade Value contém a cadeia de caracteres ou o valor numérico, de data, datetime, currency ou lógico atualmente selecionado no controle. O valor padrão é uma cadeia de caracteres. Para um controle CheckBox, a tabela a seguir lista as configurações de nSetting : nSetting Descrição 0 Desmarcado. (Padrão) 1 Selecionado. 2 Valor misto. Esta configuração está disponível somente no código. Para um controle OptionButton, a tabela a seguir lista as configurações de nSetting : nSetting Descrição 0 Não selecionado. (Padrão) 1 Selecionado.

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandGroup Control | EditBox Control | Grid Control | ListBox Control | OptionButton Control | OptionGroup Control | Spinner Control | TextBox Control (Visual FoxPro)

Para o controle Grid, a propriedade Value está disponível somente quando o controle Grid tem o foco.

O método Value não suporta o método Assign.

Você pode usar a propriedade Value de um controle CommandGroup ou OptionGroup para determinar qual botão no grupo aciona um evento. A propriedade Value é definida como um inteiro que indica qual botão no grupo causou o evento.

A propriedade Value altera o comportamento quando uma fonte de controle é definida para um controle. Quando uma fonte de controle é definida, a configuração da propriedade Value de um controle é o tipo de dados da variável ou campo referenciado pela propriedade ControlSource. Se o tipo de dados não for válido para o controle fornecido, o Visual FoxPro gera um erro.

A tabela a seguir lista os tipos de dados válidos.

| Controle | Tipos de dados permitidos |
| --- | --- |
| CheckBox | Integer, Logical, Numeric |
| ComboBox | Character, Integer, Numeric |
| CommandGroup | Character, Integer, Numeric |
| EditBox | Character, Memo |
| Grid | Character, Numeric |
| ListBox | Character, Integer, Numeric |
| OptionButton | Integer, Logical, Numeric |
| OptionGroup | Character, Integer, Numeric |
| Spinner | Currency, Integer, Numeric |
| TextBox | Qualquer tipo de dados |
