# Rotina de biblioteca de API _Execute( )

Compila e executa a instrução terminada em nulo que você especifica em stmt.

```foxpro
int _Execute(char FAR *stmt)
char FAR *stmt;            /* Statement to execute. */
```

# Observações

O parâmetro stmt pode ser qualquer comando ou função que possa ser executado a partir da janela Command. Quando a execução da instrução é concluída, o controle normalmente retorna à instrução C imediatamente após a chamada a _Execute( ). Exceções incluem a execução de código que executa um comando CANCEL ou QUIT do Visual FoxPro.

_Execute( ) retorna o número de erro interno do Visual FoxPro para qualquer erro que ocorra durante a execução da instrução, ou 0 se nenhum erro ocorrer.

> **Observação:** Não chame _Execute() a partir de um manipulador de eventos.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir usa _Execute( ) para executar a instrução Visual FoxPro passada.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EXECUTE
= EXEC("? 'Hello, world.'")
= EXEC("DISPLAY STATUS")
```

### Código C

```foxpro
#include <pro_ext.h>
FAR ExecuteEx(ParamBlk FAR *parm)
{
   char FAR *cmd;
   // Null terminate character string
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
   {
      _Error(182); // "Insufficient memory"
   }
   _HLock(parm->p[0].val.ev_handle);
   cmd = (char FAR *) _HandToPtr(parm->p[0].val.ev_handle);
   cmd[parm->p[0].val.ev_length] = '\0';
   _Execute(cmd);
   _HUnLock(parm->p[0].val.ev_handle);
}
FoxInfo myFoxInfo[] = {
   {"EXEC", (FPFI) ExecuteEx, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
