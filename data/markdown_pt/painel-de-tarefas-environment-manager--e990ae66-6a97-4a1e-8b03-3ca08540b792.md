# Painel de tarefas Environment Manager

O Environment Manager é uma ferramenta que você pode usar para gerenciar e organizar configurações de ambiente para necessidades de desenvolvimento reutilizáveis, como em um cliente ou projeto específico. Por exemplo, você pode ter vários projetos para um cliente específico que usam o mesmo modelo de formulário (por exemplo, um com o logotipo do cliente) e configurações de ambiente (por exemplo, caminhos de dados). O Environment Manager permite criar conjuntos de ambiente, que são pacotes de configurações que você pode aplicar a qualquer momento. Essas configurações incluem SET Command Overview, How to: Set Form Templates e How to: Create Controls by Dragging and Dropping Fields or Tables.

Para acessar o Painel de tarefas Environment Manager, selecione Task Pane no menu Tools para abrir o Task Pane Manager. Escolha o Environment Manager Task Pane na caixa de listagem suspensa Task Panes na parte superior.

O Environment Manager Task Pane em si é simplesmente um shell com um link que abre a ferramenta Environment Manager real. Para abrir a ferramenta, basta clicar no link Manage Environment. Este Painel de tarefas também lista os Environment Sets disponíveis e seus projetos associados. Quando você seleciona um projeto, o Environment Set será aplicado antes que o projeto seja aberto.

A ferramenta Environment Manager também é uma aplicação independente e pode ser executada fora do Task Pane Manager. Para executar o Environment Manager como uma aplicação separada, execute o seguinte comando na janela Command.

```foxpro
DO HOME() + ENVMGR.APP
```

> **Observação:** O Environment Manager armazena seus Environment Sets em uma tabela chamada Envmgr.dbf, que é armazenada no seu diretório de dados do usuário (consulte HOME(7) ).

# Trabalhando com Environment Sets

Você pode gerenciar e aplicar seus Environment Sets da seguinte forma:
 **Environment Set List**
Lista todos os Environment Sets disponíveis para uso. Quando você inicia o Environment Manager, suas configurações atuais são exibidas em um conjunto reservado chamado <current> . Isso é usado quando você clica em New para criar um novo conjunto. O conjunto <default field mapping> é outro conjunto reservado usado para armazenar suas configurações originais de Field Mapping armazenadas na caixa de diálogo Options. Se você aplicou um Environment Set com mapeamentos personalizados, pode restaurar seus padrões posteriormente selecionando este conjunto reservado e clicando no botão Set.
**New**
Cria um novo Environment Set. Depois que seu novo conjunto aparecer na lista, você deve renomeá-lo.
**Copy**
Cria um novo Environment Set baseado no selecionado na Environment Set List.
**Remove**
Exclui o Environment Set selecionado.
**Set**
Aplica as configurações definidas no seu Environment Set ao ambiente atual do Visual FoxPro.
**Name**
Permite especificar um nome amigável para o seu Environment Set.

# Default Directory/Path

A página Default Directory/Path permite especificar configurações para o seu Environment Set relacionadas a locais de arquivos.
 **Default Directory**
Especifica o diretório padrão a usar quando o Environment Set é aplicado. Isso é equivalente a usar o CD | CHDIR Command .
**Path**
Especifica uma lista de caminhos de pesquisa a usar quando o Environment Set é definido. Isso é equivalente a usar o SET PATH Command .
**Directory**
Permite alterar o caminho selecionado na lista Path.
**Add Path**
Adiciona um novo caminho à lista Path.
**Copy**
Adiciona um novo caminho à lista Path baseado no selecionado.
**Remove**
Remove o caminho selecionado da lista Path.

# Environment Settings

A página Default Directory/Path permite especificar configurações para o seu Environment Set relacionadas a locais de arquivos.
 **Setting table**
Permite especificar valores para comandos SET comuns que você deseja aplicar quando o Environment Set é definido. Dica Você pode adicionar itens adicionais que aparecem nesta tabela editando Envmgr.dbf, que é armazenado no seu diretório de dados do usuário (consulte HOME(7) ).
**Resource file**
Especifica o arquivo de recursos a usar quando o Environment Set é definido. Isso é equivalente a usar o SET RESOURCE Command .
**Run script before environment is set**
Um script de comandos do Visual FoxPro que é executado antes das configurações no Environment Set serem aplicadas.
**Run script after environment is set and project is loaded**
Um script de comandos do Visual FoxPro que é executado depois que o Environment Set é aplicado.

# Field Mapping

A página Field Mapping permite especificar configurações para o seu Environment Set relacionadas a classes de controle usadas para mapear campos quando você arrasta e solta um campo do Data Environment ou Database Designer em um formulário ou container. Para obter mais informações, consulte Field Mapping Tab, Options Dialog Box e How to: Create Controls by Dragging and Dropping Fields or Tables. Você pode restaurar suas configurações originais de Field Mapping selecionando <default field mapping> e clicando no botão Set.

# Forms

A página Forms permite especificar configurações para o seu Environment Set relacionadas a modelos de formulário e formset usados ao criar um novo formulário ou formset. Para obter mais informações, consulte Forms Tab, Options Dialog Box.

# Associated Projects

A página Associated Projects permite especificar projetos nos quais o Environment Set é aplicado quando o projeto é aberto no Environment Manager Task Pane. O Painel de tarefas lista todos os seus Environment Sets personalizados junto com seus projetos associados.
 **Projects table**
Lista projetos associados ao Environment Set selecionado.
**Add**
Adiciona um projeto ao conjunto.
**Remove**
Remove um projeto do conjunto.
