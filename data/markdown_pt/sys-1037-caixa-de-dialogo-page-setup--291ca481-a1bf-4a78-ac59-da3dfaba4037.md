# SYS(1037) - Caixa de diálogo Page Setup

Exibe a caixa de diálogo Page Setup padrão do Visual FoxPro ou de relatório, ou define as configurações da impressora para a impressora padrão no Visual FoxPro ou para o ambiente da impressora do relatório.

```foxpro
SYS(1037 [, nValue])
```

#### Parâmetros
 **nValue**
Especifica um valor que determina a funcionalidade de SYS(1037) . A tabela a seguir lista os valores possíveis de nValue . nValue Descrição 0 ou omitido Abre a caixa de diálogo Page Setup padrão. 1 Abre a caixa de diálogo Page Setup do relatório. 2 Define as configurações do ambiente da impressora de um relatório para as configurações da impressora padrão. 3 Define as configurações da impressora padrão para as configurações do ambiente da impressora de um relatório.

> **Observação:** Quando nValue é definido como 1, 2 ou 3, a tabela ou cursor do relatório deve ser aberto de forma exclusiva.

# Valor de retorno

Character. SYS(1037) retorna "1" se o Visual FoxPro realizar qualquer ação que afete aspectos do ambiente da impressora ou das configurações da impressora; caso contrário, retorna "0".

> **Observação:** Em alguns casos, se o usuário pressionou OK na caixa de diálogo sem fazer nenhuma seleção explícita, pode não ser óbvio quais alterações ocorreram. No entanto, o Visual FoxPro examinou quaisquer aspectos do ambiente da impressora padrão ou das configurações da impressora em um arquivo de relatório e atualizou tudo nessas configurações que não corresponde à lista completa de atributos disponíveis nas informações fornecidas pela caixa de diálogo Page Setup. Como essa ação ocorre, a função retorna "1."

# Observações

SYS(1037) exibe a caixa de diálogo Page Setup para que você possa alterar configurações da impressora, como tamanho e orientação do papel. As configurações disponíveis na caixa de diálogo Page Setup dependem da impressora instalada. SYS(1037) também define as configurações do ambiente da impressora do relatório para as configurações da impressora padrão ou as configurações da impressora padrão para as configurações do ambiente da impressora do relatório. Para obter mais informações, consulte Caixa de diálogo Page Setup (Visual FoxPro).

### SYS(1037,<N>) e relatórios

SYS(1037,1), SYS(1037,2) e SYS(1037,3) são úteis principalmente para desenvolvedores que trabalham com recursos de extensão do Report System do Visual FoxPro 9.0. Para obter mais informações sobre esses recursos, consulte Extending Report Functionality in Visual FoxPro.

Todas as três variantes de SYS(1037,<N>) relacionadas a relatórios exigem acesso a um cursor ou tabela aberta com o mesmo formato de um arquivo de definição de relatório (.frx) ou etiqueta (.lbx). O relatório deve ser selecionado como cursor ou aberto como tabela antes de chamar a função, e o Visual FoxPro exige que a tabela do relatório seja aberta de forma exclusiva. Caso contrário, ocorre um erro ao chamar a função. Para obter mais informações sobre a estrutura de tabelas de relatório e etiqueta, consulte Table Structures of Table Files (.dbc, .frx, .lbx, .mnx, .pjx, .scx, .vcx).

SYS(1037,1) fornece uma forma para desenvolvedores que implementam extensões do Report Builder invocar a caixa de diálogo nativa de configuração de página e persistir as escolhas do usuário diretamente em uma tabela de relatório ou etiqueta. Para obter mais informações, consulte Extending Reports at Design Time.

#### Salvando o ambiente da impressora atual

SYS(1037,2) serve como uma forma de salvar as configurações atuais da impressora em um cursor temporariamente para que você possa restaurar o ambiente da impressora posteriormente. Como tal, essa função sempre armazena detalhes completos no cursor fornecido. Se esse cursor for um relatório real e não tiver um ambiente de impressora salvo antes de usar SYS(1037,2), ele terá um ambiente de impressora completo salvo depois. Se você não quiser que os detalhes do ambiente da impressora permaneçam nesse cursor, é sua responsabilidade limpar os campos relevantes posteriormente. Para evitar a necessidade de realizar essa tarefa de limpeza, simplesmente forneça um cursor temporário no formato correto com um registro, em vez de usar um relatório ou etiqueta real com SYS(1037,2). Para obter mais informações, consulte How to: Save the Printer Environment for Reports.

SYS(1037,2) preserva qualquer informação já presente nas configurações do ambiente da impressora do relatório. Ele adiciona configurações que não estão atualmente no ambiente da impressora do relatório e não substitui configurações existentes.

Por exemplo, se uma definição de relatório incluir `ORIENTATION=1` e `COPIES=3`, para especificar um relatório em paisagem e três cópias impressas, o ambiente da impressora padrão não substituirá essa configuração por uma orientação retrato. No entanto, se você remover a linha que especifica `COPIES=3` da definição do relatório antes de chamar a função, a definição do relatório incluirá uma linha `COPIES=<N>` após chamar a função. Essa linha corresponderá ao padrão atual do Visual FoxPro.

Como esse comportamento é aditivo, se você quiser salvar o ambiente completo da impressora padrão do Visual FoxPro, deve usar um cursor vazio com essa função ou garantir que os campos relevantes estejam completamente vazios antes de chamar SYS(1037,2).

#### Restaurando o ambiente da impressora atual

SYS(1037,3) restaura as configurações da impressora de uma definição de relatório para o padrão atual do Visual FoxPro. Embora possa parecer contra-intuitivo, usar essa variante da função exige informações completas do ambiente da impressora no relatório ou etiqueta e, portanto, pode gravar dados no cursor, além de alterar o ambiente da impressora padrão. Se seu relatório ou etiqueta não tinha informações completas antes de usar a função, terá informações completas depois de usá-la.

#### Respeitando a substituição de configurações da impressora pelo usuário

Em versões anteriores do Visual FoxPro, salvar configurações da impressora em relatórios usava três campos no primeiro registro da tabela: os campos EXPR, TAG e TAG2. No Visual FoxPro 9.0, se você optar por não salvar Printer Environment com um relatório, muito menos informação é armazenada nesses campos, permitindo que seu relatório funcione de forma mais adequada com uma variedade maior de impressoras.

No Visual FoxPro 9.0, ao projetar relatórios, você também pode substituir quaisquer configurações armazenadas nesses campos usando um quarto campo, PICTURE, no primeiro registro. Suas configurações armazenadas em PICTURE substituem quaisquer configurações para os mesmos atributos da impressora nos campos EXPR e TAG. Observe que essas configurações diferenciam maiúsculas de minúsculas.

SYS(1037) está ciente das configurações do usuário em PICTURE e as leva em conta ao restaurar o ambiente da impressora de um arquivo de relatório ou etiqueta.

Ao executar relatórios ou etiquetas, os usuários podem ter outro nível de substituição das configurações da impressora armazenadas: a cláusula PROMPT nos comandos REPORT FORM e LABEL. Se você usar essa palavra-chave, ou se fornecer instruções equivalentes com o membro CommandClauses.Prompt de um objeto ReportListener, quaisquer configurações fornecidas pelo usuário em tempo de execução têm precedência sobre as configurações armazenadas no relatório, bem como sobre as configurações padrão do ambiente da impressora do Visual FoxPro. Para obter mais informações, consulte Comando REPORT FORM, Comando LABEL e Propriedade CommandClauses.
