# Comando CONTINUE

Continua o LOCATE anterior.

```foxpro
CONTINUE
```

# Observações

CONTINUE é usado depois que LOCATE encontra com sucesso um registro, para continuar a operação LOCATE. CONTINUE move o ponteiro de registro para o próximo registro para o qual a expressão lógica especificada no LOCATE anterior é avaliada como True (.T.).

CONTINUE pode ser repetido até que o final do arquivo seja encontrado ou até que o final do escopo especificado com LOCATE seja atingido.

Se CONTINUE encontrar com sucesso um registro, RECNO( ) retorna o número do registro, FOUND( ) retorna um valor True (.T.) e EOF( ) retorna um valor False (.F.).

Se CONTINUE não encontrar com sucesso um registro, RECNO( ) retorna o número de registros na tabela mais um, FOUND( ) retorna False (.F.) e EOF( ) retorna True (.T.).

# Exemplo

No exemplo a seguir, todos os clientes da França são contados e o total é exibido. Todos os registros são encontrados usando um comando LOCATE seguido por um comando CONTINUE dentro de um loop.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer  && Opens Customer table
SET TALK OFF
STORE 0 TO gnCount
LOCATE FOR ALLTRIM(UPPER(country)) = 'FRANCE'
DO WHILE FOUND()
   gnCount = gnCount + 1
   CONTINUE
ENDDO
? 'Total customers from France: '+ LTRIM(STR(gnCount))
```
