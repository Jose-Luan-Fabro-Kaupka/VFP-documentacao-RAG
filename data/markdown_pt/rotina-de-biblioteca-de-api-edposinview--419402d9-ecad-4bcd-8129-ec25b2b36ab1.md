# Rotina de biblioteca de API _EdPosInView( )

```foxpro
int _EdPosInView(WHANDLE wh, EDPOS thePos)
WHANDLE wh;            /* Handle of editing window. */
EDPOS thePos;               /* Offset position. */
```

# Observações

_EdPosInView( ) retorna True (um inteiro diferente de 0) se a posição de deslocamento no arquivo na janela de edição especificada está visível, ou False (0) se não estiver.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir abre para edição um arquivo especificado por um parâmetro. Após rolar para o topo do arquivo, o exemplo chama _EdPosInView( ) para verificar se o topo e o final do arquivo estão em visualização e os resultados são impressos na tela. Em seguida, o exemplo rola para o final do arquivo e novamente chama _EdPosInView( ) para verificar se o topo e o final do arquivo estão em visualização.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDPOSINV
= POSINVIEW("x")
```

### Código C

```foxpro
#include <pro_ext.h>
void putLong(long n)
{
   Value val;
   val.ev_type = 'I';
   val.ev_long = n;
   val.ev_width = 10;
   _PutValue(&val);
}
FAR Example(ParamBlk FAR *parm)
{
#define pFILENAME ((char FAR *) _HandToPtr(parm->p[0].val.ev_handle))
   WHANDLE wh;
   EDENV EdEnv;
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
   {
      _Error(182); // "Insufficient memory"
   }
   pFILENAME[parm->p[0].val.ev_length] = '\0';
   _HLock(parm->p[0].val.ev_handle);
   wh = _EdOpenFile(pFILENAME, FO_READONLY);
   _HUnLock(parm->p[0].val.ev_handle);
   _EdGetEnv(wh, &EdEnv);
   _EdScrollToPos(wh, 0, FALSE);
   _PutStr("\n_EdScrollToPos(wh, 0)");
   _PutStr("\n_EdPosInView(wh, 0) =");
   putLong(_EdPosInView(wh, 0));
   _PutStr("\n_EdPosInView(wh, EdEnv.length) =");
   putLong(_EdPosInView(wh, EdEnv.length));
   _EdScrollToPos(wh, EdEnv.length, FALSE);
   _PutStr("\n_EdScrollToPos(wh, EdEnv.length)");
   _PutStr("\n_EdPosInView(wh, 0) =");
   putLong(_EdPosInView(wh, 0));
   _PutStr("\n_EdPosInView(wh, EdEnv.length) =");
   putLong(_EdPosInView(wh, EdEnv.length));
}
FoxInfo myFoxInfo[] = {
   {"POSINVIEW", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
