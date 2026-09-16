# Como: estender ou substituir o Report Builder

Embora o Visual FoxPro seja fornecido com um aplicativo Report Builder padrão, completo com uma estrutura de manipuladores de eventos do Report Designer, você pode optar por substituir ou aumentar este aplicativo com sua própria implementação.

Consulte Understanding Report Builder Events para obter mais informações sobre como escrever um programa que esteja em conformidade com a API do report builder.

# Usando um aplicativo builder alternativo por padrão

### Para definir o aplicativo report builder padrão
- Adicione uma linha ao CONFIG.FPW que define a variável de sistema _REPORTBUILDER: _REPORTBUILDER = mybuilder.prg

# Substituindo reportbuilder.app "em tempo de execução"

### Para alterar report builders no código
- Use código como este para alternar para um aplicativo report builder alternativo: cOriginalBuilderApp = _REPORTBUILDER _REPORTBUILDER = "mybuilder.prg"
- Para restaurar o padrão: _REPORTBUILDER = m.cOriginalBuilderApp

# Chamando de volta para ReportBuilder.App

### Para chamar de volta para Reportbuilder.app
- Use código como este para alternar para um aplicativo report builder alternativo: parameters returnFlags, eventType, cmdClauses, sessionID : do (HOME(1)+"ReportBuilder.App") with returnFlags, eventType, cmdClauses, sessionID

Consulte o exemplo abaixo para um aplicativo builder que chama de volta para Reportbuilder.app para aumentar o comportamento padrão.

# Exemplo

Este programa de exemplo encapsula ReportBuilder.App para fornecer comportamento personalizado para o comando CREATE REPORT - Quick Report.

A funcionalidade inclui:
 - Adicionar um "cabeçalho da empresa" ao layout.
- Atualizar os controles de cabeçalho e rodapé.

Para usar, defina `_REPORTBUILDER = FULLPATH("quickreportbuilder.prg")`.

```foxpro
*-----------------------------
* QUICKREPORTBUILDER.PRG
*-----------------------------
#DEFINE QUERY_TITLE_LOC "Creating a Quick Report"
#DEFINE HEADER_QUERY_LOC "Company-standard name will be included. "+ ;
                         "Would you like to add something?"
#DEFINE FINISH_QUERY_LOC "Finished! "+CHR(13)+ ;
                         "Would you like to adjust the contents?"
#DEFINE COMPANY_HEADER_LOC  "ABC Company"
* Return value flags:---------
#DEFINE EVENT_PASSED_TO_VFP       0
#DEFINE EVENT_HANDLED_BY_BUILDER  1
#DEFINE FRX_DISCARD_CHANGES       0
#DEFINE FRX_RELOAD_CHANGES        2
* Hook event types:-----------
#DEFINE EVENTTYPE_REPORTOPEN      7
#DEFINE EVENTTYPE_OBJECTCREATE    2
#DEFINE EVENTTYPE_REPORTSAVE      6
#DEFINE EVENTTYPE_REPORTCLOSE     8
#DEFINE EVENTTYPE_PROPERTIES      1
* ReportBuilder.App Handle Modes:
#DEFINE MODE_HANDLE_CLASS         1
#DEFINE MODE_FORCE_DEBUG          2
#DEFINE MODE_FORCE_NATIVE         3
* standard FRX stuff
#DEFINE OBJTYPE_TEXT              5
#DEFINE OBJTYPE_FIELD             8
#DEFINE OBJTYPE_FONTRES          23
* ----------------------------
#DEFINE MB_YESNO                  4
#DEFINE MB_ICONQUESTION          32
#DEFINE IDYES                     6
#DEFINE IDNO                      7
* ----------------------------
LPARAMETERS returnFlags, eventType, commandClauses, designerSessionId
* This builder only takes action on a quick report.
* Criteria:  - Must be a REPORT and not a LABEL layout
*            - Must be a CREATE REPORT FROM... command
LOCAL BuilderModule
BuilderModule = HOME()+"ReportBuilder.App"
IF commandClauses.IsReport AND NOT EMPTY(commandClauses.FROM)
    LOCAL oFrxHelper
    oFrxHelper = NEWOBJECT("frxCursor", HOME()+"FFC\_frxcursor.vcx")
    DO CASE
    CASE m.eventType = EVENTTYPE_REPORTOPEN
        * This is the first event in a quick report.
        * First, replace default font resource and font
        * info in header to match our requirements, because
        * there are some hardcoded metrics for heights in this
        * simple example.
        * The FRX cursor is in the current workarea:
        REPLACE frx.fontface WITH "Courier New" ;
            FOR RECNO() = 1 OR frx.objtype = OBJTYPE_FONTRES
        LOCATE FOR frx.objtype = OBJTYPE_FONTRES
        * Now, add a font resource record for our
        * "designed" expression:
        SCATTER MEMVAR MEMO
        m.penred = 255
        m.fontface = "Tahoma"
        m.fontstyle = 1
        INSERT INTO frx FROM MEMVAR
        * Now, reuse the memvars, changing their values, to set up
        * the designed expression's record:
        m.uniqueid   = SYS(2015)
        m.objtype    = OBJTYPE_TEXT
        m.objcode    = 0
        m.timestamp  = oFrxHelper.getFrxTimeStamp()
        m.vpos       = 20
        m.hpos       = 20
        m.height     = 3000
        m.width      =  50000
        m.fillchar   = "C"
        m.penred     = 255
        STORE -1 TO m.fillred, m.fillgreen, m.fillblue
        m.mode       = 1
        m.stretch    = .T.
        m.top        = .T.
        m.spacing    = 2
        m.offset     = 2
        m.resettotal = 1
        m.supalways  = .T.
        m.suprpcol   = 3
        m.supgroup   = 0
        m.totaltype  = 0
        m.expr       = INPUTBOX(HEADER_QUERY_LOC, ;
                                QUERY_TITLE_LOC, ;
                                COMPANY_HEADER_LOC)
        DO CASE
        CASE EMPTY(m.expr)
            m.expr = COMPANY_HEADER_LOC
        CASE ATC(COMPANY_HEADER_LOC,m.expr) = 0
            m.expr = COMPANY_HEADER_LOC + " " + ALLTR(m.expr)
        ENDCASE
        m.expr = ["]+m.expr+["]
        INSERT INTO frx FROM MEMVAR
        * Finally, tell the Designer to consume our edit:
        returnFlags = FRX_RELOAD_CHANGES
    CASE  m.eventType = EVENTTYPE_REPORTSAVE
        * This is the last event in a quick report.
        IF NOT EMPTY(m.BuilderModule) AND ;
            MESSAGEBOX(FINISH_QUERY_LOC,;
                       MB_YESNO +MB_ICONQUESTION,;
                       QUERY_TITLE_LOC) = IDYES
            * Give the user a chance to adjust or eliminate
            * objects of certain types:
            SCAN ALL FOR INLIST(frx.objtype, ;
                       OBJTYPE_FIELD, OBJTYPE_TEXT)
                * Mark the object as "selected" so that the
                * builder will act on it:
                REPLACE frx.curpos WITH .T.
                * Call the builder application, ;
                * faking a regular Report Designer event:
                do (BuilderModule) with ;
                        -1, EVENTTYPE_PROPERTIES, ;
                        m.commandClauses, ;
                        m.designerSessionId
                REPLACE frx.curpos WITH .F.
            ENDSCAN
            m.returnFlags = FRX_RELOAD_CHANGES
        ENDIF
        * Find the DATE() expression control created by the
        * Quick Report process and convert it into a DATETIME():
        LOCATE FOR frx.objtype = OBJTYPE_FIELD AND ;
                        UPPER(ALLTRIM(frx.expr)) == "DATE()"
        LOCAL liWidth
        liWidth = oFrxHelper.GetFruTextWidth( ;
                                TRANSFORM(DATETIME()),;
                                frx.fontface, frx.fontsize )
        REPLACE frx.expr  WITH "DATETIME()", ;
                                frx.width WITH m.liWidth
        * Find the _pageno controls and spiff them up a bit:
        LOCATE FOR frx.objtype = OBJTYPE_TEXT ;
            AND ATC(["PAGE],frx.expr) > 0
        IF FOUND()
            REPLACE frx.expr WITH ["Page "+TRANSFORM(_PAGENO)],;
                    frx.objtype WITH OBJTYPE_FIELD, ;
                    frx.hpos WITH (frx.hpos - (frx.width*2)), ;
                    frx.width WITH frx.width*3
            SKIP
            * Remove the other _pageno object that
            * follows the "Page" one in a normal quick report:
            DELETE
        ENDIF
        * We need to instruct the Designer to respect our changes:
        returnFlags = FRX_RELOAD_CHANGES
    OTHERWISE
        returnFlags = EVENT_PASSED_TO_VFP
    ENDCASE
ELSE
    * Parameters are passed by reference:
    do (BuilderModule) with m.returnFlags, ;
                            m.eventType, ;
                            m.commandClauses, ;
                            m.designerSessionId
ENDIF
RETURN
```
