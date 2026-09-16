# Propriedade BreakOnError

Especifica se o Visual FoxPro permite que erros interrompam a execução do programa no local em que ocorreram ou os envia ao cursor adapter. Leitura/gravação em tempo de design e em tempo de execução.

BreakOnError se aplica somente quando o cursor adapter executa um evento ou um comando SQL INSERT - SQL Command, UPDATE - SQL Command ou DELETE - SQL Command.

```foxpro
CursorAdapter.BreakOnError [= lValue]
```

# Valor de retorno
 **lValue**
Tipo de dados lógico. A tabela a seguir lista os valores de lValue . lValue Descrição False (.F.) O Visual FoxPro não exibe uma mensagem de erro e envia o erro ao cursor adapter. (Padrão) Este comportamento é o mesmo que se o Visual FoxPro gerasse um erro e o usuário cancelasse a execução. A rotina de erro torna o último erro não tratado disponível para a rotina chamadora. True (.T.) O Visual FoxPro permite que a execução do evento ou método seja interrompida no local em que o erro ocorre e exibe uma mensagem de erro.

# Observações

Aplica-se a: Classe CursorAdapter
