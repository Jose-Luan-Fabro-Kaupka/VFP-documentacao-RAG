# Como: escolher o tipo de dados para um ListBox ou ComboBox

Quando você deseja preencher um controle ListBox ou ComboBox com itens ou valores, defina a propriedade RowSource do controle para especificar a fonte de itens ou valores para preencher o controle e defina a propriedade RowSourceType para identificar o tipo de fonte, como um array ou tabela.

> **Dica:** É recomendado definir a propriedade RowSourceType antes de definir RowSource para determinar a fonte que pode ser usada. Para garantir que o controle exiba os itens ou valores mais recentes, use o método Requery no método Init, por exemplo, This.Requery() .

> **Observação:** Quando você define a propriedade RowSource em código, deve colocar o valor entre aspas ("").

Quando a propriedade ColumnCount está definida como 0 ou 1, o controle exibe apenas o primeiro item ou valor em uma única coluna. Caso contrário, o controle exibe cada item ou valor em uma coluna até o número de colunas especificado por ColumnCount. Você também pode precisar definir a propriedade ColumnWidths para expandir a largura do controle para que os itens ou valores sejam exibidos corretamente.

Este tópico contém exemplos que ilustram maneiras de definir RowSourceType e RowSource dependendo da fonte de valores que você escolhe. A seguir está uma lista dos tipos de fonte disponíveis:
 - Sem tipo de fonte
- Tipo de fonte Value
- Tipo de fonte Alias
- Tipo de fonte SQL Statement
- Tipo de fonte Query
- Tipo de fonte Array
- Tipo de fonte Fields
- Tipo de fonte Files
- Tipo de fonte Field Structure
- Tipo de fonte Pop-Up
- Tipo de fonte Collection
- Tipos de fonte diferentes

Para detalhes sobre tipos de fonte, as fontes que você pode especificar e como ColumnCount afeta o preenchimento do controle para cada tipo de fonte, consulte Propriedade RowSourceType e Propriedade RowSource.

Para obter mais informações, o Visual FoxPro fornece os seguintes exemplos que usam as propriedades RowSourceType e RowSource:
 - Add New Items to a Combo Box Sample
- Allow Users to Choose List Values Sample
- Move Items Between List Boxes Sample
- Open Multiple Files Interactively Sample

# Sem tipo de fonte

Você pode preencher um list box ou combo box sem especificar uma fonte ou tipo de fonte.

### Para preencher o controle sem especificar uma fonte
- Defina RowSourceType como 0 (None). None é a configuração padrão e não preenche o controle automaticamente.
- Use o método AddItem, o método AddListItem, a propriedade List ou a propriedade ListItem para adicionar valores ou itens ao controle.

Por exemplo, as linhas de código a seguir definem RowSourceType como 0 para indicar nenhum tipo de fonte e usam o método AddItem para adicionar três itens ao list box lstMyListBox no formulário frmForm1:

```foxpro
frmForm1.lstMyListBox.RowSourceType = 0
frmForm1.lstMyListBox.AddItem("First Item")
frmForm1.lstMyListBox.AddItem("Second Item")
frmForm1.lstMyListBox.AddItem("Third Item")
```

O list box exibe os itens "First Item", "Second Item" e "Third Item". Para obter mais informações, consulte Método AddItem (Visual FoxPro), Método AddListItem, Propriedade List e Propriedade ListItem.

Para remover itens da lista, use o método RemoveItem. Por exemplo, a linha de código a seguir remove o segundo item, "Second Item", do list box:

```foxpro
frmForm1.lstMyListBox.RemoveItem(2)
```

Para obter mais informações, consulte Método RemoveItem.

# Tipo de fonte Value

Você pode preencher um list box ou combo box com uma lista de valores individuais.

### Para preencher o controle com uma lista de valores individuais
- Defina RowSourceType como 1 (Value).
- Defina RowSource especificando os valores em uma lista separada por vírgulas, sem espaços entre os valores e as vírgulas.

Por exemplo, as linhas de código a seguir definem RowSourceType como 1 para indicar que a fonte é uma lista de valores separada por vírgulas e especificam uma lista separada por vírgulas entre aspas ("") para RowSource:

```foxpro
Form1.lstMyList.RowSourceType = 1
Form1.lstMyList.RowSource = "one,two,three,four"
```

# Tipo de fonte Alias

Você pode preencher um list box ou combo box com valores de um ou mais campos em uma tabela aberta especificando o alias da tabela.

### Para preencher o controle com valores de um ou mais campos usando um alias de tabela
- Defina RowSourceType como 2 (Table alias).
- Defina RowSource especificando um alias de tabela.

Por exemplo, as linhas de código a seguir definem RowSourcetype como 2 para indicar que a fonte é uma tabela identificada pelo alias de tabela Customers e especificam "Customers" como o alias de tabela para RowSource:

> **Dica:** Certifique-se de que a tabela esteja aberta antes que o código seja executado.

```foxpro
OPEN DATABASE (HOME(2)+"Northwind\Northwind")
Form1.lstMyList.RowSourceType = 2
Form1.lstMyList.RowSource = "Customers"
```

A propriedade ColumnCount determina o número de campos dos quais os valores são usados para preencher o controle. Quando ColumnCount está definida como 0 ou 1, o controle exibe valores do primeiro campo na tabela. Quando ColumnCount está definida como um valor maior que 1, o controle exibe valores dos campos na tabela até o número especificado por ColumnCount. Por exemplo, se ColumnCount estiver definida como 3, o controle exibe valores dos três primeiros campos na tabela.

> **Observação:** Quando RowSourceType é 2 (Table alias) ou 6 (Fields), o ponteiro de registro da tabela move para o registro contendo o valor que o usuário escolhe na lista.

# Tipo de fonte SQL Statement

Você pode preencher um list box ou combo box com valores de um cursor ou tabela criado por uma instrução SQL, como SQL SELECT.

### Para preencher o controle com valores de uma instrução SQL
- Defina RowSourceType como 3 (SQL statement).
- Defina RowSource especificando uma instrução SQL SELECT.

> **Dica:** Por padrão no Visual FoxPro, instruções SQL SELECT sem cláusulas INTO exibem o cursor resultante imediatamente em uma janela browse. Para obter mais informações, consulte Janela Browse . É sugerido incluir uma cláusula INTO CURSOR em sua instrução SQL SELECT para evitar exibir a janela browse.

Por exemplo, as linhas de código a seguir definem RowSourceType como 3 para indicar que a fonte é um cursor ou tabela criado a partir de uma instrução SQL e especificam uma instrução SQL SELECT para RowSource que seleciona todos os campos e todos os registros da tabela Customers, localizada no banco de dados de exemplo Northwind no diretório ..\Samples\Northwind, em um cursor chamado myCursor:

```foxpro
OPEN DATABASE (HOME(2)+"Northwind\Northwind")
Form1.lstMyList.RowSourceType = 3
Form1.lstMyList.RowSource = "SELECT * FROM Customers INTO CURSOR myCursor"
```

Para obter mais informações sobre instruções SQL SELECT, consulte Comando SELECT - SQL.

# Tipo de fonte Query

Você pode preencher um list box ou combo box com resultados de uma query que você criou usando o Query Designer e salvou em um arquivo de query (.qpr). Para obter mais informações sobre queries, consulte Query and View Designers e Como: criar queries (Visual FoxPro).

### Para preencher o controle com valores de uma query
- Defina RowSourceType como 4 (Query file).
- Defina RowSource especificando o nome de um arquivo .qpr, incluindo um caminho se necessário. Observação Certifique-se de incluir a extensão de nome de arquivo .qpr. No entanto, se você não especificar uma extensão de arquivo, o Visual FoxPro assume que a extensão de arquivo é .qpr.

Por exemplo, as linhas de código a seguir definem RowSourceType como 4 para indicar que a fonte é um arquivo .qpr e especificam o nome de um arquivo .qpr para RowSource:

```foxpro
Form1.lstMyList.RowSourceType = 4
Form1.lstMyList.RowSource = "MyQuery.qpr"
```

# Tipo de fonte Array

Você pode preencher um list box ou combo box com itens ou valores armazenados em um array. Você usa um array criado em outro lugar em seu aplicativo ou cria uma propriedade de array do formulário ou form set para especificar em RowSource. Para obter mais informações sobre arrays, consulte Arrays. Para obter mais informações sobre como criar propriedades de array, consulte Criando formulários.

### Para preencher o controle a partir de um array
- Defina RowSourceType como 5 (Array).
- Defina RowSource especificando o nome do array.

Por exemplo, as linhas de código a seguir criam um array com 10 elementos, armazenam valores no array, definem RowSourceType como 5 para indicar que a fonte é um array e especificam o nome do array para RowSource:

```foxpro
DIMENSION gaMyArray(10)
FOR gnCount = 1 to 10
   STORE gnCount TO gaMyArray(gnCount)
NEXT
Form1.lstMyList.RowSourceType = 5
Form1.lstMyList.RowSource = "gaMyArray"
```

> **Observação:** A configuração RowSource é avaliada pelo Visual FoxPro conforme necessário em seu aplicativo e não se limita apenas ao método em que você define RowSource . Você precisa ter esse escopo em mente.

Por exemplo, se você cria um array local em um método, esse array tem escopo no método e não estará disponível em todos os casos quando o Visual FoxPro precisa avaliar a configuração da propriedade. Se você define RowSource para uma propriedade de array de um formulário ou form set, precisa referenciar a propriedade em relação ao controle, não em relação ao método em que você define a propriedade. Como exemplo, suponha que você tem uma propriedade de array de formulário chamada arrayProp e as linhas de código a seguir no evento Init do formulário. A primeira linha de código produz um erro enquanto a segunda não:

```foxpro
THIS.lst1.RowSource = "THIS.arrayprop"
THIS.lst1.RowSource = "THISFORM.arrayprop"
```

# Tipo de fonte Fields

Você pode preencher um list box ou combo box com valores de campos de uma única tabela. Diferente de quando RowSourceType está definido como 2 (Table alias), definir RowSourceType como 6 (Fields) torna possível exibir campos independentemente de suas posições reais na tabela.

> **Dica:** Se você deseja preencher o controle com campos de várias tabelas, defina RowSourceType como 3 e especifique uma instrução SQL SELECT para RowSource .

### Para preencher o controle a partir de campos de uma única tabela
- Defina RowSourceType como 6 (Fields).
- Defina RowSource especificando um campo ou uma lista de campos separada por vírgulas. Se a tabela estiver aberta, você pode especificar RowSource das seguintes maneiras: Form1.lstMyList.RowSource = field1 Form1.lstMyList.RowSource = field2, field3, ... Se a tabela não estiver aberta, preceda o campo ou lista de campos com um alias de tabela e um ponto (.), por exemplo: Form1.lstMyList.RowSource = TableAlias.field1 Form1.lstMyList.RowSource = TableAlias.field1, field3, field2, ...

Por exemplo, as linhas de código a seguir abrem uma tabela, definem RowSourceType como 6 para indicar que o tipo de fonte é fields e especificam campos da tabela Products no banco de dados Northwind, localizado no diretório ..\Samples\Northwind, para RowSource:

```foxpro
OPEN DATABASE (HOME(2)+"Northwind\Northwind")
USE Products
Form1.lstMyList.RowSourceType = 6
Form1.lstMyList.RowSource = "productname, productid"
```

As linhas de código a seguir especificam campos da tabela Customers, que não está aberta, para RowSource:

```foxpro
OPEN DATABASE (HOME(2)+"Northwind\Northwind")
Form1.lstMyList.RowSourceType = 6
Form1.lstMyList.RowSource = "Customers.companyname, customerid"
```

# Tipo de fonte Files

Você pode preencher um list box ou combo box com os nomes de arquivos do diretório atual. A lista também contém opções para escolher uma unidade e diretório diferentes para exibir nomes de arquivos.

### Para preencher o controle com nomes de arquivos de um diretório
- Defina RowSourceType como 7 (Files).
- Defina RowSource especificando um esqueleto ou máscara de arquivo, como *.* ou *.fileExt.

Por exemplo, as linhas de código a seguir definem RowSourceType como 7 para indicar que o tipo de fonte é files e especificam um esqueleto de arquivo para RowSource:

```foxpro
Form1.lstMyList.RowSourceType = 7
Form1.lstMyList.RowSource = "*.*"
```

# Tipo de fonte Field Structure

Você pode preencher um list box ou combo box com os nomes de campos em uma tabela. Exibir uma lista de nomes de campos é útil quando o usuário deseja pesquisar um campo específico por valores ou organizar esses campos na tabela.

### Para preencher o controle com nomes de campos de uma tabela
- Defina RowSourceType como 8 (Field structure).
- Defina RowSource especificando um nome de tabela ou alias de tabela.

Por exemplo, as linhas de código a seguir definem RowSourceType como 8 para indicar que o tipo de fonte é a estrutura de campos de uma tabela e especificam um nome de tabela para RowSource:

```foxpro
Form1.lstMyList.RowSourceType = 8
Form1.lstMyList.RowSource = "Customers"
```

# Tipo de fonte Pop-Up

Incluído para compatibilidade com versões anteriores, RowSourceType definido como 9 (Pop-up) tornava possível preencher um list box ou combo box a partir de um pop-up ou menu previamente definido.

### Para preencher o controle com um menu pop-up
- Defina RowSourceType como 9 (Pop-up).

# Tipo de fonte Collection

Você pode preencher um list box ou combo box com membros e valores de propriedade de objetos em uma coleção, ou objeto Collection.

### Para preencher o controle com membros de coleção
- Defina RowSourceType como 10 (Collection).
- Defina RowSource especificando o nome de uma coleção.

Por exemplo, as linhas de código a seguir criam uma coleção e dois formulários, adicionam os formulários e três cadeias de caracteres à coleção, definem RowSourceType como 10 para indicar que o tipo de fonte é um objeto Collection e especificam o nome da coleção e propriedades de objetos na coleção para RowSource:

```foxpro
colMyCollection=CREATEOBJECT("Collection")
frm1=CREATEOBJECT("Form")
frm2=CREATEOBJECT("Form")
colMyCollection.Add(frm1)
colMyCollection.Add(frm2)
colMyCollection.Add("Item 1")
colMyCollection.Add("Item 2")
colMyCollection.Add("Item 3")
Form1.lstMyList.RowSourceType = 10
Form1.lstMyList.RowSource = "colMyCollection, Caption, Name"
```

# Tipos de fonte diferentes

Você pode preencher um list box ou combo box com itens e valores de fontes diferentes.

### Para preencher um controle a partir de fontes diferentes
- Consulte Exemplo Preencher uma lista com valores de fontes diferentes .
