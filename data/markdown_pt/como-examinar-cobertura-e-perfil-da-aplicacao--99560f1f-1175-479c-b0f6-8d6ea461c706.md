# Como: examinar cobertura e perfil da aplicação

Para usar o Coverage Profiler de forma eficaz, prepare sua aplicação e seu ambiente com cuidado. Se você seguir as diretrizes a seguir, o Coverage Profiler pode fornecer informações precisas e úteis sobre seu projeto ou aplicação.

### Para usar o Coverage Profiler para examinar a cobertura da aplicação
- Use a opção Coverage Logging do menu Ferramentas do Depurador ou o Comando SET COVERAGE para iniciar o fluxo de dados de cobertura e abrir o arquivo para registrar esses dados.
- Execute o programa ou aplicação que você deseja examinar para cobertura.
- Execute a aplicação de cobertura no menu Ferramentas ou use DO (_COVERAGE) na janela Comando. A aplicação Coverage Profiler inicia no modo Coverage por padrão.

### Para usar o Coverage Profiler para examinar o perfil da aplicação
- Use o Comando SET COVERAGE para iniciar o fluxo de dados de cobertura e abrir o arquivo para registrar esses dados.
- Execute o programa ou aplicação que você deseja perfilar.
- Execute a aplicação de cobertura no menu Ferramentas ou use DO ( _COVERAGE ) na janela Comando.
- Clique no botão Profile Mode na caixa de diálogo Coverage Profiler. Se você descobrir que está mais interessado em perfilamento, pode alterar o padrão para Profile Mode na Caixa de diálogo Opções do Coverage Profiler.

### Para usar o Coverage Profiler com um arquivo de log específico
- Execute a aplicação de cobertura usando a opção WITH e o nome do arquivo de log como no exemplo a seguir: DO (_COVERAGE) WITH "Mylog.LOG" Este exemplo usa o arquivo de log Mylog.log e abre a janela da aplicação Coverage Profiler para exibir os resultados. Se você não especificar um nome de arquivo, o Coverage Profiler usa o log especificado em um comando SET COVERAGE TO atual ou exibe a caixa de diálogo Abrir arquivo quando o registro de cobertura está OFF.

### Para usar o Coverage Profiler sem a interface do usuário
- Execute a aplicação de cobertura usando a opção WITH e especifique true (.T.) para execução em modo não assistido como no exemplo a seguir: DO (_COVERAGE) WITH "Mylog.LOG",.T. Neste exemplo, a aplicação Coverage Profiler usa o arquivo de log Mylog.log e é executada sem exibir a janela da aplicação Coverage Profiler.

### Para usar o Coverage Profiler com um arquivo Add-In específico
- Execute a aplicação de cobertura usando a opção WITH e o nome do arquivo add-in como no exemplo a seguir: DO (_COVERAGE) WITH "Mylog.LOG",, "add_ui.prg" Este exemplo usa o arquivo de log Mylog.log e abre a janela da aplicação Coverage Profiler para exibir os resultados, e então o programa Add-In ADD_UI.PRG é executado. O segundo parâmetro, não especificado, é um valor lógico que especifica se o mecanismo de cobertura opera em modo não assistido. Na configuração padrão, false (.F.), a janela do Coverage Profiler é exibida.

Além de visualizar as informações do profiler, você pode inserir comentários ou marcadores e salvar as informações como um arquivo para usar posteriormente.
