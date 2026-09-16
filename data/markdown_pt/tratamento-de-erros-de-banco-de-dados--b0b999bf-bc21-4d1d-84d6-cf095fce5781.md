# Tratamento de erros de banco de dados

Erros de banco de dados ou "erros de engine" ocorrem quando erros acontecem em tempo de execução no código de evento em nível de registro. Por exemplo, um erro de banco de dados ocorre quando um usuário tenta armazenar um valor nulo em um campo que não aceita valores nulos.

Normalmente, quando um erro de banco de dados ocorre, o mecanismo de banco de dados subjacente que detecta o erro gera uma mensagem de erro. No entanto, a natureza exata da mensagem de erro depende do banco de dados acessado. Por exemplo, mensagens de erro geradas por um servidor de banco de dados remoto podem ser diferentes das geradas por uma tabela de banco de dados local do Visual FoxPro. Além disso, erros em nível de engine podem ser genéricos porque o mecanismo de banco de dados não tem informações sobre o contexto para atualizar um registro. Como resultado, mensagens de erro geradas por um mecanismo de banco de dados não são tão úteis para um usuário de aplicativo Visual FoxPro.

Para tratar erros de banco de dados de forma mais específica ao aplicativo, você pode criar triggers. Um trigger é uma expressão vinculada a uma tabela e invocada quando qualquer um dos registros da tabela é modificado usando um dos comandos de manipulação de dados especificados. Você pode escrever código de trigger na forma de funções definidas pelo usuário ou stored procedures usando o comando CREATE TRIGGER para capturar condições de erro específicas do aplicativo e gerar mensagens apropriadas.

> **Dica:** Se você tratar erros de banco de dados usando triggers, duas mensagens de erro podem ocorrer: uma do seu trigger e outra do mecanismo de banco de dados subjacente. Você pode evitar essa possibilidade ativando o buffering. O buffering permite atrasar atualizações de registros no banco de dados subjacente, mas ainda chamar seu trigger quando o registro é atualizado. Você pode ativar o buffering e exibir mensagens de erro personalizadas usando a função CURSORSETPROP( ). Para obter mais informações, consulte Função CURSORSETPROP( ).

Para obter mais informações, consulte Comando CREATE TRIGGER e Como: criar e gerenciar stored procedures.
