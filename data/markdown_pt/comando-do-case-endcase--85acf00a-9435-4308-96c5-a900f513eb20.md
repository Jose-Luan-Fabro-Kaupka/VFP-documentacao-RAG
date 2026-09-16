# Comando DO CASE ... ENDCASE

Executa o primeiro conjunto de comandos cuja expressão condicional é avaliada como true (.T.).

```foxpro
DO CASE
   CASE lExpression1
   [Commands]
   [CASE lExpression2
   [Commands]]
   ...
   [CASE lExpressionN
   [Commands]]
   [OTHERWISE
   [Commands]]
ENDCASE
```

#### Parâmetros
 **CASE lExpression1 Commands ...**
Quando a primeira expressão CASE true (.T.) é encontrada, o conjunto de comandos que a segue é executado. A execução do conjunto de comandos continua até que o próximo CASE ou ENDCASE seja alcançado. A execução então retoma no primeiro comando após ENDCASE. Se uma expressão CASE é false (.F.), o conjunto de comandos que a segue até a próxima cláusula CASE é ignorado. Apenas um conjunto de comandos é executado: os primeiros comandos cuja expressão CASE é avaliada como true (.T.). Quaisquer expressões CASE true (.T.) subsequentes são ignoradas.
**OTHERWISE Commands**
Se todas as expressões CASE são avaliadas como false (.F.), OTHERWISE determina se um conjunto adicional de comandos é executado. Se você incluir OTHERWISE, os comandos após OTHERWISE são executados e a execução salta para o primeiro comando após ENDCASE. Se você omitir OTHERWISE, a execução salta para o primeiro comando após ENDCASE .

# Observações

DO CASE é usado para executar um conjunto de comandos do Visual FoxPro com base no valor de uma expressão lógica. Quando DO CASE é executado, expressões lógicas sucessivas são avaliadas; os valores das expressões determinam qual conjunto de comandos é executado.

Comentários podem ser colocados após DO CASE e ENDCASE na mesma linha. Os comentários são ignorados durante a compilação e a execução do programa.

# Exemplo

Neste exemplo, o Visual FoxPro avalia cada cláusula CASE até que a variável MONTH seja encontrada em uma das listas. A cadeia de caracteres apropriada é armazenada na variável `rpt_title` e a estrutura DO CASE é encerrada.

```foxpro
STORE CMONTH(DATE()) TO month  && The month today

DO CASE  && Begins loop

   CASE INLIST(month,'January','February','March')
      STORE 'First Quarter Earnings' TO rpt_title

   CASE INLIST(month,'April','May','June')
      STORE 'Second Quarter Earnings' TO rpt_title

   CASE INLIST(month,'July','August','September')
      STORE 'Third Quarter Earnings' TO rpt_title

   OTHERWISE
      STORE 'Fourth Quarter Earnings' TO rpt_title
ENDCASE  && Ends loop
WAIT WINDOW rpt_title NOWAIT
```
