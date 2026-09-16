# Comando CREATE TABLE - SQL

Cria uma tabela usando os campos especificados ou a partir de uma matriz.

```foxpro
CREATE TABLE | DBF TableName1 [NAME LongTableName] [FREE]
    [CODEPAGE = nCodePage]
    ( FieldName1 FieldType [( nFieldWidth [, nPrecision] )] [NULL | NOT NULL]
    [CHECK lExpression1 [ERROR cMessageText1]]
    [AUTOINC [NEXTVALUE NextValue [STEP StepValue]]] [DEFAULT eExpression1]
    [PRIMARY KEY | UNIQUE [COLLATE cCollateSequence]]
    [REFERENCES TableName2 [TAG TagName1]] [NOCPTRANS]
    [, FieldName2 ... ]
    [, PRIMARY KEY eExpression2 TAG TagName2 |, UNIQUE eExpression3 TAG TagName3
    [COLLATE cCollateSequence]]
    [, FOREIGN KEY eExpression4 TAG TagName4 [NODUP]
    [COLLATE cCollateSequence]
    REFERENCES TableName3 [TAG TagName5]] [, CHECK lExpression2 [ERROR cMessageText2]] )
    | FROM ARRAY ArrayName
```

#### Parâmetros
 **CREATE TABLE | DBF TableName1**
Cria uma tabela ou .dbf. O parâmetro TableName1 especifica o nome da tabela. As opções TABLE e DBF são idênticas.
**nCodePage**
Especifica a página de código a usar. Para uma lista de páginas de código, consulte Code Pages Supported by Visual FoxPro.
**NAME LongTableName**
Especifica um nome longo para a tabela. Você pode especificar um nome longo de tabela apenas quando um banco de dados está aberto porque nomes longos de tabela são armazenados em bancos de dados. Nomes longos podem conter até 128 caracteres e podem ser usados no lugar de nomes curtos de arquivo no banco de dados.
**FREE**
Especifica que a tabela não será adicionada a um banco de dados aberto. Você não precisa usar FREE se um banco de dados não estiver aberto.
**FieldName1 , FieldType , nFieldWidth,nPrecision**
Especifica respectivamente o nome do campo, o tipo de campo, a largura do campo e a precisão do campo (número de casas decimais). Uma única tabela pode conter até 255 campos. Se um ou mais campos permitem valores nulos, o limite diminui em um campo para 254 campos. O parâmetro FieldType é uma única letra ou nome longo indicando o tipo de dados do campo. Você pode especificar nFieldWidth, nPrecision ou ambos para alguns tipos de campo. A tabela a seguir lista os valores de FieldType e se você pode especificar nFieldWidth e nPrecision. FieldType nFieldWidth nPrecision Data type W, Blob - - Blob C, Char, Character n – Character field of width n Y, Currency – – Currency D, Date – – Date T, DateTime – – DateTime B, Double – d Double G, General – – General I, Int, Integer – – Integer L, Logical – – Logical M, Memo – – Memo N, Num, Numeric n d Numeric field of width n with d decimal places F, Float n d Floating Numeric field of width n with d decimal places Q, Varbinary n - Varbinary field of width n V, Varchar n - Varchar field of width n Os parâmetros nFieldWidth e nPrecision são ignorados para os tipos de campo W, Y, D, T, G, I, L e M. Se nPrecision não estiver incluído para os tipos N ou F, o parâmetro nPrecision assume zero por padrão (sem casas decimais). Se nPrecision não estiver incluído para o tipo B, o parâmetro nPrecision assume por padrão o número de casas decimais especificado pela configuração do comando SET DECIMALS.
**NULL | NOT NULL**
Especifica se valores nulos são permitidos no campo. NULL permite valores nulos, enquanto NOT NULL não permite valores nulos. Se um ou mais campos podem conter valores nulos, o número máximo de campos que a tabela pode conter é reduzido de 255 para 254.
**CHECK lExpression1**
Especifica uma regra de validação para o campo. O parâmetro lExpression1 deve avaliar para uma expressão lógica e pode ser uma função definida pelo usuário ou um procedimento armazenado. O Visual FoxPro verifica a regra de validação especificada na cláusula CHECK quando um registro em branco é anexado.
**ERROR cMessageText1**
Especifica uma mensagem de erro. O Visual FoxPro exibe esta mensagem quando a regra de validação especificada com a cláusula CHECK gera um erro. A mensagem é exibida apenas quando os dados são alterados em uma janela Browse ou Edit.
**AUTOINC [NEXTVALUE NextValue [STEP StepValue ]]**
Habilita autoincremento para o campo. NextValue especifica o valor inicial e pode ser um valor inteiro positivo ou negativo variando de -2.147.483.647 a 2.147.483.647. O valor padrão é 1. Você pode definir NextValue usando a caixa de rotação Next Value na guia Fields do Table Designer. StepValue especifica o valor de incremento para o campo e pode ser um valor inteiro positivo e diferente de zero variando de 1 a 255. O valor padrão é 1. Você pode definir StepValue usando a caixa de rotação Step na guia Fields do Table Designer. Valores com autoincremento não podem ser NULL. Observação Tabelas contendo valores de campo com autoincremento automático anexam registros com buffer de tabela aproximadamente 35% mais lentamente que tabelas sem valores de campo com autoincremento automático, o que pode afetar o desempenho. Ao usar buffer de tabela, o cabeçalho da tabela é bloqueado quando o registro é anexado.
**DEFAULT eExpression1**
Especifica um valor padrão para o campo especificado em FieldName1. O tipo de dados de eExpression1 deve ser o mesmo que o tipo de dados do campo especificado. Se você usar a cláusula AUTOINC para ativar autoincremento para um campo e especificar um valor padrão, o Visual FoxPro armazena o valor padrão na tabela, mas não o usa. O Visual FoxPro usa o valor padrão se você usar o comando SQL ALTER TABLE para remover autoincremento do campo.
**PRIMARY KEY | UNIQUE**
PRIMARY KEY cria um índice primário para o campo especificado em FieldName1. UNIQUE cria um índice candidato para o campo especificado em FieldName1. A tag de índice primário ou a tag de índice candidato tem o mesmo nome que o campo. Para obter mais informações sobre índices primários e candidatos, consulte Visual FoxPro Index Types.
**COLLATE cCollateSequence**
Especifica uma sequência de ordenação diferente da configuração padrão, MACHINE. O parâmetro cCollateSequence deve ser uma sequência de ordenação válida do Visual FoxPro. Dica Você também pode usar o comando SET COLLATE antes de criar um índice. Para obter mais informações sobre como definir sequências de ordenação, consulte Optimizing International Applications e o comando SET COLLATE.
**REFERENCES TableName2 [TAG TagName1 ]**
Especifica a tabela pai à qual um relacionamento persistente é estabelecido. A tabela pai não pode ser uma tabela livre. A cláusula do parâmetro TagName1 especifica um nome de tag de índice para a tabela pai em TableName2. Nomes de tag de índice podem conter até 10 caracteres. Se você omitir a cláusula TAG, o relacionamento é estabelecido usando a chave de índice primário da tabela pai. Se a tabela pai não tiver um índice primário, o Visual FoxPro gera um erro.
**NOCPTRANS**
Impede a tradução para uma página de código diferente para campos Character, Memo e Varchar. Você pode especificar NOCPTRANS apenas para campos de caractere e memo. Isso cria o que parecem ser tipos de dados Character (Binary), Memo (Binary) e Varchar (Binary) no Table Designer.
**FieldName2 ...**
Especifica um ou mais campos e atributos adicionais.
**PRIMARY KEY eExpression2 TAG TagName2**
Especifica qualquer campo ou combinação de campos na tabela para criar um índice primário. Você não pode usar esta cláusula PRIMARY KEY se você criou anteriormente um índice primário para um campo porque uma tabela pode ter apenas um índice primário. Se você incluir mais de uma cláusula PRIMARY KEY em uma instrução CREATE TABLE, o Visual FoxPro gera um erro. O parâmetro TagName2 especifica um nome para a tag de índice primário em eExpression2. Nomes de tag de índice podem conter até 10 caracteres.
**UNIQUE eExpression3 TAG TagName3**
Especifica qualquer campo ou combinação de campos na tabela para criar um índice candidato. Uma tabela pode ter vários índices candidatos. No entanto, se você criou anteriormente um índice primário com uma das opções PRIMARY KEY, você não pode incluir o campo que foi especificado para o índice primário. O parâmetro TagName3 especifica um nome para a tag de índice candidato em eExpression3. Nomes de tag de índice podem conter até 10 caracteres.
**FOREIGN KEY eExpression4 TAG TagName4 [ NODUP ]**
Cria um índice estrangeiro (não primário), especifica a expressão de chave de índice e estabelece um relacionamento com uma tabela pai. Você pode criar vários índices estrangeiros para a tabela, mas as expressões de índice estrangeiro devem especificar campos diferentes na tabela. O parâmetro TagName4 especifica o nome da tag de chave de índice estrangeiro. Nomes de tag de índice podem conter até 10 caracteres. NODUP cria um índice estrangeiro candidato.
**REFERENCES TableName3 TAG TagName5**
Especifica a tabela pai à qual um relacionamento persistente é estabelecido. O parâmetro TagName5 especifica o nome da tag de índice para a tabela pai em TableName3 e estabelece uma relação baseada na tag de índice. Index tag names can contain up to 10 characters. Se você omitir a cláusula TAG, o relacionamento é estabelecido por padrão usando a chave de índice primário da tabela pai.
**CHECK lExpression2**
Especifica a regra de validação da tabela. O parâmetro lExpression2 deve avaliar para uma expressão lógica e pode ser uma função definida pelo usuário ou um procedimento armazenado.
**ERROR cMessageText2**
Especifica uma mensagem de erro para a regra de validação da tabela em lExpression2. O Visual FoxPro exibe esta mensagem quando a regra de validação da tabela gera um erro. A mensagem é exibida apenas quando os dados são alterados em uma janela Browse ou Edit.
**FROM ARRAY ArrayName**
Especifica o nome de uma matriz existente cujo conteúdo é o nome, tipo, precisão e escala para cada campo na tabela. Você pode usar a cláusula FROM ARRAY em vez de especificar campos individuais na instrução SQL CREATE TABLE. Para o formato adequado do conteúdo da matriz, consulte a função AFIELDS( ). O autoincremento é ativado quando StepValue é maior que 0.

# Observações

A nova tabela abre na área de trabalho disponível (não usada) de menor número e pode ser acessada por seu alias. A nova tabela abre exclusivamente, independentemente da configuração atual do comando SET EXCLUSIVE.

Se um banco de dados estiver aberto e você não incluir a cláusula FREE, a nova tabela é adicionada ao banco de dados. Você não pode criar uma nova tabela com o mesmo nome de uma tabela no banco de dados.

Se a tabela for convertida para outra página de código, os campos para os quais NOCPTRANS foi especificado não são traduzidos.

Se um banco de dados não estiver aberto quando você criar a nova tabela, incluir as cláusulas NAME, CHECK, DEFAULT, FOREIGN KEY, PRIMARY KEY ou REFERENCES gera um erro.

Tabelas criadas no Visual FoxPro OLE DB Provider usando CREATE TABLE são colocadas na pasta padrão do aplicativo chamador, a menos que você especifique outro local.

> **Observação:** A sintaxe CREATE TABLE usa vírgulas para separar certas opções CREATE TABLE. Você deve colocar as cláusulas NULL, NOT NULL, CHECK, DEFAULT, PRIMARY KEY e UNIQUE dentro dos parênteses que contêm as definições de coluna.

Se você omitir NULL e NOT NULL, a configuração atual do comando SET NULL determina se valores nulos são permitidos no campo. No entanto, se você omitir NULL e NOT NULL, mas incluir a cláusula PRIMARY KEY ou UNIQUE, o Visual FoxPro ignora a configuração atual de SET NULL e o campo assume NOT NULL por padrão.

O Visual FoxPro gera um erro se a regra de validação especificada na cláusula CHECK não permitir um valor de campo em branco em um registro anexado.

Valores nulos e registros duplicados não são permitidos em um campo usado para um índice primário ou candidato. No entanto, o Visual FoxPro não gera um erro se você criar um índice primário ou candidato para um campo que suporta valores nulos. O Visual FoxPro gera um erro se você tentar inserir um valor nulo ou duplicado em um campo usado para um índice primário ou candidato.

> **Observação:** Índices candidatos que você cria incluindo a opção UNIQUE, fornecida para compatibilidade ANSI, em comandos SQL CREATE TABLE ou ALTER TABLE não são os mesmos que índices criados usando o comando INDEX com a opção UNIQUE. Um índice criado no comando INDEX usando a opção UNIQUE permite chaves de índice duplicadas; índices candidatos não permitem chaves de índice duplicadas. Para obter mais informações sobre a opção UNIQUE no comando INDEX, consulte o comando INDEX. O termo CANDIDATE é um sinônimo de UNIQUE e pode ser usado em seu lugar, se você escolher.

Para NextValue, um valor vazio é interpretado como 0 e faz o incremento começar com 0 + StepValue.

O valor incremental StepValue é sempre adicionado positivamente. Se você deseja usar uma série com autoincremento negativo, deve começar com um NextValue negativo e avançar em direção a 0 usando o valor de incremento StepValue. Por exemplo, se NextValue for igual a -2147483647, o primeiro passo produz um valor de -2147483646.

CREATE TABLE reconhece todos os campos disponíveis na função AFIELDS( ) e ativa autoincremento na tabela quando StepValue é maior que zero.

# Exemplos

Exemplo 1

O exemplo a seguir cria um novo banco de dados chamado MyData1 e usa CREATE TABLE para criar três tabelas: Salesman, Customer e Orders. As cláusulas FOREIGN KEY e REFERENCES no segundo comando CREATE TABLE criam um relacionamento persistente um-para-muitos entre as tabelas Salesman e Customer. As cláusulas DEFAULT no terceiro comando CREATE TABLE estabelecem valores padrão, e as cláusulas CHECK e ERROR estabelecem regras de negócio para inserir dados em campos específicos. O comando MODIFY DATABASE exibe o relacionamento entre as três tabelas.

```foxpro
CLOSE DATABASES
CLEAR
CREATE DATABASE mydata1
* Create a Salesman table with a primary key.
CREATE TABLE Salesman ;
   (SalesID c(6) PRIMARY KEY, ;
   SaleName Character(20))
* Create a Customer table and relate it to the Salesman table.
CREATE TABLE Customer ;
   (SalesID c(6), ;
   CustId i PRIMARY KEY, ;
   CustName c(20) UNIQUE,   ;
   SalesBranch c(3), ;
   FOREIGN KEY SalesId TAG SalesId REFERENCES Salesman)
* Create an Orders table related to Customer with its own primary
* key and some business rules such as defaults and checks.
CREATE TABLE Orders ;
   (OrderId i PRIMARY KEY, ;
      CustId i REFERENCES customer TAG CustId, ;
      OrderAmt y(4), ;
      OrderQty i ;
      DEFAULT 10 ;
      CHECK (OrderQty > 9) ;
      ERROR "Order Quantity must be at least 10", ;
         DiscPercent n(6,2) NULL ;
      DEFAULT .NULL., ;
      CHECK (OrderAmt > 0) ERROR "Order Amount must be > 0" )
* Display new database, tables, and relationships.
MODIFY DATABASE
* Delete example files.
SET SAFETY OFF && Suppress verification message.
CLOSE DATABASES     && Close database before deleting.
DELETE DATABASE mydata1 DELETETABLES
```

Exemplo 2

O exemplo a seguir usa NOCPTRANS para impedir a tradução para uma página de código diferente. O exemplo cria uma tabela chamada MyTable que contém dois campos de caractere e dois campos memo. O segundo campo de caractere, "char2", e o segundo campo memo, "memo2", incluem NOCPTRANS para impedir a tradução.

```foxpro
CREATE TABLE MyTable (char1 C(10), char2 C(10) NOCPTRANS,;
   memo1 M, memo2 M NOCPTRANS)
```

Exemplo 3

O exemplo a seguir cria uma tabela Customer com um campo chamado MyField que tem tipo de dados Integer e usa valores de campo com autoincremento automático:

```foxpro
CREATE TABLE Customer (MyField i AUTOINC NEXTVALUE 1 STEP 1, name c(40) )
```
