# Rotina de biblioteca de API _BreakPoint( )

_BreakPoint( ) é uma macro que gera a instrução de breakpoint do depurador, INT 3 e pode ser útil para depurar rotinas externas.

```foxpro
void _BreakPoint(void any)
void any;                     /* Pointer. */
```

# Observações

Quando uma chamada _BreakPoint( ) é encontrada, o controle é transferido ao seu depurador. A maioria dos depuradores retorna o controle à linha do programa que inclui a instrução INT3, e você precisa incrementar manualmente o ponteiro de instrução (IP) além desta instrução. Nesse momento, você pode usar seu depurador para definir breakpoints adicionais. Sempre remova quaisquer breakpoints antes de sair da rotina externa. Para obter mais informações sobre depuração, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir usa a macro _BreakPoint( ) para colocar um INT 3 que os depuradores reconhecem como um breakpoint.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO BPOINT
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   int RetValue;
   _BreakPoint(); // debugger breaks execution here
   _HLock(parm->p[0].val.ev_handle);
   _HLock(parm->p[1].val.ev_handle);
   RetValue = _StrCmp(_HandToPtr(parm->p[0].val.ev_handle),
      _HandToPtr(parm->p[1].val.ev_handle));
   _RetInt(RetValue, 10); // does return control here
   _HUnLock(parm->p[0].val.ev_handle);
   _HUnLock(parm->p[1].val.ev_handle);
}
FoxInfo myFoxInfo[] = {
   {"STRCMP", (FPFI) Example, 2, "C,C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
