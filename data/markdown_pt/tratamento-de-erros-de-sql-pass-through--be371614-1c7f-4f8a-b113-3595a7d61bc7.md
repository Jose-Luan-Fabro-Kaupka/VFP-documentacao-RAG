# Tratamento de erros de SQL Pass-Through

Se uma função SQL pass-through retornar um erro, o Visual FoxPro armazena a mensagem de erro em uma matriz. A função AERROR( ) Function fornece informações sobre erros detectados em qualquer um dos níveis de componente: Visual FoxPro, a fonte de dados ODBC ou o servidor remoto. Ao examinar os valores retornados por AERROR( ), você pode determinar o erro do servidor que ocorreu e o texto da mensagem de erro.

> **Cuidado:** Você deve chamar AERROR() imediatamente para obter informações de erro. Se você gerar qualquer outro erro antes de chamar AERROR(), as informações de erro serão perdidas.
