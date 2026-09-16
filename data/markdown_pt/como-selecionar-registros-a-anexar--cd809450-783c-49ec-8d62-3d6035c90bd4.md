# Como: selecionar registros a anexar

Se você deseja anexar apenas determinados registros, pode usar uma expressão FOR. O Visual FoxPro usa a expressão para pesquisar o arquivo inteiro e anexar apenas os registros que correspondem à expressão fornecida. Os campos que você especifica na expressão FOR devem existir nos arquivos de origem e de destino.

### Para selecionar registros a anexar
- Navegue na tabela de destino e, no menu Table, escolha Append Records .
- Informe o tipo e o nome do arquivo de origem e escolha Options .
- Escolha For para construir uma expressão na caixa de diálogo Expression Builder. Observação Você não precisa informar o comando FOR porque ele está implícito. Por exemplo, digite customer.country = "Canada" para anexar apenas informações canadenses.
- Escolha OK .

Se você anexar de um arquivo de texto, o Visual FoxPro assume que seus campos são separados por vírgulas e que cada campo de caractere está entre aspas. Se você definiu o caractere de ponto decimal para ser exibido como vírgula, dados numéricos e de moeda podem ser analisados em campos separados.

Por exemplo, o Visual FoxPro traduz o valor 100,00 em dois campos porque parece ser delimitado por vírgula. Escolha um dos dois métodos para garantir que a vírgula seja traduzida corretamente:
 - Use tabulações para separar campos no arquivo de texto.
- Altere o caractere de ponto decimal de volta para ponto.

Se você deseja anexar de um arquivo de texto, altere os separadores de campo para tabulações e use o comando APPEND FROM com as palavras-chave DELIMITED WITH TAB.

Se você deseja alterar o caractere de ponto decimal para ponto antes de anexar arquivos de texto, pode alterar o caractere de volta para vírgula depois de anexar o arquivo.

### Para alterar o caractere de ponto decimal
- Na janela Command, digite o seguinte comando. SET POINT TO
- Importe o arquivo usando a palavra-chave DELIMITED.
- Na janela Command, digite o seguinte comando para redefinir o caractere de ponto decimal para vírgula. SET POINT TO ','
