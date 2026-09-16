# Caixa de diálogo Work Area Properties

Permite modificar a estrutura de uma tabela, selecionar arquivos de índice e campos e definir filtros de dados. Esta caixa de diálogo aparece quando você escolhe Properties no Table Menu.
 **Cursor**
Exibe o título da tabela aberta atualmente.
**Enable data buffering**
Ativa o buffering.

# Lock Records
 **When edited**
Impede o acesso por outros usuários enquanto você edita registros. Isso também é conhecido como buffering pessimista.
**When written**
Permite acesso por outros usuários até que o registro seja atualizado. Isso também é conhecido como buffering otimista.

# Buffer
 **Current record**
Habilita o buffering somente do registro atual. Isso também é conhecido como record buffering.
**All edited records**
Habilita o buffering de todos os registros editados. Isso também é conhecido como table buffering. Observação Quando você seleciona Buffer Current Record , SET MULTILOCKS Command são automaticamente definidos como ON (se estiverem desligados no momento), mas não são definidos como OFF se você limpar Buffer Current Record ou selecionar Buffer All Edited Records . Defina os padrões para novas tabelas na guia Data, Options Dialog Box .
**Data filter**
Fornece uma caixa de texto para digitar uma expressão de filtro de dados. Alternativamente, o botão de diálogo exibe a Expression Builder Dialog Box , na qual você pode especificar quais registros na tabela ativa estarão disponíveis para processamento. Corresponde ao comando SET FILTER.
**Index order**
Especifica a ordem de índice da tabela. No Database Designer , o índice primário da tabela aparece com um símbolo de chave ao lado dele na lista de índices. Corresponde ao comando SET ORDER.

# Allow Access To
 **All fields in the work area**
Especifica que o usuário tenha acesso a todos os campos na work area. Corresponde ao comando SET FIELDS.
**Only fields specified by field filter**
Especifica que somente registros que correspondam às seleções na Field Picker Dialog Box sejam exibidos ou disponíveis para edição.
**Field Filter**
Exibe a caixa de diálogo Field Picker, na qual você controla o número de campos ativos.
**Modify**
Exibe o Table Designer , no qual você pode modificar tabelas de banco de dados e tabelas livres, campos e índices.
