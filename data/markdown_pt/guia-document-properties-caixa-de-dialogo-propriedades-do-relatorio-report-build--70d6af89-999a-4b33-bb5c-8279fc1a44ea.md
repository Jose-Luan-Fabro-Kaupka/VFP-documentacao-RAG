# Guia Document Properties, caixa de diálogo Propriedades do relatório (Report Builder)

A guia Document Properties permite adicionar, editar ou excluir propriedades de documento para o relatório. As propriedades de documento são incluídas apenas em relatórios HTML ou XML. Elas são renderizadas como meta tags na saída de um relatório. Você pode acessar as propriedades em um objeto baseado na Classe básica ReportListener Base Foundation Class.

A caixa de diálogo Propriedades do relatório aparece quando você clica em Propriedades no menu Relatório ou no menu de atalho de um relatório.
 - Como: adicionar propriedades de documento a um relatório
 **Properties**
Lista as propriedades de documento associadas ao relatório. Também lista os valores das propriedades. Clique em um item na lista para selecioná-lo e habilitar os botões Edit e Clear.
**Edit**
Exibe a Caixa de diálogo Expression Builder para que você possa editar o valor da propriedade selecionada.
**Add**
Exibe a Caixa de diálogo Add Property (Report Builder) para que você possa adicionar uma nova propriedade personalizada. Nesta caixa de diálogo, você pode especificar o nome, tipo e valor da propriedade.
**Clear**
Exclui a propriedade selecionada.

# Propriedades padrão

As seguintes propriedades estão associadas a um relatório quando você o cria. Você pode editar os valores, excluir as propriedades ou adicionar novas propriedades.

| Propriedade | Descrição |
| --- | --- |
| Document.Title | O conteúdo do elemento <title> em um arquivo HTML ou um elemento property dentro da tag <Run> em um arquivo XML. Por exemplo, <property id="Document.Title">My Report Title</property> . |
| Document.Author | O conteúdo do elemento <meta> em um arquivo HTML. Por exemplo <meta name="description" content=""> ou um elemento property dentro da tag <Run> em um arquivo XML. |
| Document.Description | O conteúdo do elemento <meta> em um arquivo HTML ou um elemento property dentro da tag <Run> em um arquivo XML. Por exemplo <meta name="description" content="my description"> |
| Document.Keywords | O conteúdo do elemento <meta> em um arquivo HTML ou um elemento property dentro da tag <Run> em um arquivo XML. Por exemplo <meta name="keywords" content="keyword1, keyword2"> |
| Document.Copyright | O conteúdo do elemento <meta> em um arquivo HTML ou um elemento property dentro da tag <Run> em um arquivo XML. Por exemplo <meta name="copyright" content="my copyright information"> |
| Document.Date | O conteúdo do elemento <meta> em um arquivo HTML ou um elemento property dentro da tag <Run> em um arquivo XML. Por exemplo <meta name="date" content="10/11/2007"> |
| HTML.CSSFile | O valor do atributo href em uma tag <link> no <head> do seu arquivo html. Por exemplo, <link href="myStyleFile.css" rel="stylesheet" type="text/css"> |
| HTML.Metatag.HTTP-EQUIV | O valor de uma tag <META HTTP-EQUIV="name" CONTENT="content">. |
| HTML.TextAreasOff | Por padrão, uma expressão multilinha aparece em um elemento textarea na saída HTML. Neste caso, se o texto for longo, uma barra de rolagem permite que o usuário veja todo o texto. Defina HTML.TextAreasOff como true (.T.) para impedir o uso de um elemento textarea. Se você definir HTML.TextAreasOff como true, parte do texto pode ser truncada em seu relatório. |
