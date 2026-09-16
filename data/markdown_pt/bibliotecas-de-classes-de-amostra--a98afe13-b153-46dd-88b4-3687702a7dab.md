# Bibliotecas de classes de amostra

A biblioteca de classes de amostra do Visual FoxPro fornece funcionalidade encapsulada que você pode facilmente adicionar às suas aplicações. As Solution Samples ilustram o uso da maioria das classes de amostra. As classes de amostra estão contidas nos seguintes arquivos:
 - Buttons Class Library
- Samples Class Library
- Utility Class Library
- Registry Program

# Buttons Class Library

Buttons.vcx contém as seguintes classes.

| Classe | Descrição |
| --- | --- |
| CmdOK | Um command button que libera o formulário ao qual é adicionado. Se o formulário estiver contido em um form set, cmdOK libera o form set. |
| CmdCancel | Uma subclasse de cmdOK com a propriedade Caption definida como "Cancel." |
| CmdHelp | Um command button que invoca a Ajuda com o HelpContextID do formulário ao qual é adicionado. |
| MailBtn | Um container com um command button, um controle Microsoft MAPI Message e um controle Microsoft MAPI Session. O código no evento Click do command button faz logon no correio e compõe uma mensagem contendo os valores no registro atual de uma tabela. Para um exemplo de uso da classe MailBtn, consulte SENDMAIL.SCX na pasta Visual FoxPro Samples\Solution\OLE. |
| VCR | Um conjunto de botões de navegação de tabela que permite que um usuário mova o ponteiro de registro para os registros next, prior, top e bottom de uma tabela. Defina a propriedade Skiptable como o alias da tabela na qual deseja mover o ponteiro de registro. Se Skiptable estiver vazio, o ponteiro de registro é movido na área de trabalho atualmente selecionada. |

# Samples Class Library

Samples.vcx contém as seguintes classes.

| Classe | Descrição |
| --- | --- |
| CboFontName | Um combo box que exibe todas as fontes atualmente disponíveis no sistema. |
| CboFontSize | Um combo box que exibe todos os tamanhos de ponto disponíveis para uma fonte específica. Passe um nome de fonte ao método FillList para preencher o combo box. As propriedades nLargestFont e nSmallestFont delimitam os tamanhos de fonte máximo e mínimo exibidos. Você pode usar este controle em conjunto com a classe cboFontName. No evento InteractiveChange do objeto cboFontName, chame o método FillList do objeto cboFontSize: THISFORM.cboFontSize1.FillList(THIS.Value) Para um exemplo de uso desta classe, consulte a classe tbrEditing na mesma biblioteca de classes. |
| Clock | Um container que exibe a data e hora atuais. O componente "Display a system clock" na amostra Solutions também usa a classe Clock. |
| Datachecker | Uma classe personalizada que gerencia a resolução de conflitos de dados. O código no evento Error da classe VCR em BUTTONS.vcx chama o método CheckConflicts desta classe se uma tentativa de gravar dados em buffer em uma tabela encontrar valores alterados: nConflictStatus = ; THIS.DataChecker1.CheckConflicts() O componente "Run multiple instances of a form" na amostra Solutions também usa esta classe para verificar conflitos de dados. Para obter mais informações, abra a classe e leia os comentários no código. |
| Distinct_values_combo | Um combo box que é preenchido na inicialização com os valores distintos no alias ControlSource. Por exemplo, se você adicionar esta classe a um formulário e definir o ControlSource como "customer.country", o combo box será preenchido com os países na tabela customer sem exibir os nomes dos países mais de uma vez. |
| FrmNoTitle | Um formulário com propriedades definidas para que nenhum título seja exibido. Se você deseja exibir informações em uma janela separada, pode criar um objeto baseado nesta classe e usar métodos gráficos de formulário. O componente "Display line animation on a form" na amostra Solutions também usa um formulário sem título para exibir a animação. |
| Lookup_combo | Um combo box que facilita exibir valores de um campo, por exemplo um nome de empresa, enquanto vincula um ControlSource a outro campo, por exemplo um número de id de empresa. Esta classe tem quatro propriedades personalizadas: order_column : Coluna pela qual ordenar a tabela (opcional). lookup_table : Tabela para preencher o combo box. display_column : Coluna na tabela a exibir. return_column : Coluna cujo valor é gravado no ControlSource. |
| MoverLists | Um container com duas list boxes e quatro command buttons. Um usuário pode mover itens selecionados de uma lista para a outra clicando nos command buttons ou arrastando e soltando. Você precisa garantir que o RowSourceType de cada list box esteja definido como 0 e usar o método AddItem para adicionar itens à list box de origem. MoverLists tem três propriedades personalizadas: CanDropIcon : Cursor a ser exibido sobre um destino válido em uma operação de arrastar e soltar. NoDropIcon : Cursor a ser exibido quando soltar não adicionará os itens selecionados à list box. DragThreshold : Número de pixels antes que a operação de arrastar comece. O componente "Move items between list boxes" na amostra Solutions ilustra o uso desta classe. |
| Print_reports | Um formulário modal que permite que um usuário visualize um relatório, imprima-o ou direcione-o para um arquivo. Você pode definir a propriedade cReport da classe como o nome do relatório ou passar o nome do relatório como parâmetro: o = CREATEOBJECT(print_reports, ; "myreport.frx") |
| QBF | Um container com três command buttons. Adicione esta classe e a classe VCR a um formulário com controles vinculados a dados. Quando o usuário escolhe Enter QBF, os valores nos controles são apagados. Valores que o usuário digita nos controles especificam o filtro a ser definido na tabela quando o usuário escolhe Query . Os controles precisam ter um ControlSource definido e o Parent dos controles precisa ser o formulário, não outro container. O componente "Create a query by example form" na amostra Solutions ilustra o uso desta classe. |
| Resizable | Uma classe personalizada que gerencia o redimensionamento e reposicionamento dos controles em um formulário em tempo de execução, mantendo seus tamanhos e posições relativos. Adicione a classe a um formulário e, no evento Resize do formulário, chame o método AdjustControls: THIS.Resizable2.AdjustControls Resizable tem duas propriedades personalizadas que você precisa definir: RepositionList : Uma cadeia de caracteres contendo todas as classes para as quais objetos são reposicionados. ResizeList : Uma cadeia de caracteres contendo todas as classes para as quais objetos são redimensionados. O componente "Resize and reposition controls at run time" na amostra Solutions ilustra o uso desta classe. |
| RTFcontrols | Uma classe container contendo cboFontName, cboFontSize e command buttons para Bold , Italic e ForeColor . O controle cboFontSize é atualizado no evento InteractiveChange de cboFontName, mas nenhuma funcionalidade adicional é codificada com os command buttons Bold , Italic e ForeColor. O componente "Use the RichText control" na amostra Solutions ilustra o uso desta classe. |
| SoundPlayer | Esta classe pode ser usada para reproduzir um arquivo multimídia não visual, como um arquivo de áudio .WAV. Consulte a seção a seguir, Sample Multimedia Classes, para obter mais informações sobre esta classe. |
| StopWatch | Uma classe container com um timer e labels para exibir valores de cronômetro. StopWatch tem três métodos personalizados que você desejará usar: Start : Inicia o cronômetro Stop : Para o cronômetro Reset : Redefine o tempo exibido para 0:00 O componente "Display a stop watch" na amostra Solutions ilustra o uso desta classe. |
| TbrEditing | tbrEditing tem uma propriedade personalizada e um método que você desejará usar: Propriedade nAppliesTo : Esta propriedade pode ser definida como 1, 2 ou 3. As escolhas do usuário afetam o controle atual no formulário ativo. As escolhas do usuário afetam todas as text boxes e edit boxes no formulário ativo. As escolhas do usuário afetam todos os controles no formulário ativo. Refresh : Aceita uma referência de objeto como parâmetro e define todos os controles de edição para os valores apropriados do objeto. Chame o método Refresh no evento GotFocus de um controle. O componente "Change font attributes" na amostra Solutions ilustra o uso desta classe. |
| VideoFrame | Esta classe pode ser usada para reproduzir um arquivo multimídia visual, como um arquivo video for Windows. Consulte a seção a seguir, Sample Multimedia Classes, para obter mais informações sobre esta classe. |

### Sample Multimedia Classes

Duas das classes (SoundPlayer e VideoFrame) na biblioteca de classes Visual FoxPro Samples\Classes\Samples.vcx permitem que você use o MCI (Multimedia Command Interface) para reproduzir arquivos multimídia.

Para localizar documentação dos comandos MCI, pesquise por "Multimedia Commands" na MSDN Library (http://msdn.microsoft.com/library).

#### Classe Sound Player

Esta classe pode ser usada para reproduzir um arquivo multimídia não visual, como um arquivo de áudio .WAV. Permite especificar o arquivo a ser reproduzido e fornece métodos integrados para reproduzir facilmente o arquivo de mídia.

| Propriedade | Descrição |
| --- | --- |
| AutoOpen | Especifica se o arquivo de som deve ser aberto e exibido automaticamente quando o objeto é instanciado. O valor padrão é True (.T.). |
| AutoPlay | Especifica se o arquivo de som deve ser reproduzido automaticamente quando é aberto. O valor padrão é True (.T.). |
| AutoRepeat | Especifica se o arquivo de som é reproduzido continuamente. O valor padrão é False (.F.). |
| ControlSource | Especifica a coluna que contém a referência do arquivo de som. Se vazio, a classe espera um nome de arquivo estático na propriedade SoundFile. |
| MCIAlias | Especifica o alias a ser usado pelo MCI. Se deixado vazio, o alias assume como padrão a propriedade Name da classe. Normalmente isso pode ser deixado vazio, mas se o usuário deseja reproduzir o mesmo arquivo de som duas vezes ao mesmo tempo, um alias diferente precisaria ser especificado para cada um. |
| SoundFile | Contém o nome de um arquivo de som a reproduzir, por exemplo " C:\WINDOWS\CHIMES.WAV ". |

| Método | Descrição |
| --- | --- |
| OpenSound | Abre o arquivo de som. |
| PlaySound | Reproduz o arquivo de som. O arquivo deve ser aberto com o método OpenSound antes de poder ser reproduzido. |
| PauseSound | Pausa a reprodução de um arquivo de som. A reprodução pode ser continuada chamando o método PlaySound. |
| SetPosition | Permite que o usuário especifique a posição do arquivo de mídia. Pode ser executado a qualquer momento após o arquivo ter sido aberto. Valores válidos são "Start," "End," ou um milissegundo específico no som. |
| CloseSound | Fecha o arquivo de som e libera todos os recursos associados a ele. |

#### Classe VideoFrame

A classe VideoFrame pode ser usada para reproduzir um arquivo multimídia visual, como um arquivo video for Windows. Esta classe permite posicionar e dimensionar o vídeo a ser reproduzido e fornece métodos integrados para reproduzir facilmente o arquivo de mídia.

Para um exemplo de uso desta classe, consulte Video.scx na pasta Visual FoxPro Samples\Solution\Forms.

| Propriedade | Descrição |
| --- | --- |
| AutoOpen | Especifica se o arquivo de vídeo deve ser aberto e exibido automaticamente quando o objeto é instanciado. O valor padrão é True (.T.). |
| AutoPlay | Especifica se o arquivo de vídeo deve ser reproduzido automaticamente quando é aberto. O valor padrão é True (.T.). |
| AutoRepeat | Especifica se o arquivo de vídeo fará loop do vídeo. Definir isso como .T. fará o vídeo ser reproduzido continuamente. O valor padrão é False (.F.). |
| ControlSource | Especifica um Field que contém a referência do arquivo de vídeo. Se vazio, a classe espera um nome de arquivo estático na propriedade VideoFile. |
| MCIalias | Especifica o alias a ser usado pelo MCI. Se deixado vazio, o alias assume como padrão a propriedade Name da classe. Normalmente isso pode ser deixado vazio, mas se o usuário deseja reproduzir o mesmo arquivo de vídeo duas vezes ao mesmo tempo, um alias diferente precisaria ser especificado para cada um. |
| VideoFile | Contém o nome de um arquivo de vídeo a reproduzir, por exemplo: " C:\VFP\SAMPLES\SOLUTION\FORMS\FOX.AVI ". |

| Método | Descrição |
| --- | --- |
| CloseVideo | Fecha o arquivo de vídeo e libera todos os recursos associados a ele. |
| DoMCI | Chamado pelos outros métodos para executar comandos MCI. Também pode ser chamado por um usuário para executar um comando MCI específico. |
| OpenVideo | Abre o arquivo de vídeo e mostra o primeiro quadro. |
| PauseVideo | Pausa um vídeo em reprodução. O vídeo pode ser reiniciado usando o método PlayVideo. |
| PlayVideo | Reproduz o arquivo de vídeo. O arquivo de vídeo deve ser aberto no método OpenVideo antes de poder ser reproduzido. |
| SetPosition | Permite que o usuário especifique a posição do arquivo de mídia. Pode ser executado a qualquer momento após o arquivo de vídeo ter sido aberto. Valores válidos são "Start", "End", ou um milissegundo específico no vídeo. |

# Utility Class Library

Utility.vcx contém as seguintes classes.

| Classe | Descrição |
| --- | --- |
| Arraylib | Uma classe personalizada com métodos para inserir elementos de array, excluir elementos de array e examinar colunas de array. |
| Execsp | Uma classe personalizada com métodos que facilitam SQL pass through e executar stored procedures em um banco de dados remoto. |
| Filelib | Uma classe personalizada com métodos que realizam tarefas comuns de cadeia de caracteres usadas ao manipular nomes de arquivo, por exemplo, remover a extensão, adicionar uma barra invertida a um caminho, e assim por diante. |
| Menulib | Uma classe container com métodos que criam um shortcut menu a partir de um array. O componente "Create dynamic shortcut menus" na amostra Solutions ilustra o uso desta classe. |

# Registry Program

Registry.prg contém as seguintes classes.

| Classe | Descrição |
| --- | --- |
| FileReg | Uma subclasse da classe Registry que fornece métodos para ler a aplicação associada a extensões de arquivo específicas e o caminho para a aplicação. |
| FoxReg | Uma subclasse da classe Registry que fornece métodos para ler e gravar configurações do Visual FoxPro no Windows Registry. |
| ODBCReg | Uma subclasse da classe Registry que fornece métodos para ler informações de fonte de dados e driver ODBC. |
| OldINIReg | Uma subclasse da classe Registry que fornece métodos para ler e gravar em um arquivo .INI. |
| Registry | Uma classe personalizada que fornece métodos para acessar funções da API do Windows para manipular o Windows Registry. |

Para exemplos de uso das classes registry, execute SOLUTION.app na pasta ..\Samples\Solution.
