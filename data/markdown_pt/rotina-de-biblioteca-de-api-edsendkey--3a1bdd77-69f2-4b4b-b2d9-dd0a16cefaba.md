# Rotina de biblioteca de API _EdSendKey( )

Simula a pressão de tecla associada ao número de caractere ASCII especificado por charNum.

```foxpro
void _EdSendKey(WHANDLE wh, int charNum)
WHANDLE wh;            /* Handle of editing window. */
int charNum;               /* Number of character. */
```

# Exemplo

O exemplo a seguir abre para edição um arquivo especificado por um parâmetro. Ele insere uma linha de texto, "Hello, World", enviando os caracteres individuais com _EdSendKey( ). Em seguida, usa _EdSendKey( ) para enviar um carriage return e linefeed e para inserir um caractere de escape ASCII. Observe que o caractere de escape não é interpretado como "descartar sessão de edição".

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDSENDKE
= SENDKEY("x")
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
   wh = _EdOpenFile(pFILENAME, FO_READWRITE);
   _HUnLock(parm->p[0].val.ev_handle);
   // Insert a line of text using _EdSendKey()
   _EdSetPos(wh, 0);
   _EdSendKey(wh, 'H');
   _EdSendKey(wh, 'e');
   _EdSendKey(wh, 'l');
   _EdSendKey(wh, 'l');
   _EdSendKey(wh, 'o');
   _EdSendKey(wh, ',');
   _EdSendKey(wh, ' ');
   _EdSendKey(wh, 'W');
   _EdSendKey(wh, 'o');
   _EdSendKey(wh, 'r');
   _EdSendKey(wh, 'l');
   _EdSendKey(wh, 'd');
   _EdSendKey(wh, '.');
   _EdSendKey(wh, 0x0d); // carriage return
   _EdSendKey(wh, 0x0a); // line feed
   _EdSendKey(wh, 0x1b); // esc char code is inserted in file
}
FoxInfo myFoxInfo[] = {
   {"SENDKEY", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
