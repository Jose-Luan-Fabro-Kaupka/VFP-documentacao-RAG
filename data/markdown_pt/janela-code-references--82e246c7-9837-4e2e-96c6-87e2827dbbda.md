# Janela Code References

Exibe os resultados de uma pesquisa de referência de código que atendem ao escopo de projeto/pasta e tipos de arquivo especificados na caixa de diálogo Look Up Reference. Para mais informações, consulte Look Up Reference Dialog Box.

A janela Code References aparece depois que você realiza uma pesquisa na caixa de diálogo Look Up Reference ou quando você seleciona Code References no menu Tools ao pesquisar uma referência de código pesquisada anteriormente no mesmo projeto ou pasta. O projeto atualmente ativo sempre tem precedência sobre o escopo Folder. Se a caixa de diálogo Look Up Reference foi aberta anteriormente, você também pode chamar a janela Code References usando o seguinte código:

```foxpro
DO(_FOXREF)
```

Você pode configurar a janela Code References para sempre aparecer em primeiro plano quando outras janelas estiverem ativas. Na janela Code References, clique com o botão direito na área à direita da barra de ferramentas e selecione Always On Top.

No entanto, se você selecionou Always on Top para outras janelas do Visual FoxPro, não verá diferença no comportamento.

Os seguintes botões estão disponíveis na janela Code References. Você pode encontrar alguns desses comandos em menus de atalho disponíveis em diferentes painéis na janela Code Reference.
 **Open (folder icon)**
Abre ou traz para frente o designer do arquivo selecionado. O comando Open está disponível somente quando um nó de arquivo está selecionado.
**Arrow**
Alterna entre escopo de projeto e escopo de pasta.
**Search**
Exibe a caixa de diálogo Look Up Reference para você realizar uma nova pesquisa de referência de código.
**Refresh**
Atualiza resultados de pesquisa anteriores com resultados atuais.
**Replace**
Exibe uma caixa de diálogo Replace para você especificar uma expressão de substituição para referências de código selecionadas no painel de resultados. As seguintes opções estão disponíveis na caixa de diálogo Replace: Replace with Especifica a expressão de substituição para a referência de código selecionada ou referências. Confirm replacements Abre uma caixa de diálogo para você confirmar, recusar ou cancelar a operação de substituição para cada referência de código. Preserve case Realiza operações de substituição usando a capitalização original da referência de código ou texto sendo substituído. A preservação de maiúsculas/minúsculas do texto inclui somente maiúsculas, minúsculas e título (proper case), em que a primeira letra de cada palavra é capitalizada. Esta opção não suporta maiúsculas/minúsculas mistas como em "FoxPro" porque os comprimentos dos valores original e de substituição podem diferir. Create backup of modified files Faz uma cópia de backup dos arquivos selecionados antes de realizar uma operação de substituição. Cópias de backup são armazenadas nos mesmos locais dos arquivos originais. Você pode abrir a caixa de diálogo Options na janela Code References ou na caixa de diálogo Look Up Reference para controlar a nomeação de arquivos de backup. O Visual FoxPro cria um log de atividade contendo os resultados mais recentes de substituições individuais de referência de código. Esses logs de atividade são mostrados abaixo do nó Replacement Logs no painel de pesquisa. Cada log contém os seguintes itens: Uma linha que mostra o valor original e de substituição Se a operação de substituição foi bem-sucedida e se uma referência foi ignorada usando a opção Confirm Replacements Detalhes e código para você fazer alterações de estrutura de dados se arquivos de dados puderem ser afetados Observação Operações de pesquisa e substituição podem incluir todos os arquivos do Visual FoxPro, incluindo arquivos de dados. Como resultado, realizar operações de substituição pode alterar estruturas de dados. Observação Quando essa possibilidade ocorre, o Visual FoxPro mostra uma caixa de diálogo solicitando que você confirme ou recuse a operação de substituição. Se você confirmar a operação de substituição, o Visual FoxPro realiza somente as substituições que não afetam arquivos de dados e fornece código no nó de cadeia de pesquisa sob o nó Replacement Logs para você realizar manualmente as alterações desejadas. Se você recusar a substituição, nenhuma alteração é feita. Observação Além disso, a ferramenta Code Reference não suporta substituição de nomes de propriedade ou método em um formulário (.scx) ou biblioteca de classes visual (.vcx) devido a possíveis alterações em subclasses e referências pendentes.
**Print**
Exibe uma caixa de diálogo Print para você selecionar um conjunto de resultados de pesquisa de referência de código para impressão. As seguintes opções estão disponíveis na caixa de diálogo Print: Search set Especifica todos os resultados de pesquisa de referência de código ou um conjunto de resultados que você deseja imprimir. All Especifica que todas as referências no conjunto selecionado de referências de código devem ser impressas. Selected items only Especifica que somente os itens selecionados para um conjunto de referências de código são impressos. Print Imprime o conjunto especificado de referências de código. Preview Abre uma caixa de diálogo Print Preview e o Report Designer para você visualizar o conjunto de referências de código a ser impresso. Você pode especificar um relatório diferente se desejar modificando os seguintes campos no arquivo RefAddin.dbf: Type Especifique Report. Data Especifique a descrição do relatório. Filename Especifique o nome do relatório, como "report1.frx".
**Export**
Exibe uma caixa de diálogo Export para você exportar todos ou um conjunto de resultados de pesquisa de referência de código para uma variedade de formatos. As seguintes opções estão disponíveis na caixa de diálogo Export: Type Especifica o tipo de arquivo de destino para seus resultados de pesquisa. Para tornar XML Output Options disponível, selecione Extensible Markup Language (XML) na lista suspensa Type. Ao exportar seus resultados de pesquisa para HTML, o Visual FoxPro gera o arquivo usando XML e XSLT. Por padrão, o Visual FoxPro procura um arquivo FoxRef.xsl no diretório home do Visual FoxPro ou HOME(0). Se o arquivo não for encontrado, o Visual FoxPro copia um arquivo .xsl interno e o coloca no diretório Visual FoxPro User Application Data ou HOME(7), a menos que você especifique um diretório diferente. Você pode fornecer um arquivo XSLT para formatar o arquivo HTML renomeando seu arquivo XSLT para FoxRef.xsl e substituindo o arquivo .xsl original pelo novo arquivo. To Especifica um nome de arquivo para o arquivo exportado. Para escolher um local diferente da pasta atual para o arquivo exportado, clique no botão de reticências (...). Search set Especifica todos os resultados de pesquisa de referência de código ou um conjunto de resultados que você deseja exportar. View after export Especifica que você visualiza os resultados gerados após a operação de exportação terminar. Esta opção torna-se indisponível se você selecionar Clipboard como tipo de arquivo de destino. XML Output Options Especifica as seguintes opções adicionais para exportar resultados de pesquisa para saída XML: Generate element-based XML Gera um arquivo XML no qual campos são armazenados como elementos. Generate attribute-based XML Gera um arquivo XML no qual campos são armazenados como atributos. Include schema Adiciona esquema XML Schema Definition (XSD) à saída XML. All Especifica que todas as referências no conjunto selecionado de referências de código devem ser exportadas. Selected items only Especifica que somente os itens selecionados para um conjunto de referências de código são exportados.
**Options**
Abre a caixa de diálogo Options para definir opções adicionais para sua pesquisa. Para mais informações, consulte Look Up Reference Dialog Box, Options Dialog Box.
**Help**
Abre o arquivo de ajuda do Visual FoxPro.

# Painel Search

O painel de pesquisa, ou janela superior esquerda, contém uma visualização em árvore recolhível dos resultados de uma pesquisa de referência de código. A visualização em árvore exibe um nó All Results, cada referência de código e os arquivos que contêm a referência. Quando você clica em um nome de arquivo, a visualização no painel de resultados, ou janela superior direita, é filtrada para representar somente os resultados desse arquivo específico.

Um nó Replacement Logs aparece no painel de pesquisa quando logs contendo os resultados mais recentes de operações individuais de substituição de referência de código são criados.

Os seguintes comandos estão adicionalmente disponíveis em um menu de atalho que aparece quando você clica com o botão direito em um nó de navegação, referência de código ou arquivo dentro do painel de pesquisa:
 **Copy**
Copia todas as informações no painel de resultados, incluindo o nome do arquivo, classe, método ou procedimento e informações de linha, para o item selecionado na área de transferência para que você possa colar as informações em outro lugar.
**Expand All**
Expande totalmente a árvore de resultados de pesquisa.
**Collapse All**
Recolhe a árvore de resultados de pesquisa.
**Sort by Most Recent First**
Classifica os resultados de pesquisa na árvore, colocando os resultados mais recentes no topo da árvore.
**Clear Result**
Remove o resultado selecionado do painel de pesquisa. O comando Clear Result não está disponível se o nó All Results estiver selecionado. Se um arquivo estiver selecionado, somente esse arquivo é removido do painel de pesquisa.
**Clear All Results**
Remove todos os resultados de pesquisa do painel de pesquisa.
**Refresh**

# Painel Results

O painel de resultados, ou janela superior direita, exibe resultados de uma pesquisa de referência de código, incluindo definições potenciais, se existirem, para as quais você pode saltar rapidamente, e múltiplas referências que podem existir em uma única linha de código. Se existirem múltiplas referências por linha, o painel de resultados exibe um indicador (o número de referências entre parênteses) nessa linha.

O painel de resultados mostra os seguintes itens:
 - Caixas de seleção para você selecionar linhas individuais de código
- # Número de instâncias de referência de código que ocorrem no resultado, se mais de uma
- File Name Nome e local do arquivo da referência de código
- Class.Method, Line Classe, método e número da linha
- Code Linha de código que contém a referência de código

Você pode classificar itens em cada coluna clicando em cada um dos cabeçalhos de coluna.

Os seguintes comandos estão adicionalmente disponíveis em um menu de atalho que aparece quando você clica com o botão direito em uma referência selecionada dentro do painel de resultados:
 **Copy**
Copia todas as informações para a linha selecionada, incluindo o nome do arquivo, classe, método ou procedimento e informações de linha, para a área de transferência para que você possa colar as informações em outro lugar.
**Select All**
Seleciona todos os itens no painel de resultados.
**Clear Selections**
Limpa as caixas de seleção no painel de resultados.
**Sort by**
Organiza os itens da seguinte maneira: File Name Organiza itens baseado no nome do arquivo. Class.Method Organiza itens baseado no nome da classe seguido do nome do método. Selected Agrupa itens por se estão selecionados. File Type Organiza itens baseado no tipo de arquivo (extensão). Location Organiza itens por localização de pasta.

# Painel Description

O painel de descrição, ou janela inferior, exibe informações sobre uma pesquisa de referência de código, como o projeto ou pasta pesquisada e as correspondências encontradas. Quando uma referência é selecionada, o painel de descrição mostra a localização da referência e a linha de código em que a expressão aparece.

 Para ocultar ou exibir o painel de descrição
 - Na janela Code References, clique com o botão direito na área à direita da barra de ferramentas.
- No menu de atalho, selecione Display Descriptions.
