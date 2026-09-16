# Parâmetros em bibliotecas externas

Você pode passar argumentos a parâmetros quando o Visual FoxPro chama um controle ActiveX, objeto COM ou biblioteca de vínculo dinâmico do Visual FoxPro (FLL). Por exemplo, um controle ActiveX pode aceitar argumentos ao chamar um de seus métodos. Da mesma forma, um programa Visual FoxPro pode chamar uma função em sua biblioteca FLL e passar argumentos a ela.

O Visual FoxPro pode passar argumentos a parâmetros em uma biblioteca externa por valor ou por referência. Por padrão, a configuração do comando SET UDFPARMS é respeitada. No entanto, outras variáveis, como matrizes ou campos, e expressões são passadas por valor. Para obter informações sobre como alterar a forma padrão de passar argumentos, consulte Passando dados a parâmetros.

Como controles ActiveX e objetos COM são programas padrão do Windows, nenhum mecanismo especial é necessário para passar argumentos do Visual FoxPro a parâmetros em um controle ActiveX ou objeto COM. Você pode escrever código de biblioteca como se estivesse recebendo argumentos de qualquer programa C ou C++.

No entanto, funções em uma biblioteca FLL usam a estrutura FoxInfo para receber dados do Visual FoxPro. A estrutura FoxInfo lista funções de biblioteca e o número e o tipo de parâmetros que esperam. Por exemplo, a seguinte estrutura FoxInfo pertence a uma biblioteca com uma função, internamente chamada `dates`, que aceita um parâmetro Character:

```foxpro
FoxInfo myFoxInfo[] = {
   { "DATES", (FPFI) dates, 1, "C" }
};
```

Funções que você define em bibliotecas externas na verdade recebem apenas um parâmetro, um ponteiro para o bloco de parâmetros. Este bloco de parâmetros, definido na estrutura `ParamBlk`, armazena todas as informações sobre os parâmetros que foram passados da chamada de função do Visual FoxPro. O código a seguir ilustra o formato que a declaração da sua função deve seguir:

```foxpro
void function_name(ParamBlk *parm)
```

Por exemplo, a definição de função para `dates` é:

```foxpro
void dates(ParamBlk *parm)
```

A estrutura `ParamBlk` consiste em um inteiro que representa o número de parâmetros, imediatamente seguido por uma matriz de uniões de parâmetros. A definição da estrutura está incluída em Pro_ext.h:

```foxpro
/* A parameter list to a library function.      */
typedef struct {
   short int pCount;      /* number of parameters passed */
   Parameter p[1];         /* pCount parameters */
} ParamBlk;
```

O typedef `Parameter` incluído na estrutura `ParamBlk` é uma união de uma estrutura Value e uma estrutura Locator. Chamada por valor é tratada por uma estrutura Value; chamada por referência é tratada por uma estrutura Locator. Você usa essas estruturas para acessar os parâmetros passados à sua função quando a função é chamada no Visual FoxPro.

As informações a seguir são extraídas do arquivo Pro_ext.h e mostram a definição do tipo `Parameter`:

```foxpro
/* A parameter to a library function.         */
typedef union {
   Value val;
   Locator loc;
} Parameter;
```

# Definição da estrutura Value

Se um parâmetro é passado à sua função por valor, use a estrutura Value para acessá-lo. A seguinte definição da estrutura `Value` é extraída do arquivo Pro_ext.h:

```foxpro
// An expression's value.
Typedef struct {
   char         ev_type;
   char         ev_padding;
   short         ev_width;
   unsigned      ev_length;
   long         ev_long;
   double         ev_real;
   CCY         ev_currency;
   MHANDLE      ev_handle;
   ULONG         ev_object;
} Value;
```

### Campos da estrutura Value

A tabela a seguir é um guia para os valores que você pode passar e receber na estrutura Value para diferentes tipos de dados. Apenas os campos da estrutura listados para um tipo de dados são usados para esse tipo de dados.
 Conteúdo da estrutura Value para diferentes tipos de dados
| Tipo de dados | Campo da estrutura | Valor |
| --- | --- | --- |
| Character | ev_type | 'C' |
| ev_length | string length | |
| ev_handle | MHANDLE to string | |
| Numeric | ev_type | 'N' |
| ev_width | Display width | |
| ev_length | Decimal places | |
| ev_real | Double precision | |
| Integer | ev_type | 'I' |
| ev_width | Display width | |
| ev_long | Long integer | |
| Date | ev_type | 'D' |
| ev_real | Date 1 | |
| Date Time | ev_type | 'T' |
| ev_real | Date + (seconds/86400.0) | |
| Currency | ev_type | 'Y' |
| ev_width | Display width | |
| ev_currency | Currency value 2 | |
| Logical | ev_type | 'L' |
| ev_length | 0 or 1 | |
| Memo | ev_type | 'M' |
| ev_wdith | FCHAN | |
| ev_long | Length of memo field | |
| ev_real | Offset of memo field | |
| General | ev_type | 'G' |
| ev_wdith | FCHAN | |
| ev_long | Length of general field | |
| ev_real | Offset of general field | |
| Object | ev_type | 'O' |
| ev_object | Object identifier | |
| Null | ev_type | '0' (zero) |
| ev_long | Data type | |

1. A data é representada como um número de dia juliano de ponto flutuante de precisão dupla calculado usando o Algoritmo 199 de Collected Algorithms of the ACM. 2. O valor de moeda é um inteiro longo, com um ponto decimal implícito na frente dos últimos quatro dígitos.

> **Observação:** ev_length é o único indicador verdadeiro do comprimento de uma cadeia de caracteres. A cadeia não pode ter um terminador nulo porque pode conter caracteres nulos incorporados.

# Definição da estrutura Locator

Use a estrutura Locator para manipular parâmetros passados por referência. A seguinte definição da estrutura `Locator` é extraída do arquivo Pro_ext.h:

```foxpro
typedef struct {
  char  l_type;
  short l_where, /* Database number or -1 for memory */
  l_NTI,      /* Variable name table offset*/
  l_offset,  /* Index into database*/
  l_subs,  /* # subscripts specified 0 <= x <= 2 */
  l_sub1, l_sub2; /* subscript integral values */
} Locator;
```

### Campos da estrutura Locator

A tabela a seguir é um guia para os campos na estrutura Locator.

| Campo Locator | Uso do campo |
| --- | --- |
| l_type | 'R' |
| l_where | O número da tabela que contém este campo, ou – 1 para uma variável. |
| l_NTI | Name Table Index. Uso interno do Visual FoxPro. |
| l_offset | Número do campo na tabela. Uso interno do Visual FoxPro. |
| l_subs | Somente para variáveis, o número de subscritos (0 – 2). |
| l_sub1 | Somente para variáveis, o primeiro subscrito se l_subs não for 0. |
| l_sub2 | Somente para variáveis, o segundo subscrito se l_subs for 2. |

> **Observação:** É uma boa prática de programação verificar o tipo de parâmetro em ev_type para ajudar a determinar quais campos acessar da estrutura Value.

#### Um exemplo de acesso a parâmetros em uma biblioteca FLL

O exemplo a seguir usa `_StrCpy( )` para retornar um tipo Character ao Visual FoxPro que é a concatenação de seus dois parâmetros Character. Observe que, embora o handle de cada estrutura Value do parâmetro seja usado como memória de trabalho para realizar a concatenação, alterações nesta alocação de memória não afetam o argumento Visual FoxPro que foi passado por valor.

```foxpro
#include <Pro_ext.h>
Example(ParamBlk *parm)
{
// make the paramBlk structure easier
// to manage by using #define shortcuts
#define p0 (parm->p[0].val)
#define p1 (parm->p[1].val)
// make sure there is enough memory
if (!_SetHandSize(p0.ev_handle, p0.ev_length + p1.ev_length))
   _Error(182); // "Insufficient memory"
// lock the handles
_HLock(p0.ev_handle);
_HLock(p1.ev_handle);
// convert handles to pointers and make sure the
// strings are null-terminated
((char *)_HandToPtr(p0.ev_handle))[p0.ev_length] = '\0';
((char *)_HandToPtr(p1.ev_handle))[p1.ev_length] = '\0';
// concatenate strings using the API function _StrCpy
_StrCpy((char *)_HandToPtr(p0.ev_handle) + p0.ev_length,
_HandToPtr(p1.ev_handle));
// return the concatenated string to Visual FoxPro
_RetChar(_HandToPtr(p0.ev_handle));
// unlock the handles
_HUnLock(p0.ev_handle);
_HUnLock(p1.ev_handle);
}
FoxInfo myFoxInfo[] = {
   {"STRCAT", Example, 2, "CC"},
};
FoxTable _FoxTable = {
   (FoxTable *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
