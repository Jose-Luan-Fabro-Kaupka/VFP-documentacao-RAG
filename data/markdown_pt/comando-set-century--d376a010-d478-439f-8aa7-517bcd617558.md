# Comando SET CENTURY

Determina se o Microsoft Visual FoxPro exibe a porção do século em expressões de data e como o Visual FoxPro interpreta datas que especificam apenas anos com 2 dígitos.

```foxpro
SET CENTURY ON | OFF | TO [nCentury [ROLLOVER nYear]]
```

#### Parâmetros
 **ON**
Especifica um ano com quatro dígitos em um formato que inclui 10 caracteres (incluindo delimitadores de data). Observação Para fornecer conformidade com o ano 2000, é recomendado que você sempre defina SET CENTURY como ON.
**OFF**
(Padrão) Especifica um ano com dois dígitos em um formato que inclui oito caracteres e assume o século vinte para cálculos de data.
**TO nCentury**
Um número de 1 a 99 que especifica o século atual. Quando uma data tem um ano com dois dígitos, nCentury determina em qual século o ano ocorre. O valor ROLLOVER determina se o ano está em nCentury ou no século seguinte a nCentury.
**ROLLOVER nYear**
Um número de 0 a 99 que especifica o ano igual ou superior ao século atual e inferior ao século seguinte. O valor padrão para nYear são os dois últimos dígitos do ano atual mais 50 anos — se o ano atual for 1998, nYear é 48, os dois últimos dígitos de 2048 (1998 + 50). Observe que o valor de rollover determina o século apenas para uma data inserida sem porção de século — um formato de data ambíguo que não é recomendado. Por exemplo, se o ano atual for 1998 e nYear for o padrão (48), qualquer data inserida sem porção de século e com ano de 48 ou superior é considerada no século atual (o século 20). Qualquer data inserida sem porção de século, mas com ano anterior a 48, é considerada no século seguinte (o século 21).

# Observações

Use SET CENTURY para especificar como variáveis e funções de data são exibidas.

Emita SET CENTURY TO sem argumentos adicionais para restaurar o século padrão para o século atual e ROLLOVER para o valor padrão do ano atual mais 50 anos. No Visual FoxPro 5.0, emitir SET CENTURY TO sem argumentos adicionais define o século como 19 e ROLLOVER como zero.

SET CENTURY tem escopo na sessão de dados atual. Novas sessões de dados são inicializadas com os valores padrão conforme especificado acima, ignorando o valor de SET CENTURY para a sessão de dados atual.

SET CENTURY TO ROLLOVER está disponível no Visual FoxPro 5.0 e posterior, e torna possível controlar o ano assumido para datas usadas quando a configuração é SET CENTURY OFF. Também permite um valor de rollover, pois muitas aplicações contêm datas que abrangem vários séculos.

> **Observação:** SET CENTURY OFF sempre implica datas no século 20. No entanto, a sintaxe SET CENTURY TO tem precedência sobre essa configuração. Assim, com o Visual FoxPro 5.0 e posterior, a configuração SET CENTURY ON/OFF controla apenas o número de dígitos exibidos.

O valor de SET CENTURY TO tem escopo na sessão de dados atual.

No Visual FoxPro 5.0, emitir SET CENTURY TO sem parâmetros adicionais define o século como o século atual –1 e rollover como zero se o ano com dois dígitos da data do sistema for menor que 50. O século é definido como o século atual se a data do sistema com dois dígitos for maior que 50. Por exemplo, se o ano atual fosse 1998, nYear seria 48, os dois últimos dígitos de 2048 (1998 + 50).
