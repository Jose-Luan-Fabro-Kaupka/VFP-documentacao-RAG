# Aviso: conversão(ões) inválida(s) de campo memo a partir do registro "number" (Erro 1486)

Um erro de conversão de memo foi relatado ao buscar dados grandes no registro number do conjunto de resultados remoto.
 - O driver ODBC não pode converter alguns valores remotos grandes no tipo de dados da view local. Use uma função de conversão na instrução SQL remota para converter os dados para um tipo de dados diferente antes de serem buscados; use a propriedade DataType do campo da view para alterar o tipo de dados local. Use configurações específicas do servidor para limitar a quantidade de dados enviados para cada valor de dados grande.
