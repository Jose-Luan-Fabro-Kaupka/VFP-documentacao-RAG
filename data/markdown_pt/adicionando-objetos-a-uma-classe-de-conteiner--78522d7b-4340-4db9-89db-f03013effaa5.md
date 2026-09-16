# Adicionando objetos a uma classe de contêiner

Você pode usar a cláusula ADD OBJECT no comando DEFINE CLASS ou o método AddObject para adicionar objetos a um contêiner.

Por exemplo, a seguinte definição de classe é baseada em um formulário. O comando ADD OBJECT adiciona dois botões de comando ao formulário:

```foxpro
DEFINE CLASS myform AS FORM
  ADD OBJECT cmdOK AS COMMANDBUTTON
  ADD OBJECT PROTECTED cmdCancel AS COMMANDBUTTON
ENDDEFINE
```

Use o método AddObject para adicionar objetos a um contêiner depois que o objeto contêiner foi criado. Por exemplo, as seguintes linhas de código criam um objeto Form e adicionam duas caixas de texto a ele:

```foxpro
frmMessage = CREATEOBJECT("FORM")
frmMessage.AddObject("txt1", "TEXTBOX")
frmMessage.AddObject("txt2", "TEXTBOX")
```

Você também pode usar o método AddObject no código de método de uma classe. Por exemplo, a seguinte definição de classe usa AddObject no código associado ao evento Init para adicionar um controle a uma coluna de grade.

```foxpro
DEFINE CLASS mygrid AS GRID
ColumnCount = 3
PROCEDURE Init
  THIS.Column2.AddObject("cboClient", "COMBOBOX")
  THIS.Column2.CurrentControl = "cboClient"
ENDPROC
ENDDEFINE
```

# Adicionando e criando classes no código de método

Você pode adicionar objetos programaticamente a um contêiner com o método AddObject. Você também pode criar objetos com a função CREATEOBJECT( ) no Load, Init ou em qualquer outro método da classe.

Quando você adiciona um objeto com o método AddObject, o objeto se torna um membro do contêiner. A propriedade Parent do objeto adicionado refere-se ao contêiner. Quando um objeto baseado na classe de contêiner ou controle é liberado da memória, o objeto adicionado também é liberado.

Quando você cria um objeto com a função CREATEOBJECT( ), o objeto tem escopo em uma propriedade da classe ou em uma variável no método que chama esta função. A propriedade Parent do objeto é indefinida.
