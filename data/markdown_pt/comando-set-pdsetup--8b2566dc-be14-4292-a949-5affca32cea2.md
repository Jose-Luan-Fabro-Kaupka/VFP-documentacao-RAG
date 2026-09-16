# Comando SET PDSETUP

Carrega uma configuração de driver de impressora ou limpa a configuração atual do driver de impressora.

```foxpro
SET PDSETUP TO [[cPrinterDriverSetup [, Parameter1[, Parameter2 ...]]]
   [WITH Parameter3 [, Parameter4 ...]]]
```

#### Parâmetros
 **cPrinterDriverSetup**
Especifica o nome da configuração do driver de impressora a carregar. Quando você carrega uma configuração de driver de impressora, o nome da configuração é armazenado na variável de sistema _PDSETUP, e um array de variáveis especial, _PDPARMS, pode ser criado. (_PDPARMS é discutido em detalhes na cláusula WITH neste tópico.) Se o nome da configuração do driver de impressora que você especifica com cPrinterDriverSetup não existir no seu arquivo de recursos, o aplicativo de configuração atual do driver de impressora é executado para que você possa criar uma configuração com esse nome. Se o aplicativo de configuração atual do driver de impressora for Genpd.app, a caixa de diálogo Printer Setup Editing aparece para que você possa criar a configuração. Se o nome da configuração começar com um hífen (-), o programa _GENPD não será executado, mas o nome após o hífen é armazenado em _PDSETUP. Se você emitir SET PDSETUP TO sem cPrinterDriverSetup, a configuração atual do driver de impressora é limpa, a cadeia de caracteres vazia é armazenada em _PDSETUP e o array _PDPARMS é limpo da memória.
**Parameter1 [, Parameter2 ...]**
Especifica qualquer número de parâmetros opcionais. Esses parâmetros são passados ao aplicativo de interface de configuração de impressora e podem ser de qualquer tipo (caractere, numérico, lógico e assim por diante). A primeira linha no seu aplicativo de interface de configuração de impressora deve ser uma instrução LPARAMETERS ou PARAMETERS para aceitar os parâmetros passados de SET PDSETUP. Se você estiver usando Genpd.app, não inclua esses parâmetros opcionais. Genpd.app não aceita parâmetros passados de SET PDSETUP, portanto incluí-los gera um erro.
**WITH Parameter3 [, Parameter4 ...]**
Cria o array especial de impressora _PDPARMS. Cada parâmetro que você especifica com Parameter3, Parameter4 e assim por diante torna-se um elemento em _PDPARMS. O primeiro parâmetro (Parameter3) é armazenado no primeiro elemento de _PDPARMS, o segundo parâmetro (Parameter4) é armazenado no segundo elemento e assim por diante. Esses parâmetros podem ser de qualquer tipo (caractere, numérico, lógico e semelhantes). Se você estiver usando Genpd.app, quaisquer parâmetros que você incluir são substituídos pelo aplicativo.

# Observações

No Visual FoxPro, uma configuração de driver de impressora é usada quando você imprime relatórios baseados em caracteres criados no FoxPro para MS-DOS.

Uma configuração de driver de impressora consiste em uma combinação de configurações, incluindo o programa de driver de impressora e informações como orientação da página, tamanho e estilo de fonte padrão, margens e assim por diante. As configurações de driver de impressora são armazenadas no seu arquivo de recursos do FoxPro para MS-DOS, FoxUser.dbf, e podem ser criadas interativamente e atribuídas a um nome na caixa de diálogo Printer Setup Editing.

Uma configuração de driver de impressora também pode ser carregada ou limpa com a variável de sistema _PDSETUP.

Quando você emite SET PDSETUP, o aplicativo de interface de configuração de impressora atual é executado. O aplicativo de interface recebe o nome da configuração do driver de impressora incluída em SET PDSETUP. O aplicativo de interface também pode ser especificado com a variável de sistema _GENPD. O aplicativo de interface padrão é Genpd.app, o aplicativo de interface de configuração de impressora incluído com o FoxPro para MS-DOS.
