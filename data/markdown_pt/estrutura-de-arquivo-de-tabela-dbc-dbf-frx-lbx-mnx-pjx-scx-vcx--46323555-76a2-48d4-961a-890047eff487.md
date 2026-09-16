# Estrutura de arquivo de tabela (.dbc, .dbf, .frx, .lbx, .mnx, .pjx, .scx, .vcx)

O Visual FoxPro usa tabelas para armazenar dados que definem diferentes tipos de arquivo. A lista a seguir inclui os tipos de arquivo que são salvos como tabelas:
 - Database (.dbc)
- Form (.scx)
- Label (.lbx)
- Menu (.mnx)
- Project (.pjx)
- Report (.frx)
- Table (.dbf)
- Visual class library (.vcx)

Você pode usar e navegar nesses arquivos da mesma forma que navega em qualquer arquivo de tabela, porque esses arquivos são, na verdade, tabelas.

Um arquivo de tabela consiste em um registro de cabeçalho e registros de dados. O registro de cabeçalho define a estrutura da tabela e contém quaisquer outras informações relacionadas à tabela. O registro de cabeçalho começa na posição zero do arquivo. Os registros de dados seguem o cabeçalho, em bytes consecutivos, e contêm o texto real dos campos.

> **Observação:** Os dados no arquivo de dados começam na posição indicada nos bytes 8 a 9 do registro de cabeçalho. Os registros de dados começam com um byte de flag de exclusão. Se este byte for um espaço ASCII (0x20), o registro não está excluído. Se o primeiro byte for um asterisco (0x2A), o registro está excluído. Os dados dos campos nomeados nos subregistros de campo seguem a flag de exclusão.

O comprimento de um registro, em bytes, é determinado pela soma dos comprimentos definidos de todos os campos. Inteiros em arquivos de tabela são armazenados com o byte menos significativo primeiro.

Para informações sobre as estruturas de tabela dos diferentes tipos de arquivo, consulte Table Structures of Table Files (.dbc, .frx, .lbx, .mnx, .pjx, .scx, .vcx).

# Estrutura do registro de cabeçalho da tabela

| Deslocamento de byte | Descrição |
| --- | --- |
| 0 | Tipo de arquivo: 0x02 FoxBASE / dBase II 0x03 FoxBASE+ / FoxPro /dBase III PLUS / dBase IV, sem memo 0x30 Visual FoxPro 0x31 Visual FoxPro, autoincremento habilitado 0x32 Visual FoxPro, Varchar, Varbinary ou Blob habilitado 0x43 Arquivos de tabela SQL dBASE IV, sem memo 0x63 Arquivos de sistema SQL dBASE IV, sem memo 0x83 FoxBASE+/dBASE III PLUS, com memo 0x8B dBASE IV com memo 0xCB Arquivos de tabela SQL dBASE IV, com memo 0xF5 FoxPro 2.x (ou anterior) com memo 0xFB FoxBASE (?) |
| 1 - 3 | Última atualização (AAMMDD) |
| 4 – 7 | Número de registros no arquivo |
| 8 – 9 | Posição do primeiro registro de dados |
| 10 – 11 | Comprimento de um registro de dados, incluindo flag de exclusão |
| 12 – 27 | Reservado |
| 28 | Flags da tabela: 0x01 arquivo tem um .cdx estrutural 0x02 arquivo tem um campo Memo 0x04 arquivo é um banco de dados (.dbc) Este byte pode conter a soma de qualquer um dos valores acima. Por exemplo, o valor 0x03 indica que a tabela tem um .cdx estrutural e um campo Memo. |
| 29 | Marca de página de código |
| 30 – 31 | Reservado, contém 0x00 |
| 32 – n | Subregistros de campo O número de campos determina o número de subregistros de campo. Existe um subregistro de campo para cada campo na tabela. |
| n+1 | Terminador do registro de cabeçalho (0x0D) |
| n+2 a n+264 | Um intervalo de 263 bytes que contém o backlink, que é o caminho relativo de um arquivo de banco de dados (.dbc) associado. Se o primeiro byte for 0x00, o arquivo não está associado a um banco de dados. Portanto, arquivos de banco de dados sempre contêm 0x00. |

# Estrutura dos subregistros de campo

| Deslocamento de byte | Descrição |
| --- | --- |
| 0 – 10 | Nome do campo com no máximo 10 caracteres. Se for menor que 10, é preenchido com caracteres nulos (0x00). |
| 11 | Tipo de campo: W - Blob C – Character C – Character (binary) Y – Currency B – Double D – Date T – DateTime F – Float G – General I – Integer L – Logical M – Memo M – Memo (binary) N – Numeric P – Picture Q - Varbinary V - Varchar V - Varchar (binary) Observação Para cada campo Varchar e Varbinary, um bit, ou bit "varlength", é alocado no último campo de sistema, que é um campo oculto e armazena o status nulo para todos os campos que podem ser nulos. Se o campo Varchar ou Varbinary pode ser nulo, o bit nulo segue o bit "varlength". Se o bit "varlength" estiver definido como 1, o comprimento do valor real do campo é armazenado no último byte do campo. Caso contrário, se o bit estiver definido como 0, o comprimento do valor é igual ao tamanho do campo. |
| 12 – 15 | Deslocamento do campo no registro |
| 16 | Comprimento do campo (em bytes) |
| 17 | Número de casas decimais |
| 18 | Flags do campo: 0x01 Coluna de sistema (não visível ao usuário) 0x02 Coluna pode armazenar valores nulos 0x04 Coluna binária (somente para CHAR e MEMO) 0x06 (0x02+0x04) Quando um campo é NULL e binário (campos Integer, Currency e Character/Memo) 0x0C Coluna com autoincremento |
| 19 - 22 | Valor de autoincremento Próximo valor |
| 23 | Valor de autoincremento Valor do passo |
| 24 – 31 | Reservado |

Para informações sobre limitações de caracteres por registro, máximo de campos e assim por diante, consulte Visual FoxPro System Capacities.

# Observações

O Visual FoxPro modifica o cabeçalho da tabela quando você ativa ou adiciona autoincremento para valores de campo.

O Visual FoxPro não modifica o cabeçalho de um arquivo que foi salvo em um formato de arquivo FoxPro 2.x, a menos que um dos seguintes recursos tenha sido adicionado ao arquivo:
 - Suporte a valor nulo
- Tipos de dados DateTime, Currency e Double
- Campo CHAR ou MEMO marcado como Binary
- Uma tabela é adicionada a um arquivo de banco de dados (.dbc) Dica Você pode usar a seguinte fórmula para retornar o número de campos em um arquivo de tabela: (x – 296/32) . Na fórmula, x é a posição do primeiro registro (bytes 8 a 9 no registro de cabeçalho da tabela), 296 é 263 (informações de backlink) + 1 (terminador do registro de cabeçalho) + 32 (primeiro subregistro de campo), e 32 é o comprimento de um subregistro de campo.
