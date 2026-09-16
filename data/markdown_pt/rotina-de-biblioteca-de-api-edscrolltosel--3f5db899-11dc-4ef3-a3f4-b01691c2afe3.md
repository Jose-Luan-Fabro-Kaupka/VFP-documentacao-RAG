# Rotina de biblioteca de API _EdScrollToSel( )

Garante que o texto selecionado na janela designada esteja visível.

```foxpro
void _EdScrollToSel(WHANDLE wh, int Center)
WHANDLE wh;            /* Handle of editing window. */
int Center;                  /* Whether to center anchor point in
 window. */
```

# Observações

Especifique Center como TRUE para centralizar o ponto de ancoragem verticalmente na janela, ou como FALSE para não centralizar o ponto de ancoragem.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir abre para edição um arquivo especificado por um parâmetro. O exemplo faz uma seleção perto da parte inferior do arquivo. Depois que o usuário pressiona uma tecla em resposta a um comando WAIT do Visual FoxPro, o exemplo rola a janela de edição até a seleção chamando _EdScrollToSel( ). O exemplo então repete a operação para uma seleção feita perto da parte superior do arquivo.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDSCTOSE
= TOSEL("x")
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
   _EdScrollToPos(wh, 0, TRUE);
   _EdGetEnv(wh, &EdEnv);
   _EdSelect(wh, EdEnv.length - 16, EdEnv.length);
   _PutStr("\nMade selection at end of file.");
   _Execute("WAIT WINDOW 'Press any key to scroll to selection.'");
   _EdScrollToSel(wh, TRUE);
   _EdSelect(wh, 1, 16);
   _PutStr("\nMade selection at beginning of file.");
   _Execute("WAIT WINDOW 'Press any key to scroll to selection.'");
   _EdScrollToSel(wh, TRUE);
}
FoxInfo myFoxInfo[] = {
   {"TOSEL", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
