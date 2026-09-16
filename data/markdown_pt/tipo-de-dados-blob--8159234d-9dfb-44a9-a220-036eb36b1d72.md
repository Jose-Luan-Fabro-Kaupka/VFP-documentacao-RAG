# Tipo de dados Blob

Para armazenar dados binários de qualquer tipo, como texto ASCII, um arquivo executável (.exe) ou um fluxo de bytes, com comprimento indeterminado, use o tipo de dados Blob. Os tipos de dados Blob são particularmente úteis para armazenar dados de imagem do SQL Server.

Você pode atribuir valores a um campo Blob usando literais binários. Literais binários começam com um prefixo, 0h, seguido por uma cadeia de caracteres de números hexadecimais e não são delimitados por aspas (""), ao contrário das cadeias de caracteres. A lista a seguir inclui exemplos de literais binários:
 - 0h202020
- 0h6ABCDEF
- 0h (literal binário vazio)

Literais binários são limitados a 255 bytes codificados.

Para armazenar valores binários de comprimento fixo, use o tipo de dados Varbinary. Para mais informações, consulte Varbinary Data Type.

# Suporte ao tipo de dados Blob

O tipo Blob é suportado para contêineres de banco de dados (.dbc), tabelas livres, cursors e views. Por exemplo, você pode selecionar esse tipo para um campo na guia Fields do Table Designer. Tabelas podem conter vários campos Blob. Você pode especificar valores padrão e nulos para campos Blob. Campos Blob suportam validação de campo.

Você pode visualizar o conteúdo de um campo do tipo Blob usando um controle EditBox, um controle TextBox em um controle Grid ou emitindo o comando MODIFY MEMO com o nome do campo Blob; no entanto, o conteúdo é somente leitura. A caixa de edição exibe dados do tipo Blob como valores hexadecimais sem o prefixo 0h. Em grids, campos do tipo Blob exibem a cadeia de caracteres "blob" se estiverem vazios e a cadeia de caracteres "Blob" se contiverem dados. Você pode clicar duas vezes no campo Blob na grid, e uma janela de edição exibe os dados como somente leitura.

Chaves de índice baseadas em campos Blob não são suportadas. Nenhuma tradução de página de código é realizada em dados do tipo Blob.

A tabela a seguir lista a linguagem que contém funcionalidade afetada pelo tipo de dados Blob.

| AFIELDS( ) Function | ALTER TABLE - SQL Command | ALINES( ) Function |
| --- | --- | --- |
| BITAND( ) Function | BITCLEAR( ) Function | BITNOT( ) Function |
| BITOR( ) Function | BITSET( ) Function | BITTEST( ) Function |
| BITXOR( ) Function | COPY STRUCTURE EXTENDED Command | COPY TO Command |
| CREATE CURSOR - SQL Command | CREATE FROM Command | CREATE TABLE - SQL Command |
| CursorSchema Property | CURSORGETPROP( ) Function | CURSORSETPROP( ) Function |
| CURSORTOXML( ) Function | DataType Property | EMPTY( ) Function |
| ISBLANK( ) Function | MLINE( ) Function | MODIFY MEMO Command |
| SET ANSI Command | SET EXACT Command | TRANSFORM( ) Function |
| XMLTOCURSOR( ) Function | | |

> **Observação:** Valores do tipo Blob não são compatíveis com as expressões binárias produzidas pela função BINTOC( ) ou usadas pela função CTOBIN( ). Funções de cadeia de caracteres que normalmente retornam cadeias de caracteres, como a função SUBSTR( ), agora retornam valores binários quando recebem valores binários.

Para mais especificações sobre o tipo de dados Blob, consulte Visual FoxPro Data and Field Types.
