# Função DATETIME( )

Retorna a data e hora atuais como um valor DateTime, ou cria um valor DateTime compatível com o ano 2000.

```foxpro
DATETIME([nYear, nMonth, nDay [, nHours [, nMinutes [, nSeconds]]]])
```

#### Parâmetros
 **nYear**
Especifica o ano retornado no valor DateTime compatível com o ano 2000. nYear pode ser um valor de 100 a 9999.
**nMonth**
Especifica o mês retornado no valor DateTime compatível com o ano 2000. nMonth pode ser um valor de 1 a 12.
**nDay**
Especifica o dia retornado no valor DateTime compatível com o ano 2000. nDay pode ser um valor de 1 a 31.
**nHours**
Especifica as horas retornadas no valor DateTime compatível com o ano 2000. nHours pode ser um valor de 0 (meia-noite) a 23 (23h). Padrão 0 se omitido.
**nMinutes**
Especifica os minutos retornados no valor DateTime compatível com o ano 2000. nMinutes pode ser um valor de 0 a 59. Padrão 0 se omitido.
**nSeconds**
Especifica os segundos retornados no valor DateTime compatível com o ano 2000. nSeconds pode ser um valor de 0 a 59. Padrão 0 se omitido.

# Valor de retorno

DateTime

# Observações

DATETIME( ) retorna o DateTime do sistema atual se emitido sem os argumentos opcionais. Quaisquer parâmetros de data NULL são substituídos por valores do sistema atual. Um parâmetro de hora NULL é substituído por 12:00:00.

Inclua os argumentos opcionais para retornar um valor DateTime compatível com o ano 2000 no formato especificado na guia Regional, Options Dialog Box da caixa de diálogo Options Dialog Box (Visual FoxPro).

# Exemplo

Este primeiro exemplo armazena o Datetime para o Ano Novo em uma variável chamada `tNewyear` e armazena o Datetime atual em uma variável chamada `tToday`. O número de segundos entre o Datetime atual e o Ano Novo é então exibido.

O segundo exemplo usa DATETIME( ) para criar um valor DateTime compatível com o ano 2000.

```foxpro
tNewyear = DATETIME(YEAR(DATE() ) + 1, 1, 1)  && Next New Year
tToday = DATETIME()
nSecondstonewyear = tNewyear - tToday
CLEAR
? "There are " + ALLTRIM (STR(nSecondstonewyear)) ;
   + " seconds to the next New Year."
CLEAR
SET CENTURY ON
SET DATE TO AMERICAN
? DATETIME(1998, 02, 16, 12, 34, 56) && Displays 02/16/1998 12:34:56 PM
```
