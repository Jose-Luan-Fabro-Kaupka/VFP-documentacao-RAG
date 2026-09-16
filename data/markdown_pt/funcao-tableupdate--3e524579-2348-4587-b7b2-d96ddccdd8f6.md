# Função TABLEUPDATE( )

Confirma alterações feitas em uma linha em buffer, em uma tabela em buffer, cursor ou cursor adapter.

```foxpro
TABLEUPDATE( [nRows [, lForce]] [, cTableAlias | nWorkArea] [, cErrorArray] )
```

#### Parâmetros
 **nRows**
Especifica quais alterações feitas na tabela ou cursor devem ser confirmadas. Observação O Visual FoxPro habilita Optimistic Row Buffering por padrão para os cursores associados a um objeto CursorAdapter. A tabela a seguir descreve os valores para nRows . nRows Description 0 Se o buffer de linha ou de tabela estiver habilitado, confirma apenas as alterações feitas na linha atual do cursor. (Padrão) Ao trabalhar com objetos CursorAdapter, o Visual FoxPro executa o comando apropriado na propriedade InsertCmd , UpdateCmd ou DeleteCmd apenas para essa linha. 1 Se o buffer de tabela estiver habilitado, confirma as alterações feitas em todos os registros na tabela ou cursor. Se o buffer de linha estiver habilitado, confirma apenas as alterações feitas no registro atual na tabela ou cursor. Ao trabalhar com objetos CursorAdapter, o Visual FoxPro executa os comandos apropriados nas propriedades InsertCmd , UpdateCmd e DeleteCmd para cada linha afetada. 2 Confirma as alterações feitas na tabela ou cursor da mesma forma que quando nRows = 1. No entanto, um erro não ocorre quando uma alteração não pode ser confirmada. O Visual FoxPro continua a processar os registros restantes na tabela ou cursor. Se cErrorArray for incluído, uma matriz contendo informações de erro é criada quando ocorre um erro. Para compatibilidade com aplicativos anteriores do Visual FoxPro, o parâmetro nRows também aceita False (.F.) e True (.T.) em vez de 0 e 1, respectivamente. Ao especificar 0 ou 1 para nRows , o ponteiro de registro permanece no registro em que as alterações não puderam ser confirmadas. Para determinar por que as alterações não puderam ser confirmadas, use a função AERROR( ) . Ao trabalhar com objetos CursorAdapter e especificar 1 ou 2 para nRows , todas as alterações feitas no cursor nos seguintes eventos CursorAdapter devem ser confirmadas na mesma chamada a TABLEUPDATE( ), a menos que ocorra um erro: BeforeInsert AfterInsert BeforeDelete AfterDelete BeforeUpdate AfterUpdate O Visual FoxPro passa os valores de nRows para o evento BeforeCursorUpdate do CursorAdapter.
**lForce**
Determina se o Visual FoxPro sobrescreve alterações feitas na tabela ou cursor por outro usuário em uma rede. A tabela a seguir descreve os valores para lForce . lForce Description False (.F.) Confirma alterações na tabela ou cursor, começando pelo primeiro registro e continuando em direção ao final da tabela ou cursor. (Padrão) True (.T.) Sobrescreve quaisquer alterações feitas na tabela ou cursor por outro usuário em uma rede. A cláusula WHERE usa apenas campos-chave. Ao trabalhar com objetos CursorAdapter, o Visual FoxPro passa o valor de lForce para os seguintes eventos CursorAdapter: BeforeCursorUpdate BeforeInsert BeforeUpdate BeforeDelete AfterInsert AfterUpdate AfterDelete
**cTableAlias**
Especifica o alias da tabela ou cursor em que as alterações são confirmadas. Se você incluir um alias de tabela ou cursor, deve incluir o argumento lForce .
**nWorkArea**
Especifica a área de trabalho da tabela ou cursor em que as alterações são confirmadas. Se você incluir uma área de trabalho, deve incluir o argumento lForce .
**cErrorArray**
Especifica o nome de uma matriz criada quando nRows = 2 e as alterações em um registro não podem ser confirmadas. A matriz contém uma única coluna com os números de registro dos registros cujas alterações não puderam ser confirmadas. Se você incluir um nome de matriz, deve incluir um alias de tabela ou cursor cTableAlias ou um número de área de trabalho nWorkArea . Observação Se ocorrer um erro diferente de um simples erro de confirmação durante a atualização de registros, o primeiro elemento de cErrorArray conterá –1, e você poderá então usar AERROR( ) para determinar por que as alterações não puderam ser confirmadas. O Visual FoxPro passa o valor de cErrorArray , quando existir, para o evento AfterCursorUpdate do CursorAdapter.

# Valor de retorno

Tipo de dados lógico. TABLEUPDATE( ) retorna True (.T.) se as alterações em todos os registros forem confirmadas.

Caso contrário, TABLEUPDATE( ) retorna False (.F.), indicando falha. Uma rotina ON ERROR não é executada. A função AERROR( ) pode ser usada para recuperar informações sobre a causa da falha.

> **Observação:** TABLEUPDATE( ) sempre retorna True (.T.) quando você está atualizando dados, usando Table Buffering, e atualizando a tabela ou tabelas na fonte de dados a partir de vários clientes ao definir BatchUpdateCount com um valor maior que 1. Portanto, evite definir BatchUpdateCount com um valor maior que 1 nesses cenários.

# Observações

TABLEUPDATE( ) não pode confirmar alterações feitas em uma tabela ou cursor que não tenha buffer de linha ou de tabela habilitado. Se você emitir TABLEUPDATE( ) e o buffer de linha ou de tabela não estiver habilitado, o Visual FoxPro gera uma mensagem de erro. No entanto, TABLEUPDATE( ) ainda pode confirmar alterações em uma tabela ou cursor que tenha regras de validação. Para habilitar ou desabilitar o buffer de linha e de tabela, use CURSORSETPROP( ).

As alterações são confirmadas na tabela ou cursor aberta na área de trabalho atualmente selecionada se TABLEUPDATE( ) for emitido sem os argumentos opcionais cTableAlias ou nWorkArea .

Se o buffer de tabela for usado e vários registros forem atualizados, TABLEUPDATE( ) move o ponteiro de registro para o último registro atualizado.

> **Observação:** Chamar TABLEUPDATE( ) para uma tabela ou exibição local que não usa campos-chave gera uma cláusula WHERE longa para localizar a linha de atualização. O número padrão de campos suportados na cláusula WHERE é 40. Se você receber o erro SQL: Statement too long (Error 1812) , deve usar um campo-chave para a atualização ou aumentar a complexidade da cláusula WHERE com SYS(3055) . Se você usar a função SYS(3055) , aumente seu valor para um número que seja oito vezes o número de campos na tabela, conforme mostrado no exemplo a seguir:

```foxpro
SYS(3055, 8 * MIN(40, FCOUNT())
```

Ao executar uma operação TABLEUPDATE( ) em lote, devido à forma como o Open Database Connectivity (ODBC) se comporta, o Visual FoxPro não é capaz de detectar conflitos quando nenhum erro é gerado pelo servidor, mas nada é atualizado, por exemplo, quando nenhuma linha corresponde à cláusula WHERE. Isso pode ocorrer quando você usa WhereType definido como DB_KEYANDUPDATABLE, DB_KEYANDMODIFIED ou DB_KEYANDTIMESTAMP, e outro usuário alterou um dos valores subjacentes na cláusula WHERE de modo que a linha não é encontrada pela instrução de atualização.

Interação com objetos CursorAdapter Os seguintes comportamentos se aplicam ao trabalhar com objetos CursorAdapter:
 - TABLEUPDATE( ) opera apenas no cursor associado ao objeto CursorAdapter.
- TABLEUPDATE( ) executa comandos de acordo com o tipo de fonte de dados e aqueles armazenados nas propriedades InsertCmd , UpdateCmd ou DeleteCmd do CursorAdapter contra a linha ou linhas atuais do cursor, conforme apropriado.
- TABLEUPDATE( ) passa o valor de GETFLDSTATE(1) para os seguintes eventos CursorAdapter de cada linha afetada: BeforeInsert BeforeUpdate BeforeDelete Para obter mais informações sobre GETFLDSTATE( ) , consulte GETFLDSTATE( ) Function .
- A conclusão bem-sucedida de TABLEUPDATE( ) redefine os estados dos campos de acordo com o comportamento usual de TABLEUPDATE( ) .
- Quando o buffer de tabela está habilitado, você pode sair do registro atual nos seguintes eventos CursorAdapter: BeforeInsert AfterInsert BeforeUpdate AfterUpdate BeforeDelete AfterDelete Você também pode modificar dados no cursor. Essa funcionalidade suporta cenários como recuperar o valor autoincrement da tabela base e inseri-lo no cursor. Quando esse cenário ocorre, o objeto CursorAdapter deve retornar automaticamente ao registro cujas alterações estão prestes a ser confirmadas após a ocorrência do evento e confirmar as alterações. No Visual FoxPro 9.0, você não pode emitir a função TABLEREVERT( ) quando uma TABLEUPDATE( ) está em operação. Normalmente, o objeto CursorAdapter usa a funcionalidade de gerenciamento de transações fornecida pelas APIs ADO ou ODBC e o Visual FoxPro fecha transações quando a função TABLEUPDATE( ) é concluída com sucesso. No entanto, se você desejar enviar comandos de gerenciamento de transação diretamente para o backend, pode definir a propriedade UseTransactions do objeto CursorAdaptor como False (.F.) e o CursorAdapter não usa transações para enviar comandos Insert, Update ou Delete.

# Exemplo

O exemplo a seguir demonstra como você pode usar TABLEUPDATE( ) para confirmar alterações feitas em uma tabela em buffer. Uma tabela chamada `employees` é criada, e uma instrução SQL INSERT insere o valor "Smith" no campo `cLastName` .

MULTILOCKS é definido como `ON`, o que é um requisito para o buffer de tabela. CURSORSETPROP( ) é usado para definir o modo de buffer como Optimistic Table Buffering (5).

O valor original do campo `cLastName` (Smith) é exibido, e o campo `cLastName` é modificado com REPLACE. O novo valor do campo `cLastName` (Jones) é exibido. TABLEUPDATE( ) é usado para confirmar alterações na tabela (TABLEREVERT( ) poderia ser emitido em vez disso para descartar as alterações). O valor atualizado do campo `cLastName` (Jones) é então exibido.

```foxpro
CLOSE DATABASES
CREATE TABLE employee (cLastName C(10))
SET MULTILOCKS ON  && Must turn on for table buffering.
= CURSORSETPROP('Buffering', 5, 'employee' )  && Enable table buffering.
INSERT INTO employee (cLastName) VALUES ('Smith')
CLEAR
? 'Original cLastName value: '
?? cLastName  && Displays current cLastName value (Smith).
REPLACE cLastName WITH 'Jones'
? 'New cLastName value: '
?? cLastName  && Displays new cLastName value (Jones).
= TABLEUPDATE(.T.)  && Commits changes.
? 'Updated cLastName value: '
?? cLastName  && Displays current cLastName value (Jones).
```
