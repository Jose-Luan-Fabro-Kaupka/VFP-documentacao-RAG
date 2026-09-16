# Compartilhando conexões para dados remotos

O Visual FoxPro permite compartilhar um identificador de conexão para uma conexão de dados remota. Compartilhar um identificador de conexão pode ser desejável quando você deseja gerenciar melhor conexões SQL Server e recursos do servidor reduzindo o número de conexões.

Por padrão, o Visual FoxPro cria um novo identificador de conexão cada vez que uma conexão de dados remota é criada. No entanto, quando especificado, o Visual FoxPro pode usar uma conexão existente e associar a nova instrução a ela. Isso cria um novo identificador de instrução e identificador do Visual FoxPro; no entanto, o identificador de conexão associado é o mesmo.

Existem três tipos de identificadores associados a uma conexão de dados remota. A tabela a seguir descreve esses identificadores.

| Tipo de identificador | Descrição |
| --- | --- |
| Identificador de conexão (ODBC HDBC) | Um inteiro exclusivo atribuído a uma conexão. |
| Identificador de instrução (ODBC HSTMP) | Um inteiro exclusivo atribuído a uma instrução. Observação Mais de um identificador de instrução HSTMP pode ser associado a um identificador de conexão HDBC. |
| Identificador de conexão do Visual FoxPro | Um inteiro exclusivo atribuído pelo Visual FoxPro a um identificador de instrução exclusivo. |

### Conexões compartilhadas para views remotas

Uma view remota pode usar um identificador de conexão compartilhado incluindo a palavra-chave SHARE no comando CREATE SQL VIEW. Se uma conexão compartilhada estiver disponível, o Visual FoxPro a usa para criar um novo identificador de instrução e identificador de conexão do Visual FoxPro. Se uma conexão compartilhada não estiver disponível, o Visual FoxPro cria uma nova conexão compartilhada que outras views podem usar.

### Conexões compartilhadas para SQL Pass-Through

Você pode criar uma nova conexão que pode ser compartilhada incluindo o parâmetro lShared no comando SQLSTRINGCONNECT( ). O comando SQLSTRINGCONNECT( ) sempre cria uma nova conexão, instrução e identificador de conexão do Visual FoxPro.

Incluir o parâmetro lShared no comando SQLCONNECT( ) também cria uma nova conexão que pode ser compartilhada; no entanto, incluir o parâmetro nStatementHandle faz com que SQLCONNECT( ) use uma conexão compartilhada atualmente e crie apenas um novo identificador de instrução e identificador de conexão do Visual FoxPro.
