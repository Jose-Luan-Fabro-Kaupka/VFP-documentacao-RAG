# Guia General, Report Control Properties Dialog Box (Report Builder)

Permite definir opções gerais para controles de relatório no Report Designer ou Label Designer.

> **Observação:** Esta guia substitui a funcionalidade de várias caixas de diálogo nativas do Visual FoxPro quando o Report Builder está ativo.
 - Como: adicionar controles Field a relatórios
- Como: especificar expressões em controles Field
- Como: adicionar controles Label a relatórios
- Como: adicionar imagens a relatórios
- Como: adicionar campos General a relatórios
 **Caption**
(Somente controles Label) Especifica o texto da legenda. Clicar no botão de reticências (…) abre uma caixa de diálogo de edição para que você possa visualizar e editar o texto completo do controle Label.
**Expression**
(Somente controles Field) Especifica uma expressão, como o nome de uma variável ou campo de tabela. A expressão é avaliada em tempo de execução do relatório conforme o mecanismo de relatório renderiza a saída do controle Field. Clicar no botão de reticências (…) abre o Expression Builder para que você possa construir uma expressão. Para obter mais informações, consulte Expression Builder Dialog Box .

# Tipo de origem do controle

(Somente controles Picture/OLE Bound) Especifica a origem de um controle de relatório Picture/OLE Bound. Origens válidas incluem o nome de um arquivo de imagem, o nome de um campo General em uma tabela ou uma expressão ou variável que contém um nome de arquivo ou campo de caracteres não-General para o controle de relatório. Para obter mais informações, consulte Como: adicionar imagens a relatórios e Como: adicionar campos General a relatórios.
 **Image file name**
Especifica que a origem do controle deve conter um nome de arquivo de imagem literal. Importante Não coloque o nome do arquivo entre aspas ("").
**General field name**
Especifica que a origem do controle deve ser avaliada como o nome de um campo General de uma tabela ou cursor.
**Expression or variable name**
Especifica que a origem do controle deve ser uma expressão ou variável que seja avaliada como: Um nome de arquivo de imagem. Um campo de caracteres não-General. Uma literal de cadeia de caracteres contendo um nome de arquivo explícito. Uma referência de objeto a um objeto Image de formulário que tenha sua propriedade PictureVal definida adequadamente. Dica O uso da propriedade PictureVal de um objeto Image como origem de imagem em um relatório é suportado somente no modo de saída assistido por objetos. Funcionará no modo compatível com versões anteriores, em alguns casos, mas os resultados não são garantidos. Por exemplo, no modo compatível com versões anteriores, controles Picture/OLE Bound com esta origem podem não respeitar a opção de dimensionamento Clip. Para obter mais informações, consulte o comando SET REPORTBEHAVIOR .

# Origem do controle

(Somente controles Picture/OLE Bound) Especifica uma cadeia de caracteres, expressão ou nome de variável que seja avaliado como a origem do controle Picture/OLE Bound. Clicar no botão de reticências (...) executa uma ação diferente dependendo do valor do tipo de origem do controle:
 - Image file name Exibe a caixa de diálogo Open para que você possa selecionar um arquivo. Para obter mais informações, consulte Open Dialog Box .
- General field name Abre o Expression Builder para que você possa selecionar um campo General. Para obter mais informações, consulte Expression Builder Dialog Box e General Field Type .
- Expression or variable name Abre o Expression Builder para que você possa construir uma expressão ou selecionar uma variável. Para obter mais informações, consulte Expression Builder Dialog Box .

# Se a origem e o quadro tiverem tamanhos diferentes

(Somente controles Picture/OLE Bound) Especifica como o controle deve ser exibido quando as dimensões do controle não correspondem ao tamanho padrão da origem do controle:
 - Clip picture (Padrão) A saída renderizada da origem do controle sempre aparece ancorada no canto superior esquerdo do quadro do controle. Se a origem do controle for maior que o quadro, somente a região superior esquerda da origem do controle que cabe nas dimensões do controle é exibida. Se a origem do controle for menor que o contorno do controle, o controle será redimensionado para caber ou permanecerá transparente na área não coberta pela origem do controle renderizada.
- Scale picture, retain shape A saída renderizada do controle é exibida em tamanho reduzido para que a maior dimensão caiba nas restrições do quadro do controle. A saída renderizada mantém suas proporções relativas. Dica Esta opção protege a imagem ou o campo General de distorção vertical ou horizontal.
- Scale picture, fill the frame A saída renderizada do controle é dimensionada para preencher completamente as dimensões do quadro do controle, esticando-a vertical ou horizontalmente conforme necessário. Observação Esta configuração pode causar distorção vertical ou horizontal

# Centralizar campo general horizontalmente no quadro

(Somente controles Picture/OLE Bound) Centraliza o campo General quando ele é menor que o quadro que o contém. Caso contrário, o campo General é exibido no canto superior esquerdo do quadro.

# Posição do objeto

Especifica configurações de posição para o controle de relatório.
 **Float**
Especifica que o controle se move para baixo na página quando um controle que aparece acima dele se estende para baixo.
**Fix relative to top of band**
Especifica que o controle permaneça em posição relativa ao topo da faixa que o contém.
**Fix relative to bottom of band**
Especifica que o controle permaneça em posição relativa à parte inferior da faixa que o contém.

# Estender com overflow

(Somente controles Field) Especifica que a parte inferior de um controle Field seja estendida verticalmente para baixo na página para conter o valor completo da expressão avaliada.

# Estender para baixo

(Somente controles Rectangle) Especifica como um controle Rectangle deve alterar sua forma conforme o conteúdo avaliado de uma faixa força a faixa a se estender.
 **No stretch**
Especifica que a parte inferior do controle Rectangle não se expanda verticalmente conforme a faixa se estende para acomodar dados em controles Field.
**Stretch relative to tallest object in group**
Especifica que a parte inferior do controle Rectangle se estenda verticalmente para se ajustar ao objeto mais alto no grupo.
**Stretch relative to height of band**
Especifica que a parte inferior do controle Rectangle se estenda verticalmente para baixo quando a faixa se estende para acomodar dados em controles Field.

# Tamanho e posição no layout

Especifica posicionamento e tamanho para o controle de relatório no Report Designer.
 **From page top**
Especifica um valor a partir do topo da página para posicionar o controle de relatório.
**From left**
Especifica um valor a partir da esquerda da página para posicionar o controle de relatório.
**Height**
Especifica um valor para a altura do controle de relatório.
**Width**
Especifica um valor para a largura do controle de relatório.
