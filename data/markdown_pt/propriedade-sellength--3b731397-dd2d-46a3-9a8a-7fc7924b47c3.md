# Propriedade SelLength

Retorna o número de caracteres que o usuário seleciona em uma área de entrada de texto de um controle ou especifica o número de caracteres a selecionar. Não disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
 [Form.]Control.SelLength[= nLength]
```

# Valor de retorno
 **nLength**
Especifica o número de caracteres selecionados. O texto selecionado aparece destacado. O intervalo válido de configurações é de 0 até o número total de caracteres no controle. Definir SelLength como um valor menor que 0 causa um erro em tempo de execução.

# Observações

Aplica-se a: ComboBox Control | EditBox Control | Spinner Control | TextBox Control (Visual FoxPro)

Use esta propriedade com as propriedades SelStart e SelText para tarefas como:
 - Definir o ponto de inserção dentro de uma cadeia de caracteres.
- Estabelecer um intervalo de inserção que limite onde o ponto de inserção pode ir.
- Selecionar um grupo específico de caracteres (subcadeias) em um controle.
- Limpar texto.

Ao trabalhar com essas propriedades, observe os seguintes comportamentos:
 - Definir SelLength como um valor menor que 0 causa um erro em tempo de execução.
- Definir SelStart como um valor maior que o comprimento do texto define a propriedade como o comprimento atual do texto. Alterar SelStart altera a seleção para um ponto de inserção e define SelLength como 0.
- Definir SelText como um novo valor define SelLength como 0 e substitui o texto selecionado pela nova cadeia de caracteres.
