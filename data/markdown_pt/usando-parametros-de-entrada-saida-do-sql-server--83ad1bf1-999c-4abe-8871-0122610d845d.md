# Usando parâmetros de entrada/saída do SQL Server

Você pode usar parâmetros de entrada/saída para passar valores entre o Visual FoxPro e o SQL Server. Parâmetros de entrada/saída estão disponíveis apenas usando SQL pass-through; eles não podem ser usados em views.

A tabela a seguir fornece um exemplo usando parâmetros de entrada/saída para passar valores do Visual FoxPro para uma stored procedure do SQL Server, retornando o resultado para uma variável do Visual FoxPro.
 Usando parâmetros de entrada/saída com uma stored procedure do SQL Server
| Código | Comentários |
| --- | --- |
| resultCode = SQLExec(connHand, "CREATE PROCEDURE sp_test; @mult1 int, @mult2 int, @result int; OUTPUT AS SELECT @result = @mult1 * @mult2") | Cria uma stored procedure, sp_test, que multiplica duas variáveis ( mult1 e mult2 ), depois armazena o valor resultante na variável result . |
| outParam = 0 | Cria uma variável do Visual FoxPro para receber o valor do parâmetro de saída quando é passado do SQL Server para o Visual FoxPro. |
| resultCode = SQLExec(connHand, ; "{CALL sp_test (2, 4, ?@outParam)}") | Executa a stored procedure do SQL Server, passando os valores '2' e '4' para serem multiplicados juntos na stored procedure. |
| ? "outParam =", outParam && the value is 8 | Exibe o valor do parâmetro de saída. |

# Definindo parâmetros

A sintaxe para parâmetros de saída é:

```foxpro
?@parameter_name
```

Ao implementar parâmetros de entrada/saída, defina as variáveis do Visual FoxPro que deseja incluir em seu comando SQL pass-through antes de usar as variáveis na instrução SQL. Para enviar e receber informações com sucesso com parâmetros de entrada/saída, você deve definir:
 - Um parâmetro de stored procedure, com um tipo de saída, que retorna um valor. Por exemplo, se o parâmetro da sua stored procedure é @result , você deve atribuir um tipo de saída, como int , a @result , e deve atribuir um valor a @result .
- Uma expressão de parâmetro de saída ( @ parameter_name ) que avalia para uma variável do Visual FoxPro existente. Por exemplo, se sua expressão de parâmetro de saída é ?@outParam , seu aplicativo deve ter definido a variável do Visual FoxPro outParam . Observação Se você não usar um parâmetro de saída, nem no Visual FoxPro nem na stored procedure, ou não definir uma variável do Visual FoxPro para receber o valor de retorno, o valor do parâmetro do Visual FoxPro não mudará.

# Convertendo tipos de dados

O Visual FoxPro converte valores de variáveis retornados usando as seguintes regras:
 - Variáveis de tipo de dados de ponto flutuante (N, F, B) são convertidas para N.
- O tamanho de exibição é definido como 20.
- A configuração decimal é definida para a configuração da sessão atual. A configuração decimal afeta apenas o formato de exibição padrão e não afeta a precisão decimal.
- Variáveis de data e hora (D, T) são convertidas para variáveis de hora (T).

Você não pode usar tipos de dados Memo, General, Picture ou NULL em parâmetros de entrada/saída.

Se seu aplicativo usa campos de cursor como parâmetros, o Visual FoxPro tentará converter o resultado de volta para o tipo de dados do campo original.

# Retornando valores de parâmetros

Parâmetros de entrada/saída estão disponíveis apenas depois que o último conjunto de resultados de uma instrução foi buscado. Isso significa que valores de entrada/saída são retornados ao Visual FoxPro apenas depois que:
 - SQLEXEC( ) retorna (1) no modo batch -ou-
- SQLMORERESULTS( ) retorna (2) no modo não batch.

Se sua instrução SQLEXEC( ) solicita múltiplos conjuntos de resultados, os parâmetros de saída são garantidos como disponíveis apenas depois que o último conjunto de resultados foi buscado da fonte de dados.
