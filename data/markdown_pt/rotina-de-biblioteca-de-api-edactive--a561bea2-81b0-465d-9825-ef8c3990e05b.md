# Rotina de biblioteca de API _EdActive( )

Permite ocultar (desativar) ou mostrar (ativar) o intervalo de seleção ou a posição do ponto de inserção na janela especificada.

```foxpro
void _EdActive(WHANDLE wh, int Show)
WHANDLE wh;            /* Handle of editing window.*/
int Show;                     /* Boolean hide or show selection. */
```

# Observações

Especificar o parâmetro Show como TRUE mostra o intervalo de seleção ou a posição do ponto de inserção, e especificar Show como FALSE oculta o intervalo de seleção ou a posição do ponto de inserção.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir abre uma janela de edição para um arquivo cujo nome é passado como parâmetro e seleciona o primeiro caractere no arquivo. Usando _EdActive( ), o exemplo ativa e depois desativa a seleção.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDACTIVE
fc = FCREATE("x", 0)
FOR i = 1 TO 90
   = FPUTS(fc, REPL(ALLT(STR(i)), i), i)
ENDFOR
= FCLOSE(fc)
= EDACTIVE("x")   && Call our API routine
```

### Código C

```foxpro
#include <pro_ext.h>
FAR EdActiveEx(ParamBlk FAR *parm)
{
#define pFILENAME ((char FAR *) _HandToPtr(parm->p[0].val.ev_handle))
   WHANDLE wh;
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
   {
      _Error(182); // "Insufficient memory"
   }
   _HLock(parm->p[0].val.ev_handle);
   pFILENAME[parm->p[0].val.ev_length] = '\0';
   wh = _EdOpenFile(pFILENAME, FO_READONLY);
   _HUnLock(parm->p[0].val.ev_handle);
   _EdSelect(wh, 0, 1);
   _EdActive(wh, TRUE);
   _Execute("WAIT WINDOW 'Selection active'");
   _EdActive(wh, FALSE);
   _Execute("WAIT WINDOW 'Selection inactive'");
}
FoxInfo myFoxInfo[] = {
   {"EDACTIVE", (FPFI) EdActiveEx, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
