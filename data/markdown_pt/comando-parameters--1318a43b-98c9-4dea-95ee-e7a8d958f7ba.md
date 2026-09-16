# Comando PARAMETERS

Atribui dados de um programa chamador a variáveis ou matrizes privadas.

```foxpro
PARAMETERS Parameter1 [ AS type [ OF ClassLib ] ]
   [, Parameter2 [ AS type [ OF ClassLib ] ] ]
```

#### Parâmetros
 **PARAMETERS ParameterList**
Especifica um ou mais nomes de variável ou matriz para atribuir dados. Use vírgulas para separar vários parâmetros em ParameterList . Em geral, você pode passar no máximo 26 parâmetros; no entanto, em algumas circunstâncias, é possível passar 27 parâmetros. Observação A instrução PARAMETERS deve especificar pelo menos tantos parâmetros quanto os usados pela chamada ao programa, procedimento ou função que contém a instrução PARAMETERS. Se mais variáveis ou matrizes estiverem listadas na instrução PARAMETERS do que as passadas pelo programa chamador, as variáveis ou matrizes restantes na instrução PARAMETERS são inicializadas como Falso (.F.).
**[ AS type [ OF ClassLib ] ]**
Especifica o tipo de dados da variável ou matriz e a biblioteca de classes que contém a descrição de tipo de type na qual essa variável ou matriz se baseia. Você pode usar a cláusula AS para implementar tipagem forte. A funcionalidade IntelliSense está disponível para referências de objeto e variável somente quando são fortemente tipadas. Para obter mais informações, consulte How to: Implement Strong Typing for Class, Object, and Variable Code .

# Observações

Quando PARAMETERS é usado com um programa, procedimento ou função definida pelo usuário chamada com o comando DO, deve ser a primeira instrução executável no programa, procedimento ou função definida pelo usuário chamado.

Por padrão, a cláusula WITH no comando DO passa variáveis e matrizes para procedimentos por referência. Por padrão, o Visual FoxPro passa argumentos por valor para funções definidas pelo usuário.

> **Observação:** Para passar matrizes inteiras para funções, você deve passá-las por referência. Se você não passar matrizes para funções por referência, apenas o primeiro elemento é passado para a função. Para obter mais informações, consulte How to: Pass Data to Parameters by Reference .

Para obter mais informações, consulte Passing Data to Parameters e Parameters in Procedures and Functions.

# Exemplo

O exemplo a seguir passa parâmetros para uma rotina de tratamento de erros.

```foxpro
ON ERROR DO errhand WITH ERROR(), MESSAGE(), ;
   MESSAGE(1),PROGRAM(),LINENO()
USE nodatabase
ON ERROR         && restores system error-handling routine
PROCEDURE errhand
PARAMETERS gnError, gcMess, gnMess1, gcProg, gnLineNo
? 'Error number: ' + LTRIM(STR(gnError))
? 'Error message: ' + gcMess
? 'Line of code with error: ' + gnMess1
? 'Line number of error: '+ LTRIM(STR(gnLineNo))
? 'Program with error: ' + gcProg
```
