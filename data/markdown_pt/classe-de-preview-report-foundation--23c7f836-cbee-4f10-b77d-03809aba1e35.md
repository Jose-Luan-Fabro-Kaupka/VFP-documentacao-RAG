# Classe de Preview Report Foundation

Esta classe fornece um botão genérico para executar um relatório diretamente ou através da classe da caixa de diálogo Saída.

* Categoria * Botões Diversos
| --- | --- |
Catálogo padrão Visual FoxPro Catalog\Foundation Classes\Buttons
□ Classe  cmdRunReport
□ Classe base □ Button de comando
| Class Library | _miscbtns.vcx |
Classe pai  botão de comando
* Amostra ...\Amples\Solution\Ffc\buttons.scx

Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do Item da Galeria de Componentes, selecione Adicionar ao Formulário. Quando você adiciona a classe a um formulário, Visual FoxPro abre um construtor para que você possa especificar os valores cFileName e lSetCaption. Quando você larga a classe em um projeto, você pode escolher entre adicionar a classe ou criar uma subclasse.

Ver Orientações para a Utilização Visual FoxPro Aulas de Fundação para mais informações sobre a utilização de classes de fundação.

Propriedades, Eventos, Métodos Descrição
| --- | --- |
A propriedade cDialogClass □ Especifica a classe da caixa de diálogo de saída. Predefinição:  SaídaDialog
| cDialogClasslib property | Specifies the output dialog box class library. Default: (IIF(VERSION(2)=0,"",HOME( )+"FFC\")+"_REPORTS.VCX")) |
□ cFilename propriedade □ Especifica o nome do formulário a executar. Predefinição: ""
□ cOutputDialogAlias propriedade □ Especifica o nome da caixa de diálogo de saída alias. Predefinição: ""
□ lOutputDialogPreventScope propriedade Especifica se deve evitar alterar o escopo na caixa de diálogo. Predefinição: .F.
□ lOutputDialogPreventSource propriedade Especifica se deve evitar alterar o alias/report na caixa de diálogo. Predefinição: .F.
A propriedade lPromptForReport especifica se deve pedir um nome de relatório. Predefinição: .T.
□ lSetCaption propriedade □ Especifica se a legenda é automaticamente baseada no valor de cFilename. Predefinição: .T.
□ lUseOutputDialog propriedade Indica se deve exibir a caixa de diálogo Saída da classe de fundação. Predefinição: .T.
□ ShowOutputDialog method □ Mostra a caixa de diálogo de saída da classe de fundação. Sintaxe: ShowOutputDialog( ) Retorno: nenhum Argumentos: nenhum

Veja também
- Visual FoxPro Foundation Classes A-Z
- Classe de fundação da caixa de diálogo de saída
- Orientações para a utilização Visual FoxPro Classes da Fundação
- Amostras da classe da fundação
