# Classe Foundation Data Session Manager

Esta classe é usada para gerenciar sessões de dados e tratar atualizações de dados em todos os formulários ou formsets na sessão de dados atual. Ela permite que um objeto Application percorra facilmente as sessões para fornecer comportamento de fechamento de janelas durante Exit ou Shutdown. Também fornece comportamento genérico de QueryUnload para formulários e formsets, e código genérico de Update e Revert em toda a sessão. Você pode usá-la para avaliar se algum dado foi alterado em uma sessão antes de usar seu próprio procedimento de tratamento de conflitos.

| Category | Application |
| --- | --- |
| Default Catalog | Visual FoxPro Catalog\Foundation Classes\Application |
| Class | _datassession |
| Base Class | Custom |
| Class Library | _app.vcx |
| Parent Class | _custom |
| Sample | ...\Samples\Solution\Ffc\environ.scx |

# Observações

Esta classe funciona com tabelas livres, bem como com tabelas em bancos de dados. Observe o limite de transações (5).

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item da Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca a classe no formulário. Você pode então especificar os valores de propriedade apropriados e fornecer quaisquer objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de classes foundation.

| Properties, Events, Methods | Description |
| --- | --- |
| iDataChangedMode property | Especifica o tipo de alteração de dados realizada. 0 - Tudo alterado. 1 - Ignorar campos de view que não estão na lista Updatefields. 2- Ignorar views que não estão definidas para enviar atualizações. Padrão: 0 |
| iSavedSessionID property | Especifica valor inteiro representando o ID da sessão salva. Padrão: 1 |
| lSuccess property | Especifica se a operação de dados (update) foi bem-sucedida. Padrão: .T. |
| lUseTransactions property | Especifica se deve envolver a rotina de atualização em uma transação. Observação Apenas tabelas em um contêiner de banco de dados (.dbc) são afetadas em transações. Padrão: .T. |
| DataChanged method | Verifica se os dados foram alterados. Sintaxe: DataChanged( ) Retorno: nenhum Argumentos: nenhum |
| DataFlush method | Garante que o controle ativo terá seu conteúdo atual "reconhecido" mesmo se você escolher atualizar a partir de um botão da barra de ferramentas enquanto um grid tem o foco. Sintaxe: DataFlush( ) Retorno: nenhum Argumentos: nenhum |
| GetActiveControlRef method | Retorna o controle verdadeiramente ativo, loRealActiveControl , nos casos em que o controle ativo atual é um Grid. Sintaxe: GetActiveControlRef(toActiveControl) Retorno: loRealActiveControl Argumentos: toActiveControl especifica o controle atual. |
| GetMessageBoxTitle method | Retorna uma parte do texto da barra de título especificando o nome da mensagem. Sintaxe: GetMessageBoxTitle( ) Retorno: cTitlebarText Argumentos: nenhum |
| QueryUnload method | Fornece caixas de diálogo para gerenciar decisões de alteração de dados. Sintaxe: QueryUnload(tlDataChangeAlreadyConfirmed, toForm, tlNoShow) Retorno: liResult Argumentos: tlDataChangeAlreadyConfirmed especifica se os dados foram alterados. toForm especifica o formulário. tlNoShow especifica se o formulário deve ser exibido. liResult especifica o MESSAGEBOX ou valor. |
| RestoreSessionID method | Restaura a sessão de dados. Sintaxe: RestoreSessionID Retorno: nenhum Argumentos: nenhum |
| Revert method | Reverte a sessão para os dados originais. Sintaxe: Revert(tlUserChoiceAlreadyConfirmed, tlDataChangeAlreadyConfirmed, toForm, tlNoShow) Retorno: nenhum Argumentos: tlUserChoiceAlreadyConfirmed especifica se deve exibir uma caixa de diálogo de confirmação. tlDataChangeAlreadyConfirmed especifica se deve exibir uma caixa de diálogo de confirmação. toForm especifica o formulário. tlNoShow especifica se o formulário deve ser exibido. |
| SetSessionID method | Define a sessão de dados. Sintaxe: SetSessionID( ) Retorno: nenhum Argumentos: nenhum |
| Update method | Atualiza dados. Sintaxe: Update(tlUserChoiceAlreadyConfirmed, tlDataChangeAlreadyConfirmed, toForm, tlNoShow) Retorno: nenhum Argumentos: tlUserChoiceAlreadyConfirmed especifica se deve exibir uma caixa de diálogo de confirmação. tlDataChangeAlreadyConfirmed especifica se deve exibir uma caixa de diálogo de confirmação. toForm especifica o formulário. tlNoShow especifica se o formulário deve ser exibido. |
