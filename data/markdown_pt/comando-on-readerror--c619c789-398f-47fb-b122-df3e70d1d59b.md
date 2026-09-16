# Comando ON READERROR

Incluído para compatibilidade com versões anteriores. Use o evento Valid em vez disso.

Especifica um comando que é executado em resposta a um erro de entrada de dados.

```foxpro
ON READERROR
	[command]
```

#### Parâmetros
 command

 O comando especificado com ON READERROR é executado quando um dos erros de entrada acima ocorre. ON READERROR normalmente usa DO para executar um procedimento que solicita ao usuário dados corretos.

 Use ON READERROR sem command para limpar o ON READERROR anterior.

# Observações

Erros de entrada que ON READERROR captura incluem:

 - Datas inválidas.
- Entrada que está fora de um intervalo definido com @ ... GET ... RANGE.
- Entrada que não atende a uma condição definida com @ ... GET ... VALID.

# Exemplo

Neste exemplo, uma mensagem é exibida se um preço digitado é menor que o custo ou maior que três vezes o custo.

```foxpro
CLOSE DATABASES
SET STATUS OFF
SET TALK OFF
USE parts
ON READERROR DO errhand
@ 10,13 SAY 'Part Number: ' GET pno
@ 12,13 SAY 'Cost: ' GET cost
@ 14,13 SAY 'Selling Price: '
@ 14,28 GET price PICTURE '999.99' RANGE cost,(cost + (cost * 3))
READ
PROCEDURE errhand
IF price < cost
	WAIT WINDOW "Price can't be lower than cost"
ELSE
	WAIT WINDOW "Markup is too high"
ENDIF
RETURN
```
