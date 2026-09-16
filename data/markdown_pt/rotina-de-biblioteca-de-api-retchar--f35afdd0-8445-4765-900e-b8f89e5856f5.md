# Rotina de biblioteca de API _RetChar( )

Define o valor de retorno da biblioteca como uma cadeia de caracteres terminada em nulo.

```foxpro
void _RetChar(char FAR *string)
char FAR *string;            /* String. */
```

# Observações

Se você precisar retornar uma cadeia de caracteres que possa conter caracteres nulos incorporados, use a função _RetVal( ).

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir faz duas chamadas a _RetChar( ), demonstrando que o controle retorna à rotina de API a partir de _RetChar( ) e que o último _RetChar( ) determina o valor retornado ao Visual FoxPro.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO RETCHAR
```

### Código C

```foxpro
#include <pro_ext.h>
void FAR chars(ParamBlk FAR *parm)
{
   char message[] = "Hello, world";
   _RetChar(message);
}
FoxInfo myFoxInfo[] = {
   {"CHARS", (FPFI) chars, 0, ""}
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
