# Como: adicionar arquivos a um projeto

Se você deseja incluir arquivos em um aplicativo, deve adicioná-los ao projeto do aplicativo. Você pode adicionar arquivos existentes a um projeto usando o Application Builder ou o Project Manager. Novos arquivos que você cria usando o Project Manager são adicionados automaticamente ao projeto. Quando você compila seu aplicativo, o Visual FoxPro inclui os arquivos dos componentes que fazem parte do seu aplicativo.

> **Observação:** Quando você compila seu aplicativo a partir de um projeto, os arquivos incluídos no projeto são marcados como somente leitura. Se seu aplicativo inclui arquivos que são modificados pelo usuário, você deve excluir esses arquivos do processo de compilação. Para obter mais informações, consulte Excluding Modifiable Files from Builds.

### Para adicionar um arquivo a um projeto
- Abra o projeto do seu aplicativo.
- No Project Manager, expanda o nó na hierarquia do projeto que contém o tipo de componente que deseja adicionar.
- Clique no tipo de componente desejado.
- No menu Project, clique em Add File. Dica Você também pode clicar em Add no Project Manager. A caixa de diálogo Select para esse tipo de componente é aberta.
- Na caixa de diálogo Select, procure e selecione o arquivo que deseja adicionar e clique em OK.

Para obter mais informações, consulte Project Manager Window.

Quando você referencia arquivos em um programa ou formulário, o Visual FoxPro adiciona esses arquivos automaticamente ao seu projeto quando você compila o projeto, não quando você os referencia. Por exemplo, se um programa em seu projeto inclui a seguinte linha de código, o Visual FoxPro adiciona o arquivo Orders.scx ao seu projeto:

```foxpro
DO FORM ORDERS.SCX
```

Quando você compila o projeto, o Visual FoxPro resolve referências a todos os arquivos e inclui automaticamente arquivos implícitos no projeto. Além disso, se os arquivos contêm referências a outros arquivos, compilar o projeto também resolve essas referências e inclui esses arquivos. Os arquivos referenciados aparecem no Project Manager na próxima vez que você visualizar o projeto.

> **Cuidado:** O Visual FoxPro pode não conseguir resolver referências a arquivos de imagem, como arquivos .bmp e .msk, dependendo de como são usados no código. Portanto, adicione imagens aos seus arquivos manualmente. Além disso, o Visual FoxPro não pode incluir automaticamente arquivos que são referenciados usando substituição de macro porque o nome do arquivo não é conhecido até que o aplicativo seja executado. Se seu aplicativo referencia arquivos usando substituição de macro, inclua os arquivos referenciados manualmente.
