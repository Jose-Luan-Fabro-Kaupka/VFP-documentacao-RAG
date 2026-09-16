# Função OBJNUM( )

Incluída para compatibilidade com versões anteriores. Use a propriedade TabIndex para controles em vez disso.

Retorna o número do objeto de um controle @ ... GET.

```foxpro
OBJNUM(var [, expN])
```

#### Parâmetros
 var
 var é o nome da variável de memória, elemento de matriz ou campo especificado quando você cria o controle.

 expN

 READs aninhados são criados emitindo @ ... GETS e um READ em uma rotina chamada durante um READ. READs podem ser aninhados até cinco níveis. Para retornar um número de controle para um controle em um nível de leitura diferente do nível de leitura atual, inclua o número de nível de leitura opcional expN. Se expN for omitido, OBJNUM() retorna o número de controle @ ...GET para o nível de leitura atual.

# Valor de retorno

Valor de retorno - Numérico

# Observações

Você pode usar @ ... GET e @ ...EDIT para criar controles, às vezes chamados objetos. Esses controles são campos, caixas de seleção, listas, popups; botões invisíveis, push e de opção; spinners e regiões de edição de texto. OBJNUM() retorna um número que corresponde à ordem de criação de um controle em um conjunto de controles.

# Exemplo

O exemplo a seguir cria uma janela e coloca botões de opção na janela para que você possa mover o ponteiro de registro por uma tabela aberta. Se uma tabela não estiver aberta, a caixa de diálogo Open é exibida para que você possa selecionar uma tabela para abrir.

```foxpro
SET TALK OFF
DEFINE WINDOW gotodialog FROM 9, 17 TO 19,61 ;
	FLOAT NOCLOSE SHADOW DOUBLE COLOR SCHEME 5
PRIVATE file,lastobj,enter,tab,shifttab,up,down,left,right
*** Assign lastkey values ***
enter		= 13
tab			= 9
shifttab	= 15
up			= 5
down		= 24
right		= 4
left		= 19
lastobj	= 1
*** Open a table ***
IF EMPTY(DBF())
	file = GETFILE('DBF','Pick a table')
	IF EMPTY(FILE)
		WAIT WINDOW 'Cancelled' NOWAIT
		RETURN
	ENDIF
	USE (file)
ENDIF
*** Draw the fields ***
ACTIVATE WINDOW gotodialog
@ 0,1 TO 8,25
@ 1,3 GET radio PICTURE '@*RVN \ RECCOUNT()
				WAIT WINDOW 'Record out of range' NOWAIT
			ELSE
				GO recordnum
			ENDIF
		CASE radio = 4
			IF skipnum+RECNO() > RECCOUNT() OR skipnum + RECNO() < 0
				WAIT WINDOW 'Record out of range' NOWAIT
			ELSE
				SKIP skipnum
			ENDIF
	ENDCASE
ENDIF
```
