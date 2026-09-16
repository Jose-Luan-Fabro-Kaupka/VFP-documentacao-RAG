# Como: substituir a caixa de diálogo Expression Builder do Report Builder

A arquitetura do Report Builder define uma estrutura na qual você pode conectar suas próprias classes para tratar ações específicas do builder, como responder a eventos do designer de relatório. Além disso, o report builder também permite substituir a caixa de diálogo Expression Builder pela sua própria implementação, registrando uma classe na tabela de registro de manipuladores de eventos do report builder.

Este tópico descreve o processo de conectar sua própria classe para substituir a caixa de diálogo expression builder, e também fornece uma classe de exemplo mais abrangente que demonstra como criar um expression builder com consciência do Data Environment.

> **Observação:** Se você ainda não fez isso, crie uma cópia editável da tabela interna de registro de manipuladores de eventos do report builder, conforme descrito em How to: Add Your Own Handler to the Report Builder's Registry.

> **Observação:** Este tópico assume que a variável de sistema _REPORTBUILDER está definida para a aplicação Report Builder padrão. Se estiver vazia, ou foi definida para um report builder de terceiros, os procedimentos descritos abaixo provavelmente não se aplicarão. Para mais informações, consulte _REPORTBUILDER System Variable.

### Para criar uma classe wrapper GetExpression
- Crie ou edite uma biblioteca de classes programática: MODIFY COMMAND c:\temp\mylibrary.prg
- Defina uma classe que implemente a API wrapper GetExpression, conforme documentado em Report Builder Event Handler Registry Table. Você pode usar o exemplo simples mostrado aqui como modelo. Este exemplo substitui o editor de legenda de etiqueta por uma caixa de entrada simples.
- Salve suas alterações.

```foxpro
DEFINE CLASS MyGetExpressionWrapper AS Custom
   PROCEDURE GetExpression( cDefaultExpr, cDataType, ;
                            cCalledFrom,  oEvent )
      LOCAL cNewValue
      * Switch to the designer datasession, where tables
      * may be open:
      SET DATASESSION TO (oEvent.DefaultSessionID)
      DO CASE
      CASE m.cCalledFrom = "LabelCaption"
         * Specify special handling for label captions:
         cNewValue = INPUTBOX("Enter the label caption")
      OTHERWISE
         * All other expression builders will use the default:
         GETEXPR "Enter the label caption" TO cNewValue ;
            TYPE cDataType DEFAULT cDefaultExpr
      ENDCASE
      * Restore to the private builder datasession:
      SET DATASESSION TO (oEvent.FrxSessionID)
      RETURN cNewValue
   ENDPROC
ENDDEFINE
```

### Para registrar sua classe na tabela de registro de manipuladores
- Abra a caixa de diálogo Report Builder Options: DO (_REPORTBUILDER)
- Clique em Explore Registry.
- Localize o registro com Type = "G".
- Edite o registro para que Class = "MyGetExpressionWrapper" e Library = "c:\temp\mylibrary.prg"
- Clique em OK para salvar suas alterações.

### Para testar suas alterações
- Abra um layout de relatório ou etiqueta no designer.
- Clique duas vezes em um controle de etiqueta para exibir a caixa de diálogo Properties.
- Clique nas reticências (…) ao lado da caixa de texto de legenda da etiqueta para invocar o expression builder personalizado fornecido pela sua classe.

# Exemplo

Por design e por padrão, a caixa de diálogo Expression Builder invocada por ReportBuilder.App não mostra tabelas que não estão abertas na sessão de dados do designer. Tabelas e cursors incluídos no data environment do layout de relatório não estão disponíveis. Esta é uma mudança em relação ao comportamento do Expression Builder do designer em versões anteriores (e ainda ocorre quando `_REPORTBUILDER = ""`).

Este exemplo mostra como você pode definir uma classe wrapper alternativa que inspeciona o data environment, abre as tabelas em uma sessão de dados privada e depois invoca a caixa de diálogo GETEXPR padrão, para duplicar o comportamento original do Expression Builder do designer de relatório.

Você pode salvar esta classe em um arquivo de procedimento e registrá-la para uso no report builder, conforme descrito acima.

```foxpro
DEFINE CLASS GetExpressionWithDE AS Session
  DataSession = 2   && private

  PROCEDURE GetExpression
     LPARAMETERS lcDefaultExpr, lcDataType, lcCalledFrom, loEvent
     LOCAL lCurSel, lcNewExpr, liPrivateSession
     LOCAL liLines, i, iTableCount, lcAlias, lcSource
     *----------------------------------------------
     * Save this before it changes:
     *----------------------------------------------
     liPrivateSession = THIS.DataSessionId
     *----------------------------------------------
     * Scan the data environment and open tables:
     *----------------------------------------------
     SET DATASESSION TO (loEvent.FrxSessionId)
     lCurSel     = SELECT()
     iTableCount = 0
     SELECT expr FROM frx WHERE objtype = 26 ;
        INTO CURSOR environCursors
     SELECT environCursors
     SCAN
        liLines = ALINES(laValuePairs, environCursors.expr )
        FOR i = 1 TO liLines
           DO CASE
           CASE LEFT(UPPER(laValuePairs[i]),5) == "ALIAS"
              lcAlias = THIS.GetValue( laValuePairs[i])
           CASE LEFT(UPPER(laValuePairs[i]),7) == "CURSORS"
              lcSource = THIS.GetValue( laValuePairs[i])
           ENDCASE
        ENDFOR
        lcSource = EVL(lcSource,"")
        DO CASE
        CASE FILE(lcSource)
        CASE FILE(FORCEEXT(lcSource,"DBF"))
           lcSource = FORCEEXT(lcSource,"DBF")
        CASE FILE(JUSTFNAME(lcSource))
           lcSource = JUSTFNAME(lcSource)
        CASE FILE(FORCEEXT(JUSTFNAME(lcSource),"DBF"))
           lcSource = FORCEEXT(JUSTFNAME(lcSource),"DBF")
        ENDCASE
        IF FILE(lcSource)
           lcAlias = EVL( lcAlias, "Cursor"+TRANSFORM(i))
           SET DATASESSION TO (liPrivateSession)
           IF NOT USED(lcAlias)
              TRY
                 IF EMPTY(ALIAS())
                    USE (lcSource) ALIAS (lcAlias) ;
                       NOUPDATE SHARED
                 ELSE
                    USE (lcSource) ALIAS (lcAlias) ;
                       IN 0 NOUPDATE SHARED
                 ENDIF
                 iTableCount = iTableCount+1
              CATCH WHEN .T.
              ENDTRY
           ENDIF
           SET DATASESSION TO (loEvent.FrxSessionID)
        ENDIF
     ENDSCAN
     USE IN environCursors
     SELECT (lCurSel)
     IF iTableCount > 0
        SET DATASESSION TO (liPrivateSession)
     ELSE
        SET DATASESSION TO (loEvent.DefaultSessionID)
     ENDIF
     *-----------------------------------
     * Display the GETEXPR dialog:
     *-----------------------------------
     GETEXPR TO lcNewExpr TYPE lcDataType DEFAULT lcDefaultExpr
     *-----------------------------------
     * Clean up and exit:
     *-----------------------------------
     SET DATASESSION TO (liPrivateSession)
     CLOSE DATA
     SET DATASESSION TO (loEvent.FrxSessionID)
     RETURN lcNewExpr
  ENDPROC
  PROTECTED PROCEDURE GetValue
     LPARAMETER lcValuePair
     LOCAL liPos, lcReturn
     lcReturn = ""
     IF NOT EMPTY(lcValuePair)
        liPos = AT("=",lcValuePair)
        IF EMPTY(liPos)
           RETURN ""
        ENDIF
        lcReturn =CHRTRAN(ALLTRIM(SUBSTR(lcValuePair,liPos+1)),["'],[])
     ENDIF
     RETURN lcReturn
  ENDPROC
ENDDEFINE
```
