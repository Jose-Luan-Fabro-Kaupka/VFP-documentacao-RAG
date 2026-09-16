# Rotina de biblioteca API _DBSeek( )

Pesquisa uma tabela indexada na área de trabalho atual pelo primeiro registro cuja chave de índice corresponda ao valor val.

```foxpro
long _DBSeek(Value FAR *val)
Value FAR *val;            /* Sought value. */
```

# Observações

Se _DBSeek( ) encontrar um registro correspondente, move o ponteiro de registro para o registro correspondente e retorna o número do registro. A correspondência deve ser exata, a menos que SET EXACT esteja definido como OFF. Se _DBSeek( ) não encontrar um registro correspondente, retorna 0. Se nenhuma correspondência for encontrada e SET NEAR estiver definido como ON, o ponteiro de registro é posicionado imediatamente após o registro correspondente mais próximo. Se SET NEAR estiver definido como OFF, o ponteiro de registro é posicionado no final do arquivo.

Se o registro correspondente for um registro em buffer adicionado que não foi confirmado, o valor retornado por _DBSeek( ) difere do valor retornado por RECNO( ). RECNO( ) retorna um valor negativo, indicando que o registro está em buffer. O valor retornado por _DBSeek( ) é um a mais que o número de registros na tabela mais o número de registros em buffer antes do registro correspondente.

Se ocorrer um erro, _DBSeek( ) retorna um inteiro negativo cujo valor absoluto é um número de erro do Visual FoxPro.

Ao pesquisar um campo numérico, val deve ser definido como ev_type 'N', mesmo se esse campo não tiver casas decimais. Se val tiver um ev_type de 'I', _DBSeek( ) retornará o número de erro interno -302, "Data type mismatch".

Para obter mais informações sobre como criar uma biblioteca API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir executa um seek em qualquer índice que controla a ordem da tabela aberta na área de trabalho atual. Observe que o "?" na estrutura FoxInfo é necessário porque o tipo de expressão de índice não é conhecido.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO DBSEEK
DO CreateTest
INDEX ON ABC TAG ABC
SET ORDER TO TAG ABC
= DBSEEK("This is record 3")  && seeks ABC = "This is record 3"
LIST NEXT 1
USE
PROCEDURE CreateTest
   CREATE TABLE test (ABC C(20))
   APPEND BLANK
   REPLACE ABC WITH "This is record 1"
   APPEND BLANK
   REPLACE ABC WITH "This is record 2"
   APPEND BLANK
   REPLACE ABC WITH "This is record 3"
   APPEND BLANK
   REPLACE ABC WITH "This is record 4"
   GO TOP
RETURN
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   _DBSeek(&parm->p[0].val);
}
FoxInfo myFoxInfo[] = {
   {"DBSEEK", (FPFI) Example, 1, "?"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
