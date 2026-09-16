# Função PROGRAM( )

Retorna o nome do programa em um nível de programa especificado, o nome do programa em execução no momento, o nível de programa atual ou o nome do programa em execução quando ocorreu um erro.

```foxpro
PROGRAM([nLevel])
```

#### Parâmetros
 **nLevel**
Especifica o número de níveis de programa a pesquisar para o nome do programa. O parâmetro nLevel pode variar de 0 à profundidade de aninhamento de programas. Para obter mais informações sobre níveis de aninhamento de programas, consulte número máximo de chamadas DO em Visual FoxPro System Capacities. Quando nLevel é omitido, PROGRAM( ) retorna o nome do programa em execução no momento. Se você especificar 0 ou 1 para nLevel, PROGRAM( ) retorna o nome do programa mestre ou o programa de nível mais alto. Se você especificar –1 para nLevel, PROGRAM( ) retorna o nível de programa atual como um valor numérico. No entanto, usar PROGRAM(–1) na janela Command sempre retorna zero (0). Se nLevel exceder a profundidade de aninhamento de programas, PROGRAM( ) retorna uma cadeia de caracteres vazia ("").

# Valor de retorno

Caractere ou Numérico. PROGRAM( ) retorna um nome de programa, o número do nível de programa atual ou uma cadeia de caracteres vazia.

# Observações

Você pode usar PROGRAM( ) para ajudar seu programa a recuperar-se de erros. A função PROGRAM( ) é semelhante a SYS(16) - Executing Program File Name.

# Exemplo

```foxpro
ON ERROR DO errhand WITH PROGRAM()
*** The next line should generate an error ***
USE nodatabase
ON ERROR     && Returns to system default error-handling routine
PROCEDURE errhand
PARAMETERS gcProgram
WAIT 'An error occurred in the program ' + gcProgram WINDOW
```
