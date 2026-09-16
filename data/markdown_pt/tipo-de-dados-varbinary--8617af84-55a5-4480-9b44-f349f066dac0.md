# Tipo de Dados Varbinary

Para armazenar valores binários ou literais de comprimento fixo sem preenchimento por bytes zero (0) adicionais ou truncamento de bytes 0 finais, use o tipo de dados Varbinary. Para armazenar dados binários com comprimento indeterminado, use o tipo de dados Blob. Para obter mais informações, consulte Tipo de Dados Blob.

Literais binários começam com um prefixo, 0h, seguido por uma cadeia de caracteres de números hexadecimais e não são delimitados por aspas (""), diferentemente de cadeias de caracteres. A lista a seguir inclui exemplos de literais binários:
 - 0h202020
- 0h6ABCDEF
- 0h (literal binário vazio)

Literais binários são limitados a 255 bytes codificados. Campos Varbinary são limitados a 254 bytes codificados.

Ao executar operações de comparação ou concatenação, como =, !=, ==, >, >=, <=, + e -, os resultados variam dependendo da operação e da ordem dos tipos na operação. Quando você concatena dois valores binários, o resultado é um valor binário. Quando você concatena variáveis do tipo Varbinary (Q) com Varchar (V) ou Character (C), o resultado tem o tipo de dados do primeiro item na lista de concatenação. Por exemplo:

V + Q = V

Q + V = Q

Ao comparar entre tipos Varbinary e Character, o tipo no lado esquerdo da expressão de comparação governa a operação. Por exemplo, suponha uma expressão de comparação como a seguinte baseada em binário:

Q = V

O Visual FoxPro avalia esses valores byte a byte, e o resultado é o mesmo que executar `CAST(V AS Q(n) = Q`.

Suponha a seguinte expressão de comparação baseada em caractere:

V = Q

O Visual FoxPro avalia esses valores como se fossem cadeias de caracteres, e o resultado é o mesmo que executar `CAST(Q AS V(n) = V`.

Chaves de índice baseadas em campos ou expressões Varbinary são preenchidas com zeros à direita do valor até o comprimento máximo do campo. Por exemplo, os valores 0hAA, 0hAA00 e 0hAA000 têm a mesma chave de índice 0hAA0000. A sequência de ordenação padrão para chaves de índice baseadas em expressões binárias é MACHINE. Nenhuma outra sequência de ordenação é permitida. Para obter mais informações, consulte Comando INDEX e Criação de Índice Baseada em Expressões.

# Suporte ao Tipo de Dados Varbinary

O tipo Varbinary é suportado para contêineres de banco de dados (.dbc), tabelas livres, cursors e views. Por exemplo, você pode selecionar este tipo para um campo na guia Fields no Table Designer. Tabelas podem conter vários campos Varbinary. Você pode especificar valores padrão e nulos para campos Varbinary. Campos Varbinary suportam validação de campo.

Nenhuma tradução de página de código é executada para dados com tipo Varbinary.

As seguintes cláusulas e funções não oferecem suporte a tipos de dados Varbinary:
 - LIKE em condições de join e filtro para instruções SQL
- Função LIKE( )
- Função LIKEC( )
- Função BINTOC( )
- Função BITLSHIFT( )
- Função BITRSHIFT( )
- Função CTOBIN( )

As seguintes funções removem bytes zero iniciais ou finais de valores binários:
 - Função ALLTRIM( )
- Função LTRIM( )
- Função RTRIM( )
- Função TRIM( )

A tabela a seguir lista linguagem que contém funcionalidade afetada pelo tipo de dados Varbinary.

| Comando ? ?? | Função AFIELDS( ) | Função ALINES( ) |
| --- | --- | --- |
| Comando ALTER TABLE - SQL | Comando APPEND FROM | Função BITAND( ) |
| Função BITCLEAR( ) | Função BITNOT( ) | Função BITOR( ) |
| Função BITSET( ) | Função BITTEST( ) | Função BITXOR( ) |
| Comando COPY STRUCTURE EXTENDED | Comando COPY TO | Comando CREATE CURSOR - SQL |
| Comando CREATE FROM | Comando CREATE TABLE - SQL | Função CURSORGETPROP( ) |
| Propriedade CursorSchema | Função CURSORSETPROP( ) | Função CURSORTOXML( ) |
| Propriedade DataType | Função EMPTY( ) | Propriedade Format |
| Propriedade InputMask | Função ISBLANK( ) | Comandos LIST |
| Função MLINE( ) | Comando SET ENGINEBEHAVIOR | Comando SET ANSI |
| Comando SET EXACT | Função TRANSFORM( ) | Função XMLTOCURSOR( ) |

> **Observação:** Valores com tipo Varbinary não são compatíveis com as expressões binárias produzidas pela função BINTOC( ) ou usadas pela função CTOBIN( ). Funções de cadeia de caracteres que geralmente retornam cadeias de caracteres, como a função SUBSTR( ), agora retornam valores binários quando recebem valores binários.

Para mais especificações sobre o tipo de dados Varbinary, consulte Tipos de Dados e Campos do Visual FoxPro.

O exemplo a seguir limpa a janela principal do Visual FoxPro usando o comando CLEAR e cria um cursor com um campo chamado myVarbinaryField com tipo Varbinary usando o comando SQL CREATE CURSOR. Para cada instrução SQL INSERT, o comando INSERT insere uma linha no cursor contendo um literal binário no campo myVarbinary. GO TOP posiciona o ponteiro de registro no primeiro registro. O loop DO WHILE exibe o número de caracteres no campo para cada linha usando a função LEN( ) até que o último registro da tabela seja alcançado.

Você pode digitar o exemplo em um arquivo de programa (.prg) e executá-lo da janela Command usando o Comando DO.

```foxpro
CLEAR
CREATE CURSOR myCursor (myVarbinaryField Q(10))
INSERT INTO myCursor (myVarbinaryField) VALUES (0h616161202020)
INSERT INTO myCursor (myVarbinaryField) VALUES (0hABCDEF)
INSERT INTO myCursor (myVarbinaryField) VALUES (0h)
GO TOP
DO WHILE !EOF()
   ? "# Varbinary characters: ", LEN(myVarbinaryField)
   ?
   SKIP
ENDDO
```

Para obter mais informações sobre os comandos e funções usados neste exemplo, consulte Comandos CLEAR, Comando CREATE CURSOR - SQL, Comando INSERT - SQL, Comando BROWSE, Comando GOGO | GOTO, Comando DO WHILE ... ENDDO, Função EOF( ) e Comando SKIP.
