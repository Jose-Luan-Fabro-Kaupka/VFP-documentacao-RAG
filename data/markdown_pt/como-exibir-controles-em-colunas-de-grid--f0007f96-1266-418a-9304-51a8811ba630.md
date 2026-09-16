# Como: exibir controles em colunas de grid

Além de exibir dados de campo em um grid, você pode ter controles nas colunas de um grid para apresentar ao usuário caixas de texto, caixas de seleção, caixas de listagem suspensa, spinners e outros controles incorporados. Por exemplo, se você tem um campo lógico em uma tabela, quando executa o formulário, um usuário pode identificar quais valores de registro são true (.T.) e quais são false (.F.) vendo se a caixa de seleção está marcada. Alterar o valor é tão simples quanto marcar ou desmarcar a caixa de seleção.

Você pode adicionar controles a colunas de grid interativamente no Form Designer ou escrever código para adicionar os controles às colunas em tempo de execução.

### Para adicionar controles interativamente a uma coluna de grid
- Adicione um grid a um formulário.
- Na janela Properties (Visual FoxPro), defina a propriedade ColumnCount do grid para o número de colunas desejadas. Por exemplo, digite 2 para um grid de duas colunas.
- Na janela Properties, selecione a coluna pai do controle na caixa Object. Por exemplo, selecione Column1 para adicionar um controle a Column1. A borda do grid muda para indicar que você está editando um objeto contido quando seleciona a coluna.
- Selecione o controle desejado na barra de ferramentas Form Controls e clique na coluna pai. O novo controle não será exibido na coluna do grid no Form Designer, mas será visível em tempo de execução.
- Na janela Properties, certifique-se de que o controle está exibido com indentação sob a coluna pai na caixa Object. Se o novo controle é uma caixa de seleção, defina a propriedade Caption da caixa de seleção como " " e a propriedade Sparse da coluna como false (.F.).
- Defina a propriedade ControlSource da coluna pai para o campo de tabela desejado. Por exemplo, a ControlSource da coluna na ilustração a seguir é products.discontinu do Testdata.dbc no diretório Visual FoxPro ...\Samples\Data.
- Defina a propriedade CurrentControl da coluna pai para o novo controle.

Quando você executa o formulário, o controle é exibido na coluna do grid.

> **Dica:** Se você deseja centralizar uma caixa de seleção em uma coluna de grid, crie uma classe de contêiner, adicione uma caixa de seleção à classe de contêiner e ajuste a posição da caixa de seleção na classe de contêiner. Adicione a classe de contêiner à coluna do grid e defina a ControlSource da caixa de seleção para o campo desejado.

### Para remover controles de colunas de grid no Form Designer
- Na caixa Object da janela Properties (Visual FoxPro), selecione o controle.
- Ative o Form Designer. Se a janela Properties estiver visível, o nome do controle é exibido na caixa Object.
- Pressione a tecla DELETE.

Você também pode adicionar controles a uma coluna de grid usando o AddObject Method em código.

### Para adicionar controles programaticamente a uma coluna de grid
- No evento Init do grid, use o AddObject Method para adicionar o controle à coluna do grid e defina a propriedade CurrentControl da coluna.

Por exemplo, as linhas de código a seguir no evento Init de um grid adicionam dois controles a uma coluna de grid e especificam um deles como o controle atual:

```foxpro
THIS.grcColumn1.AddObject("spnQuantity", "SPINNER")
THIS.grcColumn1.AddObject("cboQuantity", "COMBOBOX")
THIS.grcColumn1.CurrentControl = "spnQuantity"
* The following lines of code make sure the control is visible
* and is diplayed in every row in the grid
THIS.grcColumn1.spnQuantity.Visible = .T.
THIS.grcColumn1.Sparse = .F.
```

Neste exemplo, Column1 tem três possíveis valores de controle atual:
 - spnQuantity
- cboQuantity
- Text1 (the default control) Observação Propriedades definidas no nível do Grid não são repassadas às colunas ou cabeçalhos. Da mesma forma, você deve definir propriedades dos cabeçalhos e controles contidos diretamente; eles não herdam suas propriedades de configurações no nível da Column. Dica Para a melhor exibição de combo boxes em colunas de grid, defina as seguintes propriedades da combo box: BackStyle = 0 && Transparent Margin = 0 SpecialEffect = 1 && Plain BorderStyle = 0 && None
