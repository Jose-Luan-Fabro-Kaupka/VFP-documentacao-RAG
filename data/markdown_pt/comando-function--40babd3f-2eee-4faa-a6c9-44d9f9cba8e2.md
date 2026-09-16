# Comando FUNCTION

Cria uma função definida pelo usuário em um arquivo de programa. Há duas versões da sintaxe.

```foxpro
FUNCTION FunctionName
   [ LPARAMETERS parameter1 [ ,parameter2 ] , ... ]
      Commands
   [ RETURN [ eExpression ] ]
[ENDFUNC]
```

```foxpro
FUNCTION FunctionName( [ parameter1 [ AS para1type ][ ,parameter2 [ AS para2type ] ],...] ) [ AS returntype ]
      Commands
   [ RETURN [ eExpression ] ]
[ENDFUNC]
```

#### Parâmetros
 **FUNCTION FunctionName**
Designa o início de uma função definida pelo usuário e especifica o nome da função. FunctionName pode conter até 254 caracteres.
**[ LPARAMETERS parameter1 [, parameter2 ] , ... ]**
Atribui dados do programa chamador a variáveis ou matrizes locais. Você também pode usar a palavra-chave PARAMETERS em vez de LPARAMETERS para aceitar parâmetros com escopo privado. Você pode passar um máximo de 26 parâmetros para uma função. Para obter mais informações, consulte LPARAMETERS Command e PARAMETERS Command .
**( [ parameter1 [ AS para1type ][ , parameter2 [ AS para2type ] ],...] )**
Atribui dados do programa chamador a variáveis ou matrizes locais. Você pode usar a cláusula AS para especificar o tipo de dados da variável. Observação Incluir os parâmetros entre parênteses (()) imediatamente após o nome da função indica que os parâmetros têm escopo local na função.
**[ AS returntype ]**
Especifica o tipo de dados do valor de retorno. Você pode usar a cláusula AS para implementar tipagem forte. Para obter mais informações, consulte How to: Implement Strong Typing for Class, Object, and Variable Code .
**Commands**
Especifica os comandos Visual FoxPro a serem executados ao executar a função.
**[ RETURN [ eExpression ] ]**
Retorna o controle ao programa chamador ou a outro programa. eExpression pode especificar um valor de retorno. Observação Você pode incluir o comando RETURN em qualquer lugar da função para retornar o controle ao programa chamador ou a outro programa e definir um valor retornado pela função. Se você não incluir o comando RETURN, o Visual FoxPro executa um RETURN implícito automaticamente quando a função termina. Se o comando RETURN não incluir um valor de retorno ou se um RETURN implícito for executado, o Visual FoxPro atribui True (.T.) como valor de retorno. Para obter mais informações, consulte RETURN Command .
**[ ENDFUNC ]**
Indica o fim da estrutura FUNCTION. Observação A palavra-chave ENDFUNC é opcional porque a função termina quando encontra outro comando FUNCTION, um comando PROCEDURE ou o fim do arquivo de programa. Você não pode incluir código de programa executável normal após funções definidas pelo usuário em um arquivo de programa. Somente outras funções definidas pelo usuário, procedimentos e definições de classe podem seguir o primeiro comando FUNCTION ou PROCEDURE no arquivo.

# Observações

Por padrão, os parâmetros são passados para funções por valor. Para obter informações sobre passar parâmetros para funções por referência, consulte SET UDFPARMS Command.

Quando você emite o comando DO com um nome de função, o Visual FoxPro pesquisa a função na seguinte ordem:
 - O arquivo contendo o comando DO.
- Arquivos de procedimento abertos com SET PROCEDURE. Para obter mais informações, consulte SET PROCEDURE Command .
- Arquivos de programa na cadeia de execução. O Visual FoxPro pesquisa arquivos de programa em ordem do programa executado mais recentemente ao primeiro programa executado.
- Um arquivo de programa autônomo.

Se um arquivo de programa correspondente for encontrado, o Visual FoxPro executa o programa. Caso contrário, o Visual FoxPro gera uma mensagem de erro.

Para executar uma função em um arquivo específico, inclua a cláusula IN no comando DO.

Para obter informações sobre o uso do comando FUNCTION ao criar classes, consulte DEFINE CLASS Command.

# Exemplo

Este exemplo cria uma classe de objeto personalizada chamada `Hello` e adiciona um método de função chamado `SayHello`. O método `SayHello` retorna a cadeia de caracteres "Hello World", que é exibida pela função MESSAGEBOX. Observação: O código de definição da classe é colocado após o código do programa que instancia o objeto.

```foxpro
Local oHello
oHello=CREATEOBJECT("Hello")
=MESSAGEBOX(oHello.SayHello(),48)
RELEASE oHello
* Class definition code
DEFINE CLASS Hello AS CUSTOM
 FUNCTION SayHello
  RETURN "Hello World"
 ENDFUNC
ENDDEFINE
```
