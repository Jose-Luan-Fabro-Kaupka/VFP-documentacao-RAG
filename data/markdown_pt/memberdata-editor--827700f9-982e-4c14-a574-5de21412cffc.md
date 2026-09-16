# MemberData Editor

A aplicação MemberData Editor permite que desenvolvedores editem MemberData Extensibility. O MemberData Editor apresenta uma interface fácil de usar para que você possa visualizar e editar MemberData associado às suas classes.

Para executar o MemberData Editor, selecione o item de menu MemberData Editor no menu Form ou Class quando um Form ou Class Designer estiver ativo. O membro selecionado na janela Properties será selecionado no MemberData Editor. No entanto, você pode clicar e editar MemberData de outros membros da classe selecionada no designer.

O MemberData que você visualiza e edita é armazenado com a propriedade _MemberData, que você também pode editar diretamente na janela Properties. MemberData global é armazenado na tabela da variável de sistema _FOXCODE. MemberData é formatado como XML.

# Usando o MemberData Editor

Você pode visualizar e editar MemberData usando o MemberData Editor. O seguinte
 **Member List**
Contém uma lista de todos os membros disponíveis (propriedades, eventos e métodos) para a classe selecionada no designer. Selecione um membro para adicionar ou alterar seu MemberData. Um prefixo de caractere ">>" indica que o membro tem MemberData associado. Se o membro estiver em negrito, ele tem MemberData para o Scope selecionado.
**Scope**
A configuração Scope especifica onde o MemberData é armazenado. As seguintes configurações estão disponíveis: Object – MemberData disponível no nível do objeto. Esta opção requer que o objeto selecionado tenha uma propriedade _MemberData, caso contrário esta opção é desabilitada. Container – MemberData disponível no nível do contêiner, como um formulário. Se um objeto não tem seu próprio MemberData, ele pode herdar do seu contêiner. Se existirem vários contêineres, cada um com sua própria propriedade _MemberData, o dropdown de contêiner é habilitado. Global – MemberData no nível global (sua tabela _FOXCODE). Esta configuração não é específica do objeto. Se um objeto não herda do MemberData do objeto ou contêiner, usará a configuração Global se disponível. Você deve entender as regras de herança com MemberData, pois isso impacta a configuração Scope. O MemberData Editor, quando invocado, é aberto para o objeto e propriedade atualmente selecionados. Por exemplo, se um controle Textbox em um formulário estiver selecionado e o controle Textbox não contiver uma propriedade _MemberData, você não pode especificar MemberData no nível do objeto Textbox. Você só pode especificar no nível do contêiner (formulário) ou global.
**Has MemberData**
Selecione esta opção para adicionar MemberData para o membro selecionado. XML de MemberData é adicionado somente para o Scope selecionado.
**Description Pane**
Lista os atributos MemberData definidos para o membro selecionado e qual Scope controla atualmente a configuração. Observação O botão Hierarchy exibe detalhes de MemberData para todos os escopos do membro selecionado.
**Filter**
Você pode filtrar a lista de Members com base nos seguintes critérios: All members - todos os membros do objeto selecionado são listados. Custom members only - somente propriedades ou métodos personalizados são listados. Custom members added in this class - somente propriedades ou métodos personalizados adicionados à instância atual do objeto são listados. Membros personalizados herdados não são mostrados. Native members only - exibe somente membros intrínsecos do Visual FoxPro. Favorites only - exibe membros que têm um atributo MemberData Favorites atribuído.
**View XML**
Exibe detalhes XML de MemberData para todos os membros do objeto selecionado no escopo selecionado.
**Hierarchy**
Exibe detalhes de atributos MemberData para todos os escopos do membro selecionado.
**Options**
Abre a caixa de diálogo Options.

# Atributos principais de MemberData

O Visual FoxPro reserva certos atributos MemberData para o uso operacional de membros na IDE do Visual FoxPro. Os seguintes atributos podem ser definidos usando o MemberData Editor:
 **Favorites**
Permite controlar se um membro é exibido na guia Favorites da janela Properties. Se você marcar esta opção, pode especificar True ou False na caixa de lista suspensa. A caixa de seleção determina se o atributo favorites é gravado no XML de MemberData e tem implicações na herança de cima.
**Override**
Permite controlar se atributos MemberData não encontrados para aquele membro são pesquisados na hierarquia. Se você marcar esta opção, pode especificar True ou False na caixa de lista suspensa. A caixa de seleção determina se o atributo override é gravado no XML de MemberData e tem implicações na herança de cima.
**Display As**
Controla como o membro é exibido na IDE do Visual FoxPro, como na janela Properties e no IntelliSense. Esta opção está disponível somente para membros personalizados (definidos pelo usuário). Esta configuração é representada pelo atributo display.
**Script**
Você pode inserir um script que é invocado quando o usuário clica no botão de reticências (…) ao lado da caixa de configurações de Property na janela Properties. A caixa Script e o botão são habilitados somente para propriedades. Clique no botão Script para abrir o script em uma janela de edição maior. Esta configuração é representada pelo atributo script. Observação Scripts estão disponíveis para todas as propriedades personalizadas e algumas propriedades nativas.

# Atributos MemberData definidos pelo usuário

MemberData é uma estrutura formatada em XML que permite extensibilidade. O Visual FoxPro fornece certos usos principais de MemberData, como Favorites. Você também pode adicionar atributos personalizados ao XML de MemberData para uso que você define. O Visual FoxPro armazenará e retém esses atributos personalizados com o MemberData principal.
 **Custom Attributes List**
Lista todos os atributos personalizados de MemberData para o membro selecionado.
**Value**
Define um valor para o atributo personalizado selecionado na lista.
**Add**
Adiciona um novo atributo personalizado ao MemberData. Como em todos os atributos XML, os que você adiciona são sensíveis a maiúsculas e minúsculas. Você não pode adicionar um nome que já esteja reservado, como favorites.
**Remove**
Remove um atributo personalizado do MemberData.

# Caixa de diálogo Options

A caixa de diálogo Options permite controlar várias configurações da interface do usuário do MemberData Editor, bem como opções para o MemberData gerado.
 **Use Hungarian names**
A capitalização padrão de propriedade para a configuração Display as (atributo display) define a primeira letra em minúscula e o restante em maiúsculas/minúsculas adequadas.
**Method prefixes**
Contém uma lista delimitada por vírgulas de prefixos para controlar como a capitalização é feita para MemberData quando um método personalizado tem um prefixo que corresponde a um desta lista. Quando um é encontrado, o MemberData Editor capitaliza o prefixo baseado no que está na lista e capitaliza o restante do nome em maiúsculas/minúsculas adequadas.
**Line break after each XML element**
Especifica se uma quebra de linha é inserida após cada elemento XML em _MemberData recém-gerado.
**Automatically add _MemberData property to objects**
Se esta configuração estiver ativada, um registro é adicionado à sua tabela IntelliSense (_FOXCODE) que cria automaticamente uma propriedade _MemberData para um formulário aberto no Form Designer ou o objeto mais externo no Class Designer.
**Script Font**
Especifica a fonte usada na caixa de edição Script.
