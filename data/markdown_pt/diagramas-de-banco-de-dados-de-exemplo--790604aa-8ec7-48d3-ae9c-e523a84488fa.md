# Diagramas de banco de dados de exemplo

Os diagramas de banco de dados a seguir podem dar ideias para o design do seu próprio banco de dados. Esses bancos de dados não estão incluídos no Visual FoxPro; estão aqui como exemplos dos tipos de bancos de dados e tabelas que você pode criar.

# Banco de dados Appointments

Esta estrutura de banco de dados armazena compromissos para um escritório profissional e pode ser facilmente modificada para uso em um consultório de médicos, dentistas, advogados ou contadores. A tabela Appointments tem uma chave primária de múltiplos campos para identificar exclusivamente cada compromisso. Essa chave primária, o índice "client_sta", é criada indexando uma expressão que combina os campos client_id e date_start time.
 Exemplo de um banco de dados de compromissos

# Banco de dados Personnel

Esta estrutura de banco de dados armazena informações de recursos humanos. A tabela Job History armazena informações sobre cada contratação ou promoção, portanto pode conter muitos registros para cada funcionário.
 Exemplo de um banco de dados de pessoal

# Banco de dados Library

Este banco de dados armazena informações sobre livros de biblioteca e empréstimos a usuários. Observe as relações muitos-para-muitos entre as tabelas Books e Authors e entre as tabelas Books e Subjects.
 Exemplo de um banco de dados de biblioteca
