# Propriedade Anchor

Define a quais bordas do contêiner pai um controle visual é ancorado ao redimensionar o contêiner. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
Control.Anchor [= nValue]
```

# Valor de retorno
 **nValue**
Especifica um valor de bit que determina o comportamento de ancoragem do controle. A tabela a seguir descreve valores de bit que você pode definir ou adicionar para produzir valores para nValue . Posição Valor de bit Número do bit Valores conflitantes Descrição Top Left 0 Ancora o controle às bordas superior e esquerda do contêiner e não altera a distância entre as bordas superior e esquerda. (Padrão) Top Absolute 1 0 16, 512 Ancora o controle à borda superior do contêiner e não altera a distância entre a borda superior. Left Absolute 2 1 32, 256 Ancora o controle à borda esquerda do contêiner e não altera a distância entre a borda esquerda. Bottom Absolute 4 2 64, 512 Ancora o controle à borda inferior do contêiner e não altera a distância entre a borda inferior. Right Absolute 8 3 128, 256 Ancora o controle à borda direita do contêiner e não altera a distância entre a borda direita. Top Relative 16 4 1, 512 Ancora o controle à borda superior do contêiner e mantém a distância relativa entre a borda superior. Left Relative 32 5 2, 256 Ancora o controle à borda esquerda do contêiner e mantém a distância relativa entre a borda esquerda. Bottom Relative 64 6 4, 512 Ancora o controle à borda inferior do contêiner e mantém a distância relativa entre a borda inferior. Right Relative 128 7 8, 256 Ancora o controle à borda direita do contêiner e mantém a distância relativa entre a borda direita. Horizontal Fixed Size 256 8 2, 8, 32, 128 Ancora o centro do controle em relação às bordas esquerda e direita, mas permanece com tamanho fixo. Vertical Fixed Size 512 9 1, 4, 16, 64 Ancora o centro do controle em relação às bordas superior e inferior, mas permanece com tamanho fixo. A tabela a seguir descreve exemplos de configurações comuns para a propriedade Anchor. Controle nValue Descrição TextBox ou EditBox 10 Redimensiona o controle horizontalmente conforme você o redimensiona. CommandButton 12 Exibe um conjunto de dois controles, por exemplo, OK e Cancel, no canto inferior direito. CommandButton 128 e 32 Centraliza dois botões de comando esquerdo e direito. CommandButton 260 Centraliza o controle na parte inferior de um formulário.

# Observações

Aplica-se a: Controle CheckBox | Controle ComboBox | Controle CommandButton | Controle CommandGroup | Objeto Container | Objeto Control (Visual FoxPro) | Controle EditBox | Controle Grid | Controle Image (Visual FoxPro) | Controle Label (Visual FoxPro) | Controle Line | Controle ListBox | Controle OLE Bound | Controle OLE Container | Controle OptionButton | Controle OptionGroup | Controle PageFrame | Controle Shape | Controle Spinner | Controle TextBox (Visual FoxPro)

A ancoragem é baseada nas coordenadas do controle no momento em que a propriedade Anchor do controle é definida originalmente, tipicamente, quando o controle é instanciado. Não é baseada na posição atual do controle. Portanto, mesmo depois de mover um controle, a ancoragem se aplica à posição original do controle. Esse comportamento explica a diferença entre um valor Anchor de 0 e 3.

Por exemplo, suponha que você tem um controle CommandButton em um formulário e a propriedade Anchor do controle está inicialmente definida como 3. Inserindo o código a seguir no evento Click do controle e clicando no botão, você pode mover o botão de comando:

```foxpro
This.Left = This.Left + 10
```

No entanto, quando você redimensiona o formulário, o controle retorna à sua posição original.

> **Dica:** Se você deseja basear a ancoragem na posição atual do controle depois que ele foi movido, redefina a propriedade Anchor do controle para 0 e depois de volta para 3. Por exemplo, usando o código a seguir no evento Click do botão de comando move o botão de comando quando você clica nele, mas mantém a posição atual do controle quando o formulário é redimensionado:

```foxpro
This.Left = This.Left + 10
This.Anchor = 0
This.Anchor = 3
```

As configurações da propriedade Anchor são obedecidas para controles aplicáveis nos seguintes contêineres:
 - Controle CommandGroup
- Objeto Container
- Objeto Control (Visual FoxPro)
- Objeto Form
- Controle OptionGroup
- Objeto Page

As configurações da propriedade Anchor são ignoradas para controles nos objetos ToolBar e Column.

Você pode redimensionar o controle se valores de ancoragem são definidos para ambas as bordas opostas, por exemplo, bordas esquerda e direita ou bordas superior e inferior. Você só pode mover o controle se definir uma única borda.

Se você não definir bits para um eixo específico, a posição do controle não altera para esse eixo quando o contêiner é redimensionado. Por exemplo, os números de bit 1, 3, 5, 7 e 10 afetam a dimensão superior e inferior.

Você não pode definir valores de bit que conflitam entre si. Esses valores de bit incluem os seguintes:
 - Bits Absolute e Relative para a mesma borda, por exemplo, um nValue de 17.
- Bits Fixed Size e Border para as mesmas bordas de eixo, por exemplo, um nValue de 258 ou 513.

Para uma descrição dos valores conflitantes, consulte a tabela que lista os valores para nValue.
