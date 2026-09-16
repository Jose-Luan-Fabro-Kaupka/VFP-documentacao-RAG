# SYS(16) - Nome do arquivo de programa em execução

Retorna o nome do arquivo do programa em execução. Você pode usar SYS(16) para recuperar-se de erros.

```foxpro
SYS(16 [, nProgramLevel])
```

#### Parâmetros
 **nProgramLevel**
Indica de quantos níveis atrás o nome do programa é obtido. Esse valor pode variar de 1 até a profundidade em que os programas estão aninhados. Para obter mais informações sobre níveis de aninhamento de programas, consulte número máximo de chamadas DO em Capacidades do sistema Visual FoxPro . Se nProgramLevel é 0 ou 1, SYS(16) retorna o nome do programa principal (o programa executado primeiro). O nome do programa em execução no momento é retornado se nProgramLevel for omitido. A cadeia de caracteres vazia é retornada se nProgramLevel for maior que a profundidade de aninhamento do programa.

# Valor de retorno

Character

# Observações

SYS(16) é semelhante a PROGRAM( ), exceto que SYS(16) retorna um caminho com o nome do programa ou formulário. Quando o programa em execução faz parte de uma aplicação (.app ou .exe), mas não está definido como o programa principal, SYS(16) retorna apenas o nome do programa, ou seja, sem o caminho. O nome do formulário é sempre retornado junto com seu caminho original. SYS(16) retorna o nome do arquivo executável se chamado de um arquivo executável (.exe); enquanto PROGRAM( ) retorna apenas o nome do programa. Se um procedimento ou função está sendo executado, SYS(16) retorna o nome do arquivo que contém o procedimento ou função após o nome do procedimento ou função.

# Exemplo

O aninhamento de programas é retornado no seguinte exemplo de programa curto:

```foxpro
STORE 1 TO gnX
DO WHILE LEN(SYS(16,gnX)) != 0
   ? SYS(16,gnX)
   STORE gnX+1 TO gnX
ENDDO
```
