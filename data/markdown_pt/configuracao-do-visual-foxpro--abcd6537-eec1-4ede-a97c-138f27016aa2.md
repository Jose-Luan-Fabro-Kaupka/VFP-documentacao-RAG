# Configuração do Visual FoxPro

A configuração do Visual FoxPro determina como sua cópia do Visual FoxPro aparece e se comporta. Por exemplo, você pode estabelecer os locais padrão dos arquivos usados com o Visual FoxPro, como seu código-fonte aparece em uma janela de edição e o formato de datas e horas.

Você pode fazer alterações na configuração do Visual FoxPro que existem apenas para a sessão atual (temporárias) ou especificá-las como configurações padrão para a próxima vez que iniciar o Visual FoxPro (permanentes). Se as configurações são temporárias, elas são armazenadas na memória e descartadas quando você sai do Visual FoxPro.

Se você fizer configurações permanentes, elas são armazenadas no registro do Microsoft Windows ou no arquivo de recursos do Visual FoxPro. O registro do Windows é um banco de dados que armazena informações de configuração sobre o sistema operacional, todos os aplicativos Windows, OLE e componentes opcionais como ODBC. Por exemplo, o registro é onde o Windows armazena as associações entre extensões de nome de arquivo e aplicativos, de modo que, ao clicar em um nome de arquivo, o Windows pode iniciar ou ativar o aplicativo apropriado.

Para um exemplo de como alterar o registro, você pode examinar Registry.prg no diretório \Samples\Classes, que contém diversos métodos baseados em chamadas de API do Windows e permite manipular o registro do Windows.

Da mesma forma, o Visual FoxPro armazena suas informações de configuração específicas do aplicativo no registro. Ao iniciar o Visual FoxPro, o programa lê as informações de configuração no registro e define a configuração conforme essas configurações. Depois de ler o registro, o Visual FoxPro também verifica se existe um arquivo de configuração, que é um arquivo de texto no qual você pode armazenar configurações para substituir os padrões armazenados no registro. Depois que o Visual FoxPro foi iniciado, você pode fazer configurações adicionais usando a Caixa de diálogo Options (Visual FoxPro) ou comandos SET. Para obter mais informações, consulte Como: visualizar e alterar configurações de ambiente.

> **Observação:** A versão de tempo de execução do Visual FoxPro não lê o registro do Windows na inicialização, pois as configurações do registro são projetadas principalmente para configurar o ambiente de desenvolvimento. Se você pretende distribuir seus aplicativos Visual FoxPro usando uma biblioteca de tempo de execução, pode estabelecer configurações de duas maneiras: com um arquivo de configuração ou com um programa que manipula o registro do Windows no computador do usuário.

O Visual FoxPro também mantém um arquivo de recursos, Foxuser.dbf, que armazena informações sobre o estado atual do programa quando você sai. Por exemplo, o arquivo de recursos contém informações sobre a localização e o tamanho da janela Command, macros de teclado atuais, as barras de ferramentas exibidas e assim por diante. O arquivo Foxuser.dbf é uma tabela Visual FoxPro comum, que você pode ler e alterar conforme necessário para seu aplicativo.

> **Dica:** Se os dados no arquivo Foxuser.dbf ficarem corrompidos ou inválidos, isso pode fazer o Visual FoxPro se comportar de forma errática. Se você não armazena nada manualmente na tabela, por exemplo macros de teclado, excluir a tabela pode ajudar.
