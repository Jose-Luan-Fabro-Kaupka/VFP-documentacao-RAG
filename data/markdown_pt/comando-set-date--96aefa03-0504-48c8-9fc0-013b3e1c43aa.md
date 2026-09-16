# Comando SET DATE

Especifica o formato para a exibição de expressões Date e DateTime.

```foxpro
SET DATE [TO] AMERICAN | ANSI | BRITISH | FRENCH | GERMAN | ITALIAN
 | JAPAN | TAIWAN | USA | MDY | DMY | YMD| SHORT | LONG
```

# Observações

Aqui estão as configurações e os formatos de data resultantes:

| Configuração | Formato |
| --- | --- |
| AMERICAN | mm/dd/yy |
| ANSI | yy.mm.dd |
| BRITISH/FRENCH | dd/mm/yy |
| GERMAN | dd.mm.yy |
| ITALIAN | dd-mm-yy |
| JAPAN | yy/mm/dd |
| TAIWAN | yy/mm/dd |
| USA | mm-dd-yy |
| MDY | mm/dd/yy |
| DMY | dd/mm/yy |
| YMD | yy/mm/dd |
| SHORT | Formato de data curto determinado pela configuração de data curta do Painel de Controle do Windows. |
| LONG | Formato de data longo determinado pela configuração de data longa do Painel de Controle do Windows. |

> **Observação:** Quando SET DATE está definido como SHORT ou LONG, uma data anterior a {^1601-01-01} é inválida e gera um erro.

A configuração de data padrão é AMERICAN.

A configuração SET DATE também determina como a data aparece em expressões datetime.

Se DATE estiver definido como SHORT ou LONG, as configurações SET CENTURY, SET MARK, SET HOURS e SET SECONDS são ignoradas.

SET DATE tem escopo na sessão de dados atual.
