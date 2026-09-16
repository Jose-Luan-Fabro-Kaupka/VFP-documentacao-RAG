# Como: usar a coleção de referências da Report Output Application

Em tempo de execução, a Report Output Application padrão (ReportOutput.app) mantém uma coleção de referências de objetos ReportListener. ReportOutput.app define o escopo da coleção globalmente, declarando a variável de referência com a palavra-chave PUBLIC. A coleção permite que o Report Engine use um único objeto derivado de ReportListener em vários comandos REPORT FORM ou LABEL. Para obter mais informações, consulte Understanding the Report Output Application.

Você pode usar essa coleção para definir propriedades em instâncias de objetos ReportListener antes dos comandos REPORT FORM e LABEL, ou para verificar os resultados de uma execução de relatório posteriormente, sem atribuir uma variável para manter a referência explicitamente.

ReportOutput.app usa um esquema de nomenclatura de chaves de coleção consistente para que você possa encontrar facilmente a referência apropriada.

> **Observação:** Parte do código neste tópico usa a variável de sistema _REPORTOUTPUT para invocar ReportOutput.app. _REPORTOUTPUT pode conter o nome de uma Report Output Application diferente no seu ambiente. Nesse caso, substitua HOME() + ReportOutput.app, ou código semelhante, para invocar a Report Output Application padrão. Onde as instruções designam o nome e a posição de uma tabela de registro personalizada, substitua pelo nome e localização de sua preferência.

# Inicializando a coleção de referências e criando membros da coleção de referências

### Para criar um membro da coleção de referências
- Você pode criar um membro da coleção de referências enquanto executa um relatório, e sem usar uma referência de variável explícita. Emita o seguinte comando, onde <N> é o tipo de saída que você deseja do comando REPORT FORM. Por exemplo, use o valor 1 como <N> para visualizar o relatório. REPORT FORM ? OBJECT TYPE <N>
- Você também pode criar um membro da coleção de referências sem executar um relatório. Emita o seguinte comando, onde <N> é um tipo de saída que você deseja para comandos REPORT FORM subsequentes. Por exemplo, use o valor 0 como <N> para imprimir o relatório: DO (_REPORTOUTPUT) WITH <N>
- Você também pode criar um membro da coleção de referências representando a tabela de registro atual da Report Output Application, inicializando a coleção ao mesmo tempo. Este método não cria referências de objetos ReportListener imediatamente. Inicializar a coleção dessa maneira e especificar uma tabela de configuração como o único membro da coleção é o comportamento padrão da Report Listener Application quando você chama a aplicação sem parâmetros: #DEFINE OUTPUTAPP_CONFIG_READ -200 DO (_REPORTOUTPUT) WITH OUTPUTAPP_CONFIG_READ * or pass a variable by reference in the second * parameter, as you normally do for ReportListener * references, to receive the name of the current * registry table: LOCAL lcFile DO (_REPORTOUTPUT) WITH OUTPUTAPP_CONFIG_READ, lcFile * or simply initialize the collection with no parameters: DO (_REPORTOUTPUT) ? _oReportOutput[TRANSFORM(OUTPUTAPP_CONFIG_READ)]

# Examinando membros da coleção de referências

### Para recuperar uma referência de objeto ReportListener da coleção do ReportOutput
- Use o valor de cadeia de caracteres do valor numérico que representa o tipo de saída para uma referência de ReportListener como valor de chave da coleção. No comando abaixo, <N> representa o tipo de saída fornecido por esta referência de objeto ReportListener. ? _oReportOutput[TRANSFORM(<N>)].Class
- Use o membro da coleção de referências após executar um relatório. Por exemplo, verifique o número total de páginas na execução do relatório: REPORT FORM ? OBJECT TYPE 0 ? _oReportOutput["0"].PageTotal
- Use o membro da coleção de referências antes de executar um relatório para personalizar seu comportamento. Por exemplo, impeça o feedback do usuário antes de gerar saída XML: DO (_REPORTOUTPUT) WITH 4 _oReportOutput["4"].QuietMode = .T. Dica Como mostrado acima, valores negativos especiais usados por ReportOutput.app para fins de configuração também podem ser usados como chaves nesta coleção, embora não forneçam referências de objetos derivados de ReportListener. Para exemplos adicionais, consulte "Verifying the Report Output Application's current Registry Table" em How to: Specify an Alternate Report Output Registry Table.

# Alterando o nome padrão da variável da coleção de referências

Nas instruções acima, você usou o nome de variável `_oReportOutput` ao acessar a coleção de referências. Para alterar esse nome de variável em seus aplicativos, recompile ReportOutput.app com instruções para usar o nome de variável de sua preferência.

### Para recompilar ReportOutput.app com um nome de variável de coleção de referências diferente
- Expanda a subpasta ReportOutput no arquivo zip localizado na pasta Tools\Xsource do Visual FoxPro. Para obter mais informações sobre Xsource, consulte XSource Folder.
- Navegue até a pasta na qual você expandiu os arquivos de origem do componente ReportOutput. Modifique o arquivo ReportOutput.H (cabeçalho). CD <your source folder> MODIFY COMMAND ReportOutput.H
- Localize as duas linhas de código a seguir no arquivo de cabeçalho: #DEFINE OUTPUTAPP_REFVAR _oReportOutput #DEFINE OUTPUTAPP_REFVARCLASS "Collection"
- Edite o valor _oReportOutput, substituindo-o pelo nome de variável que deseja que seu aplicativo use. Você também pode editar o valor "Collection", substituindo-o pelo nome da classe derivada de Collection que deseja que ReportOutput.app use ao criar uma instância da coleção. Observação Se você alterar o valor de OUTPUTAPP_REFVARCLASS, a definição de classe que você designar nesta constante deve estar no escopo antes de invocar ReportOutput.App. Para obter mais informações, consulte SET CLASSLIB Command e SET PROCEDURE Command.
- Salve suas alterações.
- Recompile o arquivo ReportOutput.App, certificando-se de usar a opção RECOMPILE: BUILD APPLICATION ReportOutput FROM ReportOutput RECOMPILE
- Armazene o nome e o local do seu novo ReportOutput.app na variável de sistema _REPORTOUTPUT, no arquivo CONFIG.FPW do seu aplicativo ou no código de configuração. Para obter mais informações, consulte Setting Configuration Options at Startup. _ReportOutput = <your ReportOutput.app filename and location>
- Distribua o novo arquivo ReportOutput.App com seus aplicativos.
