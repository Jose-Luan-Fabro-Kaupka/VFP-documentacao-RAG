# Rotina de biblioteca de API _GetNextEvent( )

Lê o próximo evento em EventRec e retorna o tipo de evento.

```foxpro
int _GetNextEvent(EventRec FAR *event)
EventRec FAR *event;   /* Event. */
```

# Observações

Eventos nulos são gerados quando nenhuma outra atividade ocorreu. Rotinas de ociosidade não devem chamar _GetNextEvent( ). Você pode chamar _GetNextEvent( ) de um manipulador de eventos, mas deve ter cuidado, pois _GetNextEvent( ) chama o manipulador de eventos recursivamente.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir é um loop que consiste em uma chamada a _GetNextEvent( ), seguida de uma chamada a _DefaultProcess( ). Todos os eventos durante esse procedimento recebem seu processamento padrão.

### Código Visual FoxPro

```foxpro
SET LIBR TO GETNXEV
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   EventRec ev;
   int i;
   for (i = 0; i < 16; i++) {
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
