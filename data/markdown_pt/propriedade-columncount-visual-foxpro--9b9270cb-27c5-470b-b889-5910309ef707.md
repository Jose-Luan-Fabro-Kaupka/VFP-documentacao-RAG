# Propriedade ColumnCount (Visual FoxPro)

Especifica o número de objetos Column em um controle Grid, ComboBox ou ListBox. Para um grid, disponível em tempo de design e leitura/gravação em tempo de execução. Para uma combo box ou list box, disponível em tempo de design e em tempo de execução.

```foxpro
Object.ColumnCount[ = nCol]
```

# Valor de retorno
 **nCol**
Para um controle Grid, especifica o número de colunas a exibir. O padrão é –1, que especifica que o controle Grid deve conter colunas suficientes para acomodar todos os campos na fonte de registros do grid. O número máximo de colunas é 255. Se você criar um número específico de colunas definindo nCol como um valor positivo, especifique os dados a exibir em uma coluna específica definindo a propriedade ControlSource dessa coluna. (Se ControlSource não for especificado para uma coluna, o controle Grid exibe o próximo campo não exibido disponível da fonte de registros do grid.) Para um controle ComboBox ou ListBox, nCol especifica o número de colunas que o controle contém. Se você definir ColumnCount como 0, a primeira coluna é exibida baseada na propriedade RowSource ou nos itens adicionados com o método AddItem.

# Observações

Aplica-se a: ComboBox Control | Grid Control | ListBox Control

Para um grid, use o método AddColumn para aumentar o número de colunas.
