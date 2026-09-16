# Função ADATABASES( )

Coloca os nomes de todos os bancos de dados abertos e seus caminhos em uma matriz de variáveis.

```foxpro
ADATABASES(ArrayName)
```

#### Parâmetros
 **ArrayName**
Especifica o nome da matriz. Se a matriz especificada não existir, o Visual FoxPro a cria automaticamente. Se a matriz existir e não for grande o suficiente para conter todas as informações do banco de dados, o Visual FoxPro aumenta automaticamente o tamanho da matriz para acomodar as informações. Se a matriz for maior que o necessário, o Visual FoxPro trunca a matriz. Se a matriz existir e ADATABASES( ) retornar 0 porque nenhum banco de dados está aberto, uma matriz existente permanece inalterada. Se a matriz não existir e ADATABASES( ) retornar 0, a matriz não é criada.

# Valor de retorno

Numérico

# Observações

Os nomes de todos os bancos de dados abertos são colocados em uma matriz de variáveis.

ADATABASES( ) cria uma matriz bidimensional. A primeira coluna da matriz contém os nomes dos bancos de dados abertos, e a segunda coluna contém os caminhos para os bancos de dados.

ADATABASES( ) retorna o número de nomes de bancos de dados (linhas) na matriz. Se nenhum banco de dados estiver aberto, ADATABASES( ) retorna 0 e a matriz não é criada.

# Exemplo

O exemplo a seguir abre o banco de dados `testdata` e, em seguida, usa ADATABASES( ) para criar uma matriz chamada `gaDatabase` contendo os nomes de todos os bancos de dados abertos.

```foxpro
SET PATH TO (HOME(2) + 'data\')     && Sets path to database
OPEN DATABASE testdata && Opens the database
CLEAR
? ADATABASES(gaDatabase)     && Creates an array of open databases
DISPLAY MEMORY LIKE gadatabase  && Displays the contents of the array
CLOSE DATABASES
```
