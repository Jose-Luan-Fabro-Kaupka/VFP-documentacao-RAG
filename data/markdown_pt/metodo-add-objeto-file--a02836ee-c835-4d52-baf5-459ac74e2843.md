# Método Add (Objeto File)

Adiciona um arquivo a um projeto.

```foxpro
Object.Add(cFileName)
```

#### Parâmetros
 **cFileName**
Especifica o nome do arquivo a adicionar ao projeto. Um erro é gerado se o arquivo especificado não existir. A janela Project Manager, se aberta, é atualizada após o arquivo ter sido adicionado.

# Valor de retorno

Objeto

# Observações

Aplica-se a: Coleção Files (Visual FoxPro)

O método Add é um método para a coleção files. Quando um arquivo é adicionado a um projeto com o método Add, um objeto File é criado para o arquivo e o objeto File é adicionado à coleção Files.

Uma referência de objeto ao arquivo recém-adicionado é retornada se o arquivo for adicionado com sucesso ao projeto. O valor nulo é retornado se o arquivo não puder ser adicionado ao projeto.

O evento QueryAddFile ocorre imediatamente antes de um arquivo ser adicionado a um projeto. Se NODEFAULT for especificado no evento QueryAddFile, o arquivo não é adicionado ao projeto.

Inclua NODEFAULT no evento QueryAddFile para impedir que um arquivo seja adicionado ao projeto.

# Exemplo

O exemplo a seguir cria programaticamente um Project e, em seguida, compila um executável (EXE) desse Project. Ele usa o método Add para adicionar código de programa ao projeto.

```foxpro
SET SAFETY OFF
LOCAL lcCode
TEXT TO lcCode NOSHOW
CLEAR
PUBLIC loForm
SET TALK OFF
SET DELETED ON
SET EXCLUSIVE OFF
SET CENTURY ON
ON SHUTDOWN clear events
loForm = CREATEOBJECT('Test1')
loForm.Show(0)
READ EVENTS
ON SHUTDOWN
RETURN
DEFINE CLASS Test1 as Form
 Top = 0
 Left = 0
 Width = 240
 Height = 150
 Caption = 'Add Method sample'
 ShowWindow = 2
 ADD OBJECT cmdClose as CommandButton WITH ;
  Caption = '\<Close', ;
  Top = 80, ;
  Left = 80, ;
  Height = 24, ;
  Width = 80
 ADD OBJECT lblTitle as Label WITH ;
  Top = 30, ;
  Left = 40, ;
  Height = 34, ;
  Width = 160, ;
  Caption = 'This sample was made programmatically.';
  WordWrap = .t.
 PROCEDURE Init
  SET TALK off
  ThisForm.AutoCenter = .t.
 ENDPROC
 PROCEDURE Unload
  CLEAR EVENTS
 ENDPROC
 PROCEDURE cmdClose.Click
  ThisForm.Release()
 ENDPROC
ENDDEFINE
ENDTEXT
STRTOFILE(lcCode, 'addsample.prg')
CREATE PROJECT 'AddSample' NOSHOW NOWAIT SAVE
LOCAL loPJX
loPJX = _VFP.ActiveProject
WITH loPJX
 .Files.Add('addsample.prg')
 .SetMain('addsample.prg')
 .Build('addsample.exe',3,.t.,.t.,.f.)
 .Close()
ENDWITH
RUN /n addsample.exe
```
