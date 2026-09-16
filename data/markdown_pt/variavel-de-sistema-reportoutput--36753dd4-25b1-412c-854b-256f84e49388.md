# Variável de sistema _REPORTOUTPUT

Especifica o aplicativo manipulador do Visual FoxPro que fornece classes derivadas de ReportListener a serem usadas com o comando REPORT FORM, mantendo um registro de classes derivadas de ReportListener para diferentes resultados de saída.

```foxpro
_REPORTOUTPUT = cProgramName
```

#### Parâmetros

cProgramName

Especifica o nome de um aplicativo ou programa que o Sistema de Relatórios do Visual FoxPro chama quando ocorre um comando REPORT FORM adequado.

# Observações

O Sistema de Relatórios do Visual FoxPro invoca o aplicativo especificado por este valor quando uma das seguintes condições ocorre:
 - Você invoca o comando REPORT FORM ou LABEL com uma cláusula OBJECT TYPE <N> explícita. O Report Engine passa o valor numérico que você usa para o aplicativo nomeado em _REPORTOUTPUT .
- Você invoca um comando REPORT FORM depois de ter usado o comando SET REPORTBEHAVIOR 90 . Esta configuração indica que você deseja usar o modo assistido por objetos para todos os comandos REPORT FORM ou LABEL. O Report Engine usa as outras palavras-chave no comando de saída (como TO PRINT ou PREVIEW ) para estabelecer o valor numérico apropriado para a cláusula OBJECT TYPE <N> equivalente.

Em ambos os cenários, o Report Engine também passa uma variável ao aplicativo especificado em _REPORTOUTPUT. O aplicativo armazena uma referência a um objeto ReportListener apropriado nesta variável. Na execução subsequente de relatório ou etiqueta, o Report Engine faz parceria com este objeto para tratar a renderização de saída.

Por padrão, _REPORTOUTPUT especifica o caminho e o nome do arquivo para o ReportOutput.app localizado no diretório principal do Visual FoxPro, conforme indicado pela função HOME().

Você também pode especificar um aplicativo de saída de relatório usando a guia File Locations na caixa de diálogo Options. Para obter mais informações, consulte File Locations Tab, Options Dialog Box.

Ao distribuir aplicativos, pode ser conveniente definir explicitamente _REPORTOUTPUT no arquivo de configuração do Visual FoxPro, Config.fpw. Você também pode definir o valor de _REPORTOUTPUT como o nome de um programa integrado ao seu aplicativo. Para obter mais informações, consulte Including Report Files for Distribution e Setting Configuration Options at Startup.

> **Observação:** Se você usar um comando REPORT FORM ou LABEL e incluir a cláusula OBJECT TYPE <N>, ou tiver usado anteriormente o comando SET REPORTBEHAVIOR 90 , sem um valor válido em _REPORTOUTPUT , o Visual FoxPro gera um erro.

# Requisitos

O aplicativo que você especifica com _REPORTOUTPUT deve atender às seguintes condições:
 - Deve aceitar pelo menos dois parâmetros. O Report Engine passa um valor numérico, indicando o tipo de saída necessário, como o primeiro parâmetro. O Report Engine passa uma variável, para conter uma referência a um ReportListener apropriado, como o segundo parâmetro.
- Deve armazenar um valor NULL ( .NULL. ) no segundo parâmetro se não puder entender o valor no primeiro parâmetro, ou não tiver a capacidade de fornecer uma referência a um objeto derivado de ReportListener que atenda aos requisitos do primeiro parâmetro.
- Deve ser capaz de fornecer referências de objetos derivados de ReportListener para (no mínimo) tipos numéricos correspondentes aos valores nativos de ListenerType suportados pelo Visual FoxPro. Para obter mais informações, consulte ListenerType Property .
- Se obtiver com sucesso uma referência de objeto ReportListener de acordo com o tipo numérico solicitado pelo ReportListener, deve armazenar esta referência no segundo parâmetro. Também deve armazenar o tipo numérico fornecido pelo Report Engine ou aplicativo chamador na propriedade OutputType deste objeto. Para obter mais informações, consulte OutputType Property (Visual FoxPro) .
- Deve ser modal, porque deve fornecer uma referência apropriada de volta ao Report Engine. Se fornecer quaisquer elementos de interface do usuário, por exemplo permitindo que o usuário selecione um ReportListener apropriado de uma lista, esta interface também deve ser modal.

# Recomendações

As condições adicionais a seguir não são exigidas para que um aplicativo funcione como _REPORTOUTPUT. No entanto, atender a essas condições é altamente recomendado para qualquer aplicativo nesta capacidade:
 - O aplicativo deve manter algum tipo de registro de ReportListener, para permitir que os usuários especifiquem classes que preferem usar para vários tipos de saída.
- O aplicativo deve propagar erros ao aplicativo chamador de uma maneira que permita ao chamador determinar qual ação tomar quando o Report Output Application não puder cumprir suas responsabilidades.

# Exemplo

O exemplo a seguir define o valor da variável de sistema _REPORTOUTPUT para o aplicativo Report Output padrão.

```foxpro
_REPORTOUTPUT = HOME() + "ReportOutput.app"
```
