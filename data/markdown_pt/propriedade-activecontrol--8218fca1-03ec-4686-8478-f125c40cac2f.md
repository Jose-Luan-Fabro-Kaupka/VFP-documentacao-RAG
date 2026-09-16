# Propriedade ActiveControl

Referencia o controle ativo em um objeto. Não disponível em tempo de design; somente leitura em tempo de execução.

```foxpro
Object.ActiveControl.Property[ = Value]
```

# Valor de retorno
 **Property**
A propriedade a retornar ou definir.
**Value**
O valor de propriedade atual ou novo.

# Observações

Aplica-se a: Container Object | Form Object | Page Object | _SCREEN System Variable | ToolBar Object

Esta propriedade não está disponível se todos os controles no objeto especificado estiverem invisíveis ou desabilitados.

Se o objeto estiver ativo, a propriedade ActiveControl referencia o controle que tem o foco. Se o objeto não estiver ativo, ocorre um erro.

# Exemplo

O exemplo a seguir usa a propriedade ActiveControl para mostrar qual controle em um Form tem o foco. Observe que Grids são contêineres e requerem código para determinar o ActiveControl atual dentro da Grid.

```foxpro
m.cTalk=SET("TALK")
SET TALK OFF
PUBLIC oTlb
oTlb = NEWOBJECT("tlbDemo")
oTlb.SHOW
PUBLIC oFrmDemo
oFrmDemo=NEWOBJECT("frmDemo")
oFrmDemo.SHOW
READ EVENTS
RELEASE oTlb
RELEASE oFrmDemo
SET TALK &cTalk
RETURN
DEFINE CLASS tlbDemo AS TOOLBAR
    HEIGHT = 31
    LEFT = 30
    TOP = 30
    WIDTH = 149
    NAME = "tlbDemo"
    CONTROLBOX = .F.
    ADD OBJECT cmdShowControl AS COMMANDBUTTON WITH ;
        TOP = 5, ;
        LEFT = 5, ;
        HEIGHT = 22, ;
        WIDTH = 100, ;
        CAPTION = "ActiveControl?", ;
        NAME = "cmdShowControl"
    ADD OBJECT sepSeparator1 AS SEPARATOR WITH ;
        TOP = 5, ;
        LEFT = 80, ;
        HEIGHT = 0, ;
        WIDTH = 0, ;
        NAME = "sepSeparator1"
    ADD OBJECT cmdExit AS COMMANDBUTTON WITH ;
        TOP = 5, ;
        LEFT = 80, ;
        HEIGHT = 22, ;
        WIDTH = 34, ;
        CAPTION = "Exit", ;
        NAME = "cmdExit"
    PROCEDURE cmdShowControl.CLICK
        DO ShowControl
    ENDPROC
    PROCEDURE cmdExit.CLICK
        CLEAR EVENTS
    ENDPROC
ENDDEFINE
DEFINE CLASS frmDemo AS FORM
    DOCREATE = .T.
    CAPTION = "Demo Form"
    NAME = "frmDemo"
    LEFT = 60
    TOP = 100
    ADD OBJECT cmdClose AS COMMANDBUTTON WITH ;
        TOP = 200, ;
        LEFT = 264, ;
        HEIGHT = 27, ;
        WIDTH = 84, ;
        CANCEL = .T., ;
        CAPTION = "Close", ;
        DEFAULT = .T., ;
        TABINDEX = 4, ;
        NAME = "cmdClose"
    ADD OBJECT grdNames AS GRID WITH ;
        COLUMNCOUNT = 2, ;
        DELETEMARK = .F., ;
        HEIGHT = 128, ;
        LEFT = 12, ;
        PANEL = 1, ;
        RECORDSOURCE = "names", ;
        SPLITBAR = .F., ;
        TABINDEX = 3, ;
        TOP = 48, ;
        WIDTH = 344, ;
        NAME = "grdNames", ;
        Column1.CONTROLSOURCE = "names.cname", ;
        Column1.WIDTH = 222, ;
        Column1.NAME = "Column1", ;
        Column2.CONTROLSOURCE = "names.nvalue", ;
        Column2.NAME = "Column2"
    ADD OBJECT txtName AS TEXTBOX WITH ;
        CONTROLSOURCE = "names.cname", ;
        HEIGHT = 24, ;
        LEFT = 56, ;
        TABINDEX = 2, ;
        TOP = 12, ;
        WIDTH = 125, ;
        NAME = "txtName"
    ADD OBJECT lblNameLabel AS LABEL WITH ;
        CAPTION = "Name:", ;
        HEIGHT = 17, ;
        LEFT = 16, ;
        TOP = 16, ;
        WIDTH = 40, ;
        TABINDEX = 1, ;
        NAME = "lblNameLabel"
    PROCEDURE LOAD
        CREATE CURSOR names (cname C(40), nvalue N(19,2))
        INSERT INTO names VALUES('Thomas',12.5)
        INSERT INTO names VALUES('Jerry',18.2)
        INSERT INTO names VALUES('Andrew',9.2)
        GO TOP
    ENDPROC
    PROCEDURE INIT
        THIS.grdNames.Column1.Header1.CAPTION = "Name"
        WITH THIS.grdNames.Column1.Text1
            .BORDERSTYLE = 0
            .MARGIN = 0
        ENDWITH
        THIS.grdNames.Column2.Header1.CAPTION = "Value"
        WITH THIS.grdNames.Column2.Text1
            .BORDERSTYLE = 0
            .MARGIN = 0
        ENDWITH
    ENDPROC
    PROCEDURE cmdClose.CLICK
        THISFORM.RELEASE
    ENDPROC
    PROCEDURE grdNames.AFTERROWCOLCHANGE
        LPARAMETERS nColIndex
        THISFORM.REFRESH
    ENDPROC
    PROCEDURE txtName.VALID
        THISFORM.grdnames.REFRESH
    ENDPROC

ENDDEFINE
PROCEDURE ShowControl
IF TYPE("_Screen.ActiveForm.ActiveControl")=="O"
    LOCAL loActiveControl
    m.loActiveControl = _SCREEN.ACTIVEFORM.ACTIVECONTROL
    IF m.loActiveControl.BASECLASS = "Grid"
        m.loActiveControl = ;
            EVALUATE("m.loActiveControl.Columns(m.loActiveControl.ActiveColumn)." + ;
            m.loActiveControl.COLUMNS(m.loActiveControl.ACTIVECOLUMN).CURRENTCONTROL)
    ENDIF
    m.cObjHierarchy=UPPER(SYS(1272,m.loActiveControl))
    WAIT WINDOW AT 4,30 "_SCREEN.ActiveForm.ActiveControl = "+m.cObjHierarchy NOWAIT
ELSE
    WAIT WINDOW AT 4,30 "There is no ActiveControl; there is no ActiveForm" NOWAIT
ENDIF
ENDPROC
```
