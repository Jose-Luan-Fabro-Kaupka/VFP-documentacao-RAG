# Caixa de diálogo Report Picture

Permite incluir imagens ou o conteúdo de campos General em seu relatório ou etiqueta.

Esta caixa de diálogo aparece quando você escolhe Picture/OLE Bound Control na barra de ferramentas Report Controls e coloca o controle em um relatório ou etiqueta. Para obter mais informações, consulte Como: adicionar imagens a relatórios e Como: adicionar campos General a relatórios.

> **Observação:** Dependendo da configuração da variável de sistema _REPORTBUILDER, esta caixa de diálogo pode ser substituída por uma interface de usuário alternativa. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER.

# Print When

Especifica uma expressão que controla a supressão ou exibição de uma imagem.
**Print When**
Exibe a caixa de diálogo Print When para que você possa controlar quando imprimir a imagem ou o campo General. Para obter mais informações, consulte Caixa de diálogo Print When.

# Picture from

Especifica a origem como um arquivo de imagem ou um campo General.
**File**
Especifica o nome de um arquivo de imagem. Clicar no botão de reticências (...) exibe a caixa de diálogo Open para que você possa selecionar um arquivo. Para obter mais informações, consulte Caixa de diálogo Open (Visual FoxPro) e Como: adicionar imagens a relatórios.
**Field**
Especifica o nome de um campo General. Clicar no botão de reticências (...) exibe a caixa de diálogo Choose Field/Variable para que você possa selecionar um campo. Para obter mais informações, consulte Caixa de diálogo Choose Field/Variable, Tipo de campo General e Como: adicionar campos General a relatórios.

# If picture and frame are different sizes

Especifica como exibir um arquivo de imagem ou um campo General ao redimensioná-lo ou quando o tamanho da imagem ou do campo General difere da moldura que o contém.
**Clip picture (Default)**
A saída renderizada da origem do controle sempre aparece ancorada no canto superior esquerdo da moldura do controle. Se a origem do controle for maior que a moldura, será exibida apenas a região superior esquerda da origem que couber nas dimensões do controle. Se a origem do controle for menor que o contorno do controle, o controle será redimensionado para se ajustar ou permanecerá transparente na área não coberta pela origem renderizada.
**Scale picture, retain shape**
A saída renderizada do controle é exibida em tamanho reduzido, de modo que a maior dimensão caiba nos limites da moldura do controle. A saída renderizada mantém suas proporções relativas. Dica: esta opção protege a imagem ou o campo General contra distorção vertical ou horizontal.
**Scale picture, fill the frame**
A saída renderizada do controle é dimensionada para preencher completamente as dimensões da moldura do controle, sendo esticada vertical ou horizontalmente conforme necessário. Observação: esta opção pode causar distorção vertical ou horizontal.

# Object Position

Especifica configurações de posição para o controle de relatório.
**Float**
Especifica que o controle se move para baixo na página quando um controle acima dele se expande para baixo.
**Fixed relative to top of band**
Especifica que o controle permaneça posicionado em relação à parte superior da faixa que o contém.
**Fixed relative to bottom of band**
Especifica que o controle permaneça posicionado em relação à parte inferior da faixa que o contém.
**Center picture**
Centraliza um campo General quando ele é menor que a moldura que o contém. Caso contrário, o campo General é exibido no canto superior esquerdo da moldura.
**Comment**
Especifica um texto de comentário para o controle, apenas como referência. Ele é salvo com o arquivo de layout, mas não aparece no relatório nem na etiqueta.
