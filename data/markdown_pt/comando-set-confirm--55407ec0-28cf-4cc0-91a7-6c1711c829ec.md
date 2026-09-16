# Comando SET CONFIRM

Especifica se o usuário pode sair de uma caixa de texto digitando além do último caractere na caixa de texto.

```foxpro
SET CONFIRM ON | OFF
```

#### Parâmetros
 **ON**
Especifica que o usuário não pode sair de uma caixa de texto digitando além do último caractere na caixa de texto. Para sair da caixa de texto, o usuário pode pressionar ENTER, TAB ou qualquer uma das teclas de seta para mover de uma caixa de texto para outro controle. SET CONFIRM ON também afeta itens de menu e títulos de menu criados com DEFINE BAR e DEFINE PAD. Se o usuário digitar a primeira letra do item de menu ou título de menu, o item ou título é selecionado, mas não é escolhido. Para escolher o item de menu ou título quando selecionado, o usuário deve pressionar ENTER ou a BARRA DE ESPAÇO.
**OFF**
Especifica que o usuário pode sair de uma caixa de texto digitando além do último caractere na caixa de texto. O ponto de inserção, quando atinge o último caractere em uma caixa de texto, move para o próximo controle e o sinal sonoro é emitido (se SET BELL estiver definido como ON). OFF é o valor padrão de SET CONFIRM. SET CONFIRM OFF também afeta itens de menu e títulos de menu. Se SET CONFIRM estiver definido como OFF, o usuário pode escolher um item de um menu ou um título de menu na barra de menus pressionando a tecla correspondente à primeira letra do item de menu ou título. (Quando SET CONFIRM está definido como ON, esta ação apenas seleciona o item de menu ou título.)

# Observações

SET CONFIRM não tem efeito nas teclas de acesso para itens de menu e títulos de menu. Se um item de menu ou título de menu é criado com uma tecla de acesso, o item de menu ou título pode ser escolhido pressionando a tecla de acesso correspondente.

Você pode criar caixas de texto usando o Form Designer.

SET CONFIRM tem escopo na sessão de dados atual.
