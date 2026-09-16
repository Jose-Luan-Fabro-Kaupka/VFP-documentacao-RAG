# Como: adicionar objetos OLE a aplicativos

Você pode adicionar objetos OLE a tabelas, formulários e relatórios. Para obter mais informações sobre como adicionar objetos OLE a relatórios, consulte How to: Add General Fields to Reports.

# Adicionando objetos OLE a tabelas

Você pode incluir documentos Word em uma tabela criando campos General e adicionando os documentos vinculando-os ou incorporando-os.

### Para adicionar um objeto OLE a uma tabela
- Abra a tabela no Table Designer .
- No Table Designer , crie um campo General.
- Abra uma janela browse para a tabela.
- Clique duas vezes no campo General para abrir uma janela de edição. Dica Você também pode usar o comando MODIFY GENERAL.
- No menu Edit, clique em Insert Object .

### Para adicionar um objeto OLE a uma tabela programaticamente
- Use o comando APPEND GENERAL.

Para obter mais informações, consulte APPEND GENERAL Command.

Você pode usar APPEND GENERAL para incorporar objetos OLE ou vincular a objetos OLE criados por aplicativos como Microsoft Excel e Word. Esses aplicativos suportam vinculação e incorporação. No entanto, alguns aplicativos como Microsoft Graph suportam somente incorporação. Quando você usa o comando APPEND GENERAL, pode importar o objeto OLE de um arquivo e inseri-lo em um campo General. Se o campo já contiver um objeto, o novo objeto o substitui.

> **Observação:** Diferentemente de APPEND e APPEND BLANK , APPEND GENERAL não adiciona um novo registro à tabela.

Por exemplo, suponha que você tenha arquivos Microsoft Word que deseja armazenar em uma tabela Visual FoxPro. Se a tabela tiver um campo General chamado `WordDoc`, você pode incorporar os documentos usando o código a seguir:

```foxpro
CREATE TABLE oletable (name c(24), worddoc g)
CD GETDIR()
nFiles = ADIR(aWordFiles, "*.doc")
IF nFiles > 0
   FOR i = 1 to nFiles
      APPEND BLANK
      REPLACE Oletable.Name WITH aWordFiles(i,1)
      APPEND GENERAL WordDoc FROM aWordFiles(i,1)
   ENDFOR
ELSE
   MESSAGEBOX("No Word files found.")
ENDIF
```

> **Observação:** O exemplo anterior procura somente arquivos terminados em .doc, a extensão padrão usada por arquivos Word. Como Microsoft Word e OLE reconhecem isso, os arquivos são automaticamente associados ao servidor Word quando você usa APPEND GENERAL .

Se você usar uma extensão diferente da esperada pelo servidor, deve declarar a classe do servidor, usando a cláusula CLASS. Por exemplo, se você adicionar a classe para Word ao exemplo anterior, o código se torna:

```foxpro
APPEND GENERAL WordDoc FROM wordfiles(i,1) CLASS "Word.Document"
```

Se você tiver arquivos com extensões comuns (por exemplo, .bmp) que outros servidores possam usar, pode usar a cláusula CLASS para especificar o servidor particular que deseja usar para esses arquivos. Alternativamente, se preferir vincular em vez de incorporar objetos, use a palavra-chave LINK, como no exemplo a seguir:

```foxpro
APPEND GENERAL WordDoc FROM wordfiles(i,1) LINK CLASS "Word.Document"
```

Além disso, você pode substituir dados em um objeto usando a palavra-chave DATA de APPEND GENERAL.

# Adicionando objetos OLE a formulários

Usando o Form Designer, você pode adicionar objetos OLE inseríveis a formulários com o controle OLE Container. Além disso, você pode exibir objetos OLE de campos General usando o controle OLE Bound. Quando você adiciona um objeto OLE a um formulário no controle OLE Container ou no controle OLE Bound, tem mais controle sobre a abertura e edição do objeto.

Você pode determinar se o objeto OLE é aberto ou editado quando o controle recebe o foco ou quando o usuário clica duas vezes no controle definindo a propriedade AutoActivate de um controle OLE bound ou container. A propriedade AutoVerbMenu especifica se o menu de atalho do controle ActiveX permite que um usuário abra ou edite o objeto OLE. Para controlar o acesso de forma que o objeto OLE possa ser aberto ou editado somente programaticamente com o método DoVerb, defina AutoActivate como 0 - Manual e AutoVerbMenu como false (.F.).

### Para adicionar um objeto OLE a um formulário
- No Form Designer, adicione um controle OLE Container ao seu formulário. A caixa de diálogo Insert Object é aberta.
- Na caixa de diálogo Insert Object, selecione Create New ou Create from File .
- Escolha o objeto OLE apropriado na lista Object Type.

Você também pode personalizar a barra de ferramentas Form Controls para adicionar diretamente objetos OLE específicos.

### Para adicionar objetos OLE à barra de ferramentas Form Controls
- No menu Tools, escolha Options.
- Na guia Controls da caixa de diálogo Options, escolha ActiveX controls .
- Na lista Selected, selecione os objetos OLE e controles ActiveX que deseja disponíveis na barra de ferramentas Form Controls.
- Escolha Set as Default e depois OK .
- Na barra de ferramentas Form Controls, escolha View Classes e depois ActiveX Controls .

### Para exibir um objeto OLE de um campo General
- No Form Designer, adicione um controle OLE Bound ao seu formulário.
- Especifique o campo General que contém os dados definindo a propriedade ControlSource do objeto. Por exemplo, se o nome da tabela for Inventory e o nome do campo General for Current , defina a propriedade ControlSource como Inventory.Current .

Você também pode exibir um objeto OLE de um campo General programaticamente:

| Código | Comentários |
| --- | --- |
| frm1 = CREATEOBJECT("form") | Criar formulário. |
| frm1.ADDOBJECT("olb1", "oleboundcontrol") | Adicionar controle. |
| frm1.olb1.ControlSource = "Inventory.Current" | Vincular os dados ao controle. |
| frm1.olb1.Visible = .T. frm1.Visible = .T. | Tornar o controle e o formulário visíveis. |
