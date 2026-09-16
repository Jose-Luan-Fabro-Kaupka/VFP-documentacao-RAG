# Rotinas para retornar resultados ao Visual FoxPro

Essas rotinas de API permitem retornar resultados ao Visual FoxPro como um tipo de dados especificado.
 **_RetChar( ) API Library Routine**
Define o valor de retorno da função como uma cadeia de caracteres terminada em nulo.
**_RetCurrency( ) API Library Routine**
Define o valor de retorno da biblioteca como um valor currency.
**_RetDateStr( ) API Library Routine**
Define o valor de retorno da função como uma data. A data é especificada no formato mm/dd/ano, onde o ano pode ter dois ou quatro dígitos.
**_RetDateTimeStr( ) API Library Routine**
Define o valor de retorno da biblioteca como um datetime.
**_RetFloat( ) API Library Routine**
Define o valor de retorno da função como um valor float.
**_RetInt( ) API Library Routine**
Define o valor de retorno da função como um valor numérico.
**_RetLogical( ) API Library Routine**
Define o valor de retorno da função como um valor lógico. Zero é considerado False. Qualquer valor diferente de zero é considerado True.
**_RetVal( ) API Library Routine**
Passa uma estrutura Value Visual FoxPro completa, para que possa retornar qualquer tipo de dados Visual FoxPro, exceto memo. Você deve chamar _RetVal( ) para retornar uma cadeia de caracteres que contenha caracteres nulos incorporados.
