# Tipo de campo Varchar

Para incluir texto alfanumérico em campos sem incluir preenchimento adicional com espaços ou truncar espaços à direita, use o tipo Varchar. Texto alfanumérico pode conter letras, números, espaços, símbolos e pontuação. O tipo Varchar também fornece um método conveniente para mapear tipos Varchar do SQL Server para os tipos de dados correspondentes do Visual FoxPro.

Para evitar que dados em campos Varchar sejam traduzidos entre páginas de código, use o tipo Varchar (Binary).

Os tipos de campo Varchar e Varchar (Binary) são semelhantes aos tipos de dados Character e Character (Binary) no sentido de que você pode armazenar informações de texto que não são usadas em cálculos matemáticos, como nomes, endereços e números. Ao armazenar valores Varchar e Varchar (Binary) em variáveis, eles são tratados como tipos Character.

> **Dica:** Para criar um campo Varchar (Binary) em uma tabela, use a opção NOCPTRANS nos comandos SQL CREATE TABLE e CREATE CURSOR ou selecione-a na guia Fields no Table Designer.

Os tipos de campo Varchar e Varchar (Binary) têm prioridade sobre o tipo Character ao executar operações UNION e concatenação entre esses tipos. Por exemplo, suponha que você tenha campos Varchar (X) e Character (Y) com X representando o comprimento do valor de caractere armazenado no campo Varchar e Y representando o comprimento do campo Character. Ao executar operações de concatenação, o resultado é um campo Varchar com comprimento de valor de caractere de X+Y.

Ao executar operações de concatenação entre Varchar (Binary) (X) e Character (Binary) (Y), o resultado é Varchar (Binary) (X+Y). Para funções do Visual FoxPro que retornam valores Character, se pelo menos um parâmetro for um campo Varchar ou Varchar (Binary) em uma tabela ou cursor, o tipo de retorno é Varchar. Para obter mais informações sobre conversão de tipos de dados e precedência em operações UNION, consulte Considerações para instruções SQL SELECT.

Chaves de índice baseadas em campos Varchar e Varchar (Binary) ou expressões são preenchidas com espaços à direita do valor até o comprimento máximo do campo. Portanto, cláusulas LIKE em condições de junção e filtro SQL com um campo Varchar ou Varchar (Binary) podem ser apenas parcialmente otimizadas pelo Rushmore. Para obter mais informações, consulte Usando otimização de consulta Rushmore para acelerar o acesso a dados.

# Suporte para tipos Varchar e Varchar (Binary)

Os tipos de campo Varchar e Varchar (Binary) são suportados para contêineres de banco de dados (.dbc), tabelas livres, cursors e visualizações locais e remotas. Por exemplo, você pode selecionar esses tipos para um campo na guia Fields no Table Designer. Tabelas podem conter vários campos Varchar e Varchar (Binary). Você pode especificar valores padrão e nulos para campos Varchar e Varchar (Binary). Campos Varchar e Varchar (Binary) suportam validação de campo.

A tabela a seguir lista a linguagem que contém funcionalidade afetada pelos tipos de campo Varchar e Varchar (Binary).

| Função AFIELDS( ) | Comando ALTER TABLE - SQL | Comando APPEND FROM |
| --- | --- | --- |
| Comando COPY STRUCTURE EXTENDED | Comando COPY TO | Comando CREATE CURSOR - SQL |
| Comando CREATE FROM | Comando CREATE TABLE - SQL | Função CURSORGETPROP( ) |
| Propriedade CursorSchema | Função CURSORSETPROP( ) | Função CURSORTOXML( ) |
| Propriedade DataType | Propriedade Format | Propriedade MaxLength |
| Propriedade InputMask | Comando SET ENGINEBEHAVIOR | Comando SET ANSI |
| Comando SET EXACT | Função XMLTOCURSOR( ) | |

Para mais especificações sobre os tipos Varchar e Varchar (Binary), consulte Tipos de dados e campos do Visual FoxPro.

O exemplo a seguir limpa a janela principal do Visual FoxPro usando o comando CLEAR e cria um cursor com dois campos chamados myVarCharField com tipo Varchar e myCharField com tipo Character usando o comando SQL CREATE CURSOR. Para cada instrução SQL INSERT, o comando INSERT insere uma linha no cursor contendo expressões de caractere de comprimento crescente em cada campo. BROWSE exibe o cursor e GO TOP posiciona o ponteiro de registro no primeiro registro. O loop DO WHILE exibe o número de caracteres em cada campo para cada linha usando a função LEN( ) até que o último registro na tabela seja alcançado.

Você pode digitar o exemplo em um arquivo de programa (.prg) e executá-lo na janela Command usando o Comando DO.

```foxpro
CLEAR
CREATE CURSOR myCursor (myVarCharField V(10), myCharField C(10))
INSERT INTO myCursor (myVarCharField, myCharField) VALUES ("a", "a")
INSERT INTO myCursor (myVarCharField, myCharField) VALUES ("aa", "aa")
INSERT INTO myCursor (myVarCharField, myCharField) VALUES ("aaa", "aaa")
INSERT INTO myCursor (myVarCharField, myCharField) VALUES ("aaaa", "aaaa")
BROWSE
GO TOP
DO WHILE !EOF()
   ? "# VarChar characters: ", LEN(myVarCharField), ;
      ", # Char characters:      ", LEN(myCharField)
   ?
   SKIP
ENDDO
```

Para obter mais informações sobre os comandos e funções usados neste exemplo, consulte Comandos CLEAR, Comando CREATE CURSOR - SQL, Comando INSERT - SQL, Comando BROWSE, Comando GOGO | GOTO, Comando DO WHILE ... ENDDO, Função EOF( ) e Comando SKIP.
