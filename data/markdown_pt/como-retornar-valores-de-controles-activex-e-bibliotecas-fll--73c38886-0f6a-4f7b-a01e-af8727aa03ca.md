# Como: retornar valores de controles ActiveX e bibliotecas FLL

Você pode retornar valores de controles ActiveX ou bibliotecas de vínculo dinâmico do Visual FoxPro (FLL) para o Visual FoxPro.

### Para retornar valores de controles ActiveX para o Visual FoxPro
- Use a instrução RETURN no controle e passe um único valor.

O exemplo a seguir usa uma instrução RETURN para retornar o número da versão armazenado em VERSION:

```foxpro
#define VERSION 101
// other code here
long CPyCtrl::GetVersion()
{
   // set the version number here in variable fVersion
   return VERSION;
}
```

# Retornando valores de bibliotecas FLL

Quando você deseja retornar valores de bibliotecas FLL, use funções de API, não comandos nativos de C ou C++.

> **Observação:** Ao retornar valores de um arquivo de controle ActiveX (.ocx), não use as funções de API para retornar valores de bibliotecas FLL. Em vez disso, use a instrução RETURN.

### Para retornar valores de uma biblioteca FLL
- Use as funções de API listadas na tabela a seguir.

As seguintes funções de API devem ser usadas somente para bibliotecas FLL.

| Função | Descrição |
| --- | --- |
| _RetChar(char *string) | Define o valor de retorno da função como uma cadeia de caracteres terminada em nulo. |
| _RetCurrency(CCY cval, int width) | Define o valor de retorno da função como um valor de moeda. |
| _RetDateStr(char *string) | Define o valor de retorno da função como uma data. A data é especificada no formato mm/dd/aa[aa]. |
| _RetDateTimeStr(char *string) | Define o valor de retorno da função como uma data e hora especificadas no formato mm/dd/aa[aa] hh:mm:ss. |
| _RetFloat(double flt, int width, int dec) | Define o valor de retorno da função como um valor de ponto flutuante. |
| _RetInt(long ival, int width) | Define o valor de retorno da função como um valor numérico. |
| _RetLogical(int flag) | Define o valor de retorno da função como um valor lógico. Zero é considerado FALSE. Qualquer valor diferente de zero é considerado TRUE. |
| _RetVal(Value *val) | Passa uma estrutura Value completa do Visual FoxPro; qualquer tipo de dados do Visual FoxPro, exceto memo, pode ser retornado. Você deve chamar _RetVal( ) para retornar uma cadeia de caracteres que contém caracteres nulos embutidos ou para retornar um valor .NULL. |

> **Observação:** Para retornar o valor de um tipo de dados de objeto, use a função _RetVal(), preenchendo o campo ev_object na estrutura Value.

O exemplo a seguir, `Sum`, aceita uma referência a um campo numérico em uma tabela e usa `_RetFloat` para retornar a soma dos valores no campo:

```foxpro
#include <Pro_ext.h>
Sum(ParamBlk *parm)
{
// declare variables
double tot = 0, rec_cnt;
int i = 0, workarea = -1; // -1 is current workarea
Value val;
// GO TOP
_DBRewind(workarea);
// Get RECCOUNT()
rec_cnt = _DBRecCount(workarea);
// Loop through table
for(i = 0; i < rec_cnt; i++)
{
   //Place value of the field into the Value structure
   _Load(&parm->p[0].loc, &val);
   // add the value to the cumulative total
   tot += val.ev_real;
   // SKIP 1 in the workarea
   _DBSkip(workarea, 1);
}
// Return the sum value to Visual FoxPro
_RetFloat(tot, 10, 4);
}
// The Sum function receives one Reference parameter
FoxInfo myFoxInfo[] = {
   {"SUM", Sum, 1,"R"}
};
FoxTable _FoxTable = {
   (FoxTable *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```

Supondo que haja um campo numérico chamado `amount` na tabela aberta atualmente, a seguinte linha de código em um programa Visual FoxPro chama a função:

```foxpro
? SUM(@amount)
```
