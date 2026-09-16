# Rotina de biblioteca da API _ActivateIdle( )

Adiciona uma função manipuladora de ociosidade ao final da lista de manipuladores de eventos de ociosidade chamados quando o Visual FoxPro aguarda uma entrada do usuário ou o tempo limite de um evento.

```foxpro
unsigned int _ActivateIdle(FPFI handler)
FPFI handler               /* Event handler. */
```

# Observações

_ActivateIdle( ) retorna um identificador inteiro para essa rotina. Use o identificador para remover o manipulador de eventos de ociosidade do loop ocioso com _DeActivateIdle( ).

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir ativa um manipulador de eventos de ociosidade quando a biblioteca é carregada. O manipulador apenas imprime uma mensagem. Ele é desativado quando a biblioteca é descarregada.

### Código do Visual FoxPro

```foxpro
SET LIBRARY TO ACTIIDLE
WAIT WINDOW TO m.test TIMEOUT 5
SET LIBRARY TO
```

### Código C

```foxpro
#include <pro_ext.h>
static unsigned IdlerID;
//   This is the routine that is registered as an idle event handler.
void FAR IdleHandler(WHandle wh, EventRec *ev)
{
   _PutStr("\nIdleHandler() called.");
}
void FAR Activate(ParamBlk FAR *parm)
{
   IdlerID = _ActivateIdle((FPFI) IdleHandler);
}
//   When the library is unloaded we must deactivate the idle event
//   handlerin a CALLONUNLOAD function.
void FAR DeActivate(ParamBlk FAR *parm)
{
   _DeActivateIdle(IdlerID);
}
FoxInfo myFoxInfo[] = {
   {"ACTIVATE",  (FPFI) Activate, CALLONLOAD,   ""},
   {"DEACTIVATE",  (FPFI) DeActivate, CALLONUNLOAD, ""}
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
