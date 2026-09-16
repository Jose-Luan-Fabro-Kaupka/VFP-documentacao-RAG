# Função TRANSFORM( )

Retorna uma cadeia de caracteres de uma expressão em um formato determinado por um código de formato.

> **Observação:** Usar TRANSFORM( ) com um número negativo grande que contém decimal pode resultar em overflow numérico quando esse número é passado como variável de memória. Você deve usar a função STR( ) em vez disso com esses números.

```foxpro
TRANSFORM(eExpression, [cFormatCodes])
```

#### Parâmetros
 **eExpression**
Especifica a expressão a formatar.
**cFormatCodes**
Especifica um ou mais códigos de formato que determinam como formatar a expressão.

> **Observação:** A tabela a seguir lista os códigos de formato disponíveis para cFormatCodes .

| cFormatCodes | Descrição |
| --- | --- |
| @B | Alinha à esquerda dados numéricos na região de exibição. |
| @C | Acrescenta um CR a valores de moeda ou numéricos positivos para indicar crédito. |
| @D | Converte valores Date e DateTime para o formato SET DATE atual. |
| @E | Converte valores Date e DateTime para um formato de data BRITISH. |
| @L | Preenche dados numéricos com zeros à esquerda. |
| @R | A transformação usa uma máscara de formato. Os caracteres da máscara não são armazenados no valor transformado. Use apenas com dados de caractere ou numéricos. Caracteres de máscara incluem: 9 ou # Representa um caractere ou número. ! Converte letras minúsculas em maiúsculas. Observação O Visual FoxPro não exibe caracteres de máscara especificados que excedam o comprimento convertido da cadeia da expressão passada. |
| @T | Remove espaços à esquerda e à direita de valores de caractere. |
| @X | Acrescenta DB a valores de moeda ou numéricos negativos para indicar débito. |
| @YL | Usa a configuração de data longa do sistema. |
| @YS | Usa a configuração de data curta do sistema. |
| @Z | Se 0, converte valores de moeda ou numéricos em espaços. |
| @( | Coloca valores de moeda ou numéricos negativos entre parênteses. |
| @^ | Converte valores de moeda ou numéricos em notação científica. |
| @0 | Converte valores numéricos ou de moeda em seus equivalentes hexadecimais. O valor numérico ou de moeda deve ser positivo e menor que 4.294.967.296. |
| @! | Converte uma cadeia de caracteres inteira para maiúsculas. |
| @$ | Adiciona o símbolo de moeda atual especificado por SET CURRENCY a valores de moeda e numéricos. Por padrão, o símbolo é colocado imediatamente antes ou depois do valor. No entanto, o símbolo de moeda e sua posição (especificados com SET CURRENCY ), o caractere separador (especificado com SET SEPARATOR ) e o caractere decimal (especificado com SET POINT ) podem ser alterados. |
| X | Especifica a largura de valores de caractere. Por exemplo, se cFormatCodes é 'XX', 2 caracteres são retornados. |
| Y | Converte valores lógicos True (.T.) e False (.F.) em Y e N, respectivamente. |
| ! | Converte um caractere minúsculo em maiúsculo na posição correspondente em uma cadeia de caracteres. |
| . | Especifica a posição do ponto decimal em valores de moeda e numéricos. |
| , | Separa dígitos à esquerda do ponto decimal em valores de moeda e numéricos. |
| 9 | Especifica a largura de valores numéricos. Por exemplo, se cFormatCodes é '999.99', os caracteres numéricos são formatados com três caracteres à esquerda do ponto decimal e dois à direita. Observação Ao especificar cFormatCodes para valores numéricos, o código de formato deve ter pelo menos o tamanho do valor que você deseja exibir. O exemplo a seguir mostra os resultados quando o código de formato está ausente, é menor que e é igual ao tamanho do valor que você deseja exibir. CREATE CURSOR myCursor (col1 n(5,2)) INSERT INTO myCursor VALUES (-555.5) * Sem código de formato e retorna **.** ? TRANSFORM(myCursor.col1 ) * Um código de formato 1 menor que o valor retorna ***.** ? TRANSFORM(myCursor.col1,'999.99' ) * Um código de formato do mesmo tamanho do valor retorna -556.00 ? TRANSFORM(myCursor.col1,'9999.99' ) Quando o valor da expressão é maior que a largura do campo numérico, o Visual FoxPro força o valor a caber executando as seguintes etapas: Trunca casas decimais e arredonda a parte decimal restante do campo. Se o valor não cabe, armazena o conteúdo do campo usando notação científica. Se o valor ainda não cabe, substitui o conteúdo do campo por asteriscos. |

Para obter mais informações sobre códigos de formato, consulte InputMask Property e Format Property.

Se você omitir cFormatCodes, o Visual FoxPro executa uma transformação padrão em eExpression. A tabela a seguir descreve a transformação executada para cada tipo de dados que eExpression pode assumir.

| Tipo de dados | Descrição da transformação |
| --- | --- |
| Blob | Produz a representação em cadeia de caracteres do valor binário sem o prefixo hexadecimal. Por exemplo, a linha de código a seguir produz a cadeia de caracteres "FEOAF2": TRANSFORM(0hFE0AF2) Para valores binários, TRANSFORM( ) ignora códigos de formato, exceto os que restringem a largura. Por exemplo, as linhas de código a seguir produzem "FE0A": TRANSFORM(0hFE0AF2, "XXXX") TRANSFORM(0hFE0AF2, "9999") TRANSFORM(0hFE0AF2, "####") Para esses códigos de formato que restringem a largura, o comprimento máximo de saída é 255 caracteres. |
| Character | Não executa transformação. |
| Currency | A transformação é determinada pelas configurações especificadas na guia Regional da caixa de diálogo Opções. |
| Date | Executa uma transformação DTOC( ) na data. |
| DateTime | Executa uma transformação TTOC( ) na data e hora. |
| General | Retorna "Gen" se o campo General contém um objeto ou "gen" se o campo General não contém um objeto. |
| Logical | Transforma valores lógicos True (.T.) e False (.F.) nas cadeias de caracteres ".T." e ".F." respectivamente. |
| Memo | Não executa transformação. |
| Numeric (inclui tipos de dados Double , Float ou Integer) | Remove zeros à direita da parte decimal de um valor numérico quando todos os números após o ponto decimal são zeros. Se o valor numérico é um número inteiro, um ponto decimal não é incluído no valor transformado; por exemplo, 4.0 é transformado em 4. Se o valor numérico é menor que um, mas maior que menos um, zero é incluído antes do ponto decimal; por exemplo, .4 é transformado em 0.4. |
| Object | Retorna a cadeia de caracteres "(Object)". |
| Varbinary | Produz a representação em cadeia de caracteres do valor binário sem o prefixo hexadecimal. Por exemplo, a linha de código a seguir produz a cadeia de caracteres "FEOAF2": TRANSFORM(0hFE0AF2) Para valores binários, TRANSFORM( ) ignora códigos de formato, exceto os que restringem a largura. Por exemplo, as linhas de código a seguir produzem "FE0A": TRANSFORM(0hFE0AF2, "XXXX") TRANSFORM(0hFE0AF2, "9999") TRANSFORM(0hFE0AF2, "####") |

# Valor de retorno

Tipo de dados Character. TRANSFORM( ) retorna uma cadeia de caracteres de uma expressão em um formato determinado por um código de formato.

# Exemplo

```foxpro
STORE 12.34 TO gnPrice
CLEAR
? TRANSFORM(gnPrice, '$$$$.99')  && Displays $12.34
? TRANSFORM(_SCREEN)   && Displays (Object)
```
