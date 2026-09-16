# Propriedade AutoCompTable

Especifica o nome e o local da tabela que armazena os dados usados por um controle Textbox para sugerir valores com base em valores inseridos anteriormente.

```foxpro
Textbox.AutoCompTable [ = cValue]
```

# Valor de retorno
 **cValue**
Especifica o nome e o caminho da tabela que suporta a exibição de uma lista de entradas usadas anteriormente em uma caixa de texto.

# Observações

Aplica-se a: TextBox Control (Visual FoxPro)

O local e o nome padrão desta propriedade é HOME(7) + "Autocomp.DBF". Se você inserir um nome para uma tabela que não existe, a tabela será criada para você.

A tabela a seguir descreve a estrutura da tabela Auto Complete.

| Nome do campo | Tipo (tamanho) | Descrição |
| --- | --- | --- |
| Source | C (20) | Nome de origem do controle Textbox. |
| Data | C (254) | Item de dados a exibir. |
| Count | I | Número de vezes que o item de dados foi selecionado. |
| Weight | I | Especifica o valor a usar quando AutoComplete está definido como 4 (Custom). |
| Created | T | Carimbo de data/hora quando o item de dados foi criado pela primeira vez. |
| Updated | T | Carimbo de data/hora quando o item de dados foi atualizado pela última vez. |
| User | M | Especifica informações do usuário. |
