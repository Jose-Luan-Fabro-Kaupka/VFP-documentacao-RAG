# Aprimoramentos diversos

O Visual FoxPro contém os seguintes aprimoramentos diversos. Você pode clicar em Collapse All para ver uma lista de aprimoramentos.

# Caixas de diálogo de impressão e aprimoramentos da linguagem de impressão

O Visual FoxPro inclui vários aprimoramentos para suas caixas de diálogo de impressão e linguagem de impressão.

O Visual FoxPro usa as caixas de diálogo mais recentes do sistema operacional para Printer Setup e outras operações de impressão relacionadas. Se o usuário estiver executando no Windows XP, as caixas de diálogo aparecerão com tema.

As seguintes funções de linguagem contêm novos aprimoramentos que impactam operações gerais de impressão:
 - SYS(1037) - Caixa de diálogo Page Setup
- Função APRINTERS( )
- Função GETFONT( ) Contém uma configuração adicional para exibir apenas as fontes disponíveis na impressora padrão atual e valores esclarecidos para o script de linguagem.

Para obter mais informações, consulte Aprimoramentos de linguagem.

# Suporte aprimorado para aplicativos detectando Terminal Servers

O Visual FoxPro agora inclui automaticamente suporte para aplicativos gerados pelo processo de build para detectar se estão executando em um Terminal Server e impedir o carregamento de arquivos de biblioteca de vínculo dinâmico (.dll) desnecessários que podem impactar o desempenho. Para obter mais informações, consulte Comando BUILD EXE.

# Relatório de erros Dr. Watson atualizado para 2.0

O Visual FoxPro inclui e atualiza seu relatório de erros de produto para suportar Dr. Watson 2.0. Esta versão inclui novos e aprimorados recursos de relatório de erros, registro e auditoria. Por exemplo, erros são registrados offline e publicados quando você reconecta.

# Aplicativo Anchor Editor

O Visual FoxPro 9.0 permite criar um editor de propriedades personalizado por meio de atributos de metadados estendidos para membros de classe. Por meio deste novo modelo de extensibilidade, você agora tem a capacidade de estender a funcionalidade de propriedades e métodos de classe, permitindo criar aprimoramentos em tempo de design, como um editor de propriedades personalizado. Para obter mais informações sobre como criar editores de propriedades personalizados, consulte Extensibilidade MemberData.

Uma amostra de editor de propriedades personalizado, Anchoreditor.app, está incluída no Visual FoxPro 9.0 e está localizada no diretório Wizards. Este aplicativo é executado quando a propriedade Anchor é clicada duas vezes na janela Properties, ou escolhendo a propriedade Anchor na janela Properties e clicando no botão de reticências (…).

| Termo | Definição |
| --- | --- |
| Anchor but do not resize vertically | Especifica que o centro do controle está ancorado às bordas superior e inferior de seu contêiner, mas o controle não redimensiona. |
| Anchor but do not resize horizontally | Especifica que o centro do controle está ancorado às bordas esquerda e direita de seu contêiner, mas o controle não redimensiona. |
| Border values | Exibe as configurações atuais para os valores de borda. |
| Common settings | Seleciona configurações comumente usadas para a propriedade Anchor. |
| Sample | Clique no botão Sample para testar o valor de âncora atual em um formulário de exemplo. |
| Anchor value | O valor da propriedade Anchor que é a combinação das configurações atuais para os valores de borda. |

# Class Browser

Você pode abrir e visualizar definições de classe especificadas em um programa (.prg) de forma semelhante a bibliotecas de classes (.vcx). Você pode selecionar um programa (.prg) na caixa de diálogo File Open/Add. Consulte Janela Class Browser para obter mais informações.

# CursorAdapter Builder

O CursorAdapter Builder contém vários aprimoramentos que correspondem a melhorias adicionadas à classe CursorAdapter. Consulte CursorAdapter Builder para obter mais informações.

# Toolbox

A Toolbox (Visual FoxPro) agora é acoplável e pode ser acoplada à área de trabalho ou a outras janelas da IDE.

# Code References

A janela Code References foi atualizada com os seguintes aprimoramentos menores:
 - Para a grade de resultados, a caixa de diálogo Options fornece uma nova configuração para mostrar colunas separadas para classe, método e linha, em vez de concatená-las todas em uma única coluna.
- Agora você pode ordenar por nome de método clicando com o botão direito no cabeçalho do método ou selecionando o item de menu Sort By no menu de clique com o botão direito.
- Com a lista em árvore de resultados, as seguintes novas opções de menu de clique com o botão direito estão disponíveis: Expand All - expande todos os nós Collapse All - recolhe todos os nós Sort by Most Recent First - coloca os conjuntos de resultados mais recentes no topo da lista em vez de na parte inferior

> **Observação:** Os resultados abaixo de um nó de árvore não são preenchidos até que o nó seja expandido. Isso é feito para aumentar o desempenho se você tiver conjuntos de resultados grandes.

# GENDBC.PRG

O programa Gendbc.prg que gera programa usado para recriar um banco de dados foi atualizado com os seguintes aprimoramentos menores:
 - Suporte para novos tipos de campo Varchar, Varbinary e Blob
- Suporte para propriedades AllowSimultaneousFetch, RuleExpression e RuleText para visualizações

# Environment Manager Task Pane

O Environment Manager Task Pane foi aprimorado com os seguintes recursos:
 - Form and Formset Template Classes - agora você pode especificar classes de modelo para novos formulários e formsets com cada conjunto de ambiente. Esta configuração é especificada na Guia Forms, Caixa de diálogo Options .
- Field Mapping - você pode definir classes para usar quando arrastar e soltar um campo em um formulário com cada conjunto de ambiente. Esta configuração é especificada na Guia Field Mapping, Caixa de diálogo Options .
- Resource File - o Environment Manager agora suporta a configuração de um Resource File. Se não existir, o Environment Manager criará opcionalmente quando o ambiente for definido.
- O Environment Manager agora contém um novo conjunto de ambiente <default field mapping>. Este conjunto é criado na primeira vez que o Environment Manager é executado para que as configurações padrão originais da caixa de diálogo Options para Field Mapping e Form Template Classes possam ser salvas e restauradas posteriormente, se desejado.
- Para obter mais informações, consulte Environment Manager Task Pane .

# Data Explorer Task Pane

O Task Pane Manager inclui o novo Data Explorer Task Pane que permite visualizar e trabalhar com fontes de dados remotas, como bancos de dados SQL Server.

Para obter mais informações, consulte Data Explorer Task Pane.

# MemberData Editor

O novo MemberData Editor permite editar MemberData para suas classes. O MemberData Editor está disponível no menu Class quando o Class Designer está ativo. O MemberData Editor também é invocado silenciosamente quando você clica com o botão direito em um item na janela Properties e seleciona o item de menu Add to Favorites. O aplicativo MemberData Editor é especificado como um builder e pode ser alterado na tabela Builder.dbf localizada no diretório Wizards.

Para obter mais informações, consulte MemberData Editor e Extensibilidade MemberData.

# Novas Foundation Classes (FFC)

As seguintes são novas FoxPro Foundation classes adicionadas a esta versão do Visual FoxPro:
 - _REPORTLISTENER.VCX - um conjunto de classes principais que você pode usar ao criar report listeners personalizados.
- _FRXCURSOR.VCX - uma biblioteca de classes usada para trabalhar com arquivos de relatório (FRX).
- _GDIPLUS.VCX - um conjunto de classes que você pode usar para manipulação GDI+. Isso é destinado principalmente para uso ao criar classes de report listener personalizadas.

# Novos exemplos de solução

O Visual FoxPro 9.0 contém muitos novos exemplos que mostram os novos recursos do produto. Para ver uma lista desses exemplos, selecione o painel de tarefas Solution Samples no Task Pane Manager e expanda o nó New in Visual FoxPro 9.0.
