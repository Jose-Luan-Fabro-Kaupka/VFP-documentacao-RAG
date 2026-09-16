# Propriedade Centered

Especifica se um controle CheckBox está centralizado dentro dos limites do controle.

```foxpro
CheckBox.Centered [= lExpr]
```

# Valor de retorno
 **lExpr**
Tipo de dados lógico. A tabela a seguir lista os valores de lExpr . lExpr Descrição False (.F.) O controle CheckBox não está centralizado dentro dos limites do controle. (Padrão) True (.T.) Centraliza o controle CheckBox dentro dos limites do controle.

# Observações

Aplica-se a: CheckBox Control

Se um controle CheckBox não estiver contido em um grid, o controle é centralizado dentro de seus próprios limites de controle.

Centered funciona em conjunto com a propriedade Alignment. Se você fornecer uma legenda, os valores de alinhamento esquerdo e direito da propriedade Alignment determinam de qual lado da caixa de seleção a legenda aparece. Se a propriedade Centered também estiver definida como True (.T.), tanto a legenda quanto a caixa de seleção são centralizadas horizontal e verticalmente na coluna do grid.

Se a propriedade Sparse da coluna estiver definida como True (.T.) (padrão), a propriedade Alignment da coluna determina o posicionamento do texto em todas as células da coluna. No entanto, quando uma célula específica recebe foco e o controle aparece, o Visual FoxPro usa a propriedade Alignment do controle. Se você definir a propriedade Sparse da coluna como False (.F.), o Visual FoxPro usa a propriedade Alignment do controle e ignora a propriedade Alignment da coluna.

Quando a propriedade Alignment da coluna é definida em tempo de design, o designer tenta definir a propriedade Alignment nos controles da coluna também. Quando esse controle é um CheckBox, definir o Alignment da coluna para qualquer um dos valores de propriedade "center" define automaticamente a propriedade Centered como True (.T.).

Se Centered for True (.T.), a caixa de seleção permanece centralizada horizontal e verticalmente na célula do grid conforme as colunas e linhas do grid são redimensionadas.

# Exemplo

O exemplo a seguir mostra como você pode definir a propriedade Centered para alinhar uma caixa de seleção com o centro do controle e sua legenda à direita da caixa de seleção:

```foxpro
Checkbox1.Centered = .T.
Checkbox1.Alignment = 1
```

# Exemplo 2

O exemplo a seguir mostra como você pode definir a propriedade Centered para alinhar uma caixa de seleção no centro de uma coluna do grid. Definir a propriedade Sparse da coluna como False (.F.) especifica que a propriedade Alignment do controle tem precedência sobre a propriedade Alignment da coluna do grid:

```foxpro
Column1.Sparse = .F.
Column1.Checkbox1.Centered = .T.
Column1.Checkbox1.Caption = ""
```
