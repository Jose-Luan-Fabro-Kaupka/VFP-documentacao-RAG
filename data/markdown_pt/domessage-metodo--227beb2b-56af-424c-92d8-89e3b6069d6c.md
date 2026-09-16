# DoMessage Método

Fornece uma caixa de diálogo modal quando AllowModalMessages é True (`.T.`), caso contrário aciona DoStatus.

```foxpro
oReportListener.DoMessage(cMessage[,nParams[,cTitle])
```

#### Parâmetros
 **cMessage**
Especifica a mensagem mostrada pelo mecanismo de feedback do usuário do objeto ReportListener.
**nParams**
Valor numérico que especifica os atributos da caixa de diálogo, idêntico aos valores permitidos na função MESSAGEBOX.
**cTitle**
Especifica a legenda da caixa de diálogo. Assim como a função MESSAGEBOX, esse valor será padronizado como Microsoft Visual FoxPro se você não incluí-lo.

# Valor de retorno
Nenhum.

# Observações
Aplica-se a: ReportListener Objeto.

O objeto de classe base ReportListener usa uma caixa de diálogo MESSAGEBOX para fornecer feedback modal. Seu segundo e terceiro parâmetros são idênticos aos usados ​​na função MESSAGEBOX. Para obter mais informações, consulte MESSAGEBOX( ) Função.

Se você substituir ou aumentar o método this, deverá observar as convenções de parâmetro same, bem como os requisitos de interface adicionais definidos pela classe base: respeite os valores das propriedades AllowModalMessages e QuietMode ao avaliar que tipo de feedback o método the deve exibir. Para obter mais informações, consulte Função MESSAGEBOX( ) e Propriedade QuietMode.

Ao contrário da função MESSAGEBOX, a classe base ReportListener não possui um quarto argumento especificando um valor numérico de tempo limite e não possui mecanismo para responder a um valor de retorno. Na classe a derivada de ReportListener, entretanto, você pode optar por implementar essa funcionalidade e escolher como deseja lidar com a resposta do usuário.

Por exemplo, a classe ReportListener User Feedback Foundation usa uma versão aumentada do método this para permitir que os usuários cancelem um relatório no meio da execução do relatório.

# Exemplo
O código a seguir mostra como a classe ReportListener User Feedback invoca DoMessage para permitir que os usuários cancelem um relatório. A classe This aproveita a versão do DoMessage implementada pelo ReportListener Base Foundation Class, seu pai. O método enhanced fornece um valor de retorno adequado, para que a classe User Feedback possa responder à escolha do usuário. ReportListener Base Foundation A implementação da classe do método DoMessage também é mostrada abaixo.

> **Dica:** Observe que a classe ReportListener Base Foundation fornece um valor numérico consistente para o parâmetro second quando invoca MESSAGEBOX . Se você usar o método DoMessage da classe base ReportListener e se não precisar especificar atributos de caixa de diálogo, mas desejar fornecer uma legenda de caixa de diálogo personalizada, você deverá fornecer um valor 0 para o parâmetro second, semelhante ao que você vê neste exemplo. Se você especificar um valor não numérico para o parâmetro this (como .F. ), ocorrerá um erro.

```foxpro
* UpdateListener class
* (ReportListener User Feedback Foundation Class)
PROCEDURE CancelReport
   IF THIS.IsRunning AND ;
      (THIS.QuietMode OR ;
       (NOT THIS.AllowModalMessages) OR ;
        THIS.DoMessage(;
             OUTPUTCLASS_REPORT_CANCELQUERY_LOC, ;
             MB_ICONQUESTION+MB_YESNO) =  IDYES )
      DODEFAULT()
      IF SYS(2024) = "Y"
         THIS.ThermForm = NULL
         THIS.DoMessage(OUTPUTCLASS_REPORT_INCOMPLETE_LOC, ;
                        MB_ICONEXCLAMATION)
      ENDIF
   ELSE
      NODEFAULT
   ENDIF
ENDPROC
* _ReportListener class
* (ReportListener Base Foundation Class)
PROCEDURE DoMessage(cMessage,iParams,cTitle)
   NODEFAULT
   IF THIS.QuietMode OR ;
   (THIS.IsRunning AND THIS.CommandClauses.NoDialog)
   * to emulate the base class behavior, do both checks,
   * in case the call to DoMessage() occurs
   * before the baseclass sets QuietMode .T. in response
   * to NoDialog at the beginning of the report run,
   * or after the baseclass re-sets QuietMode to .F.
   * at the end of the report run.
      RETURN 0
   ELSE
      IF THIS.AllowModalMessages
         IF VARTYPE(cTitle) = "C"
            RETURN ;
            MESSAGEBOX(TRANS(cMessage), ;
                       VAL(TRANS(iParams)),cTitle)
         ELSE
            RETURN  ;
            MESSAGEBOX(TRANS(cMessage), ;
                       VAL(TRANS(iParams)),THIS.AppName)
         ENDIF
      ELSE
         THIS.DoStatus(cMessage)
         RETURN 0
      ENDIF
   ENDIF
ENDPROC
```
