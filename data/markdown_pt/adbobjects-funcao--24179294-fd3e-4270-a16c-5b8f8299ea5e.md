# ADBOBJECTS( ) Função

Coloca os nomes de conexões nomeadas, relações, tabelas, ou SQL visualizações no banco de dados atual em um array variável.

```foxpro
ADBOBJECTS(ArrayName, cSetting)
```

Parâmetros
**ArrayName**
Especifica o nome do array no qual os nomes são colocados. Se o array especificado não existir, Visual FoxPro cria automaticamente o array. Se o array existe e não é grande o suficiente para conter todos os nomes, Visual FoxPro aumenta automaticamente o tamanho do array para acomodar os nomes. Se o array for maior do que o necessário, Visual FoxPro trunca o array. Se o array existe e ADBOBJECTS( ) retorna 0 porque nenhum nome é encontrado, o array permanece inalterado. Se o array não existe, e ADBOBJECTS( ) retorna 0, o array não é criado. Um array unidimensional é criado quando você especifica CONNECTION, TABLE, ou VIEW para cSetting . Cada linha no array unidimensional contém o nome de uma conexão, tabela ou visualização no banco de dados. Um array bidimensional é criado quando você especifica RELATION para cSetting . Cada linha no array bidimensional corresponde a uma relação no banco de dados. A primeira coluna em uma linha de array contém o nome da tabela filho e a segunda coluna em uma linha de array contém o nome da tabela pai. A terceira coluna contém o nome da etiqueta de índice para a tabela de filhos e a quarta coluna contém o nome da etiqueta de índice para a tabela pai. A quinta coluna em uma linha de array contém informações de integridade referencial. Esta coluna está vazia se a relação não tiver regras de integridade referencial. Se o relacionamento tiver regras de integridade referencial, a coluna contém caracteres correspondentes ao tipo de regras de integridade referencial para atualizações, deleções e inserções. O primeiro caracter indica o tipo de regra de atualização, o segundo caracter indica o tipo de regra de exclusão, e o terceiro caracter indica o tipo de regra de inserção. Valores possíveis para atualizações e deleções são "C" para cascata, "R" para restrição e "I" para ignorar. Valores possíveis para inserções são "R" para restrição, e "I" para ignorar. Por exemplo, se uma relação tem atualizações em cascata, deleções restritas e ignora regras de integridade referencial de inserção, a coluna contém "CRI".
**cSetting**
Specifies the names to place in the variable array. The following table lists the values for cSetting and the corresponding names placed in the array: cSetting Names CONNECTION Connection names RELATION Table relationships TABLE Table names VIEW View names The CONNECTION, RELATION, TABLE, and VIEW settings cannot be abbreviated.

# Valor de Retorno

Numérico

Observações

A database must be open and current when ADBOBJECTS( ) is issued; otherwise Visual FoxPro generates an error message.

Exemplo

The following example opens the `testdata` database and uses ADBOBJECTS( ) to create an array named `gaTables` containing names of tables in the database. The tables names are then displayed.

```foxpro
* Close any open databases
CLOSE DATABASES
* Clear desktop to prepare for displaying the array
CLEAR
* Open sample testdata database
OPEN DATABASE (HOME(2) + 'Data\testdata')
* Function call with cSetting for table names
=ADBOBJECTS(gaTables, "TABLE")
* Displays array gaTables created by ADBOBJECTS() function
DISPLAY MEMORY LIKE gaTables
```

Veja também
- ADATABASES( ) Function
- CREATE Command
- CREATE CONNECTION Command
- CREATE DATABASE Command
- CREATE SQL VIEW Command
