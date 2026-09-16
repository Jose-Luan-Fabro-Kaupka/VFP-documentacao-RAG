# Tratamento de erros em tempo de execução

Depois que um aplicativo começa a executar, erros podem ocorrer em tempo de execução. Por exemplo, erros podem ocorrer em tempo de execução a partir das seguintes ações:
 - Gravar em um arquivo que não existe.
- Tentar abrir uma tabela aberta ou selecionar uma tabela fechada.
- Encontrar um conflito de dados.
- Dividir um valor por zero.

Você pode tratar esses erros, incluindo erros que ocorrem em relatórios e aqueles devido a tabelas com links de banco de dados inválidos, usando os manipuladores de erro que o Visual FoxPro fornece. No entanto, se o seu aplicativo não contém rotinas de tratamento de erros quando um erro ocorre em tempo de execução, o aplicativo pausa e a mensagem de erro do sistema Visual FoxPro apropriada aparece com os seguintes botões:
 - Cancel Se um usuário escolhe Cancel, o aplicativo para imediatamente de executar e retorna o controle ao sistema.
- Ignore Se um usuário escolhe Ignore, o Visual FoxPro ignora a linha que causou o erro e continua para a próxima linha no programa.

Para uma lista e explicação das mensagens de erro do Visual FoxPro, consulte Mensagens de erro.

> **Dica:** Para erros que você não pode evitar, certifique-se de fornecer documentação que descreva erros que os usuários podem ver e sugira maneiras de corrigir esses erros.

# Usando rotinas de tratamento de erros

Você pode usar a linguagem Visual FoxPro para criar rotinas de tratamento de erros para condições de erro. Os tópicos a seguir explicam vários mecanismos para tratar erros em tempo de execução no código e a ordem de sua operação:
 - Tratamento de erros procedural Discute o uso do comando ON ERROR para tratar erros em código procedural.
- Tratamento de erros de classe e objeto Discute o uso do evento Error para tratar erros locais para objetos e classes.
- Tratamento estruturado de erros Discute o uso da estrutura de controle TRY...CATCH...FINALLY para tratar erros ou exceções que podem ocorrer em tempo de execução.
- Prioridade do manipulador de erros Discute a ordem de prioridade para rotinas de tratamento de erros.

### Executando a linha de código executada mais recentemente

Você pode usar o comando RETRY, exceto com TRY...CATCH...FINALLY, para executar uma linha de código que causou um erro depois de alterar as condições que causaram o erro.

> **Observação:** Às vezes, a linha de código que causou um erro não existe para você executar com RETRY . O evento Error pode ocorrer mesmo quando o erro encontrado não está associado a uma linha do seu código. Por exemplo, se você chamar o método CloseTables do data environment no código quando a propriedade AutoCloseTables estiver definida como True (.T.) e então liberar o formulário, o Visual FoxPro gera um erro interno quando tenta fechar as tabelas novamente. Você pode capturar o erro; no entanto, nenhuma linha de código existe para você executar com RETRY .

Para obter mais informações, consulte Comando RETRY.
