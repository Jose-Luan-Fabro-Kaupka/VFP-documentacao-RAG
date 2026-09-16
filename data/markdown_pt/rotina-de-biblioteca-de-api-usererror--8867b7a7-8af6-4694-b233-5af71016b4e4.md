# Rotina de biblioteca de API _UserError( )

Relata um erro com o texto terminado em nulo que você especificar em message.

```foxpro
void _UserError(char FAR *message)
char FAR *message;         /* Error message. */
```

# Observações

O código interno do Visual FoxPro para este erro é 98. O código retornado pela função ERROR( ) do Visual FoxPro é 1098. A função MESSAGE( ) do Visual FoxPro retorna ao usuário a mensagem especificada por você. O controle é passado ao manipulador de erros do Visual FoxPro e não retorna.

> **Observação:** Não chame _UserError() em uma rotina CALLUNLOAD: a biblioteca não será carregada, devido à chamada _UserError(), e nenhuma mensagem será exibida.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir chama _UserError( ), demonstrando que a execução não retorna à rotina de API após _UserError( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EXAMPLE
= EXAMPLE()
```

### Código C

```foxpro
#include <pro_ext.h>
FAR UserErrorEx(ParamBlk FAR *parm)
{
   _UserError("This is a _UserError() example.");
   _PutStr("This should never be displayed.");
}
FoxInfo myFoxInfo[] = {
   {"EXAMPLE", (FPFI) UserErrorEx, 0, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
