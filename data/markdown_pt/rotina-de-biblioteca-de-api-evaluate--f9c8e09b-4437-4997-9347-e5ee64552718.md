# Rotina de biblioteca de API _Evaluate( )

Compila e executa uma expressão do Visual FoxPro que você especifica com expr, colocando o resultado em res.

```foxpro
int _Evaluate(Value FAR *res, char FAR *expr)
Value FAR *res;            /* Address for result. */
char FAR *expr;            /* Expression. */
```

# Observações

Você pode especificar qualquer expressão que possa ser avaliada pela função EVALUATE( ) do Visual FoxPro. Depois que a expressão é avaliada, o controle geralmente retorna à instrução C imediatamente após a chamada a _Evaluate( ). Exceções incluem a avaliação de uma expressão do Visual FoxPro que executa um comando CANCEL ou QUIT do Visual FoxPro.

_Evaluate( ) retorna o número de erro interno do Visual FoxPro para quaisquer erros que ocorram durante a avaliação da expressão do Visual FoxPro, ou retorna 0 se nenhum erro ocorrer. O conteúdo de res é válido somente quando _Evaluate( ) retorna um valor 0.

> **Observação:** Não chame _Evaluate() a partir de um manipulador de eventos.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir tem a mesma funcionalidade da função EVALUATE( ) do Visual FoxPro.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EVALUATE
? XEVAL("2 + 3")
? XEVAL("'a' + 'b'")
? XEVAL("SIN(PI()/2))")
```

### Código C

```foxpro
#include <pro_ext.h>
FAR EvaluateEx(ParamBlk FAR *parm)
{
   char FAR *expr;
   Value result;
//   Null terminate character string
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length + 1))
   {
      _Error(182); // "Insufficient memory"
   }
   _HLock(parm->p[0].val.ev_handle);
   expr = (char FAR *) _HandToPtr(parm->p[0].val.ev_handle);
   expr[parm->p[0].val.ev_length] = '\0';
   _Evaluate(&result, expr);
   _RetVal(&result);
   _HUnLock(parm->p[0].val.ev_handle);
}
FoxInfo myFoxInfo[] = {
   {"XEVAL", (FPFI) EvaluateEx, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
