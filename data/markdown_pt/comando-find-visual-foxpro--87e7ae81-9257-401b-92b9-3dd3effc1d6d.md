# Comando FIND (Visual FoxPro)

Incluído para compatibilidade com versões anteriores. Use o Comando SEEK em vez disso.

Pesquisa em uma tabela indexada.

```foxpro
FIND expC
```

# Observações

FIND está incluído para compatibilidade com versões anteriores. Use SEEK em vez disso.

FIND move o ponteiro de registro para o primeiro registro na tabela cuja chave de índice corresponde à expressão de caractere expC. FIND exige que a tabela selecionada esteja indexada. A correspondência com a expressão de índice deve ser exata, a menos que SET EXACT esteja OFF.

Se um registro correspondente é encontrado, RECNO() retorna o número do registro correspondente, FOUND() retorna true (.T.) e EOF() retorna false (.F.).

Se nenhuma correspondência é encontrada, RECNO() retorna o número de registros na tabela mais 1, FOUND() retorna false (.F.) e EOF() retorna true (.T.).

Se SET NEAR estiver ON e FIND não for bem-sucedido, o ponteiro de registro é posicionado imediatamente após o registro correspondente mais próximo. Se SET NEAR estiver OFF e FIND não for bem-sucedido, o ponteiro de registro é posicionado no final do arquivo. Em ambos os casos, RECNO() emitido com um argumento de 0 retorna o número do registro correspondente mais próximo.

# Exemplo

```foxpro
CLOSE DATABASES
USE customer ORDER company	&& Open file and set order
SET EXACT OFF
STORE 'Aspen' TO mval
FIND &mval
IF FOUND()
	DISPLAY
ENDIF
```
