# Comando SHOW OBJECT

Incluído para compatibilidade com versões anteriores. Use o Método Refresh (Visual FoxPro) para redesenhar um controle depois de alterar as propriedades do controle.

Redesenha o controle @ ... GET que tem o número de objeto especificado.

```foxpro
SHOW OBJECT expN1
	[ENABLE | DISABLE]
	[LEVEL expN2]
	[PROMPT expC]
	[COLOR SCHEME expN3
	| COLOR color pair list]
```

#### Parâmetros
 expN1

 Todo controle tem um número de controle associado (expN1), que é determinado pela ordem em que esse controle foi criado. Cada botão dentro de um conjunto de botões push, radio e invisíveis é considerado um controle separado. Um campo, caixa de seleção, popup, lista, spinner ou região de edição de texto também é um único controle.

ENABLE | DISABLE

 Incluir ENABLE permite que o controle especificado seja selecionado ou escolhido. Incluir DISABLE impede que o controle seja selecionado ou escolhido.

LEVEL expN2

 Você pode aninhar READs emitindo @ ... GETS e um READ em uma rotina que é chamada por um READ ativo. READs podem ser aninhados até cinco níveis.

 SHOW OBJECT usa o nível READ atual por padrão se LEVEL for omitido. Incluir LEVEL permite que você redesenhe um controle em um nível diferente do nível atual. A expressão numérica expN2 pode assumir o valor 1, 2, 3, 4 ou 5, correspondendo ao nível READ do controle a redesenhar. RDLEVEL() retorna o nível READ atual.

PROMPT expC

 Você pode substituir o prompt de um botão push, radio ou caixa de seleção individual por outro prompt incluindo PROMPT expC. expC substitui o prompt original do botão ou caixa de seleção. Você também pode alterar os atributos do botão ou caixa de seleção (que determinam se o controle está habilitado ou desabilitado, quais teclas de atalho são atribuídas e se é a escolha padrão ou Esc) especificando os caracteres especiais apropriados com expC.

COLOR SCHEME expN3 | COLOR color pair list

 Os controles podem ser redesenhados nas cores que você especificar. Para obter mais informações sobre cores de controle, consulte @ ... GET e @ ... EDIT - Regiões de edição de texto.

# Observações

SHOW OBJECT redesenha um único controle (uma caixa de seleção, campo, botão invisível, push ou radio, uma lista, popup, spinner ou região de edição de texto). Quando o valor em um campo @ ... GET muda (o cursor se move para um novo registro, por exemplo), SHOW OBJECT atualiza o valor exibido no campo @ ... GET. Quando um controle é redesenhado, ele pode ser habilitado ou desabilitado. SHOW OBJECT também pode ser usado para redesenhar um botão individual dentro de um conjunto de botões invisíveis, radio ou push. Você também pode alterar os prompts de caixas de seleção e botões.

SHOW OBJECT é tipicamente usado em uma rotina executada em uma cláusula VALID ou WHEN de nível de controle ou uma cláusula ACTIVATE ou DEACTIVATE de nível READ.

SHOW GET vs. SHOW GETS e SHOW OBJECT

 Controles individuais podem ser redesenhados com SHOW OBJECT ou SHOW GET. Todos os controles podem ser redesenhados com SHOW GETS. SHOW GETS executa uma rotina SHOW de nível READ. SHOW GET e SHOW OBJECT não.

 SHOW OBJECT é semelhante a SHOW GET, exceto que SHOW OBJECT referencia controles por seu número de objeto, e SHOW GET referencia controles por uma variável de memória, elemento de matriz ou campo.

 Para obter mais informações sobre numeração de controle, consulte OBJNUM() ou _CUROBJ.

# Exemplo

O exemplo a seguir cria uma caixa de seleção. Quando a caixa de seleção é escolhida, a rotina VALID Newprompt é executada. A rotina altera o prompt da caixa de seleção e a tecla de atalho.

```foxpro
CLEAR
STORE 1 TO check
@ 4,2 GET check FUNCTION '*C \
```
