# Tipo de dados Date (Visual FoxPro)

Para armazenar datas sem valores de hora, use o tipo de dados Date.

O Visual FoxPro 5.0 e versões posteriores oferece suporte a um formato Date e DateTime rigoroso que fornece conformidade com o ano 2000. É recomendável usar formatos de data rigorosos para todas as constantes e expressões Date e DateTime. Para obter mais informações, consulte StrictDateEntry Property.

Nos tipos de dados Date e DateTime, as seguintes regras se aplicam:
 - {00:00:00AM} é equivalente a {12:00:00AM}, meia-noite.
- {00:00:00PM} é equivalente a {12:00:00PM}, meio-dia.
- {00:00:00} a {11:59:59} é equivalente a {12:00:00AM} a {11:59:59AM}.
- {12:00:00} a {23:59:59} é equivalente a {12:00:00PM} a {11:59:59PM}.

Para mais especificações sobre o tipo de dados Date, consulte Visual FoxPro Data and Field Types.
