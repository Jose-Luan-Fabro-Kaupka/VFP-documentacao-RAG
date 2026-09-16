# Guia às Melhorias de Relatórios

O Sistema de Relatórios do Visual FoxPro 9 passou por uma revisão completa. Este tópico descreve os contornos amplos das alterações e fornece informações sobre onde procurar detalhes.

As seguintes áreas principais de aprimoramentos ao Sistema de Relatórios são cobertas em seções deste tópico.
 **Aprimoramentos em tempo de design.**
Vários recursos e alterações tornam o design de relatórios no Visual FoxPro melhor para você e seus usuários finais. O Report Builder Application reorganiza sua experiência de design pronta para uso. Se deseja personalizar o processo de design, as caixas de diálogo do Report Builder e os eventos do Report Designer estão totalmente expostos para isso.
**Várias bandas de detalhe.**
Você pode lidar com várias tabelas filhas e relações de dados de forma mais flexível no Report Designer revisado. Ao executar relatórios com várias bandas de detalhe, pode aproveitar as novas bandas, com cabeçalhos e rodapés de detalhe associados, tanto para apresentação adequada dessas relações quanto para cálculos mais capazes.
**Processamento de relatório em tempo de execução assistido por objetos.**
Um sistema de saída totalmente reconstruído, incluindo uma nova classe base, altera a forma como o Visual FoxPro fornece arquivos de relatório e etiqueta em tempo de execução. Relatórios assistidos por objetos fornecem saída de melhor qualidade, novos tipos de saída e uma arquitetura aberta baseada em uma nova classe base do Visual FoxPro, o ReportListener. Uma interface programável de Visualização de Relatório interage com ReportListeners para dar controle total sobre a experiência de visualização de relatório. O Report Preview Application fornece recursos de visualização aprimorados prontos para uso.
**Melhorias em impressão, renderização e tratamento de conjuntos de caracteres.**
O Visual FoxPro 9 faz melhor uso dos recursos de impressão do sistema operacional e do subsistema de renderização GDI+. Também trata vários locais e conjuntos de caracteres melhor que versões anteriores. Essas alterações são demonstradas no Sistema de Relatórios e são acessíveis para uso em código personalizado durante o design e o processamento de relatórios em tempo de execução.
**Uso extensível de arquivos de definição de relatório e etiqueta (tabelas .frx e .lbx).**
O Visual FoxPro 9 trata seus relatórios e etiquetas existentes sem modificação, permitindo adicionar novos recursos e comportamentos a esses relatórios facilmente. Esta estratégia de migração compatível com versões anteriores, porém voltada para o futuro, é possibilitada pelo tratamento recém-flexível da estrutura de tabelas .frx e .lbx pelo Sistema de Relatórios.

# Aprimoramentos em Tempo de Design

Numerosas alterações no Sistema de Relatórios ajudam a aprimorar a experiência em tempo de design para desenvolvedores e usuários finais. Esta seção direciona você a informações sobre melhorias em tempo de design.

### Ganchos de Eventos do Report Designer e o Report Builder Application

O Report Designer agora oferece Report Builder Hooks, que permitem interceptar eventos ocorrendo durante uma sessão de design de relatório ou etiqueta para substituir e estender a atividade do designer. O Report Builder Application padrão substitui muitas das caixas de diálogo de relatório padrão por novas escritas em código Visual FoxPro. Componentes do Report Builder Application são expostos como Visual FoxPro Foundation Classes para seu uso.

| Para saber sobre: | Leia: |
| --- | --- |
| Report Builder Hooks | Understanding Report Builder Events |
| Como o Report Builder Application usa Report Builder Hooks | How to: Configure the Report Builder's Event Handling |
| Como especificar e distribuir um Report Builder com suas aplicações | _REPORTBUILDER System Variable How to: Specify and Distribute ReportBuilder.App Including Report Files for Distribution |
| Usando algoritmos do Report Builder em seu código | FRX Cursor Foundation Class FRX Device Helper Foundation Class |

### Proteção para Sessões de Design de Usuários Finais e Outras Oportunidades de Personalização em Tempo de Design

Você pode permitir que usuários finais MODIFY e CREATE relatórios e etiquetas, definindo limitações sobre o que podem fazer na interface do Report Designer, usando a nova palavra-chave PROTECTED. A proteção está disponível individualmente por objeto e globalmente para o relatório. Você pode alterar o que usuários finais veem na superfície de layout do designer, de expressões complexas a legendas simples ou dados de amostra, trabalhando no modo de design PROTECTED, usando Design-Time Captions. Você também pode fornecer instruções úteis, tanto para o modo PROTECTED quanto para o modo de design padrão, especificando Tooltips para controles de relatório.

| Para saber sobre: | Leia: |
| --- | --- |
| Usando a palavra-chave PROTECTED | MODIFY REPORT Command MODIFY LABEL Command |
| Definindo Proteção no Report ou Label Designer, e o que as configurações de Proteção fazem | Setting Protection for Reports |
| Configurações de proteção expostas nas caixas de diálogo Report or Label Dialog quando você usa o Report Builder Application padrão | Protection Tab, Report Control Properties Dialog Box (Report Builder) Protection Tab, Report Properties Dialog Box (Report Builder) Protection Tab, Report Band Properties Dialog Box (Report Builder) |
| Design-Time Captions | How to: Add Design-time Captions to Field Controls |
| ToolTips para Controles de Relatório | How to: Add Tooltips to Report Controls |

### Uso Aprimorado do Data Environment em Relatórios

Você pode salvar o Data Environment que projetou para um Relatório ou Etiqueta como uma classe visual. Você pode carregar um Data Environment em um design de Relatório ou Etiqueta a partir de uma classe visual ou de um relatório ou etiqueta salvo anteriormente.

| Para saber sobre: | Leia: |
| --- | --- |
| Salvando um Data Environment de Relatório | How to: Save Report Data Environments as Classes |
| Carregando um Data Environment de Relatório | Data Environment Tab, Report Properties Dialog Box (Report Builder) How to: Load Data Environments for Reports |

### Melhorias Diversas de Design

Houve numerosos aprimoramentos aos Report e Label Designers. Alguns recursos são alterações sutis para tornar sessões de design mais eficientes e agradáveis, e outros melhoram suas opções para a saída resultante.

| Para saber sobre: | Leia: |
| --- | --- |
| Melhorias ao Interactive Development Environment (IDE) de Relatório e Etiqueta, como: Barra de ferramentas aprimorada do Report Designer e acesso mais fácil à Report Designer Toolbar no menu View Novo menu de contexto global Report Properties Melhorias e adições aos menus de contexto existentes Menu Report revisado e ampliado | Report Layout and Design |
| Alterações nas opções globais de design de relatório e etiqueta | Reports Tab, Options Dialog Box |
| Usando a nova propriedade PictureVal do controle Image para especificar imagens em relatórios | How to: Add Pictures to Reports PictureVal Property |
| Novos caracteres de template picture ( U e W ) e instruções de formato atualizadas ( Z , agora suportado para dados date e datetime), úteis em relatórios e etiquetas | Format Expressions for Field Controls InputMask Property Format Property |
| Recebendo saída HTML aprimorada, que aproveita aprimoramentos de relatório em tempo de execução, ao escolher Save As HTML… durante o design de um relatório ou etiqueta | How to: Generate Output for Reports Tip Outros componentes Visual FoxPro que invocam Genhtml.prg , a implementação padrão _GENHTML, compartilham automaticamente a saída HTML aprimorada, embora esses componentes não tenham mudado. Estes incluem o FRX to HTML Foundation Class e o Output Object Foundation Class . |
| Propriedades de documento de relatório permitem incluir informações sobre o relatório no relatório. Propriedades de documento são incluídas como elementos e atributos na saída XML e HTML. | How to: Add Document Properties to a Report Document Properties Tab, Report Properties Dialog Box (Report Builder) |
| Você pode alterar dinamicamente as propriedades dos controles de relatório em tempo de execução baseado na avaliação de uma expressão. | How to: Dynamically Format Report Controls Dynamics Tab, Report Control Properties Dialog Box (Report Builder) |

# Várias Bandas de Detalhe

O Report Engine agora pode percorrer um escopo de registros várias vezes. Os registros podem representar conjuntos relacionados de linhas de detalhe em tabelas filhas, ou podem ser várias passagens por uma única tabela. Essas múltiplas passagens por um escopo de registros são representadas como várias bandas de detalhe.

Bandas de detalhe podem ter seus próprios cabeçalhos e rodapés, seu próprio código onEntry e onExit associado, e suas próprias variáveis de relatório associadas. Cada banda de detalhe pode ser explicitamente associada a um alias de destino separado, permitindo controlar o número de entradas em cada banda de detalhe separadamente para tabelas relacionadas.

Relatórios com várias bandas de detalhe fornecem muitas novas formas de representar dados em relatórios e etiquetas, e novas formas de calcular ou resumir dados, conforme você percorre um escopo de registros.

| Para saber sobre: | Leia: |
| --- | --- |
| Projetando relatórios e etiquetas com várias bandas de detalhe e seus cabeçalhos e rodapés associados | Optional Bands Dialog Box Report Band Properties Dialog Box Band Tab, Report Band Properties Dialog Box (Report Builder) |
| Lidando com várias tabelas relacionadas em dados de relatório e etiqueta | Controlling Data in Reports Working with Related Tables using Multiple Detail Bands in Reports |
| Associando variáveis de relatório com bandas de detalhe | How to: Reset Report Variables |
| Comparando vários grupos e várias bandas de detalhe | Report Bands |

# Processamento de Relatório em Tempo de Execução Assistido por Objetos

O Visual FoxPro 9 tem um novo método assistido por objetos de gerar saída de relatórios e etiquetas. Você pode usar seus layouts de relatório e etiqueta existentes no modo assistido por objetos, para:
 - Gerar vários tipos de saída durante uma execução de relatório.
- Conectar vários relatórios como parte de um resultado de saída.
- Melhorar a qualidade da saída de relatório tradicional.
- Ajustar dinamicamente o conteúdo de um relatório enquanto o processa.
- Fornecer novos tipos de saída não disponíveis em versões anteriores do Visual FoxPro.

Esta seção cobre o conjunto de aprimoramentos em tempo de execução que trabalham juntos para suportar o modo de relatório assistido por objetos.

### Arquitetura Assistida por Objetos e Classe Base ReportListener

A nova classe base ReportListener e aprimoramentos de linguagem de suporte são o coração dos aprimoramentos de relatório em tempo de execução.

| Para saber sobre: | Leia: |
| --- | --- |
| Fundamentos da arquitetura, como seus componentes trabalham juntos e o que acontece durante uma execução de relatório assistida por objetos | Understanding Visual FoxPro Object-Assisted Reporting |
| A classe base ReportListener e seus membros | ReportListener Object ReportListener Object Properties, Methods, and Events |
| Invocando o modo de relatório assistido por objetos automaticamente | SET REPORTBEHAVIOR Command _REPORTOUTPUT System Variable Reports Tab, Options Dialog Box |
| Invocando o modo de relatório assistido por objetos explicitamente com comandos Visual FoxPro | REPORT FORM Command LABEL Command |
| Depuração e tratamento de erros em execuções de relatório assistidas por objetos | Handling Errors During Report Runs |

### API de Visualização de Relatório e o Report Preview Application

O modo de relatório assistido por objetos do Visual FoxPro 9 dá controle completo sobre visualizações de relatório e etiqueta.

| Para saber sobre: | Leia: |
| --- | --- |
| Como a visualização assistida por objetos funciona | The Preview Container API Creating a Custom Preview Container |
| O Report Preview Application padrão | Leveraging the Default Preview Container |
| Como especificar e distribuir componentes Report Preview com suas aplicações | _REPORTPREVIEW System Variable How to: Specify and Distribute ReportPreview.App Including Report Files for Distribution |

### Novos Tipos de Saída e o Conjunto de Componentes Report Output

Como você pode fazer subclasse de ReportListener, pode criar novos tipos de saída. O Visual FoxPro 9 fornece um Report Output Application para conectar subclasses ReportListener com tipos de saída, bem como classes derivadas de ReportListener com capacidades de saída aprimoradas.

| Para saber sobre: | Leia: |
| --- | --- |
| Requisitos para Report Output Application e como o Visual FoxPro usa Report Output Applications | _REPORTOUTPUT System Variable |
| Recursos do Report Output Application padrão | Understanding the Report Output Application |
| Especificando manipuladores de saída personalizados usando o Report Output Application padrão | How to: Specify an Alternate Report Output Registry Table How to: Register Custom ReportListeners and Custom OutputTypes in the Report Output Registry Table Considerations for Creating New Report Output Types |
| Entendendo e configurando as Visual FoxPro Foundation Classes fornecendo comportamento ReportListener padrão para visualização e impressão assistidas por objetos | ReportListener User Feedback Foundation Class |
| Entendendo e configurando as Visual FoxPro Foundation Classes responsáveis pela saída XML e HTML padrão | ReportListener XML Foundation Class ReportListener HTML Foundation Class |
| Aproveitando o conjunto completo de Report Output Foundation Classes suportadas e o formato VFP Report Output XML | ReportListener Foundation Classes Using VFP Report Output XML |
| Como especificar e distribuir componentes Report Output com suas aplicações | How to: Specify and Distribute Report Output Application Components Including Report Files for Distribution |

### Estratégias de Migração e Alterações na Renderização de Saída

Você pode usar as alterações em tempo de design para melhorar todos os relatórios e etiquetas, seja escolhendo o modo de relatório compatível com versões anteriores ou assistido por objetos em tempo de execução.

Ao avaliar se deve mudar para o modo de relatório assistido por objetos em tempo de execução, considere primeiro os itens na lista Reporting de Important Changes in the Changes in Functionality for the Current Release topic, alguns dos quais são específicos para este novo método de criar saída. O tópico inclui uma tabela de diferenças menores entre saída de relatório compatível com versões anteriores e assistida por objetos. Você pode examinar quais efeitos essas alterações podem ter em relatórios existentes individuais e usar as recomendações na tabela para abordá-las. Você encontrará detalhes adicionais no tópico Using GDI+ in Reports.

Depois de experimentar com seus relatórios atuais, pode decidir sobre uma estratégia de migração para saída:
 - Você pode mudar aplicações para usar o modo de relatório assistido por objetos completamente, usando o comando SET REPORTBEHAVIOR 90 .
- Você pode usar SET REPORTBEHAVIOR 90 mas preceder comandos REPORT FORM específicos para relatórios com problemas de formatação com SET REPORTBEHAVIOR 80 , retornando sua aplicação ao modo assistido por objetos depois.
- Você pode usar o modo assistido por objetos o tempo todo, mas ajustar o comportamento de suas classes derivadas de ReportListener para atender necessidades específicas. Por exemplo, você poderia alterar a configuração padrão da DynamicLineHeight Property do ReportListener para False ( .F. ).
- Você pode deixar SET REPORTBEHAVIOR em sua configuração padrão de 80 , e adicionar uma cláusula OBJECT explícita a relatórios específicos quando tiver oportunidade, conforme avalia e ajusta layouts de relatório e etiqueta individuais.

# Melhorias em Impressão, Renderização e Tratamento de Conjuntos de Caracteres

Alterações gerais no uso do Visual FoxPro dos recursos de impressão, renderização e tratamento de fontes do Windows suportam as melhorias na saída do Sistema de Relatórios. Essas alterações aprimoram sua capacidade de suportar várias impressoras e vários idiomas em relatórios.

| Para saber sobre: | Leia: |
| --- | --- |
| Recursos GDI+ e seu impacto na saída nativa do Visual FoxPro | Using GDI+ in Reports |
| Aprimoramentos de relatório Visual FoxPro que permitem que seu código use GDI+ no modo de relatório assistido por objetos, e Visual FoxPro Foundation Classes para começar | GDIPlusGraphics Property Render Method GDI Plus API Wrapper Foundation Classes |
| Fazendo uso completo de vários conjuntos de caracteres, ou scripts de idioma, em relatórios, para elementos individuais de layout de relatório, para padrões de relatório ou globalmente no Visual FoxPro | GETFONT( ) Function Style Tab, Report Control Properties Dialog Box (Report Builder) How to: Change Page Settings for Reports Reports Tab, Options Dialog Box Reporting Features for International Applications |
| Alterações nas caixas de diálogo de configuração de página no Visual FoxPro, melhorias no acesso programático a elas, e fornecimento de substituições às configurações Printer Environment em arquivos de relatório e etiqueta | SYS(1037) - Page Setup Dialog Box |
| Recebendo informações aprimoradas sobre as impressoras instaladas do usuário | APRINTERS( ) Function |
| Limitando uma lista de fontes às apropriadas para o usuário da impressora | GETFONT( ) Function |

# Uso Extensível de Arquivos de Definição de Relatório e Etiqueta

Por baixo de todas as alterações ao Sistema de Relatórios do Visual FoxPro, o Report Designer e Report Engine tratam suas definições de relatório e etiqueta usando as mesmas estruturas de arquivo .frx e .lbx que nas versões anteriores. Eles alteram a forma como usam certos campos, sem tornar esses relatórios e etiquetas inválidos em versões anteriores, e também permitem estender seu uso de campos existentes ou adicionar campos personalizados.

> **Dica:** Esta alteração é crítica para sua capacidade de criar extensões dos novos recursos de relatório. Por exemplo, você pode armazenar dois conjuntos de ToolTips em dois campos de extensão de relatório, um conjunto para uso por desenvolvedores e outro para usuários finais. Em uma extensão do Report Builder, você poderia avaliar se o Designer estava trabalhando no modo protegido ou padrão, e substituir o conjunto real de ToolTips do campo de extensão apropriado. Em versões anteriores, você não podia adicionar campos à estrutura de relatório ou etiqueta; o Designer e Engine considerariam a tabela inválida. Você também não podia adicionar conteúdo personalizado com segurança a campos padrão não utilizados em vários registros de relatório e etiqueta, porque o Report Designer removia tal conteúdo.

O Visual FoxPro 9 fornece uma tabela FILESPEC revisada para arquivos de relatório e etiqueta, com informações extensas sobre o uso de cada coluna em versões anteriores, bem como aprimoramentos atuais.

O Visual FoxPro 9 também estabelece um novo formato de metadados estruturado para uso com relatórios. Este formato é um esquema de documento XML compartilhado com o XML MemberData do Class Designer.

O formato de documento XML permite empacotar informações de relatório personalizadas em um único campo de relatório ou etiqueta. O Report Builder Application padrão facilita adicionar Report XML MemberData a registros de relatório e etiqueta.

| Para saber sobre: | Leia: |
| --- | --- |
| Como o Visual FoxPro usa tabelas .frx e .lbx, e como estender essas estruturas | Understanding and Extending Report Structure |
| Como encontrar e exibir o conteúdo da tabela FILESPEC revisada, 60FRX.dbf | Table Structures of Table Files (.dbc, .frx, .lbx, .mnx, .pjx, .scx, .vcx) |
| Como você pode editar os dados XML usando o Report Builder Application | How to: Assign Structured Metadata to Report Controls |
| Como você pode usar Report XML MemberData | Report XML MemberData Extensions |
| O esquema de documento MemberData compartilhado | MemberData Extensibility |

# Consulte também
- Data and XML Feature Enhancements
- SQL Language Improvements
- Class Enhancements
- Language Enhancements
- Interactive Development Environment (IDE) Enhancements
