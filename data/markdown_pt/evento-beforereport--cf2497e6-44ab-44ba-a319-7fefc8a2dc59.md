# Evento BeforeReport

Ocorre imediatamente antes que o Report Engine comece a processar um formulário de relatório.

```foxpro
PROCEDURE Object.BeforeReport
```

#### Parâmetros

Nenhum.

# Observações

Aplica-se a: objeto ReportListener.

Quando o Visual FoxPro dispara o evento BeforeReport para uma execução de relatório, ele fez todo o trabalho interno de configuração necessário para renderizar o relatório. Ele leu o conteúdo do arquivo de definição de relatório (frx) e abriu uma cópia somente leitura desse arquivo em uma sessão de dados privada para uso pela sua classe derivada. Para mais informações, consulte a propriedade FRXDataSession.

Antes de disparar o evento BeforeReport, o Report Engine também criou uma sessão de dados privada para os dados do relatório, se o relatório especificar uma. Ele abriu as tabelas e executou outras tarefas de inicialização conforme especificado pelo DataEnvironment do relatório. Para mais informações, consulte a propriedade CurrentDataSession. Você pode investigar a definição de layout do relatório e os dados do relatório, conforme necessário, alternando entre essas duas sessões de dados.

Neste ponto, o Engine também verificou o escopo do relatório, fornecendo o número de registros a serem processados nesta execução de relatório. Essa informação está disponível para seu código no membro CommandClauses.RecordTotal. Em BeforeReport, todos os outros valores de membro de CommandClauses também estão totalmente disponíveis. Para mais informações, consulte a propriedade CommandClauses.

Depois que o evento BeforeReport() retorna, o Report Engine pode iniciar a execução do relatório. Ele começa avaliando as expressões no relatório, para avaliar se este relatório requer uma passagem de pré-processamento ou cálculo. Ele atribui propriedades adicionais do Listener neste momento, indicando o resultado dessa avaliação. Para mais informações, consulte a propriedade TwoPassProcess e a propriedade CurrentPass. O próximo evento disparado é o primeiro evento BeforeBand do relatório.

> **Observação:** Para mais informações sobre a ordem dos eventos em uma execução de relatório, consulte Entendendo relatórios assistidos por objetos do Visual FoxPro .
