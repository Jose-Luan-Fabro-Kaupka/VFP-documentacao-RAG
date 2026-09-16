# Comando SCATTER

Copia dados do registro atual para um conjunto de variáveis, para um array ou para um objeto.

SCATTER e COPY TO ARRAY se comportam de forma semelhante. SCATTER copia apenas um único registro atual para um array ou um conjunto de variáveis e cria automaticamente o array ou as variáveis se eles ainda não existirem. COPY TO ARRAY copia vários registros para um array. Para obter mais informações, consulte COPY TO ARRAY Command.

Para copiar variáveis ou elementos de array para registros de tabela, use o GATHER Command.

```foxpro
SCATTER [FIELDS FieldNameList | FIELDS LIKE Skeleton
   | FIELDS EXCEPT Skeleton] [MEMO] [BLANK]
   TO ArrayName | TO ArrayName | MEMVAR
   | NAME ObjectName [ADDITIVE]
```

#### Parâmetros
 **FIELDS FieldNameList**
Especifica os campos cujos valores devem ser copiados para as variáveis ou para o array. SCATTER ignora campos memo por padrão; no entanto, você pode incluir campos memo na lista de campos seguindo a lista de campos com a palavra-chave MEMO. No entanto, SCATTER ignora campos general mesmo quando você inclui a palavra-chave MEMO. Omitir FIELDS FieldNameList copia valores de todos os campos.
**FIELDS LIKE Skeleton | FIELDS EXCEPT Skeleton**
Copia campos que correspondem ou excluem Skeleton para variáveis ou um array. Você pode incluir a cláusula LIKE ou EXCEPT ou ambas. Para copiar valores de campos que correspondem a Skeleton para variáveis ou um array, use LIKE Skeleton . Para copiar valores de todos os campos, exceto os que correspondem a Skeleton, para variáveis ou um array, use EXCEPT Skeleton . Skeleton suporta caracteres curinga. Por exemplo, para copiar os valores de todos os campos que começam com as letras A e P para variáveis ou um array, use as linhas de código a seguir: SCATTER FIELDS LIKE A*,P* TO myArray A cláusula LIKE pode ser combinada com a cláusula EXCEPT: SCATTER FIELDS LIKE A*,P* EXCEPT PARTNO* TO myArray
**MEMO**
Especifica que a lista de campos inclui um ou mais campos memo. Observação Seu computador deve ter memória suficiente para espalhar campos memo grandes em variáveis ou em um array. O Visual FoxPro gera uma mensagem de erro se seu computador não tiver memória suficiente. SCATTER não copia dados de um campo memo se ele for grande demais para caber na memória, nem copia de quaisquer campos memo adicionais na lista de campos. Se SCATTER não tiver sucesso para um campo memo, o valor da variável ou do elemento do array é definido como False (.F.).
**TO ArrayName**
Especifica um array para o qual o conteúdo do registro é copiado. Começando com o primeiro campo, SCATTER copia o conteúdo de cada campo para cada elemento do array em ordem sequencial. Se o array que você especificar contiver mais elementos do que o número de campos, os elementos extras do array permanecem inalterados. SCATTER cria automaticamente um novo array se o array ainda não existir ou se contiver menos elementos do que o número de campos. Os elementos do array têm o mesmo tamanho e tipos de dados dos campos correspondentes.
**TO ArrayName**
Cria um array com elementos vazios, que têm o mesmo tamanho e tipo dos campos na tabela.
**MEMVAR**
Espalha os dados em um conjunto de variáveis em vez de um array. SCATTER cria uma variável para cada campo na tabela e preenche cada variável com dados do campo correspondente no registro atual, atribuindo à variável o mesmo nome, tamanho e tipo de seu campo. SCATTER cria uma variável para cada campo na lista de campos se uma lista de campos for incluída. Para referenciar uma variável que tem o mesmo nome de um campo na tabela atual, prefixe o nome da variável com o qualificador m. Cuidado Não inclua a palavra TO com MEMVAR . O Visual FoxPro cria um array chamado MEMVAR se você incluir a palavra TO . Inclua a palavra-chave BLANK para criar um conjunto de variáveis vazias. Cada variável recebe o mesmo nome, tipo de dados e tamanho de seu campo. Se uma lista de campos for incluída, uma variável é criada para cada campo na lista de campos.
**NAME ObjectName [ADDITIVE]**
Cria um objeto cujas propriedades têm os mesmos nomes dos campos na tabela. Para copiar o valor de cada campo na tabela para cada propriedade do objeto, não inclua a palavra-chave BLANK. Para deixar as propriedades vazias, inclua a palavra-chave BLANK. Para uma descrição do que as propriedades vazias contêm, com base no tipo de campo correspondente, consulte EMPTY( ) Function . Propriedades não são criadas para campos general que existem na tabela. Para atualizar os valores de propriedade de um objeto Visual FoxPro existente e válido especificado por ObjectName , mas não objetos COM, com valores do registro atual, inclua a palavra-chave ADDITIVE. Se o objeto não existir, o Visual FoxPro cria o objeto automaticamente. Você não pode usar a palavra-chave ADDITIVE sem a cláusula NAME. Fazer isso gera um erro. Usar BLANK com ADDITIVE omite os valores de propriedades existentes que têm nomes de campos correspondentes.

# Observações

Se propriedades correspondentes a nomes de campos não existirem para o objeto, SCATTER...NAME ADDITIVE as cria automaticamente. No entanto, SCATTER pode não criar todas as propriedades necessárias porque algumas podem estar marcadas como Hidden ou Protected. Se o Visual FoxPro não puder criar ou definir uma propriedade, ele gera um erro. Por exemplo, você pode ter um nome de campo que corresponda a um nome de propriedade de objeto Visual FoxPro nativo, desde que o campo e os tipos de dados da propriedade sejam os mesmos. No entanto, o Visual FoxPro gera um erro se o nome do campo corresponder a um método, evento ou nome de objeto.

Você pode evitar problemas usando um objeto criado por SCATTER...NAME e não um derivado de uma classe Visual FoxPro. Diferente de quando SCATTER é usado apenas com NAME, o Visual FoxPro não sobrescreve o objeto existente para criar um novo objeto.

SCATTER...NAME ADDITIVE não gera um erro quando uma propriedade somente leitura não pode ser definida para um campo na tabela. No entanto, o valor da propriedade permanece inalterado.

Para referenciar uma propriedade em um objeto que tem o mesmo nome de uma tabela aberta, prefixe o nome da propriedade com o qualificador `m.`. O exemplo a seguir exibe o valor do campo `Company` na tabela `Customer` seguido pelo valor da propriedade `Company` do objeto `Customer`:

```foxpro
USE Customer
SCATTER NAME Customer
? Customer.Company  && Returns the table value
? m.Customer.Company  && Returns the object property value
```

# Exemplos

### Exemplo 1

Este exemplo usa SCATTER para criar um conjunto de variáveis com base nos campos da tabela test. Cada campo recebe um valor e um novo registro em branco é adicionado à tabela. Os dados são copiados para a tabela usando o comando GATHER.

```foxpro
CREATE TABLE Test FREE ;
   (Object C(10), Color C(16), SqFt n(6,2))
SCATTER MEMVAR BLANK
m.Object="Box"
m.Color="Red"
m.SqFt=12.5
APPEND BLANK
GATHER MEMVAR
BROWSE
```

### Exemplo 2

Este exemplo usa SCATTER junto com a cláusula NAME para criar um objeto com propriedades com base nos campos da tabela. As propriedades do objeto recebem valores e um novo registro em branco é adicionado à tabela. Os dados são copiados para o novo registro usando GATHER com a cláusula NAME.

```foxpro
CREATE TABLE Test FREE ;
   (Object C(10), Color C(16), SqFt n(6,2))
SCATTER NAME oTest BLANK
oTest.Object="Box"
oTest.Color="Red"
oTest.SqFt=12.5
APPEND BLANK
GATHER NAME oTest
RELEASE oTest
BROWSE
```

### Exemplo 3

Suponha que você tenha duas ou mais tabelas ou cursors e deseje criar um objeto que combine os dados desses cursors. O exemplo a seguir seleciona a tabela `Customer` e usa SCATTER...NAME para criar o objeto `oCustomer` e suas propriedades a partir dos campos na tabela `Customer`. SCATTER...NAME...ADDITIVE então atualiza os valores dos campos `ReportDate` e `Rating` na tabela `CreditHistory` e dos campos `CookieText` e `SessionId` na tabela `MySessionTable` no objeto `oCustomer` ou cria essas propriedades se elas não existirem.

```foxpro
SELECT Customer
SCATTER NAME oCustomer
SELECT CreditHistory
SCATTER FIELDS ReportDate, Rating NAME oCustomer ADDITIVE
SELECT MySessionTable
SCATTER FIELDS CookieText, SessionId NAME oCustomer ADDITIVE
```
