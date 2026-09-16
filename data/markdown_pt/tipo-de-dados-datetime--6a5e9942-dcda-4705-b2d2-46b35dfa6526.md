# Tipo de dados DateTime

Para armazenar valores que são datas e horas ou apenas datas, use o tipo de dados DateTime. Um valor DateTime é armazenado em oito bytes — dois inteiros de quatro bytes.

As versões 5.0 e posteriores do Visual FoxPro suportam um formato Date e DateTime rigoroso que fornece conformidade com o ano 2000. É recomendável usar formatos de data rigorosos para todas as constantes e expressões Date e DateTime. Para obter mais informações, consulte Propriedade StrictDateEntry.

Nos tipos de dados Date e DateTime, as seguintes regras se aplicam:
 - {00:00:00AM} é equivalente a {12:00:00AM}, meia-noite.
- {00:00:00PM} é equivalente a {12:00:00PM}, meio-dia.
- {00:00:00} a {11:59:59} é equivalente a {12:00:00AM} a {11:59:59AM}
- {12:00:00} a {23:59:59} é equivalente a {12:00:00PM} a {11:59:59PM}

Para mais especificações sobre o tipo de dados DateTime, consulte Tipos de dados e campos do Visual FoxPro.
