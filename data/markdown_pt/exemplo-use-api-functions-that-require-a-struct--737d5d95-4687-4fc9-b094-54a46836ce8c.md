# Exemplo Use API Functions that Require a STRUCT

Arquivo: ...\Samples\Solution\Winapi\Systime.scx

Este exemplo ilustra a chamada da função de API do Windows GetSystemTime. GetSystemTime preenche uma estrutura de valores WORD (inteiro sem sinal de 16 bits) com informações de hora do sistema.

# Declaração de função C e definição de struct

```foxpro
VOID GetSystemTime(
    LPSYSTEMTIME lpSystemTime    // address of system time structure
   );
```

Esta é a definição da struct:

```foxpro
typedef struct _SYSTEMTIME {
    WORD wYear;
    WORD wMonth;
    WORD wDayOfWeek;
    WORD wDay;
    WORD wHour;
    WORD wMinute;
    WORD wSecond;
    WORD wMilliseconds;
} SYSTEMTIME;
```

# Chamando a função no Visual FoxPro

O código Visual FoxPro passa para GetSystemTime uma referência a uma variável de caractere, que é preenchida com os valores WORD.

```foxpro
* Visual FoxPro Code: cmdSystemTime.Click
DECLARE INTEGER GetSystemTime IN win32api STRING @
cBuff=SPACE(40)
GetSystemTime(@cBuff)
```

Para recuperar as informações da variável de caractere cBuff, o código a seguir converte caracteres ASCII de 8 bits para ano e mês na variável em equivalentes de 16 bits.

```foxpro
THIS.Parent.lblYear.Caption = ALLTRIM(STR(ASC(SUBSTR(cBuff,2)) * 256 + ASC(SUBSTR(cBuff,1))))
THIS.Parent.lblMonth.Caption = MONTH_LOC + ALLTRIM(STR(ASC(SUBSTR(cBuff,4)) * 256 + ASC(SUBSTR(cBuff,3))))
```
