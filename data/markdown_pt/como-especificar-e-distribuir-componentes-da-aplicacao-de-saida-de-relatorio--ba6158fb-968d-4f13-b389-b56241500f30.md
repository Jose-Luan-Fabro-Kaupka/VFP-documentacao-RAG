# Como: especificar e distribuir componentes da aplicação de saída de relatório

Ao escrever e distribuir aplicações Visual FoxPro, você pode distribuir ReportOutput.app ou seus arquivos de componentes como parte de suas aplicações. Neste tópico, você aprende como:
 - Distribuir o ReportOutput.app padrão com suas aplicações com instruções apropriadas para usar a aplicação e uma tabela de registro acompanhante.
- Ajustar os padrões da tabela de registro no ReportOutput.app.
- Integrar a tabela de registro da Report Output Application e outros componentes da Report Output Application em suas aplicações sem distribuir ReportOutput.app.

# Usando uma tabela de registro não padrão em uma aplicação

Se você distribuir ReportOutput.App como um arquivo separado de sua aplicação e planejar distribuir a tabela de registro externamente, a tabela pode ter qualquer nome.

### Para incluir código designando uma tabela de registro com nome não padrão para o ReportOutput.app padrão
- Crie uma nova tabela de registro em disco. Para obter mais informações sobre como criar a tabela, consulte Como: especificar uma tabela de registro de saída de relatório alternativa.
- Edite a tabela com registros adequados para sua aplicação. Para obter mais informações, consulte Como: registrar ReportListeners personalizados e OutputTypes personalizados na tabela de registro de saída de relatório.
- Armazene o nome e a localização em que você está distribuindo ReportOutput.app na variável de sistema _REPORTOUTPUT, no arquivo CONFIG.FPW de sua aplicação ou em seu código de configuração. Para obter mais informações, consulte Definindo opções de configuração na inicialização. _ReportOutput = <nome e localização do arquivo ReportOutput.app>
- Inclua código semelhante ao seguinte durante o código de configuração em sua aplicação: #DEFINE OUTPUTAPP_CONFIG_READ -200 DO (_REPORTOUTPUT) with OUTPUTAPP_CONFIG_READ, ; <nome e localização do arquivo da tabela de registro>

# Alterando as informações padrão da tabela de registro do ReportOutput.app

Você pode distribuir uma cópia recompilada do ReportOutput.app com nomes de tabela de registro padrão diferentes para adequar-se à sua aplicação.

### Para recompilar ReportOutput.app com nomes de arquivo de registro padrão diferentes
- Expanda a subpasta ReportOutput no arquivo zip localizado na pasta Tools\Xsource do Visual FoxPro. Para obter mais informações sobre Xsource, consulte Pasta XSource.
- Navegue até a pasta em que você expandiu os arquivos de origem do componente ReportOutput. Modifique o arquivo ReportOutput.H (header). CD <sua pasta de origem> MODIFY COMMAND ReportOutput.H
- Localize as duas linhas de código a seguir no arquivo header: #DEFINE OUTPUTAPP_INTERNALDBF "_ReportOutputConfig" #DEFINE OUTPUTAPP_EXTERNALDBF "OutputConfig"
- Edite o valor "OutputConfig", substituindo-o pelo nome da tabela (.dbf) que deseja que sua aplicação use como valor padrão para localizar a tabela em disco. Edite o valor "_ReportOutputConfig", substituindo-o pelo nome da tabela que deseja que sua aplicação use como valor padrão para localizar a tabela incorporada em sua aplicação, se ela não localizar primeiro uma tabela com o nome padrão em disco.
- Salve suas alterações.
- Reconstrua o arquivo ReportOutput.App, certificando-se de usar a opção RECOMPILE: BUILD APPLICATION ReportOutput FROM ReportOutput RECOMPILE
- Se você alterou o valor em OUTPUTAPP_INTERNALDBF, o processo de build deve incorporar automaticamente a tabela que você especificou e criar a referência apropriada em seu projeto. Localize a tabela para o Project Manager, durante o processo de build, se ele solicitar que você encontre a tabela.
- Armazene o nome e a localização do seu novo ReportOutput.app na variável de sistema _REPORTOUTPUT, no arquivo CONFIG.FPW de sua aplicação ou em seu código de configuração. Para obter mais informações, consulte Definindo opções de configuração na inicialização. _ReportOutput = <nome e localização do arquivo ReportOutput.app>
- Distribua o novo arquivo ReportOutput.App com suas aplicações. Inclua uma tabela de registro apropriada para corresponder ao nome de arquivo que você escolheu, incorporada na aplicação ou em disco.

# Incorporando componentes da Report Output Application diretamente em sua aplicação

Se você distribuir componentes da Report Output Application em seu arquivo de aplicação (.app ou .exe), a tabela de registro pode ter qualquer nome, quer você distribua a tabela internamente ou externamente. Esta seção mostra como incorporar os componentes em seus arquivos de projeto e aplicação.

> **Dica:** Você não precisa distribuir o arquivo ReportOutput.App externamente com sua aplicação se seguir este procedimento.

### Para incluir uma tabela de registro e componentes da Report Output Application em seu arquivo de aplicação (.app ou .exe)
- Inclua código semelhante ao seguinte durante o código de configuração em sua aplicação para incorporar os componentes da Report Output Application em sua aplicação: * certifique-se de que o programa principal da * Report Output Application esteja incluído * em seu projeto: EXTERNAL proc frxoutput.prg * certifique-se de que a tabela de registro também esteja * incluída, se você planeja incorporá-la * ao arquivo de aplicação: EXTERNAL TABLE MyConfig
- No código de configuração da aplicação, designe o programa principal da Report Output Application padrão * defina o valor da variável de sistema * _REPORTOUTPUT para o programa principal da * Report Output Application padrão: _REPORTOUTPUT = FULLPATH("frxoutput.prg")
- No código de configuração da aplicação, designe a tabela de registro apropriada conforme descrito na última seção. Você não precisa incluir um caminho se incorporar a tabela de registro na aplicação: * designe a tabela de registro apropriada: #DEFINE OUTPUTAPP_CONFIG_READ -200 DO (_REPORTOUTPUT) with OUTPUTAPP_CONFIG_READ, "myconfig"
- Reconstrua sua aplicação. Como você incluiu o programa principal da Report Output Application, os outros componentes necessários devem ser incorporados automaticamente em sua aplicação pelo processo de build. Durante o processo de build, localize quaisquer arquivos solicitados pelo Project Manager.
- Sua aplicação agora está pronta para usar os arquivos incorporados da Report Output Application e sua tabela de registro personalizada: * a linha a seguir procurará uma classe * para instanciar usando sua tabela de registro. * Ela gerará um erro se nenhum registro * apropriado existir na tabela de registro: REPORT FORM <seu relatório> OBJECT TYPE 993 * a linha a seguir procurará uma classe * para instanciar usando sua tabela de registro. * Ela usará os valores padrão incorporados da Report Output Application * se nenhum registro apropriado existir na tabela de registro: REPORT FORM <seu relatório> OBJECT TYPE 5 * as linhas de código a seguir fazem o Visual FoxPro * solicitar automaticamente à Report Output Application * um objeto derivado de ReportListener do * TYPE 1 (impressão). Sua tabela de registro * será usada para encontrar uma classe do tipo * apropriado, e os padrões da Report Output Application * serão usados se a tabela não tiver registros * designando uma classe para este tipo: SET REPORTBEHAVIOR 90 REPORT FORM <seu relatório> TO PRINT
