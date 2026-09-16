# Exceção estruturada não tratada (Erro 2059)

Uma exceção não tratada pode ocorrer nas seguintes condições:
 - Um erro ocorrido ou uma exceção lançada em um bloco TRY, CATCH ou FINALLY não foi capturado por um manipulador de erros estruturado, como TRY...CATCH...FINALLY.
- Um manipulador de erros estruturado não capturou uma exceção lançada fora de uma estrutura TRY...CATCH...FINALLY.

Você pode capturar uma exceção estruturada não tratada usando os seguintes manipuladores de exceção não estruturados:
 - Comando ON ERROR
- Evento Error
- Manipulador de sistema do Visual FoxPro

Para cada um desses manipuladores de erros, o número de erro retornado pela função ERROR( ) é 2059. O Visual FoxPro fornece detalhes sobre o erro original. Você também pode obter informações adicionais sobre o erro original que causou a exceção não tratada por meio de SYS(2018) — Parâmetro de mensagem de erro e das funções MESSAGE( ) e AERROR( ). A função SYS(2018) retorna o mesmo valor que o terceiro elemento da matriz retornada pela função AERROR( ). A função MESSAGE( ) retorna o mesmo valor que o segundo elemento da matriz retornada por AERROR( ).

Se a exceção não tratada tiver sido causada por uma instrução THROW, o valor de SYS(2018) será 2071, ou Erro lançado pelo usuário (Erro 2071).
