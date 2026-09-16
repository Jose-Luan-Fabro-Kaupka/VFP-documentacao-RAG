# Rotina de biblioteca de API _EdGetPos( )

Retorna a posição de deslocamento atual do ponto de inserção no arquivo da janela de edição especificada.

```foxpro
EDPOS _EdGetPos(WHANDLE wh)
WHANDLE wh;            /* Handle of editing window. */
```

# Observações

Se houver texto selecionado, _EdGetPos( ) retornará a posição de deslocamento da âncora.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir abre uma sessão de edição para um arquivo especificado por parâmetro. Depois de definir o ponto de inserção atual com _EdSetPos( ), chama _EdGetPos( ) para verificar se retorna sua posição de deslocamento. Depois de selecionar texto com _EdSelect( ), chama _EdGetPos( ) para verificar se retorna a posição de deslocamento da âncora.

### Código do Visual FoxPro

```foxpro
SET LIBRARY TO EDGETPOS
= EDGETPOS("x")
```

### Código C

```foxpro
#include <pro_ext.h>
void putLong(long n)
{
   Value val;
   val.ev_type = 'I';
   val.ev_long = n;
   val.ev_width = 6;
   _PutValue(&val);
}
FAR Example(ParamBlk FAR *parm)
{
#define pFILENAME ((char FAR *) _HandToPtr(parm->p[0].val.ev_handle))
   WHANDLE wh;
   EDPOS edpos;
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
   {
      _Error(182); // "Insufficient memory"
   }
   pFILENAME[parm->p[0].val.ev_length] = '\0';
   _HLock(parm->p[0].val.ev_handle);
   wh = _EdOpenFile(pFILENAME, FO_READONLY);
   _HUnLock(parm->p[0].val.ev_handle);
   _EdSetPos(wh, 19);
   _PutStr("\n_EdSetPos(wh, 19)");
   edpos = _EdGetPos(wh);
   _PutStr("\n_EdGetPos(wh) ="); putLong(edpos);
   _EdSelect(wh, 5, 12);
   _PutStr("\n_EdSelect(wh, 5, 12)");
   edpos = _EdGetPos(wh);
   _PutStr("\n_EdGetPos(wh) ="); putLong(edpos);
}
FoxInfo myFoxInfo[] = {
   {"EDGETPOS", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
