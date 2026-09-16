# Rotina de biblioteca de API _EdScrollToPos( )

Garante que a posição de deslocamento que você especifica no arquivo na janela de edição designada esteja visível.

```foxpro
void _EdScrollToPos(WHANDLE wh, EDPOS thePos, int Center)
WHANDLE wh;            /* Handle of editing window. */
EDPOS thePos;               /* Offset position to make visible. */
int Center;                  /* Whether or not to center position
 in window. */
```

# Observações

_EdScrollToPos( ) não move o ponto de inserção. Especifique Center como TRUE para centralizar a posição verticalmente na janela, ou como FALSE para não centralizar a posição verticalmente.

Para mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir abre para edição um arquivo especificado por um parâmetro. Depois de rolar até o topo do arquivo chamando _EdScrollToPos( ), o procedimento chama _EdPosInView( ) para verificar se o topo e o final do arquivo estão em exibição e imprime os resultados na tela. Em seguida, rola até o final do arquivo chamando _EdScrollToPos( ) e novamente chama _EdPosInView( ) para verificar se o topo e o final do arquivo estão em exibição.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDSCTOPO
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
      parm->p[0].val.ev_length+1)) {
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
