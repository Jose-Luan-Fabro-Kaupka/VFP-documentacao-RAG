# Controlando dados em relatórios

Antes de executar um relatório ou etiqueta, você configura os dados necessários para o layout do relatório ou etiqueta. Você fornece dados para relatórios e etiquetas escolhendo e disponibilizando fontes de dados, controlando os registros selecionados ou filtrados nessas fontes de dados, e classificando, ordenando e relacionando esses registros.

Você também pode manipular dados dentro de relatórios usando variáveis de relatório e campos calculados. Variáveis de relatório e campos calculados armazenam valores que são calculados dinamicamente durante a execução do relatório. Seus layouts de relatório podem exibir os resultados desses cálculos, bem como os dados derivados diretamente de suas fontes de dados.

# Controlando fontes de dados para relatórios

Você pode fornecer dados para relatórios e etiquetas de várias maneiras, dependendo do que é melhor para sua situação.

Se você sempre executa um relatório com as mesmas fontes de dados, pode definir um data environment que é armazenado com o relatório, apontando para tabelas específicas. Salvar o data environment coloca registros adicionais na tabela de definição do relatório ou etiqueta para todas as tabelas e arquivos de índice abertos, ordem de índice e quaisquer relacionamentos entre tabelas. As etapas que você usa para definir os objetos do data environment para um relatório ou etiquetas são as mesmas que o processo que você usa para definir o data environment para um formulário. Para obter mais informações, consulte How to: Set the Data Environment.

Você também pode disponibilizar dados para um relatório especificando as fontes de dados usando código cada vez que executa um relatório, o que é útil ao executar o mesmo relatório com fontes de dados diferentes.

A tabela a seguir descreve métodos de disponibilizar dados durante uma execução de relatório. Escolha o método que se adequa à maneira como você deseja usar fontes de dados.

| Para | Adicionar |
| --- | --- |
| Sempre usar as mesmas fontes de dados. | Tabelas ou views ao data environment do relatório. -OU- Uma instrução DO <query> ou SQL SELECT ao evento Init do data environment do relatório. Para obter mais informações, consulte DO Command, SELECT - SQL Command e Init Event. |
| Usar conjuntos separados de fontes de dados. | Uma ou mais instruções USE, USE <view>, DO <query> ou SQL SELECT ao evento Click ou outro código que precede um comando REPORT ou LABEL. Para obter mais informações, consulte USE Command e Click Event. |

> **Observação:** Use aliases com os campos da tabela selecionada ou de condução no relatório apenas se você não planeja usar o relatório com fontes de dados diferentes da tabela original. Se você usa uma view ou query como fonte de dados e aliases estão incluídos nos controles do relatório, às vezes o alias com o qual você projetou o relatório pode não estar disponível em tempo de execução. Um erro como "Alias 'X' not found" ocorre quando o mecanismo de relatório avalia expressões incluindo o alias. Em outros momentos, se a tabela original está realmente aberta, o alias pode estar disponível, mas não selecionado para esta execução de relatório. Neste caso nenhum erro ocorre, mas o relatório exibe o mesmo registro repetidamente na página do relatório.

# Controlando sessões de dados para relatórios

Como parte de decidir quando e como abrir fontes de dados para um relatório, você determina se deseja compartilhar essas fontes de dados com o ambiente do relatório.

Fontes de dados para um relatório podem ser manipuladas por seu aplicativo antes de executar o relatório. Por exemplo, você pode criar um formulário que permite ao usuário navegar por uma tabela de clientes. Quando o usuário clica em um botão Print no formulário, você executa um relatório imprimindo um extrato atual para o cliente selecionado no formulário. Neste cenário, você executa o relatório na mesma sessão de dados que o formulário.

Você também pode escolher manipular dados para o relatório imediatamente antes de executar o relatório, e completamente independente do ambiente circundante do relatório. Por exemplo, o mesmo formulário de clientes pode ter um botão ou opção de menu para Print a Sales Territory Summary, exigindo que você resuma dados de várias tabelas não usadas diretamente neste formulário. Neste cenário, você pode escolher abrir os dados do relatório em uma sessão de dados privada. Quando o relatório termina de imprimir, o data environment do formulário e o registro de cliente selecionado não são perturbados.

Para obter mais informações, consulte How to: Specify a Report's Data Session.

# Controlando seleção de registros

Por padrão, quando você executa um relatório contra uma tabela, cada registro na tabela é processado. O relatório avalia expressões no layout do relatório para cada registro, exibindo resultados apropriados.

Você pode controlar a seleção dos registros que aparecem no relatório através da fonte de dados, opções de impressão do relatório, ou ambos.

A tabela a seguir descreve como controlar a seleção de registros no relatório baseado em se você usa uma fonte de dados ou opções de impressão do relatório.

| Ao usar para seleção de registros | Use |
| --- | --- |
| View ou query | Condições na guia Filter do View Designer ou Query Designer. Para obter mais informações, consulte Filter Tab, Query and View Designers. |
| Instrução SQL SELECT | Cláusula WHERE ou HAVING. Para obter mais informações, consulte SELECT - SQL Command. |
| Report Designer | Configuração na caixa de diálogo Print Options. Para obter mais informações, consulte Report and Label Print Options Dialog Box. |
| Comando REPORT FORM | Expressões Scope, FOR ou WHILE. Para obter mais informações, consulte REPORT FORM Command e Field and Record Manipulation. |
| Tabela | Índice filtrado. Para obter mais informações, consulte INDEX Command. |

# Controlando relacionamentos de registros

Relatórios e etiquetas processam seus registros selecionados movendo o ponteiro de registro na área de trabalho atual. Ao configurar relacionamentos entre a tabela ou view aberta nas áreas de trabalho atuais e outras fontes de dados, você pode acessar outros campos para uso em expressões de relatório. Você pode definir os relacionamentos em código, usando os comandos SET RELATION e SET SKIP, ou usando objetos Relation no DataEnvironment.

Quando você se refere a campos que não estão na área de trabalho atual em expressões de relatório, você prefixa os nomes dos campos com o alias sob o qual as tabelas ou views adicionais estão abertas. Consulte How to: Create and Use Table Aliases para obter mais informações.

> **Observação:** A tabela ou view na área de trabalho atual conduz o REPORT FORM ou LABEL FORM e é frequentemente denominada seu alias de condução. Tabelas ou views nas áreas de trabalho relacionadas são conhecidas como aliases de destino porque essas áreas de trabalho são os destinos do comando SET RELATION. Quando você estabelece relacionamentos entre tabelas, pode alterar a maneira como relatórios e etiquetas se movem pelos seus dados, para contabilizar múltiplos registros nos aliases de destino que podem estar relacionados a cada registro no alias de condução. Por exemplo, um relatório em uma tabela de informações de resumo de faturas pode estar relacionado a múltiplas linhas de detalhe para cada fatura. Consulte Working with Related Tables using Multiple Detail Bands in Reports para informações sobre coordenar múltiplas tabelas e relacionamentos em relatórios.

# Controlando ordem de registros

O layout de página para relatórios e etiquetas não classifica e ordena dados de fato. Ele processa registros na mesma ordem em que existem na fonte de dados. Você deve realizar a classificação com uma view, índice ou outra forma de manipulação de dados fora do layout.

Por exemplo, se a fonte de dados é uma tabela, você pode classificar e ordenar os dados definindo um índice apropriado para a tabela, usando uma view ordenada no data environment, ou usando uma query como fonte de dados para exibir os registros em grupos. Você pode criar um índice de tabela usando código, por exemplo, usando o comando INDEX, ou como parte do data environment do relatório. Se a fonte de dados é uma query, view ou instrução SQL SELECT, você pode usar a cláusula ORDER BY.

Se você não usa as fontes de dados do relatório para controlar a ordem dos registros, a única maneira de controlar a ordem dos registros através do relatório é através da propriedade Order de um cursor no data environment.
