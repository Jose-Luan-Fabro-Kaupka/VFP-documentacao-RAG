# Exemplo Create a Cursor from an XML DataSet

Arquivo: ...\Samples\Solution\Toledo\CAXML.scx

Este exemplo demonstra como criar um cursor a partir de um XML DataSet usando as classes CursorAdapter e XMLAdapter e como vincular os dados a controles em um formulário.

### Para ver as alterações em um XML DiffGram
- Faça alterações na grade e clique em Show DiffGram .

### Para visualizar configurações de propriedades do CursorAdapter
- Clique em Show CursorAdapter Properties .

Para obter mais informações sobre CursorAdapter e XMLAdapter, consulte Classe CursorAdapter e Classe XMLAdapter.

# Carregando XML em um cursor

Neste exemplo, o método LoadXML do XMLAdapter carrega um XML DataSet em um objeto XMLAdapter e trabalha com um objeto CursorAdapter para criar um cursor. Carregar o XML DataSet no XMLAdapter cria objetos XMLTable na coleção Tables do XMLAdapter correspondentes às tabelas no XML DataSet. A propriedade SelectCmd do CursorAdapter é definida para o objeto XMLTable que você deseja exibir. Quando o método CursorFill do CursorAdapter é chamado no objeto CursorAdapter, o cursor é criado.

Para obter mais informações, consulte Método LoadXML, Classe XMLTable e Método CursorFill.

Este exemplo usa um ADO.NET DataSet como o arquivo XML, mas o arquivo XML também pode ser um XML DataSet gerado pelo Visual FoxPro.

### Para carregar um XML DataSet em um objeto XMLAdapter
- No evento Init do formulário de exemplo, adicione uma propriedade que é uma referência de objeto a um XMLAdapter usando os designers Form ou Class ou usando o método AddProperty em código: ThisForm.AddProperty('oXMLAdapter',CREATEOBJECT('XMLAdapter'))
- Para criar a coleção Tables no objeto XMLAdapter, carregue o arquivo XML conforme mostrado no código a seguir: WITH ThisForm.oXMLAdapter .LoadXML(ThisForm.cRunPath+'getcustomers.xml',.T.) ENDWITH
- Defina SelectCmd do CursorAdapter para o objeto XMLTable e chame o método CursorFill do CursorAdapter: ThisForm.DataEnvironment.cursor1.SelectCmd= ; "ThisForm.oXMLAdapter.Tables.Item(1)" ThisForm.DataEnvironment.cursor1.CursorFill()

Para visualizar as propriedades do objeto CursorAdapter, procure no objeto DataEnvironment. Você pode abrir o DataEnvironment Designer clicando com o botão direito no objeto CursorAdapter e selecionando Builder. As propriedades do CursorAdapter foram definidas pelo CursorAdapter Builder.

Para obter mais informações, consulte Objeto DataEnvironment, Evento Init e CursorAdapter Builder.

# Controlando vinculação de dados

O cursor que contém os dados usados pelo formulário não existe quando a vinculação de dados geralmente ocorre. Isso ocorre porque o objeto XMLAdapter está carregando o XML no evento Init do formulário, que ocorre após a vinculação de dados por padrão. No entanto, você pode controlar quando a vinculação de dados ocorre definindo a propriedade BindControls do Form.

Neste exemplo, a propriedade BindControls do formulário é definida como False (.F.). Depois que o método CursorFill do CursorAdapter cria o cursor contendo os dados, BindControls é definido como True (.T.). Você pode então vincular os controles no formulário usando o código a seguir:

```foxpro
ThisForm.BindControls = .T.
```

Para obter mais informações, consulte Propriedade BindControls.

# Gerando XML DiffGrams com o XMLAdapter

Para gerar um XML DiffGram, use o método ToXML do XMLAdapter, conforme ilustrado no evento `cmdDiffgram.Click` deste exemplo:

```foxpro
WITH ThisForm.oXMLAdapter
   .ReleaseXML(.F.)      && Release XML document but preserve schema.
   .UTF8Encoded = .T.    && Indicates International characters.
   .IsDiffgram = .T.     && Generate XML DiffGram.
   llIncludeBefore = .T. && Include <diffgram:before> format.
   llChangesOnly = .T.   && Generate only changes made.
   llIsFile = .F.        && XML is a variable.
   lcSchemaLocation = "" && Generate inline schema.
   .ToXml("lcXML",lcSchemaLocation,llIsFile,llIncludeBefore,llChangesOnly)
ENDWITH
```
