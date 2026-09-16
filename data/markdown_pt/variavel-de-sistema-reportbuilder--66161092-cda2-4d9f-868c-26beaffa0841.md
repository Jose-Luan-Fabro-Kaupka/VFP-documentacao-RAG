# Variável de sistema _REPORTBUILDER

Especifica o aplicativo usado pelo Report Designer para tratar eventos de builder.

Para obter mais informações sobre report builders, consulte How to: Extend or Replace the Report Builder

```foxpro
_REPORTBUILDER = cProgramName
```

#### Parâmetros
 **cProgramName**
Especifica o nome de um aplicativo ou programa que o Report Designer chama quando ocorre um evento de builder. Você também pode especificar uma cadeia de caracteres vazia (""), o que faz com que caixas de diálogo apareçam como em versões anteriores ao Visual FoxPro 9.0. Observação Se o aplicativo estiver localizado em um diretório diferente do diretório padrão atual, inclua um nome de caminho com o nome do programa.

# Observações

Por padrão, _REPORTBUILDER especifica o caminho e o nome de arquivo do ReportBuilder.app localizado no diretório principal do Visual FoxPro.

Você também pode especificar um arquivo de aplicativo de builder usando a guia File Locations na caixa de diálogo Options. Para obter mais informações, consulte File Locations Tab, Options Dialog Box.

O aplicativo que você especifica com _REPORTBUILDER deve ser modal em operação, aceitar parâmetros passados a ele pelo Report Designer e retornar valores apropriados para o primeiro parâmetro, que é passado por referência.

O Visual FoxPro não gera um erro se não localizar um aplicativo para _REPORTBUILDER. O Report Designer dispara eventos de builder somente se você especificar um aplicativo ou arquivo de programa válido.

> **Observação:** Ao distribuir report builders com seus aplicativos, pode ser conveniente definir explicitamente _REPORTBUILDER no arquivo de configuração do Visual FoxPro, Config.fpw. Para obter mais informações, consulte Including Report Files for Distribution e Setting Configuration Options at Startup .

# Exemplo

A linha de código a seguir define a variável de sistema _REPORTBUILDER para o aplicativo Report Builder padrão:

```foxpro
_REPORTBUILDER = HOME(1)+"ReportBuilder.app"
```
