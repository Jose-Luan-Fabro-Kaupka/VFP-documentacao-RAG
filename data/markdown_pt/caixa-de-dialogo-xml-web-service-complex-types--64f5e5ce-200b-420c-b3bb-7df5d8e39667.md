# Caixa de diálogo XML Web Service - Complex Types

Permite que você especifique informações para tipos complexos, como nomes de tabela e campo para operações de XML Web service que retornam ADO.NET DataSets ou nomes de propriedade para um objeto retornado, como um XMLDOMNodeList, que o SOAP Toolkit 3.0 retorna para a maioria dos tipos complexos.

Esta caixa de diálogo aparece quando você clica em Complex Types na caixa de diálogo XML Web Service - Client Detail Dialog Box.
 **Dataset**
Especifica um nome de tabela e campo do DataSet retornado. O controle de XML Web service importa o DataSet para um objeto XMLAdapter que seu aplicativo pode usar. Quando a operação do cliente é chamada, o cursor é criado automaticamente. Dataset tables Especifica uma tabela das tabelas disponíveis no DataSet. Table fields Especifica um campo dos campos disponíveis na tabela do DataSet selecionada. Selecionar um campo pode ser útil ao vincular à propriedade ControlSource do TextBox Control. Use existing cursor if already opened Especifica usar um cursor existente que tenha o mesmo nome; caso contrário, cria um novo cursor.
**Object**
A maioria das operações de XML Web service que retornam tipos complexos são objetos, que são tratados pelo SOAP Toolkit 3.0 como XMLDOMNodeLists e possuem propriedades às quais você pode querer vincular seu controle. Values Exibe propriedades associadas ao objeto.
**Query**
Chama o XML Web service para que você possa visualizar os valores disponíveis para o DataSet ou objeto.
**Reset**
Redefine todos os valores para cadeias de caracteres vazias.
**Attach Schema**
Define a propriedade CursorAdapterCursorSchema do CursorAdapter para o esquema da tabela selecionada. Disponível quando um objeto CursorAdapter é selecionado na caixa de diálogo Client Detail.
