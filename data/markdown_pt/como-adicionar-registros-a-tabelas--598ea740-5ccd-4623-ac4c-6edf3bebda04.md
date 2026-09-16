# Como: adicionar registros a tabelas

Antes de armazenar dados em tabelas, você deve adicionar registros para armazenar os dados. Você pode adicionar um ou mais registros em branco ao final de uma tabela anexando registros. Também é possível copiar registros de outras tabelas ou arquivos e anexá-los a uma tabela.

### Para adicionar um registro em branco a uma tabela
- Abra a tabela em uma janela de navegação.
- No menu Tabela, clique em Anexar novo registro. Na janela de navegação, um registro em branco aparece ao final dos registros da tabela.

Para obter mais informações, consulte Como: visualizar registros em tabelas.

### Para adicionar um registro em branco após digitar dados
- Abra a tabela em uma janela de navegação.
- No menu Exibir, clique em Modo de anexação.

Ao trabalhar no modo de anexação, um novo registro em branco aparece na linha seguinte depois que você digita dados no registro anterior.

Para obter mais informações, consulte Como: visualizar registros em tabelas.

### Para adicionar um registro em branco a uma tabela programaticamente
- Escolha uma das opções a seguir: use o comando APPEND com a palavra-chave BLANK. -OU- Para adicionar registros e especificar os dados a armazenar nos novos registros, use o comando SQL INSERT.

Ao usar o comando SQL INSERT, você pode armazenar dados em registros diretamente especificando texto ou a partir de constantes, variáveis, matrizes, objetos e outras fontes de dados. Para obter mais informações, consulte Comando INSERT - SQL e Comando APPEND.

### Para anexar registros de outra tabela ou arquivo
- Use o comando APPEND FROM ou o comando IMPORT.

Para obter mais informações, consulte Comando APPEND FROM, Comando IMPORT e Importação e exportação de dados.
