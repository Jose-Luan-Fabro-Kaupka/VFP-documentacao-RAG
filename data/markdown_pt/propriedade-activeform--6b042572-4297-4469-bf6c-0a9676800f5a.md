# Propriedade ActiveForm

Referencia o objeto Form ativo em um form set ou o objeto _SCREEN. Não disponível em tempo de design; somente leitura em tempo de execução.

```foxpro
Object.ActiveForm.Property [ = Setting]
-or-
Object.ActiveForm.Method
```

# Valor de retorno
 **Property**
Especifica qualquer propriedade do formulário ativo contido no form set; por exemplo, a propriedade Caption.
**Setting**
A configuração existente ou nova da Property.
**Method**
Especifica qualquer método do formulário ativo contido no form set; por exemplo, o método Move.

# Observações

Aplica-se a: Form Object | FormSet Object | Variável de sistema _SCREEN

Se o objeto FormSet contenedor estiver ativo, ActiveForm referencia o objeto Form que tem o foco. Se o objeto FormSet contenedor não estiver ativo, ocorre um erro.

Use a propriedade ActiveForm para acessar as propriedades e métodos do objeto Form ativo.

# Exemplo

Este exemplo mostra como a propriedade ActiveForm pode ser usada em um menu para habilitar a abertura e o fechamento de um formulário. Ao executar este exemplo, observe que o item de menu Close no pad Window do menu só é habilitado se houver um formulário aberto. Esse comportamento é controlado pela cláusula SKIP FOR na barra 1 do popup Wwindow, que verifica se há um formulário ativo testando se o Name do formulário é do tipo caractere. A propriedade Name será do tipo caractere se houver um formulário ativo; caso contrário, a propriedade será indefinida.

```foxpro
SET SYSMENU TO
SET SYSMENU AUTOMATIC
DEFINE PAD _0k50sa3dr OF _MSYSMENU PROMPT "\<Window" COLOR SCHEME 3 ;
    KEY ALT+W, ""
DEFINE PAD _0k50sa3ds OF _MSYSMENU PROMPT "E\<xit" COLOR SCHEME 3 ;
    KEY ALT+X, ""
ON PAD _0k50sa3dr OF _MSYSMENU ACTIVATE POPUP Wwindow
ON SELECTION PAD _0k50sa3ds OF _MSYSMENU DO CloseDemo
DEFINE POPUP Wwindow MARGIN RELATIVE SHADOW COLOR SCHEME 4
DEFINE BAR 1 OF Wwindow PROMPT "\<Close" ;
    SKIP FOR TYPE("_Screen.ActiveForm.Name")<>"C"
DEFINE BAR 2 OF Wwindow PROMPT "\<Open"
ON SELECTION BAR 1 OF Wwindow =_SCREEN.ACTIVEFORM.RELEASE()
ON SELECTION BAR 2 OF Wwindow DO OpenForm
PUBLIC ARRAY aoForms(1)
aoForms[1] = NEWOBJECT("frmdemo")
aoForms[1].SHOW
READ EVENTS
SET SYSMENU TO DEFAULT
CLEAR ALL
    PROCEDURE OpenForm
    DIMENSION aoForms(ALEN(aoForms)+1)
    aoForms[ALEN(aoForms)] = NEWOBJECT("frmdemo")
    aoForms[ALEN(aoForms)].SHOW
    RETURN
    PROCEDURE CloseDemo
    CLEAR EVENTS
    RETURN
DEFINE CLASS frmdemo AS FORM
    CAPTION = "Demo Form"
    NAME = "frmDemo"
    ADD OBJECT cmdClose AS COMMANDBUTTON WITH ;
        TOP = 200, ;
        LEFT = 264, ;
        HEIGHT = 27, ;
        WIDTH = 84, ;
        CANCEL = .T., ;
        CAPTION = "Close", ;
        DEFAULT = .T., ;
        NAME = "cmdClose"
    PROCEDURE cmdClose.CLICK
    m.nOKButton=0
    m.nInfo=64
    =MESSAGEBOX("After this Form closes, select Exit from the menu to return to the Command Window",m.nInfo+m.nOKButton)
    THISFORM.RELEASE
ENDPROC
    PROCEDURE RELEASE
    LOCAL m.nIndex
    FOR m.nIndex = 1 TO ALEN(aoForms)
        IF VARTYPE(aoForms[m.nIndex])=="O"
            IF aoForms[m.nIndex]=THIS
                aoForms[m.nIndex] = ""
                EXIT
            ENDIF
        ENDIF
    ENDFOR
ENDPROC
ENDDEFINE
```
