# Objeto Column

Cria um objeto Column em um controle Grid. Uma coluna de grade pode conter dados de um campo em uma tabela ou o valor de uma expressão. Uma coluna também pode conter controles.

```foxpro
Grid.Column
```

# Observações

Para especificar os dados exibidos na coluna, use a propriedade DataSource da coluna.

Você pode especificar o número de colunas em uma grade com a propriedade ColumnCount da grade.

Você pode adicionar controles a uma coluna em uma grade usando o método AddObject no evento Init do formulário que contém a grade. Para definir o controle ativo na coluna da grade, use a propriedade CurrentControl da coluna. Para especificar a origem dos dados do controle, defina a propriedade ControlSource do controle.

> **Observação:** Você não pode acessar cabeçalhos e controles de uma coluna até que ocorra o evento Init da grade.

Para obter informações adicionais sobre a criação de colunas em uma grade, consulte Grid Control e Using Controls.

Ocultando colunas Para ocultar uma coluna em uma grade, defina a propriedade Visible da coluna como False (.F.). Você ainda pode definir a propriedade Value de qualquer controle na coluna. Por exemplo, você ainda pode alterar o valor de `Column.Text1.Value` especificando um novo valor, mesmo quando a coluna estiver oculta.

O Visual FoxPro processa alterações não confirmadas em uma coluna oculta normalmente e no momento apropriado de acordo com a propriedade BufferMode do formulário. Por exemplo, ocultar uma coluna não faz com que atualizações pendentes sejam confirmadas nem impede que sejam confirmadas nessa coluna.

Quando você oculta uma coluna que tem o foco, o foco não se move automaticamente da coluna oculta para a coluna seguinte ou anterior. Em essência, nenhuma coluna tem o foco. Se você desejar mover o foco para outra célula, coluna ou controle, deverá mover o foco manualmente, por exemplo, pressionando a tecla TAB ou usando o mouse.

Quando você oculta todas as colunas em uma grade, apenas a parte do indicador de registro da grade ao longo do lado esquerdo permanece visível.

Definir a propriedade AllowAutoColumnFit e usar o método AutoFit não afeta colunas ocultas. Para obter mais informações, consulte AllowAutoColumnFit Property e AutoFit Method.
