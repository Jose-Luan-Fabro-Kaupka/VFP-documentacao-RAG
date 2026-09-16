# Como: substituir referências de código

Depois de executar uma pesquisa de referências de código, você pode substituir código ou texto em seus projetos ou pastas. Para obter mais informações, consulte How to: Search For Code References.

### Para substituir uma referência de código em um projeto ou pasta
- Execute uma pesquisa de referências de código para localizar o código ou o texto que deseja substituir. Se a pesquisa for bem-sucedida, a janela Code References exibe os resultados da pesquisa no painel de resultados.
- Na janela Code References, escolha as linhas de código nas quais deseja substituir a referência de código ou o texto, executando uma das seguintes ações: Para selecionar linhas específicas de código, clique na caixa de seleção de cada linha que aparece no painel de resultados. Para selecionar todas as linhas de código, clique com o botão direito no painel de resultados para exibir um menu de atalho e escolha Select All .
- Na janela Code References, clique em Replace na barra de ferramentas para abrir a caixa de diálogo Replace. Cuidado Se você selecionar linhas de código para substituição em que arquivos de dados possam ser afetados ou em que alterações em estruturas de dados, valores de propriedade ou nomes de propriedades e métodos em formulários (.scx) ou bibliotecas de classes visuais (.vcx) possam ocorrer, o Visual FoxPro solicita que você confirme ou recuse a operação de substituição. Se você confirmar a substituição, o Visual FoxPro executa apenas as substituições que não afetam arquivos de dados e fornece código no nó da cadeia de pesquisa sob o nó Replacement Logs para que você execute manualmente as alterações desejadas. Se você recusar a substituição, nenhuma alteração é feita.
- Na caixa Replace with da caixa de diálogo Replace, digite o código ou o texto de substituição.
- Selecione as opções desejadas no grupo Options.
- Clique em Replace para iniciar a substituição. Observação Se você selecionou Confirm replacements no grupo Options, deve confirmar a operação de substituição para cada linha de código selecionada. A janela Code References exibe um registro da operação de substituição como um nó de log abaixo do nó Replacement Logs no painel de pesquisa e os resultados da substituição no painel de resultados.

Para obter mais informações, consulte Code References Window e Replace Dialog Box.

Depois que a ferramenta Code References concluir a substituição do código ou do texto, você deve confirmar se deseja atualizar os resultados na janela Code References.
