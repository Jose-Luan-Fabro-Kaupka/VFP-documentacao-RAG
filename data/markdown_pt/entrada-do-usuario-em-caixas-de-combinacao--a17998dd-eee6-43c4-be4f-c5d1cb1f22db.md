# Entrada do usuário em caixas de combinação

O controle de caixa de combinação tem a funcionalidade de uma caixa de listagem e de uma caixa de texto. Há dois estilos para uma caixa de combinação: Drop-down combo e Drop-down list. Especifique qual deseja alterando a propriedade Style Property do controle. Listas suspensas são discutidas em Controls for Displaying Lists.

# Caixa de combinação suspensa

Um usuário pode clicar no botão de uma caixa de combinação suspensa para ver uma lista de opções ou inserir um novo item diretamente na caixa ao lado do botão. A propriedade Style padrão de uma caixa de combinação é 0 — Dropdown Combo.

# Adicionar itens do usuário a listas de caixas de combinação suspensas

Para adicionar o novo valor do usuário à caixa de combinação suspensa, você pode usar a linha de código a seguir no método associado ao evento Valid Event da caixa de combinação:

```foxpro
THIS.AddItem(THIS.Text)
```

Antes de adicionar um item, porém, seria uma boa ideia verificar se o valor ainda não está na lista suspensa da caixa de combinação:

```foxpro
lItemExists = .F. && assume the value isn't in the list.
FOR i = 1 to THIS.ListCount
   IF THIS.List(i) = THIS.Text
      lItemExists = .T.
      EXIT
   ENDIF
ENDFOR
IF !lItemExists
   THIS.AddItem(THIS.Text)
ENDIF
```

# Propriedades comuns de caixa de combinação

As propriedades de caixa de combinação a seguir são comumente definidas em tempo de design.

| Propriedade | Descrição |
| --- | --- |
| ControlSource | Especifica o campo da tabela onde o valor que o usuário escolhe ou insere é armazenado. |
| DisplayCount | Especifica o número máximo de itens exibidos na lista. |
| InputMask | Para caixas de combinação suspensas, especifica o tipo de valores que podem ser digitados. |
| IncrementalSearch | Especifica se o controle tenta corresponder a um item na lista conforme o usuário digita cada letra. |
| RowSource | Especifica a fonte dos itens na caixa de combinação. |
| RowSourceType | Especifica o tipo da fonte para a caixa de combinação. Os valores RowSourceType para uma caixa de combinação são os mesmos de uma List. |
| Style | Especifica se a caixa de combinação é uma drop-down combo ou uma drop-down list. |
