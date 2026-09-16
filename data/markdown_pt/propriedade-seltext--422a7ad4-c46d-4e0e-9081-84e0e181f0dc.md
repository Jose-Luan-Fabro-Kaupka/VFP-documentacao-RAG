# Propriedade SelText

Retorna o texto que o usuário selecionou em uma área de entrada de texto de um controle ou retorna uma cadeia vazia ("") se nenhum caractere estiver selecionado. Especifica a cadeia de caracteres que contém o texto selecionado. Não disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
 [Form.]Control.SelText[= cString]
```

# Valor de retorno
 **cString**
Especifica a cadeia de caracteres que contém o texto selecionado ou consiste em uma cadeia vazia se nenhum caractere estiver selecionado. O texto selecionado aparece sombreado.

# Observações

Aplica-se a: ComboBox Control | EditBox Control | Spinner Control | TextBox Control (Visual FoxPro)

Use esta propriedade com as propriedades SelLength e SelStart para tarefas como:
 - Definir o ponto de inserção em uma cadeia de caracteres.
- Estabelecer um intervalo de inserção que limite onde o ponto de inserção pode ir.
- Selecionar um grupo específico de caracteres (subcadeias) em um controle.
- Limpar texto.

Ao trabalhar com essas propriedades, observe os seguintes comportamentos:
 - Definir SelLength como menor que 0 causa um erro em tempo de execução.
- Definir SelStart como maior que o comprimento do texto define a propriedade para o comprimento de texto existente. Alterar SelStart altera a seleção para um ponto de inserção e define SelLength como 0.
- Definir SelText como um novo valor define SelLength como 0 e substitui o texto selecionado pela nova cadeia de caracteres.
