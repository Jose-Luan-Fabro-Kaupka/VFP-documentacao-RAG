# Incluindo arquivos de relatório para distribuição

Ao distribuir um aplicativo, você tem várias decisões a tomar sobre como implantar os relatórios que projetou para fornecer saída do aplicativo. Este tópico descreve opções para inclusão de tabelas de definição de relatório e etiqueta (.frx e .lbx) e os componentes distribuíveis do Sistema de Relatórios do Visual FoxPro.

# Distribuindo arquivos de relatório e etiqueta

Relatórios e etiquetas podem ser incluídos em seu projeto e compilados em seu aplicativo (arquivo .exe ou .app), ou podem ser entregues separadamente em disco.

> **Dica:** Você pode referenciar relatórios e etiquetas em seu projeto de aplicativo, para fácil referência durante o design do aplicativo, sem compilar os arquivos de relatório e etiqueta no arquivo de aplicativo compilado. Para obter mais informações, consulte Como: excluir arquivos de compilações .

A estratégia que você decidir usar geralmente depende de se deseja que os usuários finais tenham a capacidade de ajustar os relatórios e etiquetas. Se os relatórios e etiquetas estiverem em disco como arquivos separados, seu aplicativo pode fornecer recursos para os usuários finais personalizá-los, usando os comandos MODIFY REPORT e MODIFY LABEL.

> **Dica:** No Visual FoxPro 9, você pode oferecer aos usuários finais uma experiência de design personalizada e segura, aproveitando caixas de diálogo personalizadas do Report Builder e recursos como Proteção de relatório, ToolTips do Report Designer e Legendas em tempo de design. Para obter mais informações, consulte Definindo proteção para relatórios , Como: adicionar tooltips a controles de relatório e Como: adicionar legendas em tempo de design a controles de campo .

Você pode usar uma abordagem combinada, compilando os relatórios e etiquetas em seu aplicativo para servir como modelos de saída somente leitura, mas copiando-os para disco para modificações dos usuários finais. Esta abordagem tem a vantagem de garantir que você possa reverter para uma cópia "limpa" do arquivo de definição de relatório ou etiqueta original quando necessário.

> **Dica:** Usar um modelo incorporado também permite fazer alguns ajustes de última hora no relatório ou etiqueta antes de uma sessão de design do usuário final. Por exemplo, você poderia ajustar flags de proteção na cópia editável usando uma tabela de consulta de aplicativo para permissões de usuário. Você também poderia substituir os ToolTips para controles de relatório que usa para fins de desenvolvimento, com notas do desenvolvedor, por outro conjunto contendo instruções para o usuário final. Como você pode adicionar campos de extensão a tabelas de relatório e etiqueta, este ajuste programático em tempo de execução seria tão simples quanto abrir a tabela de relatório ou etiqueta com o comando USE, seguido de um comando como REPLACE ALL ORDER WITH <seu campo de extensão> . Para obter mais informações, consulte Compreendendo e estendendo a estrutura de relatório .

Em algumas circunstâncias, o Visual FoxPro permite que os comandos MODIFY REPORT e MODIFY LABEL sejam usados com os nomes de arquivos de relatório e etiqueta somente leitura compilados no aplicativo. Quando o usuário final do aplicativo salva o relatório ou etiqueta do designer, o Visual FoxPro salva a cópia em disco. Para esta estratégia funcionar, os arquivos de relatório e etiqueta devem estar na mesma pasta que o arquivo de projeto (.pjx) ou em uma pasta cujo nome o Visual FoxPro possa resolver em tempo de execução, relativo ao arquivo de aplicativo (.exe ou .app).

Por exemplo, suponha que seu projeto esteja em uma pasta chamada d:\app e o formulário de relatório que deseja incluir é d:\app\reports\my.frx em seu computador de desenvolvimento. Em tempo de execução, você instala o arquivo de aplicativo (.exe) em c:\programs\myapp. Se você criar uma subpasta reports, c:\programs\myapp\reports, pode usar o comando `MODIFY REPORT my.frx`. Quando o usuário escolhe salvar o relatório, o Visual FoxPro salva o relatório como c:\programs\myapp\reports\my.frx por padrão. No entanto, se c:\programs\myapp não tiver a subpasta, ocorre um erro no comando MODIFY REPORT.

Você pode verificar a disponibilidade da subpasta em tempo de execução e usar o Comando MD | MKDIR se necessário. Alternativamente, use os seguintes comandos, onde `lcDir` contém o nome de uma pasta de destino que você verificou anteriormente com o usuário.

```foxpro
SELECT * FROM my.frx INTO TABLE (lcDir + "my.frx")
MODIFY REPORT(lcDir + "my.frx")
```

Esta abordagem coloca o processo completamente sob seu controle. Permite configurar a pasta de destino para atender às necessidades do usuário em vez da estrutura de design do projeto.

> **Observação:** Ao distribuir relatórios, seja incorporados ou como arquivos externos, garanta que todos os arquivos adicionais necessários estejam disponíveis para seu aplicativo em tempo de execução. Por exemplo, se seu relatório referencia um arquivo de imagem, inclua o arquivo de imagem em seu aplicativo ou distribua o arquivo como um arquivo separado em disco. Garanta que o arquivo de imagem esteja no mesmo local na estrutura de compilação do seu projeto, ou na estrutura de pastas do seu aplicativo distribuído em disco, relativo ao arquivo de relatório, como estava quando você projetou o relatório. Caso contrário, o Visual FoxPro não encontrará o arquivo de imagem quando gerar o relatório. Se você optar por compilar relatórios em seu aplicativo, outros módulos compilados, como ReportOutput.app ou ReportBuilder.app, podem não conseguir localizar os arquivos dentro do seu módulo compilado. Você pode garantir que os componentes do sistema de relatórios encontrem seus arquivos compilando seus arquivos de origem em seu aplicativo, em vez de distribuí-los como aplicativos separados. A próxima seção discute suas opções para distribuir esses componentes.

# Distribuindo componentes do sistema de relatórios

Se você oferece aos usuários finais a oportunidade de modificar relatórios e etiquetas, deve distribuir o Report Builder Application, ou sua versão personalizada do Report Builder Application, para garantir que seus usuários tenham todas as vantagens de seus aprimoramentos do Report Designer.

Por padrão, o Visual FoxPro procura um arquivo com o nome ReportBuilder.app em HOME() ou no local de inicialização. Para um aplicativo executável (.exe), este local é sempre a pasta onde as bibliotecas de suporte em tempo de execução do Visual FoxPro estão instaladas, como C:\Program Files\Common Files\Microsoft Shared\VFP. Para obter mais informações, consulte Função HOME( ) . Se você incluir o módulo de mesclagem Microsoft Visual FoxPro 9 Report Applications com seus programas de instalação Setup do aplicativo, conforme descrito na próxima seção, o ReportBuilder.app padrão é instalado no local apropriado no disco do usuário.

> **Cuidado:** Instalar quaisquer outros aplicativos com os nomes ReportBuilder.app, ReportPreview.app e ReportOutput.app no local padrão das bibliotecas de suporte em tempo de execução não é recomendado, pois você pode instalar sobre os aplicativos padrão exigidos por outros aplicativos Visual FoxPro. Se desejar instalar versões personalizadas desses aplicativos no local padrão, use nomes de aplicativo diferentes e designe seus componentes de relatório preferidos por nome, em seu aplicativo, conforme descrito nesta seção.

Você pode usar a Variável de sistema _REPORTBUILDER em seu aplicativo, ou no arquivo de configuração (CONFIG.FPW) de seu aplicativo, para especificar um local diferente e um nome de arquivo diferente para seu Report Builder Application distribuído. Para obter mais informações, consulte Definindo opções de configuração na inicialização.

Ao implantar aplicativos, você tem a opção de compilar arquivos de componentes do Report Builder em seu aplicativo executável (.exe) em vez de distribuir o Report Builder Application como um arquivo autônomo. Para obter mais informações, consulte Como: especificar e distribuir ReportBuilder.App.

Para fornecer os recursos de saída aprimorados do Visual FoxPro 9 em seus aplicativos, usando objetos ReportListener e PreviewContainer, você também deve distribuir o Report Output Application (ReportOutput.app) e o Report Preview Application (ReportPreview.app) ou substitutos adequados. As técnicas para especificar os nomes e locais desses componentes são as mesmas para os três aplicativos de relatório. Para obter mais informações, consulte Como: especificar e distribuir ReportPreview.App e Como: especificar e distribuir componentes do Report Output Application.

> **Dica:** Você pode aproveitar as classes derivadas de ReportListener padrão usadas pelo Report Output Application e muitos dos recursos do Report Builder Application separadamente dos dois aplicativos, usando bibliotecas de classes Foundation Class contendo classes visuais idênticas. Para obter mais informações, consulte Foundation Classes ReportListener , Foundation Class FRX Cursor e Foundation Class FRX Device Helper .

# Distribuindo arquivos adicionais para relatórios e o Sistema de Relatórios do Visual FoxPro

O Visual FoxPro fornece módulos de mesclagem (arquivos .msm) para que você possa criar programas Setup distribuíveis para seus aplicativos e incluir todos os arquivos de suporte necessários. Para obter mais informações, consulte Walkthrough: criando um programa Setup de aplicativo Visual FoxPro usando InstallShield. A tabela a seguir lista os módulos de especial significado para aplicativos que usam os recursos de relatório do Visual FoxPro.

| Nome do arquivo do módulo de mesclagem | Título do módulo de mesclagem | Observações |
| --- | --- | --- |
| vfp9rptapps.msm | Visual FoxPro 9 Report Applications | Instala ReportBuilder.app, ReportOutput.app e ReportPreview.app em seus locais padrão para aplicativos executáveis. |
| msxml4sxs32.msm msxml4sys32.msm | MSXML 4.0 | Estes módulos são necessários para todas as instalações de aplicativos Visual FoxPro e são usados extensivamente pelos Report Applications padrão. |
| GDIPlus.msm | Microsoft GDI+ | Este módulo é necessário para todas as instalações de aplicativos Visual FoxPro e é usado extensivamente pelo Sistema de Relatórios no modo de relatório assistido por objetos. |
