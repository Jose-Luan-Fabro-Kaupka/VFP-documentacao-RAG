# Erro de conectividade: "name" (Erro 1526)

Ocorreu um erro ODBC. O Visual FoxPro fornece esta mensagem como um invólucro para o erro ODBC real. O erro ODBC pode ser gerado pelo gerenciador de driver ODBC, pelo driver ODBC ou pelo servidor de dados de back-end. A função AERROR( ) retorna os erros ODBC. O formato de um erro ODBC 1526, conforme retornado por AERROR( ), é mostrado na tabela a seguir.

| Número do elemento | Descrição |
| --- | --- |
| 1 | Numérico. Contém 1526. |
| 2 | Character. O texto da mensagem de erro. |
| 3 | Character. O texto da mensagem de erro ODBC. |
| 4 | Character. O estado SQL ODBC atual. |
| 5 | Numérico. O número de erro da fonte de dados ODBC. |
| 6 | Numérico. O identificador de conexão ODBC. |
| 7 | O valor nulo. |

A mensagem de erro ODBC (número do elemento 3) contém a origem do erro como o último nome na lista que precede o texto real do erro.

Use o código de estado ODBC (número do elemento 4) para procurar o erro no livro ODBC (Programmer's Reference).

Para um erro de servidor, o erro da fonte de dados é definido (número do elemento 5). Use-o para procurar o erro na documentação do servidor.
