# Rotina de biblioteca de API _DeActivateHandler( )

_DeActivateHandler( ) remove o manipulador de eventos especificado da lista de processadores de eventos.

```foxpro
void _DeActivateHandler(unsigned int EventIdentifier)
unsigned int EventIdentifier;      /* ID of event handler
 to be removed from list. */
```

# Observações

Você deve remover cada manipulador de eventos, indicado por EventIdentifier, da lista de manipuladores quando sua biblioteca é descarregada.

Para mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir ativa um manipulador de eventos quando a biblioteca é carregada. O manipulador de eventos imprime uma mensagem para cada evento e permite que o Visual FoxPro processe a mensagem. O manipulador de eventos é desativado quando a biblioteca é descarregada. Como no exemplo a seguir, _DeActivateHandler( ) geralmente é chamado de uma função CALLONUNLOAD.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO DEACTHAN
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
   {"ACTIVATE",  (FPFI) Activate, CALLONLOAD, ""},
   {"DEACTIVATE", (FPFI)  DeActivate, CALLONUNLOAD, ""}
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
