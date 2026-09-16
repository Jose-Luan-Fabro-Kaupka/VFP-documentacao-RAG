# Função FOUND( )

Determina se o comando CONTINUE, FIND, LOCATE ou SEEK executado mais recentemente foi bem-sucedido ou se o ponteiro de registro foi movido em uma tabela relacionada.

> **Dica:** Você pode usar FOUND( ) para determinar se uma tabela filha tem um registro correspondente ao registro pai.

```foxpro
FOUND([nWorkArea | cTableAlias])
```

#### Parâmetros
 **nWorkArea**
Especifica a área de trabalho da tabela na qual o comando CONTINUE, FIND, LOCATE ou SEEK mais recente foi chamado.
**cTableAlias**
Especifica o alias da tabela na qual o comando CONTINUE, FIND, LOCATE ou SEEK mais recente foi chamado. Observação: se você especificar um alias de tabela inexistente, o Visual FoxPro gerará uma mensagem de erro.

# Valor de retorno

Logical. FOUND( ) retorna True (.T.) se o comando CONTINUE, FIND, LOCATE ou SEEK mais recente tiver sido bem-sucedido; caso contrário, retorna False (.F.). Se uma tabela não estiver aberta na área de trabalho especificada, FOUND( ) retornará False. Quando FOUND( ) encontra o fim do arquivo, que pode ser determinado pela função EOF( ), ele sempre retorna False.

# Observações

Se você chamar FOUND( ) sem argumentos, FOUND( ) será chamado na tabela aberta na área de trabalho selecionada no momento.

# Exemplos

O exemplo a seguir localiza e conta todos os clientes cujo campo Country da tabela Customer contém "GERMANY". CLOSE DATABASES fecha todos os bancos de dados, e OPEN DATABASE abre o banco de dados de exemplo do Visual FoxPro, TestData.dbc. USE abre a tabela Customer.

STORE armazena o valor 0 na variável gnCount. LOCATE procura o primeiro registro em que o campo Country contém o valor "GERMANY". O loop DO WHILE incrementa a variável gnCount em 1 e usa CONTINUE para executar outra operação LOCATE. Quando não há mais registros correspondentes, o número total de clientes é exibido.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\TestData')
USE Customer
STORE 0 TO gnCount
LOCATE FOR UPPER(Country)='GERMANY'
DO WHILE FOUND()
   gnCount = gnCount + 1
   CONTINUE
ENDDO
? "Total customers from Germany: "+LTRIM(STR(gnCount))
```
