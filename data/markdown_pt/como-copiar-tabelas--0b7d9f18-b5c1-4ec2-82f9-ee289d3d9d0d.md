# Como: copiar tabelas

Você pode copiar tabelas em duas etapas:
- Copie a estrutura da tabela.
- Copie os dados da tabela de origem para a tabela de destino.

### Para copiar a estrutura de uma tabela
- Abra a tabela de origem com o comando USE.
- Copie a estrutura da tabela de origem e crie a tabela de destino escolhendo uma das opções a seguir: para copiar somente a estrutura da tabela, sem incluir informações como valores padrão, gatilhos e regras de validação, use o comando COPY STRUCTURE. -OU- Para copiar a estrutura da tabela incluindo informações como valores padrão, gatilhos e regras de validação, use o comando COPY STRUCTURE EXTENDED.

Para obter mais informações, consulte Comando USE, Comando COPY STRUCTURE e Comando COPY STRUCTURE EXTENDED.

### Para copiar dados entre tabelas
- Abra as tabelas de origem e de destino com o comando USE.
- Copie os dados da tabela de origem para a tabela de destino com o comando APPEND FROM.

Para obter mais informações, consulte Comando USE e Comando APPEND FROM.
