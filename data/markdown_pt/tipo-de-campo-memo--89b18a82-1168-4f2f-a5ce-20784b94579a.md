# Tipo de campo Memo

Para armazenar blocos de dados de qualquer tipo, como valores nulos, código assembler, drivers de impressora e texto alfanumérico de comprimento indeterminado, ou uma referência a um bloco de dados em um campo, use o tipo de campo Memo. Para evitar que dados em campos Memo sejam traduzidos entre páginas de código, use o tipo de campo Memo (Binary).

> **Dica:** Para criar um campo Memo (Binary), use a opção NOCPTRANS nos comandos SQL CREATE TABLE e CREATE CURSOR ou selecione-a na guia Fields no Table Designer.

Campos Memo e Memo (Binary) contêm uma referência de dez bytes ao conteúdo real do memo. No entanto, o tamanho real dos memos depende da quantidade de dados que você armazena neles. Dados de campos Memo e Memo (Binary) de registros em uma tabela são armazenados em um arquivo separado com o mesmo nome da tabela e extensão de nome de arquivo .fpt. Campos Memo e Memo (Binary) são limitados apenas pela quantidade de espaço em disco disponível.

Você pode armazenar conteúdo de campos Memo como cadeias de caracteres residentes na memória. Você pode então manipular essas cadeias com todas as funções que operam em dados de caracteres.

Para especificações sobre o tipo de campo Memo e Memo (Binary), consulte Tipos de dados e campos do Visual FoxPro.
