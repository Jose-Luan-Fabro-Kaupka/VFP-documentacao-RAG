# Comando SHOW GET

Incluído para compatibilidade com versões anteriores. Use o método Refresh (Visual FoxPro) para exibir novamente um controle após alterar suas propriedades.

Exibe novamente o objeto @ ... GET que representa a variável de memória especificada.

```foxpro
SHOW GET var
	[, expN1 [PROMPT expC]]
	[ENABLE | DISABLE]
	[LEVEL expN2]
	[COLOR SCHEME expN3
	| COLOR color pair list]
```

#### Parâmetros
 var
 var é a variável de memória, o elemento de array ou o campo especificado quando o controle foi criado.

No exemplo a seguir, são criados três botões de opção com os textos Apples, Oranges e Lemons. var é uma variável de memória chamada FRUIT que inicializa os botões; o número do botão escolhido é armazenado em FRUIT.

 CLEAR

 STORE 2 TO fruit

 @ 4,2 GET fruit PICTURE '@*R Apples;Oranges;Lemons'

 READ CYCLE

 expN1
 expN1 é o número do botão a exibir novamente em um conjunto de botões invisíveis, de opção ou de comando. O número é determinado pela ordem de criação dos textos.

O programa a seguir cria os mesmos botões. Quando um botão é escolhido, a rotina NOORANGE VALID é executada e desabilita Oranges com SHOW GET e DISABLE.

 CLEAR

 STORE 2 TO fruit

 @ 4,2 GET fruit PICTURE '@*R Apples;Oranges;Lemons' VALID noorange()

 READ CYCLE

 FUNCTION noorange

 SHOW GET fruit,2 DISABLE && Disables the second button

 _CUROBJ = 1

 RETURN .T.

PROMPT expC

Você pode substituir o texto de um botão individual ou caixa de seleção incluindo PROMPT expC. expC substitui o texto original e também pode alterar atributos do controle por meio dos caracteres especiais apropriados.

SHOW GET normalmente é colocado em uma rotina VALID do controle.

No exemplo a seguir, a rotina Newprompt altera o texto e a tecla de atalho de uma caixa de seleção.

 CLEAR

 STORE 1 TO check

 @ 4,2 GET check FUNCTION '*C \<Checked' SIZE 1,13 VALID NEWPROMPT()

 READ CYCLE

 FUNCTION newprompt

 IF check = 0

 SHOW GET check,1 PROMPT '\<Unchecked'

 ELSE

 SHOW GET check,1 PROMPT '\<Checked'

 ENDIF

 RETURN .T.

No FoxPro para Windows e Macintosh, PROMPT pode especificar arquivos de imagem exibidos em controles gráficos quando habilitados, selecionados ou desabilitados. Podem ser informados até três arquivos separados por vírgulas em expC, um para cada estado.

ENABLE | DISABLE

ENABLE permite selecionar o controle. DISABLE impede a seleção e exibe o controle com as cores de desabilitado.

LEVEL expN2

READs podem ser aninhados em até cinco níveis. Sem LEVEL, SHOW GET usa o nível READ atual. expN2 pode ser de 1 a 5. Use RDLEVEL() para obter o nível atual.

COLOR SCHEME expN3 | COLOR color pair list

Os controles podem ser exibidos novamente com as cores especificadas por um esquema ou lista de pares de cores.

# Observações

Textos de imagem são aceitos no FoxPro para Windows e Macintosh.

SHOW GET exibe novamente um único controle e atualiza seu valor exibido. O controle pode ser habilitado ou desabilitado; também é possível atualizar botões individuais e alterar textos.

SHOW GET normalmente é usado em uma rotina executada por uma cláusula VALID ou WHEN do controle, ou ACTIVATE ou DEACTIVATE do READ.

SHOW GET versus SHOW GETS e SHOW OBJECT

SHOW GET ou SHOW OBJECT atualizam controles individuais. SHOW GETS atualiza todos os controles criados com @ ... GET e executa a rotina READ LEVEL SHOW. SHOW OBJECT referencia controles pelo número do objeto; SHOW GET usa var.
