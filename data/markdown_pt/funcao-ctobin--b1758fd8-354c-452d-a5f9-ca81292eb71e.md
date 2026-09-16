# Função CTOBIN( )

Converte uma representação de caractere binário em um valor numérico.

```foxpro
CTOBIN(cExpression [, cFlags])
```

#### Parâmetros
 **cExpression**
Especifica a representação de caractere binário a converter.
**cFlags**
Se a representação de caractere binário especificada com cExpression foi gerada usando um tipo de dados de 8 bytes (moeda ou double, por exemplo), inclua cFlags para controlar o tipo de valor retornado por CTOBIN( ). cFlags Descrição 1 cExpression é uma expressão com 1 byte de comprimento. 2 cExpression é uma expressão com 2 bytes de comprimento. 4 cExpression é uma expressão com 4 bytes de comprimento. 8 cExpression é uma expressão com 8 bytes de comprimento. B cExpression é um tipo de dados double e deve ter 8 bytes de comprimento. CTOBIN( ) retorna um valor do tipo double. Este é o padrão para uma expressão com 8 bytes de comprimento. N cExpression é um tipo de dados numérico e deve ter 4 ou 8 bytes de comprimento. CTOBIN( ) retorna um valor do tipo numérico. Y cExpression é um tipo de dados currency e deve ter 8 bytes de comprimento. CTOBIN( ) retorna um valor do tipo currency. R Inverte a expressão binária. S Impede que o bit de sinal do número seja alternado (BITXOR).

# Valor de retorno

Numérico. CTOBIN( ) retorna um valor numérico de uma expressão de caractere binário.

# Observações

O parâmetro cFlags é uma expressão de caractere. As configurações 'R' e 'S' são aditivas, enquanto as outras são mutuamente exclusivas. As configurações de caractere podem ser passadas em maiúsculas ou minúsculas (por exemplo, 'R' ou 'r'). Especificar um valor de '1', '2' ou '4' não é obrigatório, mas está disponível como conveniência para fornecer feedback sobre o comprimento de cExpression.

Os exemplos a seguir mostram vários usos do parâmetro cFlags.

```foxpro
? CTOBIN("A")&& same as CTOBIN("A","1")
? CTOBIN(BINTOC($12.34,"8"),"Y")
? CTOBIN(BINTOC(12.34,"8"),"B")
? CTOBIN(BINTOC(PI(),"BR"),"NRS")
```

Você pode usar CTOBIN( ) para converter uma representação de caractere binário criada com BINTOC( ) em seu valor inteiro. CTOBIN( ) também pode ser usado ao trabalhar com rotinas de API Win32 em que você pode precisar converter de ou para um membro de struct Win32. As configurações 'R' e 'S' permitem usar CTOBIN( ) para trabalhar com mais eficiência nesses cenários.
