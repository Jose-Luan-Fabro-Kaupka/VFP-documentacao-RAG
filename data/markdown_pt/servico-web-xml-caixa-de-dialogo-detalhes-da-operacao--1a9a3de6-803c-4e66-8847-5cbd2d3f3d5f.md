# Serviço Web XML — Caixa de diálogo Detalhes da operação

Permite escolher operações ou métodos específicos que você deseja chamar em seu aplicativo. Você também pode especificar valores de parâmetros para essas operações.

Essa caixa de diálogo aparece quando você clica em Adicionar ou Editar no grupo Operações da guia Operações do Construtor de Serviços Web XML. Para obter mais informações, consulte Guia Operações, Construtor de Serviços Web XML.
 **Nome**
Especifica um nome que você deseja usar para se referir à operação.
**Descrição**
Especifica uma descrição para a operação. (Opcional)
**Selecionar uma operação (método)**
Especifica a operação que você deseja usar. Os detalhes da operação selecionada aparecem na caixa Sintaxe, incluindo quaisquer parâmetros definidos anteriormente.
**Definir parâmetro(s)**
Especifica como os valores de parâmetros são definidos para a operação: Inserir valores agora Permite definir antecipadamente os valores dos parâmetros. Para especificar valores ou origens de parâmetros de tempo de execução, clique em Definir para abrir a caixa de diálogo Serviço Web XML — Valores de parâmetros. Definir programaticamente em tempo de execução Define os valores dos parâmetros em tempo de execução usando a coleção de parâmetros da operação. Solicitar em tempo de execução Especifica que uma caixa de diálogo seja exibida para inserção de valores quando a operação for chamada em tempo de execução. A caixa de diálogo oferece suporte somente a tipos de dados simples.
**Definir**
Exibe uma caixa de diálogo para que você defina valores de parâmetros para a operação. Essa opção só fica disponível quando Inserir valores agora está selecionado na caixa Definir parâmetro(s).
**Sintaxe**
Exibe a sintaxe da operação.

# Opções
 **Permitir o cache offline de chamadas ao serviço Web**
Especifica que as chamadas de operação, incluindo valores de parâmetros e resultados, sejam armazenadas localmente. Se a operação for chamada offline usando os mesmos parâmetros, os resultados originais serão retornados, permitindo que seu aplicativo seja executado desconectado sem interrupção.
