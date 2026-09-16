# Projetando um aplicativo OLE

Aplicativos habilitados para Automation e componentes COM podem atuar como servidores Automation, clientes ou ambos. Componentes que atuam como servidores podem fornecer objetos a outro aplicativo; componentes que atuam como clientes podem criar objetos.

Você pode incorporar facilmente o poder e a flexibilidade de aplicativos, como Microsoft Excel e Word, em seus aplicativos Visual FoxPro. Como o Visual FoxPro também atua como servidor, você também pode fornecer funcionalidade que pode ser integrada em pacotes de solução baseados no Microsoft Office ou em outros componentes COM.

Objetos OLE inseríveis vêm de aplicativos habilitados para OLE, como Microsoft Excel e Word. Esses objetos incluem documentos Word e planilhas Excel. Em formulários, você pode vincular ou incorporar esses objetos usando o controle OLE Container, e pode armazenar esses objetos em campos General de uma tabela, exibindo-os em seus formulários com o controle OLE Bound.

Em um aplicativo Visual FoxPro, você pode usar tecnologia OLE e ActiveX de muitas maneiras. Antes de criar um aplicativo, considere as maneiras pelas quais você pode usar essas tecnologias.

# Vinculando ou incorporando objetos OLE

Você pode incorporar ou vincular arquivos de outros aplicativos Windows em suas tabelas e formulários. Por exemplo, você pode incorporar ou vincular um documento Word em um campo General de uma tabela, e pode incorporar ou vincular uma planilha Excel em um formulário.

A diferença entre incorporar e vincular está em onde os dados são armazenados. A incorporação armazena os dados na tabela ou formulário, enquanto o vínculo não. Por exemplo, quando você incorpora uma planilha Excel em um formulário, o formulário contém uma cópia da planilha. Quando você vincula, no entanto, o formulário contém apenas uma referência à planilha — não a planilha em si.

Tanto dados incorporados quanto vinculados começam com o conteúdo original do arquivo servidor.

Mas quando o arquivo original é alterado, os dados vinculados são atualizados automaticamente para refletir a alteração, enquanto os dados incorporados não são:
 Dados vinculados atualizados em um formulário

Os dados incorporados não são necessariamente estáticos, no entanto. Tanto dados incorporados quanto vinculados podem ser exibidos, alterados e manipulados de forma interativa e programática no Visual FoxPro.

# Adicionando objetos OLE vinculados ou não vinculados

Em um formulário ou em um relatório, você pode criar objetos vinculados a campos General em tabelas. Esses objetos são chamados objetos OLE vinculados e você os usa para exibir o conteúdo de objetos OLE em campos General. Você cria objetos OLE vinculados usando o controle OLE Bound na barra de ferramentas Form Controls. Alternativamente, você cria objetos OLE não vinculados usando o controle OLE Container. Um objeto OLE não vinculado não está conectado a um campo General em uma tabela.
