# Conclusão de sintaxe IntelliSense

Ao digitar código, o IntelliSense do Visual FoxPro pode ajudá-lo a completar a sintaxe de programação do Visual FoxPro usando a seguinte funcionalidade:
 - Quick Info
- List Members
- List Values

# Quick Info

A funcionalidade Quick Info exibe informações adicionais de sintaxe para elementos de linguagem do Visual FoxPro, como funções e métodos. Por exemplo, quando você digita uma função SYS( ) na janela Command, o Quick Info exibe uma caixa de listagem contendo elementos de sintaxe disponíveis que você pode escolher. Ao inserir valores de argumento para métodos, o Quick Info exibe a sintaxe em uma janela Tip e o próximo argumento em negrito. Para outros elementos de linguagem do Visual FoxPro, como comandos, as informações de sintaxe são exibidas em uma janela Tip.

O Quick Info está disponível em qualquer local onde você pode digitar código Visual FoxPro, como a janela Command, editores e janelas de código.

# List Members

A funcionalidade List Members exibe uma caixa de listagem de membros disponíveis para certos elementos de linguagem do Visual FoxPro, como as variáveis de sistema _VFP e _SCREEN, e em locais mais limitados, membros disponíveis como propriedades, métodos, eventos e objetos para objetos instanciados. O List Members também está disponível para objetos visuais, controles ActiveX, servidores COM, classes nativas do Visual FoxPro e membros definidos pelo usuário quando são fortemente tipados. Para obter mais informações, consulte Como: implementar tipagem forte para código de classe, objeto e variável.

Para objetos criados em tempo de execução por funções como CREATEOBJECT( ), CREATEOBJECTEX( ), NEWOBJECT( ) e GETOBJECT( ), o IntelliSense preenche a caixa de listagem List Members com informações de definições de classe ou bibliotecas de tipos que o Visual FoxPro pesquisa nos seguintes locais:
 - Classes base de objetos do Visual FoxPro.
- Definições de classe na memória na ordem em que foram carregadas.
- Definições de classe no programa atual.
- Definição de classe em um arquivo de biblioteca de classes visual (.vcx) aberto pelo comando SET CLASS.
- Definições de classe nos arquivos de procedimento abertos pelo comando SET PROCEDURE.
- Definições de classe na cadeia de execução de programa do Visual FoxPro. Para obter mais informações, consulte Comando DO .
- Banco de dados de registro do sistema (registro).
- Atalhos de teclado para Quick Info e List Members.

# List Values

Ao atribuir valores a propriedades programaticamente para objetos, a funcionalidade List Values exibe editores de valor, como seletores de fonte ou cor, ou uma caixa de listagem de valores disponíveis. O List Values está disponível para propriedades que possuem um conjunto definido de valores, e a biblioteca de tipos do objeto referenciado determina o conteúdo da caixa de listagem List Values. Para propriedades em bibliotecas de tipos, o List Values suporta enumerações.
