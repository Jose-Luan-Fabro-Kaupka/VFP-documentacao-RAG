# Como: testar um projeto

Antes de compilar uma aplicação, você pode testar o projeto para verificar referências e confirmar que todos os componentes estão disponíveis. Testar um projeto recompila o projeto, o que força o Visual FoxPro a resolver referências de arquivo e recompilar arquivos desatualizados.

> **Dica:** Para percorrer o código com mais facilidade, marque locais no código usando bookmarks, atalhos e breakpoints. Para obter detalhes, consulte Como: criar bookmarks e atalhos da lista de tarefas.

Você pode testar projetos usando o Project Manager ou o comando BUILD PROJECT. No entanto, mais opções estão disponíveis quando você usa o Project Manager. Para obter mais informações, consulte Comando BUILD PROJECT.

### Para testar um projeto
- Abra o projeto da sua aplicação.
- No Project Manager, clique em Build.
- Na caixa de diálogo Build Options, selecione Rebuild project.
- Selecione quaisquer outras opções desejadas e clique em OK. Dica Você pode visualizar e salvar mensagens de compilação que ocorrem durante o processo de compilação. Para obter mais informações, consulte Como: visualizar e salvar mensagens de compilação.

Para obter mais informações, consulte Janela Project Manager e Caixa de diálogo Build Options.

> **Dica:** Depois que o projeto compila com sucesso, execute o projeto antes de compilar o arquivo de aplicação. À medida que você adiciona componentes ao seu projeto, é recomendável testar e executar seu projeto após adicionar cada componente.

### Para executar o projeto
- No Project Manager, selecione o programa principal e clique em Run.

Você também pode executar projetos usando o comando DO com o nome do programa principal. Por exemplo, digitar a seguinte linha de código na janela Command executa um projeto contendo o programa Main.prg:

```foxpro
DO Main.prg
```

Se o programa executa corretamente, você pode compilar um arquivo de aplicação que contém todos os arquivos no projeto. Para obter mais informações, consulte Compilar uma aplicação.
