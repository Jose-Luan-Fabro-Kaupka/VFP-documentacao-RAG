# Janela Visual FoxPro IntelliSense Manager

O IntelliSense Manager permite executar tarefas de gerenciamento do IntelliSense:
 - General Tab Defina opções que afetam a aparência e a funcionalidade do IntelliSense, como níveis de disponibilidade de recursos e capitalização de letras para conclusão de sintaxe.
- Types Tab Gerencie itens que aparecem na caixa de listagem da cláusula AS para certos elementos de linguagem do Visual FoxPro ao implementar tipagem forte.
- Custom Tab Edite registros na tabela IntelliSense.
- Advanced Tab Edite propriedades personalizadas do IntelliSense que afetam sua funcionalidade. Execute manutenção para registros na tabela IntelliSense e outras funcionalidades do IntelliSense.

O aplicativo IntelliSense Manager é especificado pela variável de sistema _CODESENSE. Para obter mais informações, consulte _CODESENSE System Variable.

A tabela IntelliSense, que é armazenada no arquivo FoxCode.dbf, contém registros que fornecem dados para o IntelliSense Manager. Para obter mais informações, consulte Customizing IntelliSense in Visual FoxPro e _FOXCODE System Variable.

# General Tab

Controla níveis de disponibilidade e opções de formatação de capitalização de letras para a funcionalidade IntelliSense.
 **Enable IntelliSense**
Ativa ou desativa o IntelliSense no Visual FoxPro. Para obter mais informações, consulte How to: Activate or Disable IntelliSense .
**List members**
Especifica o nível de disponibilidade para a funcionalidade List Members. Os seguintes níveis estão disponíveis: Automatic Exibe caixas de listagem List Members automaticamente na posição atual do cursor quando você pressiona a tecla ativadora apropriada. Manual Exibe caixas de listagem List Members quando você seleciona List Members no menu Edit ou pressiona CTRL+J. Disabled Não exibe caixas de listagem List Members. Para obter mais informações, consulte How to: Set IntelliSense Options e IntelliSense Syntax Completion .
**Quick info tips**
Especifica o nível de disponibilidade para a funcionalidade Quick Info. Os seguintes níveis estão disponíveis: Automatic Exibe caixas de listagem Quick Info automaticamente na posição atual do cursor quando você pressiona a tecla ativadora apropriada. Manual Exibe caixas de listagem Quick Info quando você seleciona List Members no menu Edit ou pressiona CTRL+I. Disabled Não exibe caixas de listagem Quick Info. Para obter mais informações, consulte How to: Set IntelliSense Options e IntelliSense Syntax Completion .
**Browse**
Abre uma janela browse para a tabela IntelliSense. Para obter mais informações, consulte Customizing IntelliSense in Visual FoxPro e _FOXCODE System Variable .
**Tips**
Abre uma janela que exibe informações de sintaxe quando você digita caracteres suficientes para desambiguar um comando do Visual FoxPro. Use isso para comandos e funções que têm muitas cláusulas ou parâmetros. A janela Tips exibe somente informações de comandos e funções do Visual FoxPro contidas na tabela IntelliSense. IntelliSense de classe e objeto não é exibido.

### Capitalization/Expansion

Esta seção fornece a capacidade de controlar como o IntelliSense formata a capitalização de letras para sintaxe de programação nativa do Visual FoxPro ao realizar conclusão ou expansão de sintaxe. Você também pode desabilitar a expansão ou usar a capitalização de letras definida na tabela IntelliSense.
 **Functions**
Lista configurações de capitalização de letras do IntelliSense para funções do Visual FoxPro. A configuração padrão é UPPERCASE.
**Commands**
Lista configurações de capitalização de letras do IntelliSense para comandos do Visual FoxPro. A configuração padrão é UPPERCASE.
**FoxCode default**
Lista configurações de capitalização de letras para itens na tabela IntelliSense. Esta configuração serve como configuração padrão global que os itens na tabela IntelliSense podem usar se não tiverem sua própria configuração de capitalização de letras. Esta configuração é armazenada no primeiro registro Version item na tabela IntelliSense. Para obter mais informações, consulte IntelliSense Table Structure .
**Apply changes to Visual FoxPro language only**
Especifica se deve fazer alterações em todos ou somente em comandos e funções nativos do Visual FoxPro. Esta configuração é armazenada no campo Source para itens afetados na tabela IntelliSense. Para obter mais informações, consulte IntelliSense Table Structure .

# Types Tab

Controla a exibição de tipos de dados disponíveis e outros itens ao implementar tipagem forte, por exemplo, ao declarar `LOCAL myVar AS` usando o comando LOCAL. Os tipos podem ser elementos intrínsecos principais, como cadeias de caracteres, números e classes Visual FoxPro e COM. Para obter mais informações, consulte How to: Implement Strong Typing for Class, Object, and Variable Code.
 **Types**
Lista itens e tipos de dados que podem aparecer na caixa de listagem da cláusula AS para certos comandos do Visual FoxPro. Um asterisco na terceira coluna indica que o campo Data para esse item contém código de script na tabela IntelliSense. Para ocultar um item da lista, desmarque a caixa de seleção ao lado do item. Dica Para classificar por coluna, clique no cabeçalho da coluna.
**Edit**
Exibe o item selecionado da lista Types em uma janela browse para que você possa editar seu registro na tabela IntelliSense.
**Type Libraries**
Pesquisa seu registro do Windows por bibliotecas de tipos COM Server e ActiveX Control disponíveis. Você pode selecionar bibliotecas de tipos que aparecem na caixa de diálogo Type Library References para adicioná-las à lista de itens disponíveis para tipagem forte.
**Classes**
Abre a caixa de diálogo Open para que você possa selecionar uma classe Visual FoxPro que deseja adicionar à lista de itens disponíveis para tipagem forte.
**Web Services**
Abre a caixa de diálogo Visual FoxPro XML Web Services Registration para que você possa adicionar um serviço Web à lista de itens disponíveis para tipagem forte. Para detalhes, consulte Visual FoxPro XML Web Services Registration Dialog Box .

# Custom Tab

Permite adicionar ou modificar registros para itens IntelliSense definidos pelo usuário na tabela IntelliSense. No entanto, você pode visualizar todos os outros itens IntelliSense abrindo a tabela diretamente. Para obter mais informações, consulte Customizing IntelliSense in Visual FoxPro.

> **Observação:** Um asterisco na terceira coluna indica que o campo Data no registro desse item IntelliSense contém código de script na tabela IntelliSense.
 **Replace**
Especifica os caracteres que ativam a expansão de sintaxe usando os caracteres na caixa With.
**With**
Especifica os caracteres a inserir quando você digita os caracteres na caixa Replace.
**Type**
Lista tipos que você pode selecionar para o item IntelliSense.
**Script**
Abre uma janela de edição para adicionar ou editar código de script para o item IntelliSense. O código de script aparece no campo Data no registro desse item.
**Edit**
Exibe o registro inteiro para editar o item IntelliSense.
**Add**
Adiciona um novo item IntelliSense com o texto Replace e With especificado à tabela IntelliSense. Observação O botão Add torna-se disponível quando você seleciona inicialmente um tipo diferente de Command. O botão Add muda para Replace se você estiver modificando um item IntelliSense existente.
**Delete**
Exclui o item selecionado.

# Advanced Tab

Permite editar propriedades personalizadas do IntelliSense que afetam a funcionalidade do IntelliSense e executar tarefas de manutenção do IntelliSense.
 **Edit Properties**
Exibe propriedades personalizadas do IntelliSense na caixa de diálogo Custom Properties para que você possa especificar ou editar valores para funcionalidade avançada do IntelliSense. Fechar a caixa de diálogo Custom Properties salva suas alterações. Property Lista propriedades personalizadas do IntelliSense. Description Exibe uma descrição da propriedade personalizada do IntelliSense. Value Exibe o valor da propriedade personalizada do IntelliSense. A tabela a seguir descreve propriedades personalizadas do IntelliSense. Property Description Default value lEnableFullSetDisplay Controls whether to add the second word, for example, TO , automatically in certain SET commands. T lHideScriptErrors Suppresses screen output of IntelliSense script errors. F lKeywordCapitalization Enables capitalization and expansion of command keywords. T lPropertyValueEditors Enables scripts that trigger value editors for certain properties. T lExpandCOperators Enables auto expansion of C type operators, such as ++, --, +=, -+, *=, and /=. T lAllowCustomDefScripts Enables scripts to be included into the default script handler. T lEnableMultiWordCmdExp Controls whether to expand commands with multiple words. T lDebugScribts Allows debugging for IntelliSense scripts. F
**Clean Up**
Abre a caixa de diálogo Maintenance para que você possa executar tarefas de manutenção do IntelliSense. Restore Foxcode Restaura a tabela IntelliSense padrão para elementos de linguagem nativos do Visual FoxPro. Itens definidos pelo usuário permanecem, a menos que você os exclua manualmente na guia Custom do IntelliSense Manager. Clean Up FoxCode Remove registros marcados para exclusão na tabela IntelliSense. Clean Up Lists Remove arquivos que não existem mais das listas de uso mais recente (MRU). Zap Lists Remove todos os arquivos das listas de uso mais recente (MRU).
