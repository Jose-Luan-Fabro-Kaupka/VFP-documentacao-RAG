# Função BINTOC( )

Converte um valor numérico em uma representação de caractere binário.

```foxpro
BINTOC(nExpression [, eFlags])
```

#### Parâmetros
 **nExpression**
Especifica o valor a converter. Para configurações eFlags 1, 2 ou 4, esse valor é um inteiro. Caso contrário, o tipo de dados da expressão é baseado na configuração eFlags.
**eFlags**
Especifica o comprimento em caracteres da cadeia de caracteres retornada. eFlags determina o valor que você pode especificar para nExpression . eFlags pode ser numérico ou de caractere. A tabela a seguir lista os valores permitidos para eFlags e o intervalo correspondente de valores para nExpression : eFlags Intervalo de nExpression 1 –128 a 127 2 –32.768 a 32.767 4 –2.147.483.648 a 2.147.483.647 Esta é a configuração padrão. 8 O intervalo de nExpression depende de seu tipo. Somente tipos de dados numeric, float, double e currency são suportados com esta opção. Consulte Visual FoxPro Data and Field Types para os intervalos dos tipos de dados numeric, float, double e currency. BINTOC( ) retorna 8 bytes para esta configuração. F nExpression é interpretado como um Float Field Type e BINTOC( ) retorna 4 bytes. B nExpression é interpretado como um Double Field Type e BINTOC( ) retorna 8 bytes. R Inverte a expressão binária resultante. S Impede que o bit de sinal do número seja alternado (BITXOR). Se este parâmetro for omitido, BINTOC( ) retorna uma cadeia de caracteres composta por quatro caracteres.

# Valor de retorno

Character. BINTOC( ) retorna uma expressão de caractere binário.

# Observações

O parâmetro eFlags pode ser numérico ou de caractere. As configurações 'R' e 'S' são aditivas, enquanto as outras são mutuamente exclusivas. Configurações de caractere podem ser passadas em maiúsculas ou minúsculas (por exemplo, 'R' ou 'r'). Os exemplos a seguir mostram vários usos do parâmetro eFlags.

```foxpro
? BINTOC(1,1)
? BINTOC(1000,"2")&& same as BINTOC(1000,2)
? BINTOC($12.34,8)
? BINTOC(1, "4RS")&& same as BINTOC(1,"RS")
? BINTOC(-100, "Fr")
```

Você pode usar BINTOC( ) para reduzir o tamanho de índices para campos numéricos que contêm dados inteiros passando um parâmetro eFlags numérico. Por exemplo, um campo numérico chamado `nPartCode` pode conter um valor inteiro de 1 a 32.767, que corresponde a um código de classificação de peças. BINTOC( ) permite converter o valor no campo numérico em uma representação de caractere menor. Por exemplo, o comando a seguir cria um índice com uma chave de índice de dois caracteres:

```foxpro
INDEX ON BINTOC(nPartCode,2) TAG PartCode
```

Ao usar BINTOC( ) para criação de índice de 8 bytes, você deve usar 8 e não "B". Para resultados de 4 bytes, você deve usar 4 se nExpression for um tipo inteiro. Caso contrário, você deve usar 'F' para tipo de ponto flutuante.

BINTOC( ) também pode ser usado ao trabalhar com rotinas Win32 API onde você pode precisar converter de ou para um membro de struct Win32. Quando usado para indexação, BINTOC( ) precisa tratar adequadamente números negativos para a expressão binária resultante. Isso é feito usando uma operação BITXOR no bit mais alto. Isso também significa que o byte mais significativo vem primeiro. Para rotinas Win32 API em uma plataforma Intel, a arquitetura segue a regra little-endian, onde o byte menos significativo é armazenado primeiro (local de memória com endereço mais baixo). As configurações 'R' e 'S' permitem usar BINTOC( ) para trabalhar com mais eficiência com rotinas que usam structs.
