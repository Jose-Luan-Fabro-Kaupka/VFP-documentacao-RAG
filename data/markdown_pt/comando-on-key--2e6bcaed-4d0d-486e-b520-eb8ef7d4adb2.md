# Comando ON KEY

Incluído para compatibilidade com versões anteriores. Use o comando ON KEY LABEL em vez disso.

Especifica um comando que é executado quando você pressiona qualquer tecla durante a execução do programa.

```foxpro
ON KEY
	[command]
```

# Observações

Quando você pressiona qualquer tecla durante a execução do programa, o FoxPro executa o comando que você especifica com ON KEY. Normalmente, ON KEY usa DO para executar um procedimento.

Depois que o comando que você especificou com ON KEY é executado, a execução do programa continua na linha imediatamente após a linha do programa que estava sendo executada quando uma tecla foi pressionada. No entanto, se um procedimento especificado com ON KEY incluir RETRY, a linha do programa que estava sendo executada quando uma tecla foi pressionada é executada novamente.

Use ON KEY sem um comando para que nenhum comando seja executado quando uma tecla é pressionada (o padrão).

Se tanto ON KEY quanto ON ESCAPE estiverem em vigor e Esc for pressionado, o comando especificado com ON ESCAPE é executado.

# Exemplo

Neste exemplo, registros da tabela CUSTOMER são exibidos. Se uma tecla for pressionada enquanto os registros estão sendo exibidos, o procedimento chamado PAUSE é chamado. PAUSE usa WAIT para suspender a exibição.

```foxpro
SET TALK OFF
USE customer
CLEAR
ON KEY DO pause
DO WHILE NOT EOF()
	? 'Company: ' + company
	? 'Address: ' + address
	?
	SKIP
ENDDO
PROCEDURE pause
STORE INKEY() TO HOLD
WAIT
RETURN
```
