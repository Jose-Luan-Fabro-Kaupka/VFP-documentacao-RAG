# Objeto DataEnvironment

Criado quando você cria um formulário, conjunto de formulários ou relatório. Um objeto DataEnvironment funciona como um contêiner para os objetos Cursor, CursorAdapter e Relation associados ao formulário, conjunto de formulários ou relatório.

> **Observação:** Você pode definir somente as seguintes propriedades de DataEnvironment em tempo de execução: DataSource, DataSourceType, InitialSelectedAlias, Name, OpenViews e Tag. Para que uma nova configuração de propriedade entre em vigor, chame os métodos CloseTables e OpenTables do objeto DataEnvironment. Definir qualquer outra propriedade de DataEnvironment em tempo de execução gera um erro.

```foxpro
DataEnvironment
```

# Observações

Você pode definir e criar subclasses da classe DataEnvironment. Em um formulário, é possível salvar o ambiente de dados existente como um arquivo de biblioteca de classes visuais (.vcx) selecionando o formulário, escolhendo Salvar como classe no menu Arquivo e selecionando DataEnvironment. Todas as propriedades, métodos e eventos de DataEnvironment ficam disponíveis, conforme apropriado, na janela Propriedades depois que você abre o Designer de Classes. No entanto, só é possível acessar o Designer de Ambiente de Dados pelo Designer de Formulários, e não pelo Designer de Classes.

Em tempo de design, você pode adicionar uma classe DataEnvironment preexistente a um formulário por meio de uma barra de ferramentas de biblioteca de classes ou no código usando o método AddObject. No entanto, o Visual FoxPro considera a classe DataEnvironment adicionada de qualquer uma dessas maneiras como uma classe membro, e não como um ambiente de dados nativo.

Você pode usar as propriedades DEClass e DEClassLibrary de Form para especificar e carregar uma classe DataEnvironment externa em tempo de design ou de execução. O Visual FoxPro oferece suporte às propriedades DEClass e DEClassLibrary para arquivos de formulário (.scx), biblioteca de classes visuais (.vcx) e programa (.prg), mas não para conjuntos de formulários nem no Designer de Relatórios.

Para obter mais informações, consulte as propriedades DEClass e DEClassLibrary. Para obter mais informações sobre o ambiente de dados de formulários e conjuntos de formulários, consulte Criação de formulários.
