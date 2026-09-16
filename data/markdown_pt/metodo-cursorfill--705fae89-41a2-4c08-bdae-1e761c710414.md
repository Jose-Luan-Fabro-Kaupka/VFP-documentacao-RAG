# Método CursorFill

Executa o comando na propriedade SelectCmd Property contra a origem de dados na propriedade CursorAdapter DataSource, cria um cursor, recupera dados e executa qualquer conversão de dados necessária conforme as propriedades CursorAdapter DataSourceType Property e CursorSchema Property.

```foxpro
CursorAdapter.CursorFill( [ lUseCursorSchema [, lNoData [, nOptions [, Source ] ] ] ] )
```

#### Parâmetros
 **lUseCursorSchema**
A tabela a seguir lista os valores para lUseCursorSchema. lUseCursorSchema Descrição True (.T.) Usa o esquema na propriedade CursorSchema para criar o cursor. Observação O Visual FoxPro gera mensagens de erro quando CursorSchema é necessário, mas está ausente ou é inválido. False (.F.) ou vazio Não usa o esquema na propriedade CursorSchema para criar o cursor. Em vez disso, CursorFill cria o cursor usando os tipos de dados conforme normalmente determinado pelo Visual FoxPro de acordo com a propriedade CursorAdapter DataSourceType.
**lNoData**
A tabela a seguir lista os valores para lNoData. lNoData Descrição True (.T.) Cria o cursor, mas não o preenche com dados. Quando a propriedade CursorAdapter DataSourceType é "ADO" e SelectCmd contém parâmetros, CursorFill tenta avaliar os parâmetros em SelectCmd. Se CursorFill não puder avaliar os parâmetros, usa valores null (.NULL.) para os valores dos parâmetros. Quando a propriedade CursorAdapter DataSourceType é "XML", CursorFill cria o cursor usando o esquema na propriedade CursorSchema, independentemente do valor passado para lUseCursorSchema. Se CursorSchema estiver vazio ou for inválido, o Visual FoxPro gera um erro. False (.F.) ou vazio Cria o cursor e o preenche com dados. Se você especificar lNoData para CursorFill e SelectCmd for um comando SQL SELECT - SQL Command contra uma view parametrizada, o Visual FoxPro continua solicitando a entrada de parâmetros. Esta ação é equivalente à seguinte instrução: SELECT * FROM "customers in specific country" WHERE 1=0
**nOptions**
Especifica valores numéricos ou flags para criar o cursor. Os valores para nOptions também são usados para o método CursorRefresh. A tabela a seguir lista valores para nOptions dependendo da configuração da propriedade CursorAdapter DataSourceType. DataSourceType nOptions "ADO" Um inteiro representando o tipo de Command ou valores Execution Enum que você deseja definir para o método Open do RecordSet ActiveX Data Object (ADO). O valor padrão é -1. "XML" Qualquer combinação de flags válidas da função XMLTOCURSOR( ) Function, exceto 8192, que é automaticamente definida quando o parâmetro lUseCursorSchema contém um valor True (.T.).
**Source**
Especifica uma referência a um Command ADO ou a um objeto RecordSet aberto. O objeto ADO Command deve ter sua propriedade ActiveConnection definida para o objeto ADO Connection apropriado e já aberto. Quando um objeto ADO Command é passado para Source, o Visual FoxPro define a propriedade ADO Command CommandText para o valor da propriedade CursorAdapter SelectCmd. O Visual FoxPro analisa quaisquer parâmetros em SelectCmd e cria e define valores de parâmetro no objeto ADO Command. O método CursorFill então executa da seguinte maneira: CursorAdapter.DataSource.Open( Source,,,,Options ) Nesta chamada, DataSource é o objeto ADO RecordSet na propriedade CursorAdapter DataSource, e Source é o objeto ADO Command referenciado neste parâmetro. O objeto ADO RecordSet deve estar aberto quando passado para Source; CursorFill executa contra o objeto ADO RecordSet e preenche o cursor de acordo. Neste caso, apenas a propriedade CursorAdapter DataSourceType deve ser definida como "ADO". As propriedades CursorAdapter SelectCmd e DataSource não são usadas. Se você não especificar um valor para Source, CursorFill executa da seguinte maneira: CursorAdapter.DataSource.Open( CursorAdapter.SelectCmd,,,,Options ) Nesta chamada, DataSource é o objeto ADO RecordSet na propriedade CursorAdapter DataSource. No entanto, o objeto ADO RecordSet executa diretamente a propriedade CursorAdapter SelectCmd atual em vez de usar um objeto ADO Command. O ADO RecordSet deve ter sua propriedade ActiveConnection definida para um objeto ADO Connection válido.

# Valor de retorno

Tipo de dados Logical. CursorFill retorna True (.T.) se o cursor for criado com sucesso e False (.F.) se não for criado com sucesso.

> **Observação:** Se CursorFill retornar False (.F.), o cursor é descartado. Neste caso, os eventos BeforeCursorClose Event e AfterCursorClose Event não ocorrem. Para recuperar informações de erro quando CursorFill retorna False (.F.), você deve chamar a função AERROR( ) Function porque o tratamento de erros do Visual Foxpro, como o comando ON ERROR, o evento Error e o comando TRY...CATCH...FINALLY, não captura essas informações de erro.

# Observações

Aplica-se a: Classe CursorAdapter

A tabela a seguir lista como CursorFill se comporta dependendo de como a propriedade CursorAdapter DataSourceType está definida.

| DataSourceType | Comportamento da propriedade SelectCmd |
| --- | --- |
| "Native" | CursorFill executa SelectCmd, que deve conter um comando SQL SELECT válido do Visual FoxPro. |
| "ADO" | CursorFill executa SelectCmd chamando o método Open do ADO RecordSet. Você deve, portanto, definir a propriedade CursorAdapter DataSource para um objeto ADO RecordSet válido. Se SelectCmd contém parâmetros, você deve especificar um objeto ADO Command válido no parâmetro Source para o método CursorFill Fechar manualmente o cursor fecha o ADO RecordSet associado. No entanto, isso não se aplica se o cursor foi obtido usando o método CursorAttach Method. CursorFill não define a propriedade ADO RecordSet MaxRecords para a propriedade MaxRecords Property. |
| "ODBC" | CursorFill executa SelectCmd usando o identificador de conexão da propriedade DataSource do objeto CursorAdapter. O Visual FoxPro retorna o cursor usando SQL Pass-Through. O nome do cursor corresponde ao alias obtido chamando This.Alias. Observação Quando vários objetos CursorAdapter compartilham o mesmo identificador de instrução ODBC, CursorFill pode falhar para alguns objetos CursorAdapter porque outro objeto CursorAdapter não terminou de recuperar dados. Para evitar esta situação, defina a propriedade FetchSize como 1 para todos os objetos CursorAdapter ou use um identificador de instrução ODBC dedicado para cada objeto. |
| "XML" | Um dos seguintes: SelectCmd é uma expressão que é avaliada como um objeto XMLTable válido. CursorFill chama o método XMLTable ToCursor e o cursor resultante é anexado. SelectCmd é uma expressão, comando ou função que retorna XML. CursorFill usa a função XMLTOCURSOR( ) para transformar o XML em um cursor. Para obter mais informações, consulte a lista a seguir de observações adicionais. |

Além disso, quando DataSourceType está definido como "XML" e SelectCmd é uma expressão, comando ou função que retorna XML:
 - Os requisitos XML são os mesmos daqueles para o primeiro parâmetro da função XMLTOCURSOR( ). Você pode especificar esses requisitos passando o valor XMLTOCURSOR( ) nFlags apropriado para o parâmetro CursorFill nOptions. Você pode especificar flags XMLTOCURSOR( ) adicionais ou combiná-las como em XMLTOCURSOR( ).
- CursorFill escolhe entre eExpression e cXMLFile de XMLTOCURSOR( ) baseado em nOptions: Se nOptions for 0, CursorFill processa XMLSource como eExpression e espera uma variável de memória contendo uma cadeia de caracteres XML válida ou uma expressão que resulte em uma cadeia de caracteres XML. Se nOptions for 512, CursorFill processa XMLSource como cXMLFile e espera um literal de cadeia de caracteres com aspas ("") ou uma variável de memória contendo um nome de arquivo válido.
- O parâmetro cCursorName em XMLTOCURSOR( ) é sempre o valor atual na propriedade Alias do objeto CursorAdapter.
- Se lUseCursorSchema for True (.T.), CursorFill adiciona automaticamente a flag 8192 para impor o uso do cursor existente para o XML.

Quando o Visual FoxPro chama CursorFill, ele fecha o cursor atualmente anexado, se existir, e a área de trabalho que contém o cursor recém-criado torna-se a área de trabalho ativa.

> **Observação:** Se você deseja preservar o cursor atualmente anexado, chame o método CursorDetach Method antes de chamar CursorFill.

Quando o Visual FoxPro anexa um cursor, você não pode alterar o cursor ou tabela usando os comandos MODIFY STRUCTURE Command ou SQL ALTER TABLE - SQL Command.
