# Como: usar sessões de dados

Para garantir que cada usuário em um ambiente compartilhado tenha uma cópia exata e segura do ambiente de trabalho, e para garantir que várias instâncias de um formulário possam operar de forma independente, o Visual FoxPro fornece sessões de dados.

Uma sessão de dados é uma representação do ambiente de trabalho dinâmico atual. Você pode pensar em uma sessão de dados como um mini ambiente de dados em execução dentro de uma sessão aberta do Visual FoxPro em uma máquina. Cada sessão de dados contém:
 - Uma cópia dos itens no ambiente de dados do formulário.
- Cursors que representam as tabelas abertas, seus índices e relacionamentos.

O conceito de sessão de dados é facilmente compreendido quando você considera o que acontece ao abrir o mesmo formulário simultaneamente de estações de trabalho separadas em um aplicativo multiusuário. Nesse caso, cada estação de trabalho está executando uma sessão separada do Visual FoxPro e, portanto, possui seu próprio conjunto de áreas de trabalho: cursors que representam tabelas base abertas, índices e relacionamentos. Para obter mais informações sobre acesso simultâneo a dados, consulte Updating Data Using Multiple Form Instances and Locking Data.

No entanto, se você abrir várias instâncias do mesmo formulário em um único projeto, em uma máquina, dentro da mesma sessão do Visual FoxPro, os formulários compartilham a sessão de dados Default, representando um único ambiente de trabalho dinâmico. Cada instância do formulário aberto na mesma sessão do Visual FoxPro usa o mesmo conjunto de áreas de trabalho, e ações em uma instância de um formulário que movem o ponteiro de registro em uma área de trabalho afetam automaticamente outras instâncias do mesmo formulário.

# Usando sessões de dados privadas

Se você deseja ter mais controle sobre várias instâncias de um formulário, pode implementar sessões de dados privadas. Quando seu formulário usa sessões de dados privadas, o Visual FoxPro cria uma nova sessão de dados para cada instância do controle Form, FormSet ou Toolbar que seu aplicativo cria. Cada sessão de dados privada contém:
 - Uma cópia separada de cada tabela, índice e relacionamento no ambiente de dados do formulário.
- Um número ilimitado de áreas de trabalho.
- Ponteiros de registro para cada cópia de cada tabela que são independentes das tabelas base do formulário.

O número de sessões de dados disponíveis é limitado apenas pela memória do sistema e pelo espaço em disco disponíveis.

Você implementa sessões de dados privadas definindo a propriedade DataSession do formulário. A propriedade DataSession tem duas configurações:
 - 1 – Sessão de dados padrão (a configuração padrão).
- 2 – Sessão de dados privada.

Por padrão, a propriedade DataSession de um formulário é definida como 1.

### Para habilitar sessões de dados privadas
- No Form Designer, defina a propriedade DataSession do formulário como 2 – Private data session. -OU-
- No código, defina a propriedade DataSession como 2. Por exemplo, digite: frmFormName.DataSession = 2 Observação Você só pode definir a propriedade DataSession em tempo de design. A propriedade DataSession é somente leitura em tempo de execução.

Quando um formulário usa sessões de dados privadas, cada instância de um formulário aberto em uma única máquina em uma única sessão do Visual FoxPro usa seu próprio ambiente de dados.

> **Observação:** O comando OPEN DATABASE não tem escopo em uma sessão de dados. Diferentemente de uma tabela, um banco de dados, uma vez aberto, está disponível para todas as sessões de dados.
 Sessões de dados múltiplas equivalentes

# Identificando sessões de dados

Cada sessão de dados privada é identificada separadamente. Você pode ver o conteúdo de cada sessão de dados na Data Session Window. Você também pode alterar a descrição da sessão de dados por meio de comandos no código do evento Load.

### Para visualizar o número de identificação de cada sessão de dados
- Use a propriedade DataSessionID em tempo de execução. O exemplo a seguir exibe a propriedade DataSessionID de um formulário chamado frmMyForm: DO FORM frmMyForm ? frmMyForm.DataSessionID

Se você ativar o formulário usando a cláusula NAME, pode usar o nome do formulário para acessar a propriedade DataSessionID, como no código a seguir:

```foxpro
DO FORM MyForm NAME one
? one.DataSessionID
```

A propriedade DataSessionID foi projetada apenas para identificar uma sessão de dados específica. Evite alterar o DataSessionID de uma instância de formulário porque os controles vinculados a dados perdem suas fontes de dados quando você altera o DataSessionID.

# Substituindo a atribuição automática de sessão de dados privada

Quando sessões de dados privadas para um formulário estão em uso, as alterações que você faz nos dados em um formulário não são automaticamente representadas em outras instâncias do mesmo formulário. Se você deseja que todas as instâncias de um formulário acessem os mesmos dados e reflitam imediatamente alterações em dados comuns, pode substituir a atribuição automática de sessão de dados.

### Para substituir a atribuição automática de sessão de dados
- Defina o comando SET DATASESSION como 1 ou sem valor.

Por exemplo, o código a seguir permite que a Command window e o Project Manager controlem a sessão de dados padrão:

```foxpro
SET DATASESSION TO 1
```

-OU-

```foxpro
SET DATASESSION TO
```
