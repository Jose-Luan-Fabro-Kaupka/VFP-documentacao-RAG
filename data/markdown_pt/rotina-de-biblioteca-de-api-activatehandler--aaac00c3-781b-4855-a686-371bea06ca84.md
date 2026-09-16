# Rotina de biblioteca de API _ActivateHandler( )

Adiciona uma função handler ao final da lista de handlers de eventos.

```foxpro
unsigned int _ActivateHandler(FPFI handler)
FPFI handler               /* Event handler to be added. */
```

# Observações

_ActivateHandler( ) retorna um identificador inteiro para este handler. Use este identificador para remover o handler da lista do processador de eventos com _DeActivateHandler( ).

O handler é invocado com dois parâmetros: o WHANDLE da janela à qual o evento pertence e um ponteiro FAR (32 bits) para um registro de evento. Se seu handler não procura um evento, ou modifica um evento para handlers de eventos subsequentes, ele retorna False (0) para indicar que o evento ainda deve ser passado para outros handlers ou para as rotinas de interface do Visual FoxPro. Se o handler determina que o evento não precisa ser passado adiante, ele retorna True (um inteiro diferente de 0) para indicar que o evento foi tratado.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir ativa um handler de eventos quando a biblioteca é carregada. O handler de eventos imprime uma mensagem para cada evento e deixa o Visual FoxPro processar o evento normalmente. O handler de eventos é desativado quando a biblioteca é descarregada.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO ACTIHAND
WAIT WINDOW TO m.test TIMEOUT 5
SET LIBRARY TO
```

### Código C

```foxpro
#include <pro_ext.h>
static int HandlerID;
//   This is the routine that is registered as an event handler.
FAR EventHandler(WHandle theWindow, EventRec FAR *ev)
{
   _PutStr("\nEventHandler() called.");
   return NO;   // event still needs to be handled by Visual FoxPro
}
FAR Activate()
{
   HandlerID = _ActivateHandler(EventHandler);
}
//   When the library is unloaded we must deactivate the event handler
//   in a CALLONUNLOAD function.
FAR DeActivate()
{
   _DeActivateHandler(HandlerID);
}
FoxInfo myFoxInfo[] = {
   {"ACTIVATE",  Activate,   CALLONLOAD, ""},
   {"DEACTIVATE", DeActivate, CALLONUNLOAD, ""}
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
