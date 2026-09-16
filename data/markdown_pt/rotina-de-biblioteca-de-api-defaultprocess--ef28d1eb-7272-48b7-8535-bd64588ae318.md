# Rotina de biblioteca de API _DefaultProcess( )

Fornece o processamento de eventos padrão para um evento retornado por _GetNextEvent( ) quando o evento não precisa de tratamento especial.

```foxpro
void _DefaultProcess(EventRec FAR *event)
EventRec FAR *event;      /* Event to be processed. */
```

# Observações

Isso facilita que uma rotina externa use janelas e ainda as faça agir de forma consistente com o restante do produto.

> **Observação:** Não chame _DefaultProcess() de um manipulador de eventos.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir é um loop que consiste em uma chamada a _GetNextEvent( ) seguida de uma chamada a _DefaultProcess( ). Todos os eventos durante este procedimento recebem seu processamento padrão.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO DEFAPROC
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   EventRec ev;
   int i;
   for (i = 0; i < 16; i++)
{
      _GetNextEvent(&ev);
      _DefaultProcess(&ev);
   }
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
