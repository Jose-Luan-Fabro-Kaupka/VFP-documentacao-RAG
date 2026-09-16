# Rotina de biblioteca de API _Load( )

Coloca o valor da variável de memória ou campo de registro atual especificado por loc em val.

```foxpro
int _Load(Locator FAR *loc, Value FAR *val)
Locator FAR *loc;         /* Variable location. */
Value FAR *val;            /* Holds value of the variable. */
```

# Observações

_Load( ) retorna 0 se a rotina for bem-sucedida. Se a rotina falhar, retorna um inteiro negativo cujo valor absoluto é um número de erro do Visual FoxPro. Você pode usar _Load( ) para recuperar o conteúdo de um campo memo, mas não recupera caracteres no campo após os primeiros 65.000 bytes. Se loc especificar um array unidimensional, o Visual FoxPro retorna o valor do primeiro elemento do array.

_Load( ) não funciona com objetos. Se loc especificar uma referência de objeto, _Load( ) retorna 0 sem preencher a estrutura Value val. Use _Evaluate( ) para obter uma referência de objeto.

Se a configuração do campo Locator l_offset for – 1, o Visual FoxPro retorna uma estrutura de valor lógico que indica se o registro atual na área de trabalho especificada está excluído:
 - ev_length = .T. = DELETED( )
- ev_length = .F. = NOT DELETED( ) Observação _Load() cria um handle somente quando a variável de memória que seu programa está carregando é uma cadeia de caracteres (ev_type = 'C'). Todos os outros tipos de dados armazenam seus valores na própria estrutura Value. Seu programa deve liberar os handles criados com _Load().

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir converte para maiúsculas um argumento de cadeia de caracteres passado por referência.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO LOAD
x = "abc"
= XUPPER(@x)
? x
```

### Código C

```foxpro
#include <pro_ext.h>
void FAR Upper(ParamBlk FAR *parm)
{
      char FAR *pString;
      Value val;
      int i;
//
//   _Load() and _Store are the functions of interest for pass-by-reference.
//
   _Load(&parm->p[0].loc, &val);
//
//   FoxPro doesn't check the type of pass-by-reference arguments, so we do.
//
  if (val.ev_type != 'C')
   {
      _Error(9); // "Data type mismatch"
   }
  pString = _HandToPtr(val.ev_handle);
   for (i = 0; i < val.ev_length; i++)
   {
      if ('a' <= *pString && *pString <= 'z')
      {
         *pString += ('A' - 'a');
      }
      pString++;
   }
   _Store(&parm->p[0].loc, &val);
   //
   // We need to free the handle that we created with  _LOAD()
   //
   _FreeHand(val.ev_handle);
}
FoxInfo myFoxInfo[] =
{
   {"XUPPER", (FPFI) Upper, 1, "R"},
};
FoxTable _FoxTable =
{
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
