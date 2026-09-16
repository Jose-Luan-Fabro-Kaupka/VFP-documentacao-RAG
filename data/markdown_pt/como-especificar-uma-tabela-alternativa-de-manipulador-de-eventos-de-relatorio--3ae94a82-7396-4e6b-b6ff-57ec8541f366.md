# Como: especificar uma tabela alternativa de manipulador de eventos de relatório

Reportbuilder.app contém uma tabela de pesquisa interna que define se determinadas combinações de objeto de relatório / evento de construtor são ignoradas ou direcionadas a classes específicas para manipulação.

Consulte Report Builder Event Handler Registry Table para obter informações detalhadas sobre a estrutura necessária da tabela de pesquisa.

Reportbuilder.app tem um mecanismo que permite especificar tabelas de pesquisa de manipulador de eventos alternativas para que você possa personalizar completamente como o report builder responde a eventos no Report ou Label Designer.

> **Importante:** Diferentemente das configurações na caixa de diálogo Options (Visual FoxPro), esta configuração de preferência não persiste entre sessões do Visual FoxPro.

# Definindo a tabela de registro de eventos usando a caixa de diálogo Options

A caixa de diálogo Report Builder Options (Report Builder) inclui a capacidade de especificar qual tabela de pesquisa de manipulador de eventos o report builder usa.

A caixa de texto Current registry table exibe o nome do arquivo da tabela de pesquisa que o report builder está usando. Se o construtor estiver usando a tabela integrada à aplicação, isso exibirá "internal lookup table."

### Para especificar uma tabela de pesquisa alternativa
- Abra a caixa de diálogo Report Builder Options. Consulte Como: exibir a caixa de diálogo Report Builder Options para obter etapas detalhadas que descrevem como exibir a caixa de diálogo.
- Selecione Use alternate lookup table.
- Clique na reticência ( … ) para exibir a caixa de diálogo File Open.
- Selecione a tabela desejada e clique em OK.
- Selecione Close para fechar a caixa de diálogo de opções.

### Para reverter ao uso da tabela de pesquisa interna
- Abra a caixa de diálogo Report Builder Options. Consulte Como: exibir a caixa de diálogo Report Builder Options para obter etapas detalhadas que descrevem como exibir a caixa de diálogo.
- Selecione Use internal lookup table.
- Selecione Close para fechar a caixa de diálogo de opções.

# Definindo a tabela de registro de eventos usando parâmetros de linha de comando

Você pode usar os parâmetros de linha de comando do report builder para definir a tabela de pesquisa que ele usa para localizar classes de manipulador de eventos de construtor.

### Para selecionar uma tabela de pesquisa alternativa
- Abra a Command window.
- Digite um dos comandos a seguir: DO (HOME() + "reportbuilder.app") WITH 3, cFilename * OU: DO (_REPORTBUILDER) WITH 3, cFilename

O parâmetro cFilename deve ser uma especificação de arquivo com caminho completo de um arquivo de tabela (.dbf) que contém os campos necessários. Para obter mais informações sobre a estrutura de tabela necessária, consulte Report Builder Event Handler Registry Table.

Você pode usar um asterisco para forçar o report builder a usar sua tabela de pesquisa interna:

### Para forçar o uso da tabela de pesquisa interna
- Abra a Command window.
- Digite um dos comandos a seguir: DO (HOME() + "reportbuilder.app") WITH 3, "*" * OU: DO (_REPORTBUILDER) WITH 3, "*"

Se você passar uma cadeia de caracteres vazia ao report builder, ele reverterá ao comportamento padrão, que é procurar uma tabela chamada "reportbuilder.dbf" no PATH atual e usá-la se encontrada. Se não for encontrada, o report builder usará a tabela de pesquisa interna.

### Para reverter ao comportamento padrão
- Abra a Command window.
- Digite um dos comandos a seguir: DO (HOME() + "reportbuilder.app") WITH 3, "" * OU: DO (_REPORTBUILDER) WITH 3, ""
