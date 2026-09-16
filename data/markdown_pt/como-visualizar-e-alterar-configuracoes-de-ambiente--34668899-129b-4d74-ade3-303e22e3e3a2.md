# Como: visualizar e alterar configurações de ambiente

Para visualizar e alterar configurações de ambiente, use a caixa de diálogo Options. A caixa de diálogo Options contém uma série de guias que representam diferentes categorias de opções de ambiente.

### Para exibir a caixa de diálogo Options
- No menu Tools, clique em Options.

A caixa de diálogo Options aparece e exibe guias nas quais você pode escolher as configurações desejadas. Para detalhes sobre opções que você pode definir usando cada guia, consulte Caixa de diálogo Options (Visual FoxPro).

# Exibindo configurações de ambiente

Quando você executa o Visual FoxPro, pode verificar configurações de ambiente usando a caixa de diálogo Options ou o comando DISPLAY STATUS. Além disso, você pode exibir os valores de comandos SET individuais para verificar configurações.

### Para exibir várias configurações de ambiente
- No menu Tools, clique em Options para exibir a caixa de diálogo Options e visualizar as configurações atuais. – OU –
- Digite DISPLAY STATUS na janela Command.

### Para exibir configurações de ambiente individuais
- Use a função SET( ) na janela Command para exibir o valor atual de qualquer comando SET.

Por exemplo, para visualizar o status atual de SET TALK, digite:

```foxpro
? SET("TALK")
```

> **Observação:** Como as configurações são válidas apenas para a sessão de dados atual, você deve capturar suas configurações e colocá-las em um programa ou no código do evento Init de um formulário para cada sessão de dados privada.

Para obter mais informações, consulte Visão geral do comando SET.

### Para ecoar configurações da caixa de diálogo Options para a janela Debug Output
- No menu Tools, clique em Debugger.
- Clique na janela principal do Visual FoxPro para selecioná-la e no menu Tools, clique em Options.
- Na caixa de diálogo Options, faça escolhas de configuração.
- Mantenha pressionada a tecla SHIFT e clique em OK. As configurações são ecoadas para a janela Debug Output.
- Clique na janela Visual FoxPro Debugger para selecioná-la e copie os comandos de configuração da janela Debug Output.

# Salvando configurações de ambiente

Você pode salvar as configurações feitas na caixa de diálogo Options para a sessão de dados atual ou como configurações padrão (permanentes) para sua cópia do Visual FoxPro.

### Para salvar configurações apenas para a sessão atual
- Na caixa de diálogo Options, selecione suas configurações.
- Clique em OK.

Quando você salva configurações apenas para a sessão atual, elas permanecem em vigor até você sair do Visual FoxPro (ou até alterá-las novamente). Para salvar alterações permanentemente, salve-as como configurações padrão. Essa ação armazena suas configurações no registro do Windows.

### Para salvar configurações atuais como configurações padrão
- Na caixa de diálogo Options, selecione suas configurações.
- Clique em Set As Default. Observação O botão Set as Default é desabilitado até que você faça uma alteração nas configurações atuais.

Você pode substituir configurações padrão emitindo comandos SET ou especificando um arquivo de configuração ao iniciar o Visual FoxPro. Para detalhes, consulte Definindo opções de configuração na inicialização.

# Definindo o ambiente usando o comando SET

Você pode modificar programaticamente a maioria das opções exibidas nas guias da caixa de diálogo Options usando comandos SET ou atribuindo um valor a uma variável de sistema.

> **Observação:** Quando você configura o ambiente usando comandos SET, as configurações entram em vigor apenas para a sessão atual do Visual FoxPro. Quando você sai do programa, o sistema descarta suas configurações. Isso significa que você deve reemitir os comandos SET. No entanto, você pode automatizar esse processo emitindo comandos SET na inicialização ou usando um arquivo de configuração. Para detalhes, consulte Definindo opções de configuração na inicialização.

> **Dica:** Para salvar uma configuração feita com comandos SET, abra a caixa de diálogo Options e salve suas configurações lá.

### Para definir o ambiente programaticamente
- Use os comandos SET que desejar.

Por exemplo, as seguintes linhas de código definem um caminho padrão, adicionam um relógio à barra de status e usam um formato de data ano-mês-dia (yy.mm.dd):

```foxpro
SET DEFAULT TO HOME()+"\VFP"
SET CLOCK ON
SET DATE TO ANSI
```

Para obter mais informações, consulte Visão geral do comando SET.
