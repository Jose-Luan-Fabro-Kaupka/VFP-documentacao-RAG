# Como: especificar uma tabela de registro de saída de relatório alternativa

O Report Output Application padrão suporta uma tabela de registro na qual você pode especificar as classes derivadas de ReportListener para diferentes tipos de resultados de saída. Este tópico descreve mecanismos disponíveis para:
 - Criar uma nova tabela de registro.
- Informar ao Report Output Application para usar esta tabela em tempo de execução.
- Descobrir qual tabela de registro o Report Output Application está usando atualmente.

> **Observação:** Parte do código neste tópico usa a variável de sistema _REPORTOUTPUT para invocar ReportOutput.app. _REPORTOUTPUT pode conter o nome de um Report Output Application diferente em seu ambiente. Neste caso, substitua HOME() + ReportOutput.app, ou código semelhante, para invocar o Report Output Application padrão. Onde as instruções designam o nome e a posição de uma tabela de registro personalizada, substitua seu nome e localização preferidos.

Para obter mais informações sobre o uso da tabela de registro com suas próprias classes e extensões de saída, consulte How to: Register Custom ReportListeners and Custom OutputTypes in the Report Output Registry Table.

Para obter mais informações sobre o formato da tabela de registro, consulte Understanding the Report Output Application.

# Criando uma tabela de registro do Report Output

Você pode usar ReportOutput.app ou uma ReportListener Foundation Class para criar a tabela, porque elas usam o mesmo formato de tabela de configuração.

> **Observação:** Esses dois métodos podem gerar registros de amostra e configuração diferentes na tabela, e podem incluir potencialmente conjuntos diferentes de índices. Se você compartilhar uma tabela de registro entre diferentes componentes de relatório, cada componente que usa a tabela verifica o conteúdo da tabela em relação aos seus próprios requisitos. Se necessário, cada componente é capaz de adicionar seus próprios registros e índices dinamicamente.

### Para criar uma nova tabela de registro do Report Output usando ReportOutput.app
- Na janela Command Window ou em um programa (.prg), use a seguinte linha de código: * #DEFINE OUTPUTAPP_CONFIG_WRITE -100 DO (_REPORTOUTPUT) WITH -100
- O Report Output Application cria uma tabela chamada OutputConfig.DBF e arquivos associados memo (.fpt) e de índice de estrutura (.cdx) no mesmo local que ReportOutput.App (normalmente, o diretório principal ou HOME() do Visual FoxPro).
- O Report Output Application apresenta um BROWSE desta nova tabela, para que você possa verificar o conteúdo. O conteúdo incluirá os registros exigidos pela ReportListener XML Foundation Class, além de alguns registros excluídos que servem como exemplos de diferentes tipos de registros de registro
- Você vê um registro excluído para debugListener, a ReportListener Debug Foundation Class. Este registro mostra como é um registro de registro ReportListener, de acordo com os requisitos do Report Output Application.
- Você também vê registros excluídos para dois registros com valores ObjType de 1000. Este valor está no intervalo reservado para uso por utilityReportListener, a ReportListener Utility and File-handling Foundation Class. Um registro mostra como criar um registro de configuração para definir uma propriedade de classe e o outro mostra como criar um registro de configuração para invocar um método de classe. Para obter mais informações sobre como esta classe e seus descendentes usam registros de configuração, consulte ReportListener Utility and File-handling Foundation Class.
- Você pode renomear os três arquivos OutputConfig.* e colocá-los em outro local do disco para uso posterior.

### Para criar uma nova tabela de registro do Report Output usando uma classe Foundation ReportListener
- Crie uma instância da ReportListener Utility and File-handling Foundation Class, ou de qualquer uma das ReportListener Foundation Classes derivadas dela. Você pode criar uma instância desta classe usando a biblioteca de classes (vcx) integrada em ReportOutput.app, ou pode criar uma instância da classe usando a cópia da biblioteca de classes disponível na pasta FFC do Visual FoxPro. * "borrow" a copy directly from ReportOutput.App: #DEFINE CONFIG_REPORTLISTENER_CLASS "utilityReportListener" oRL = NEWOBJECT(CONFIG_REPORTLISTENER_CLASS, ; "listener.vcx", ; _REPORTOUTPUT) * - OR - * access the Foundation Class library directly: #DEFINE FFC_HOME HOME()+"FFC\" oRL = NEWOBJECT(CONFIG_REPORTLISTENER_CLASS, ; FFC_HOME + "_reportListener.vcx") Dica Todas as ReportListener Foundation Classes que fornecem saída baseada em arquivo, como a ReportListener HTML Foundation Class, derivam de ReportListener Utility and File-handling Foundation Class. Algumas dessas classes exigem uma tabela de registro. Qualquer classe que exija uma tabela verifica a disponibilidade da tabela quando você a inicializa. Se a tabela não estiver disponível, ela cria uma cópia da tabela, em seu local padrão, durante os procedimentos de inicialização. Para obter mais informações, consulte ReportListener Utility and File-handling Foundation Class.
- Solicite uma nova tabela de configuração da instância ReportListener. Você pode especificar seu nome e localização: * if SAFETY is ON, prompt for overwrite if the file exists: oRL.createConfigTable("c:\temp\myconfig.dbf") *- OR - * use the second parameter to explicitly overwrite: oRL.createConfigTable("c:\temp\myconfig.dbf", .T.) Dica As classes respeitam a configuração de SAFETY em seu ambiente, pois solicitarão confirmação para sobrescrever a tabela se SET SAFETY estiver ON e se você não especificar o segundo parâmetro do método createConfigTable como True ( .T. ). Para obter mais informações, consulte SET SAFETY Command. Se você recusar sobrescrever a tabela quando solicitado, as classes ainda executam algumas ações; investigam a tabela para garantir que os índices necessários estejam disponíveis e adicionam quaisquer registros de que precisem à tabela.

# Atribuindo sua própria tabela de registro ao Report Output Application

Na seção anterior, você viu que, para criar uma tabela de registro, você pode invocar ReportOutput.app usando um número negativo (`-100`) como o primeiro parâmetro enviado ao programa. ReportOutput.app entende valores negativos neste parâmetro como instruções especiais para executar tarefas de manutenção, em vez de instruções para executar sua tarefa normal de fornecer referências ReportListener.

ReportOutput.app reserva um segundo valor, `-200`, para permitir que você designe o nome e a localização da sua tabela de registro, conforme mostrado abaixo.

### Para designar sua tabela de registro personalizada para uso do ReportOutput.app
- Execute a seguinte linha de código, substituindo o nome e o caminho da sua tabela de registro personalizada: * #DEFINE OUTPUTAPP_CONFIG_READ -200 DO (_REPORTOUTPUT) WITH -200,"c:\temp\myconfig.dbf"

# Verificando a tabela de registro atual do Report Output Application

Em tempo de execução, ReportOutput.app mantém uma coleção de referências de objetos ReportListener. Para obter mais informações, consulte How to: Use the Report Output Application's Reference Collection. ReportOutput.app usa um membro especial desta coleção para armazenar o nome de sua tabela de registro. Você pode usar a coleção de referências para descobrir qual tabela de registro está em uso atualmente pelo Report Output Application. Você também pode verificar o nome da tabela de registro atual chamando o Report Output Application diretamente.

### Para verificar o nome da tabela de registro atual do Report Output Application usando a coleção de referências
- Se você emitiu um comando CLEAR ALL ou RELEASE da variável pública da coleção de referências depois da última vez que invocou com sucesso o Report Output Application, ou se ainda não o invocou nesta sessão do Visual FoxPro, a coleção pode ainda não existir. Verifique se a coleção existe e então verifique o valor do membro apropriado da coleção #DEFINE OUTPUTAPP_CONFIG_READ -200 IF VARTYPE(_oReportOutput) = "O" lcFile = _oReportOutput[TRANSFORM(OUTPUTAPP_CONFIG_READ)] ENDIF
- Examine os resultados que você recebeu na variável lcFile. Se for um nome de arquivo totalmente qualificado (com caminho), o Report Output Application está usando uma tabela de registro em disco. Se lcfile não incluir um caminho, o Report Output Application está usando uma tabela de registro integrada em um aplicativo (.app ou .exe).

### Para verificar o nome da tabela de registro atual do Report Output Application chamando o Report Output Application
- Inicialize uma variável para armazenar o nome do arquivo de registro LOCAL lcFile
- Chame o Report Output Application com o valor de configuração especial que você usou anteriormente, usando a variável que inicializou como seu segundo parâmetro. Isso é semelhante a como você chama o Report Output Application para receber uma referência a um ReportListener: #DEFINE OUTPUTAPP_CONFIG_READ -200 DO (_REPORTOUTPUT) WITH OUTPUTAPP_CONFIG_READ, lcFile
- Examine os resultados que você recebeu na variável lcFile. Se for um nome de arquivo totalmente qualificado (com caminho), o Report Output Application está usando uma tabela de registro em disco. Se lcfile não incluir um caminho, o Report Output Application está usando uma tabela de registro integrada em um aplicativo (.app ou .exe). Observação A coleção de referências é criada automaticamente quando você usa esta sintaxe.
