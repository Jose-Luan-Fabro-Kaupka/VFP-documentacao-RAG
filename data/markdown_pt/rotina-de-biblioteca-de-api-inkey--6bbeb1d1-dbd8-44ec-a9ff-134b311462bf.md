# Rotina de biblioteca de API _InKey( )

Retorna a primeira tecla pressionada durante o período de timeout.

```foxpro
int _InKey(int timeout, int flag)
int timeout;                  /* Timeout period. */
int flag;                     /* Option(s). */
```

# Observações

O período de timeout é especificado como um número de ticks do timer do sistema operacional (1000/segundo). Um período de timeout de 0 faz com que o Visual FoxPro aguarde até que o usuário pressione uma tecla. Um valor de timeout negativo faz com que _InKey( ) retorne ao programa chamador imediatamente se o usuário não pressionar uma tecla.

Você pode especificar flag como uma ou ambas as seguintes opções:
 - SHOWCURSOR ou HIDECURSOR
- MOUSEACTIVE

Use SHOWCURSOR para forçar o cursor a aparecer, ou HIDECURSOR para forçar o cursor a desaparecer. Se nenhum for especificado, o cursor respeita a configuração SYS(2002). O valor de flag adicional MOUSEACTIVE faz com que _InKey( ) trate cliques do mouse como pressionamentos de tecla. _InKey retorna 151 para um clique do mouse. Para especificar dois valores de flag, use o operador C | ou +.

> **Observação:** Rotinas idle não devem chamar _InKey().

Você pode escrever manipuladores de eventos que chamam _InKey( ), mas deve ter cuidado porque _InKey( ) chama o manipulador de eventos recursivamente.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir chama _InKey( ) do Visual FoxPro com duas flags.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO INKEY
#define SHOWCURSOR   1
#define HIDECURSOR   2
#define MOUSEACTIVE 4
= XINKEY(0, SHOWCURSOR + MOUSEACTIVE)
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   _RetInt(_InKey((int) parm->p[0].val.ev_long,
      (int) parm->p[1].val.ev_long), 10);
}
FoxInfo myFoxInfo[] = {
   {"XINKEY", (FPFI) Example, 2, "I,I"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
