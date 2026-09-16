# Como: usar o Debugger

Você pode usar o depurador do Visual FoxPro para rastrear o código durante a execução.

# Iniciando uma sessão de depuração

Você inicia uma sessão de depuração abrindo o ambiente de depuração.

### Para abrir o depurador
- No menu Tools, escolha Debugger . Observação Se você estiver depurando no ambiente Visual FoxPro, escolha a ferramenta de depuração que deseja abrir no menu Tools.

Você também pode abrir o depurador com qualquer um dos seguintes comandos:
 - DEBUG
- SET STEP ON
- SET ECHO ON

O depurador abre automaticamente sempre que uma condição de breakpoint é atendida.

# Rastreando o código

Uma das estratégias de depuração mais úteis à sua disposição é a capacidade de rastrear o código, ver cada linha de código conforme ela é executada e verificar os valores de todas as variáveis, propriedades e configurações de ambiente.

### Para rastrear o código
- Inicie uma sessão de depuração.
- Se nenhum programa estiver aberto na janela Trace, escolha Do no menu Debug.
- Escolha Step Into no menu Debug ou clique no botão Step Into na barra de ferramentas.

Uma seta na área cinza à esquerda do código indica a próxima linha a ser executada.

> **Dica:** As seguintes dicas se aplicam:
 - Defina breakpoints para restringir o intervalo de código que você precisa percorrer passo a passo.
- Você pode pular uma linha de código que sabe que gerará um erro posicionando o cursor na linha de código após a linha problemática e escolhendo Set Next Statement no menu Debug.
- Se você tem muito código associado a eventos Timer, pode evitar rastrear esse código desmarcando Display Timer Event na guia Debugging da caixa de diálogo Options.

Se você isolar um problema ao depurar um programa ou código de objeto, pode corrigir imediatamente.

### Para corrigir problemas encontrados ao rastrear o código
- No menu Debug, escolha Fix .

Quando você escolhe Fix no menu Debug, a execução do programa é cancelada e o editor de código é aberto na localização do cursor na janela Trace.
