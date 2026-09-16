# Rotina de biblioteca API _ErrorInfo( )

Retorna o número de erro externo que corresponde ao número de erro interno do Visual FoxPro especificado por code.

```foxpro
int _ErrorInfo(int code, char FAR *message)
int code;                     /* Internal Visual FoxPro error number. */
char FAR *message;         /* Pointer to space for an error message. */
```

# Observações

O parâmetro message é um ponteiro para uma cadeia de caracteres que é a mensagem de erro do Visual FoxPro. Se message não for um ponteiro nulo, o Visual FoxPro preenche o texto da mensagem de erro associado ao número de erro externo.

Para obter mais informações sobre como criar uma biblioteca API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir mostra as informações retornadas por _ErrorInfo( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO ERRORINF
= ERRORINFO(0)
= ERRORINFO(1)
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
void FAR ErrorInfo(ParamBlk FAR *parm)
{
   int ext;
   char FAR *message;
   if ((message =_Alloca(128)) == 0)
   {
      _Error(182); // "Insufficient memory"
   }
   ext = _ErrorInfo((int) parm->p[0].val.ev_long, message);
   _PutChr('\n'); putLong(ext); _PutStr(" "); _PutStr(message);
}
FoxInfo myFoxInfo[] = {
   {"ERRORINFO", (FPFI) ErrorInfo, 1, "I"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
