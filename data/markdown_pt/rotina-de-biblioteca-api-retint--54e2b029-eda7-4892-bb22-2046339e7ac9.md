# Rotina de biblioteca API _RetInt( )

Define o valor de retorno da biblioteca como um valor numérico.

```foxpro
void _RetInt(long ival, int width)
long ival;                     /* Long integer value. */
int width;                     /* Number of columns to display number. */
```

# Observações

O parâmetro width especifica o número de colunas que o Visual FoxPro usa ao exibir o número. Se você não conhece a largura, use 10.

Para obter mais informações sobre como criar uma biblioteca API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir executa algumas operações na tabela aberta na área de trabalho atual. Ele exibe o valor retornado por _RecCount( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO RETINT
? CTEST()
```

### Código C

```foxpro
#include  <pro_ext.h>
#define nl _PutChr('\n')
long FAR CTest()
{
   long rc,rec;
   int workarea = -1;
   int flag = 0;
   int rn,recn;
   rc = _DBRewind(workarea);
   _PutStr("top");  nl;
   rc = _DBSkip(workarea, 5);
   _PutStr("skipped 5");  nl;

   rc = _DBAppend(workarea,flag);
   _PutStr("Appending"); nl;
   rc = _DBRewind(workarea);
   _PutStr("top");  nl;
   rn = _DBRecCount(workarea);
   _RetInt(rn, 10);
   rec = rn;
   return rn;
}
FoxInfo myFoxInfo[] = {
   {"CTEST", (FPFI) CTest,0 , ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *)0, sizeof(myFoxInfo) / sizeof(FoxInfo), myFoxInfo
};
```
