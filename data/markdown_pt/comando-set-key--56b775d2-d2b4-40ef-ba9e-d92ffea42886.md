# Comando SET KEY

Especifica o acesso a um intervalo de registros com base em suas chaves de índice.

```foxpro
SET KEY TO [eExpression1 | RANGE eExpression2 [, eExpression3]]
   [IN cTableAlias | nWorkArea]
```

#### Parâmetros
 **eExpression1**
Permite acesso a um conjunto de registros com chaves de índice idênticas. eExpression1 é um único valor de chave de índice. Todos os registros com chaves de índice que correspondem a eExpression1 são acessíveis.
**RANGE eExpression2 [, eExpression3 ]**
Permite acesso a um conjunto de registros com chaves de índice que caem dentro de um intervalo de valores de chave de índice. eExpression2 permite acesso a registros com chaves de índice iguais ou maiores que eExpression2 . eExpression3 (precedido por uma vírgula) permite acesso a registros com chaves de índice iguais ou menores que eExpression3 . Incluir ambos eExpression2 e eExpression3 (separados por uma vírgula) permite acesso a registros com chaves de índice iguais ou maiores que eExpression2 e iguais ou menores que eExpression3 . Por exemplo, a tabela CUSTOMER inclui um campo de caracteres contendo códigos postais. Se a tabela está indexada no campo de código postal, você pode especificar um intervalo de códigos postais com SET KEY. No exemplo a seguir, apenas registros com códigos postais no intervalo de 40000 a 43999 aparecem em uma janela Browse: CLOSE DATABASES USE customer SET ORDER TO postalcode SET KEY TO RANGE '40000', '43999' BROWSE
**IN cTableAlias | nWorkArea**
Permite acesso a um intervalo de registros para uma tabela aberta em uma área de trabalho específica. cTableAlias especifica o alias da área de trabalho e nWorkArea especifica o número da área de trabalho. Se nenhuma tabela tem o alias especificado, o Visual FoxPro gera uma mensagem de erro. Se você omitir o alias e o número da área de trabalho, SET KEY opera na tabela na área de trabalho atualmente selecionada.

# Observações

Use SET KEY para limitar o intervalo de registros que você pode acessar em uma tabela. A tabela deve estar indexada, e o valor ou valores de chave de índice que você inclui devem ser do mesmo tipo de dados que a expressão de índice do arquivo de índice mestre ou tag mestre.

Emita SET KEY TO sem argumentos adicionais para restaurar o acesso a todos os registros na tabela.
