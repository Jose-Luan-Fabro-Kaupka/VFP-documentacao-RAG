# Rotina de biblioteca de API _DeActivateIdle( )

Remove a rotina especificada do loop de ociosidade.

```foxpro
void _DeActivateIdle(unsigned int IdleIdentifier)
unsigned int IdleIdentifier;         /* Rotina a ser removida
 da lista de ociosidade. */
```

# Observações

Você deve remover cada rotina de ociosidade da lista de rotinas de ociosidade quando sua biblioteca é descarregada.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir ativa um manipulador de eventos de ociosidade quando a biblioteca é carregada. O manipulador de eventos de ociosidade simplesmente imprime uma mensagem e é desativado quando a biblioteca é descarregada. Como no exemplo a seguir, _DeActivateIdle( ) geralmente é chamado de uma função CALLONUNLOAD.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO DEACTIDL
```

### Código C

```foxpro
#include <pro_ext.h>
static unsigned IdlerID;
//   Esta é a rotina registrada como manipulador de eventos de ociosidade.
void FAR IdleHandler(WHandle wh, EventRec *ev)
{
   _PutStr("\nIdleHandler() called.");
}
void FAR Activate(ParamBlk FAR *parm)
{
   IdlerID = _ActivateIdle((FPFI) IdleHandler);
}
//   Quando a biblioteca é descarregada, devemos desativar o manipulador
//   de eventos de ociosidade em uma função CALLONUNLOAD.
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
