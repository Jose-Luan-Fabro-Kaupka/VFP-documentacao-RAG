# Comando INSERT - SQL

Acrescenta um novo registro ao final de uma tabela que contém os valores de campo especificados. O comando INSERT SQL possui três sintaxes:
 - Use a primeira sintaxe para inserir valores especificados em campos especificados em uma tabela.
- Use a segunda sintaxe para inserir o conteúdo de elementos de uma matriz, variável de memória ou propriedade de um objeto que correspondam aos nomes de campo na tabela.
- Use a terceira sintaxe para inserir linhas de um comando SQL SELECT nos campos especificados na tabela.

```foxpro
INSERT INTO dbf_name [(FieldName1 [, FieldName2, ...])]
   VALUES (eExpression1 [, eExpression2, ...])
```

```foxpro
INSERT INTO dbf_name FROM ARRAY ArrayName | FROM MEMVAR | FROM NAME ObjectName
```

```foxpro
INSERT INTO dbf_name [(FieldName1 [, FieldName2, ...])]
   SELECT SELECTClauses [UNION UnionClause SELECT SELECTClauses ...]
```

#### Parâmetros
 **INSERT INTO dbf_Name**
Especifica o nome da tabela para acrescentar um novo registro. dbf_Name pode incluir um caminho e pode ser uma expressão de nome.
**[( FieldName1 [, FieldName2 [, ...]])]**
Especifica os nomes dos campos no novo registro nos quais os valores são inseridos.
**VALUES ( eExpression1 [, eExpression2 [, ...]])**
Especifica os valores de campo a serem inseridos no novo registro. Se você omitir os nomes de campo, deve especificar os valores de campo na ordem definida pela estrutura da tabela. Se eExpression for um nome de campo, deve incluir o alias da tabela. Se SET NULL estiver ON, INSERT tenta inserir valores nulos em quaisquer campos não especificados na cláusula VALUES.
**FROM Source**
Especifica inserir dados de uma matriz, variável de memória ou objeto do Visual FoxPro. A lista a seguir descreve itens válidos para Source: ARRAY ArrayName especifica a matriz cujos dados são inseridos no novo registro. Começando com o primeiro elemento, o conteúdo dos elementos da matriz é inserido nos campos correspondentes do registro. O conteúdo do primeiro elemento da matriz é inserido no primeiro campo do novo registro; o conteúdo do segundo elemento da matriz é inserido no segundo campo, e assim por diante. Quando você inclui a cláusula FROM ARRAY, o Visual FoxPro ignora quaisquer valores padrão para campos. MEMVAR MEMVAR especifica que o conteúdo de variáveis de memória é inserido em campos com os mesmos nomes das variáveis. Se não existir uma variável com o mesmo nome do campo, o campo fica vazio. NAME ObjectName especifica um objeto válido do Visual FoxPro, cujos nomes de propriedade correspondem aos nomes de campo na tabela para a qual você deseja inserir um novo registro contendo os valores de propriedade do objeto. Você pode especificar qualquer objeto válido do Visual FoxPro, que normalmente criaria usando o comando SCATTER...NAME. Para obter mais informações, consulte Comando SCATTER. Se a tabela tiver um campo que não corresponda a uma propriedade do objeto, o Visual FoxPro ignora o campo e o deixa em branco como se chamasse o comando APPEND BLANK. Se o tipo de uma propriedade do objeto não corresponder ao tipo de campo na tabela, o Visual FoxPro gera uma mensagem de incompatibilidade de tipo de dados. Observação Use cuidado ao especificar objetos derivados de classes do Visual FoxPro porque muitas propriedades nativas têm tipos que podem diferir dos campos com os quais você está trabalhando e não podem ser alterados. Se existir um campo autoincremento na tabela, você não pode ter uma propriedade de objeto que corresponda ao campo autoincremento, a menos que defina o comando SET AUTOINCERROR como OFF para a sessão de dados. Caso contrário, o Visual FoxPro gera um erro. Se você usar SCATTER...NAME para criar o objeto enquanto SET AUTOINCERROR estiver definido como ON, pode usar a função REMOVEPROPERTY( ) para remover quaisquer propriedades autoincremento e evitar gerar um erro. Para obter mais informações, consulte Comando SET AUTOINCERROR e Função REMOVEPROPERTY( ). Uma matriz, variável de memória ou um objeto não é suportado no Visual FoxPro OLE DB Provider.
**SELECT SELECTClauses [UNION UnionClause SELECT SELECTClauses ...]**
Recupera dados de campos especificados em uma tabela ou cursor, usando uma ou mais instruções SQL SELECT, para inserção em outra tabela ou cursor. No entanto, a instrução SELECT não pode conter cláusulas não SQL, como as seguintes: cláusulas INTO, TO e PREFERENCE; opções NOFILTER, READWRITE, NOCONSOLE, PLAIN e NOWAIT. Para combinar instruções SQL SELECT adicionais com a primeira instrução SQL SELECT, use a cláusula UNION. Para a sintaxe do comando SQL SELECT, que contém a cláusula UNION, consulte Comando SELECT - SQL. Observação Ao usar INSERT SQL com uma instrução SELECT, certifique-se de que os dados inseridos sejam compatíveis com os tipos de dados na tabela na qual você está inserindo. O Visual FoxPro tenta converter os tipos de dados no cursor criado pelo SQL SELECT nos tipos de dados na coluna correspondente da tabela ou cursor na qual os dados são inseridos. Se os dados inseridos não forem compatíveis, a precisão pode ser perdida, tipos de dados Date são convertidos em tipos de dados Character, e assim por diante.

# Observações

Se a tabela que você especificar estiver aberta, INSERT SQL acrescenta o novo registro à tabela. Se a tabela estiver aberta em uma área de trabalho diferente da área de trabalho atual, ela não é selecionada depois que o registro é acrescentado; a área de trabalho atual permanece selecionada.

Se a tabela que você especificar não estiver aberta, o Visual FoxPro a abre em uma nova área de trabalho e o novo registro é acrescentado à tabela. A nova área de trabalho não é selecionada; a área de trabalho atual permanece selecionada.

Enquanto o comando INSERT SQL está sendo executado, a área de trabalho atual torna-se a área na qual o novo registro é inserido. Em outras palavras, quando o comando INSERT SQL é executado, ele está no contexto da tabela sendo inserida, independentemente da área de trabalho atual antes de o comando ser emitido.

Depois de executar o comando INSERT, o Visual FoxPro posiciona o ponteiro de registro no novo registro.

O Visual FoxPro atualiza a variável de sistema _TALLY com o número de linhas inseridas se você incluir uma instrução SQL SELECT. Para obter mais informações, consulte Variável de sistema _TALLY.

# Exemplos

### Exemplo 1

O exemplo a seguir abre a tabela Employee e adiciona um registro.

```foxpro
USE employee
INSERT INTO employee (emp_no, fname, lname, officeno) ;
   VALUES (3022, "John", "Smith", 2101)
```

### Exemplo 2

O exemplo a seguir usa o comando USE para abrir a tabela Customer no banco de dados TestData.dbc e o comando SCATTER para copiar o conteúdo do registro atual em variáveis. COPY STRUCTURE copia a estrutura da tabela para uma nova tabela chamada Cust2.

INSERT insere um novo registro na tabela Cust2 a partir de variáveis de memória. SELECT recupera os dados de Cust2 e BROWSE exibe o novo registro.

Para limpar, o comando USE sem tabela especificada fecha a tabela na área de trabalho atual e DELETE remove Cust2.

```foxpro
CLOSE DATABASES
CLEAR
OPEN DATABASE (HOME(2) + 'Data\TestData')
USE Customer
SCATTER MEMVAR
COPY STRUCTURE TO Cust2
INSERT INTO Cust2 FROM MEMVAR
SELECT CUST2
BROWSE
USE
DELETE FILE cust2.dbf
```

### Exemplo 3

O exemplo a seguir insere dados da tabela OrdersArchive a partir de uma instrução SELECT executada na tabela Orders.

```foxpro
INSERT INTO OrdersArchive (order_id, order_date, ship_name) ;
   SELECT order_id, order_date, ship_name FROM Orders ;
      WHERE order_date >= (DATE()-30)
```
