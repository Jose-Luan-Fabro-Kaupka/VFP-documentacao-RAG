# Função DATE( )

Retorna a data atual do sistema, controlada pelo sistema operacional, ou cria um valor Date compatível com o ano 2000.

```foxpro
DATE([nYear, nMonth, nDay])
```

#### Parâmetros
 **nYear**
Especifica o ano retornado no valor Date compatível com o ano 2000. nYear pode ser um valor de 100 a 9999.
**nMonth**
Especifica o mês retornado no valor Date compatível com o ano 2000. nMonth pode ser um valor de 1 a 12.
**nDay**
Especifica o dia retornado no valor Date compatível com o ano 2000. nDay pode ser um valor de 1 a 31.

# Valor de retorno

Date

# Observações

DATE( ) retorna a data atual do sistema se for emitida sem os argumentos opcionais. Inclua os argumentos opcionais para retornar um valor Date compatível com o ano 2000 no formato definido na guia Regional da caixa de diálogo Opções da caixa de diálogo Opções (Visual FoxPro). Qualquer parâmetro NULL é substituído pelo valor atual do sistema.

Nenhum comando ou função do Microsoft Visual FoxPro pode alterar diretamente a data do sistema.

# Exemplo

O exemplo a seguir exibe a data atual do sistema com e sem o século e depois exibe uma data compatível com o ano 2000.

```foxpro
CLEAR
SET CENTURY OFF
? DATE()  && Displays today's date without the century
SET CENTURY ON
? DATE()  && Displays today's date with the century
? DATE(1998, 02, 16)  && Displays a year 2000-compliant Date value
```
