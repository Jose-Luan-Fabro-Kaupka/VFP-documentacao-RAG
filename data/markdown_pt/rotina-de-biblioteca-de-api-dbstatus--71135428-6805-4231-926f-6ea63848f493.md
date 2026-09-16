# Rotina de biblioteca de API _DBStatus( )

Retorna flags de status para a área de trabalho especificada.

```foxpro
int _DBStatus(int workarea)
int workarea;               /* Work area. */
```

# Observações

Se nenhuma tabela estiver aberta na área de trabalho especificada, _DBStatus( ) retorna um inteiro negativo cujo valor absoluto é um número de erro do Visual FoxPro. A tabela a seguir mostra os flags de status retornados:

| Flag | Configuração |
| --- | --- |
| DB_BOF | Definido nas mesmas condições que a função Visual FoxPro BOF( ). |
| DB_EOF | Definido nas mesmas condições que a função Visual FoxPro EOF( ). |
| DB_RLOCKED | Definido quando o registro atual está bloqueado, a tabela está bloqueada ou a tabela está aberta de forma exclusiva. |
| DB_FLOCKED | Definido quando a tabela está bloqueada ou a tabela está aberta de forma exclusiva. |
| DB_EXCLUSIVE | Definido quando a tabela está aberta de forma exclusiva. |
| DB_READONLY | Definido quando a tabela está aberta sem acesso de gravação. |

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir exibe o status da tabela aberta na área de trabalho atual. Ele verifica cada bit no valor retornado por _DBStatus( ) e exibe uma mensagem apropriada na tela.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO DBSTATUS
= DBSTATUS()  && displays status of DBF in current work area
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   int dbstatus = _DBStatus(-1);
   _PutStr("\nStatus of DBF in current work area:");
   if (dbstatus & DB_BOF)
      _PutStr("\nBOF()");
   if (dbstatus & DB_EOF)
      _PutStr("\nEOF()");
   if (dbstatus & DB_RLOCKED)
      _PutStr("\nCurrent record is RLOCKed");
   if (dbstatus & DB_FLOCKED)
      _PutStr("\nDatabase is FLOCKed");
   if (dbstatus & DB_EXCLUSIVE)
      _PutStr("\nDatabase is open EXCLUSIVEly");
   if (dbstatus & DB_READONLY)
      _PutStr("\nDatabase is READONLY");
}
FoxInfo myFoxInfo[] = {
   {"DBSTATUS", (FPFI) Example, 0, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
