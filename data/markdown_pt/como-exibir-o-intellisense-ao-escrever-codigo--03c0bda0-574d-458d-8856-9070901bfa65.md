# Como: exibir o IntelliSense ao escrever código

Você pode exibir os recursos do IntelliSense ao digitar código nos editores, janelas de código e janela Command do Visual FoxPro ou ao depurar código na janela Watch do Visual FoxPro Debugger.

Quando List Members ou Quick Info do IntelliSense está definido como Automatic, os recursos do IntelliSense são exibidos ao pressionar uma tecla de ativação. Essa tecla varia conforme o contexto do código. Quando List Members ou Quick Info está definido como Manual, você pode exibir os recursos pressionando o atalho de teclado apropriado na posição adequada do cursor. Para obter mais informações, consulte Teclas de ativação, navegação e encerramento do IntelliSense e Atalhos de teclado (Visual FoxPro).

As seções a seguir descrevem como exibir os recursos do IntelliSense ao digitar código:
 - Exibindo Quick Info e membros e valores disponíveis
- Exibindo arquivos usados mais recentemente (MRU)
- Exibindo tabelas, campos e variáveis disponíveis

# Exibindo Quick Info e membros e valores disponíveis

Você pode exibir Quick Info (informações de sintaxe) ou os membros e valores disponíveis ao digitar código. Para obter mais informações, consulte Preenchimento de sintaxe do IntelliSense.

### Para exibir Quick Info para comandos
- Digite a primeira palavra do comando e pressione a BARRA DE ESPAÇOS. O IntelliSense executa uma das seguintes ações para que você continue digitando: insere a sintaxe parcial; exibe uma lista de membros válidos para seleção; exibe uma janela Tip com a sintaxe restante. Dica: para percorrer a lista e ver Quick Info de cada membro, pressione SETA PARA BAIXO ou SETA PARA CIMA. O IntelliSense exibe uma janela Tip com informações disponíveis sobre cada membro.
- Continue digitando. -OU- Selecione um membro clicando duas vezes nele. Você também pode clicar no membro e pressionar a BARRA DE ESPAÇOS. O membro aparece na posição atual do cursor.

Por exemplo, suponha que você digite a seguinte linha de código seguida de um espaço (" ") na janela Command:

```foxpro
ALTER
```

O IntelliSense preenche parcialmente o comando SQL ALTER TABLE e exibe as informações de sintaxe restantes em uma janela Tip.

### Para exibir Quick Info para funções e métodos de objetos
- Digite o nome da função ou método do objeto seguido imediatamente por um parêntese de abertura ((). O IntelliSense executa uma das seguintes ações: exibe uma janela Tip com a sintaxe restante; ao inserir valores de argumentos, mostra em negrito a sintaxe do próximo argumento; exibe uma lista de valores válidos. Dica: para percorrer a lista e ver Quick Info de cada valor, pressione SETA PARA BAIXO ou SETA PARA CIMA.
- Continue digitando. -OU- Selecione um valor válido clicando duas vezes nele ou clicando nele e pressionando a BARRA DE ESPAÇOS.

Por exemplo, suponha que você digite a seguinte linha de código seguida imediatamente por um parêntese de abertura na janela Command:

```foxpro
SYS(
```

O IntelliSense exibe uma lista de valores válidos para seleção.

Para obter mais informações, consulte Preenchimento de sintaxe do IntelliSense.

### Para exibir membros disponíveis de variáveis de sistema ou objetos
- Digite o nome de uma variável de sistema válida ou de um objeto instanciado seguido imediatamente por um ponto (.). O IntelliSense exibe uma lista de membros disponíveis. Dica: para percorrer a lista e ver Quick Info de cada membro, pressione SETA PARA BAIXO ou SETA PARA CIMA.
- Para selecionar um membro válido, clique duas vezes nele. Você também pode clicar no membro e pressionar a BARRA DE ESPAÇOS.

Por exemplo, suponha que você queira definir programaticamente a propriedade Visible de um formulário digitando o seguinte na janela Command:

```foxpro
oMyForm = CREATEOBJECT("Form")
oMyForm.
```

Quando você digita o ponto (.) após `oMyForm`, o IntelliSense exibe uma lista com os membros do objeto oMyForm. Você pode então escolher a propriedade Visible.

A lista de membros permanece visível até que você:
 - Insira todos os parâmetros obrigatórios seguidos por um espaço (" ").
- Digite uma tecla de encerramento, como ESC, END ou HOME, ou uma tecla de caractere inválida.
- Altere a janela ativa.

Para obter mais informações, consulte Preenchimento de sintaxe do IntelliSense.

### Para exibir valores disponíveis para propriedades
- Digite o nome da propriedade seguido imediatamente por um sinal de igual (=). -OU- Selecione a propriedade em uma lista de membros, pressione a BARRA DE ESPAÇOS e digite um sinal de igual. O IntelliSense exibe uma lista de valores disponíveis.
- Selecione um valor clicando duas vezes nele. Você também pode clicar no valor e pressionar a BARRA DE ESPAÇOS. O valor aparece na posição atual do cursor.

Por exemplo, suponha que você defina programaticamente a propriedade Visible de um formulário digitando o seguinte na janela Command:

```foxpro
oMyForm = CREATEOBJECT("Form")
oMyForm.Visible=
```

Quando você digita o sinal de igual (=) para atribuir verdadeiro (.T.) ou falso (.F.) à propriedade Visible, o IntelliSense exibe uma caixa de listagem com os valores apropriados.

Para obter mais informações, consulte Preenchimento de sintaxe do IntelliSense.

# Exibindo arquivos usados mais recentemente (MRU)

Você pode exibir e selecionar arquivos usados mais recentemente nos locais apropriados ao digitar código. Para obter mais informações, consulte Arquivos MRU (usados mais recentemente) automáticos do IntelliSense.

### Para exibir arquivos disponíveis e usados mais recentemente (MRU)
- Digite o comando apropriado seguido imediatamente por um espaço (" "). O IntelliSense exibe uma lista de arquivos disponíveis.
- Selecione um arquivo clicando duas vezes nele. Você também pode clicar no arquivo e pressionar a BARRA DE ESPAÇOS. O caminho, se apropriado, e o nome do arquivo aparecem na posição atual do cursor.

# Exibindo tabelas, campos e variáveis disponíveis

Você pode exibir e selecionar tabelas, campos e variáveis disponíveis nos locais apropriados ao digitar código. Para obter mais informações, consulte Nomes automáticos de tabelas, campos e variáveis do IntelliSense.

### Para exibir tabelas e campos disponíveis
- Abra uma tabela no Visual FoxPro.
- Digite o comando apropriado seguido imediatamente por um espaço (" "). Dependendo do comando, o IntelliSense exibe uma lista de tabelas ou campos disponíveis.
- Selecione uma tabela ou campo clicando duas vezes. Você também pode clicar no item e pressionar a BARRA DE ESPAÇOS. O nome aparece na posição atual do cursor.

### Para exibir variáveis disponíveis
- Na janela Command, digite a letra "m" seguida imediatamente por um ponto ( . ). O IntelliSense exibe uma lista de todas as variáveis declaradas e disponíveis.

Por exemplo, suponha que você declare duas variáveis digitando o seguinte código na janela Command:

```foxpro
oMyForm=CREATEOBJECT("Form")
oMyForm2=CREATEOBJECT("Form")
m.
```

Quando você digita o ponto após a letra "m", o IntelliSense exibe uma lista de todas as variáveis declaradas e disponíveis.
