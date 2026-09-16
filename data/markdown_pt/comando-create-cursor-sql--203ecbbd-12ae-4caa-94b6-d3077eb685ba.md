# Comando CREATE CURSOR - SQL

Cria uma tabela temporária que existe até ser fechada.

```foxpro
CREATE CURSOR alias_name
...[CODEPAGE=nCodePage]
   (fname1 cFieldType [(nFieldWidth [, nPrecision])] [NULL | NOT NULL]
   [CHECK lExpression [ERROR cMessageText]]
   [AUTOINC [NEXTVALUE NextValue [STEP StepValue]]]
   [DEFAULT eExpression] [UNIQUE [COLLATE cCollateSequence]]
   [NOCPTRANS] [, fname2 ...])
   | FROM ARRAY ArrayName
```

#### Parâmetros
 **alias_name**
Especifica o nome da tabela temporária a criar. O parâmetro alias_name pode ser uma expressão de nome.
**nCodePage**
Especifica a página de código a usar. Para obter uma lista, consulte Páginas de código aceitas pelo Visual FoxPro.
**fname**
Especifica o nome de um campo da tabela temporária. Cada fname pode ser uma expressão de nome.
**cFieldType**
Especifica uma letra ou um nome longo que indica o tipo de dados do campo.
**nFieldWidth**
Especifica a largura do campo indicado por fname. Alguns tipos de dados exigem um valor para nFieldWidth.
**nPrecision**
Especifica o número de casas decimais do tipo de dados. Alguns tipos exigem um valor para nPrecision. Os valores possíveis são: W, Blob: Blob; C, Char, Character n: campo Character de largura n; Y, Currency: Currency; D, Date: Date; T, DateTime: DateTime; B, Double d: Double; G, General: General; I, Int, Integer: Integer; L, Logical: Logical; M, Memo: Memo; N, Num, Numeric n d: campo Numeric de largura n com d casas decimais; F, Float n d: campo Numeric de ponto flutuante de largura n com d casas decimais; Q, Varbinary n: campo Varbinary de largura n; V, Varchar n: campo Varchar de largura n. nFieldWidth e nPrecision são ignorados para os tipos W, Y, D, T, G, I, L e M. Se nPrecision não for incluído para N, F ou B, o padrão será zero.
**NULL | NOT NULL**
Especifica se valores nulos são permitidos no campo. NULL os permite; NOTNULL não.
**CHECK lExpression**
Especifica uma regra de validação para o campo. lExpression deve ser avaliada como expressão lógica e pode ser uma função definida pelo usuário ou um procedimento armazenado.
**ERROR cMessageText**
Especifica uma mensagem de erro. O Visual FoxPro a exibe quando a regra da cláusula CHECK gera um erro. A mensagem só aparece quando os dados são alterados em uma janela Browse ou Edit.
**AUTOINC [NEXTVALUE NextValue [STEP StepValue ]]**
Habilita o incremento automático do campo. NextValue especifica o valor inicial e pode ser um inteiro positivo ou negativo entre 2.147.483.647 e -2.147.483.647. O padrão é 1. Você pode defini-lo na caixa Próximo valor da guia Campos do Designer de Tabelas. StepValue especifica o incremento, um inteiro positivo diferente de zero entre 1 e 255; o padrão é 1. Valores de incremento automático não podem ser nulos (.NULL.). Observação: tabelas com esses campos acrescentam registros com buffer de tabela aproximadamente 35% mais lentamente, o que pode afetar o desempenho. Com buffer de tabela, o cabeçalho é bloqueado quando o registro é acrescentado.
**DEFAULT eExpression**
Especifica um valor padrão para o campo. O tipo de dados de eExpression deve ser igual ao tipo do campo. Se AUTOINC habilitar o incremento automático e um padrão for especificado, o Visual FoxPro armazenará o padrão, mas não o usará. Ele será usado se ALTER TABLE - SQL remover o incremento automático.
**UNIQUE**
Cria um índice candidato para o campo. A tag do índice tem o mesmo nome do campo. Para obter mais informações, consulte Tipos de índice do Visual FoxPro.
**COLLATE cCollateSequence**
Especifica uma sequência de intercalação diferente do padrão MACHINE. cCollateSequence deve ser uma sequência válida do Visual FoxPro. Consulte Otimizando aplicativos internacionais e o comando SET COLLATE.
**NOCPTRANS**
Impede a conversão para outra página de código nos campos Character, Memo e Varchar. NOCPTRANS só pode ser especificado nesses tipos.
**FROM ARRAY ArrayName**
Especifica um array existente cujo conteúdo define nome, tipo, precisão e escala de cada campo da tabela temporária. Você pode usar FROM ARRAY em vez de especificar campos individuais. Para conhecer o formato correto, consulte a função AFIELDS( ). O incremento automático é ativado quando o valor Step é maior que 0.

# Observações

Uma tabela temporária criada com CREATE CURSOR pode ser manipulada como qualquer outra: você pode consultá-la, indexá-la, acrescentar e modificar registros. Ela é aberta na área de trabalho disponível com o menor número e pode ser acessada pelo alias. Cada campo é definido com nome, tipo, precisão e escala, obtidos do comando ou de um array. A tabela é aberta exclusivamente, independentemente de SET EXCLUSIVE.

Se NULL e NOT NULL forem omitidos, SET NULL determinará se o campo permite valores nulos. Porém, se também for incluída a cláusula PRIMARY KEY ou UNIQUE, o Visual FoxPro ignorará SET NULL e o campo assumirá NOT NULL.

Valores nulos e registros duplicados não são permitidos em campos usados para índices candidatos. O Visual FoxPro não gera erro ao criar o índice para um campo que aceita nulos, mas gera erro ao tentar inserir nele um valor nulo ou duplicado.

> **Observação:** Índices candidatos criados com a opção UNIQUE (fornecida para compatibilidade ANSI) nos comandos CREATE TABLE – SQL ou ALTER TABLE – SQL não são iguais aos índices criados pelo comando INDEX com UNIQUE. Um índice criado com INDEX e UNIQUE permite chaves duplicadas; índices candidatos não. Consulte o comando INDEX.

Se a tabela for convertida para outra página de código, os campos com NOCPTRANS não serão convertidos.

CREATE CURSOR...FROM ARRAY reconhece todos os campos disponíveis na função AFIELDS( ) e habilita o incremento automático no cursor quando Step é maior que zero.

# Exemplo

O exemplo cria um cursor com o alias "employee". Um registro em branco é acrescentado, preenchido e exibido com BROWSE.

```foxpro
CLOSE DATABASES
CLEAR
CREATE CURSOR employee ;
 (EmpID N(5), Name Character(20), Address C(30), City C(30), ;
  PostalCode C(10), OfficeNo C(8) NULL, Specialty Memo)
DISPLAY STRUCTURE
WAIT WINDOW "Press a key to add a record."
INSERT INTO employee (EmpId, Name, Address, City, PostalCode, ;
   OfficeNo, Specialty);
   VALUES (1002, "Dr. Bonnie Doren", "University of Oregon", "Eugene", ;
   "98403", "", "Secondary Special Education")
BROWSE
* At this point you can copy this record to a permanent table.
CLOSE ALL   && Once the cursor closes, all data is flushed from memory.
CLEAR
```

O exemplo a seguir usa NOCPTRANS para impedir a conversão para outra página de código. Ele cria um cursor "mycursor" com dois campos Character e dois campos Memo. O segundo campo Character, "char2", e o segundo campo Memo, "memo2", incluem NOCPTRANS.

```foxpro
CREATE CURSOR mycursor (char1 C(10), char2 C(10) NOCPTRANS,;
   memo1 M, memo2 M NOCPTRANS)
```
