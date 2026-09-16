# Comando PRIVATE

Oculta variáveis ou arrays especificados que foram definidos em um programa chamador do programa atual. Há duas versões da sintaxe.

```foxpro
PRIVATE VarList
```

```foxpro
PRIVATE ALL[LIKE Skeleton | EXCEPT Skeleton]
```

#### Parâmetros
 **VarList**
Especifica as variáveis ou arrays a serem declarados privados. As letras simples A a J e M são reservadas e não podem ser usadas como nomes de variáveis.
**ALL LIKE Skeleton**
Faz com que PRIVATE oculte todas as variáveis e arrays cujos nomes correspondem a Skeleton, que pode conter os curingas ponto de interrogação (?) e asterisco (*).
**ALL EXCEPT Skeleton**
Faz com que PRIVATE oculte todas as variáveis ou arrays, exceto se seus nomes corresponderem a Skeleton, que pode conter os curingas ponto de interrogação (?) e asterisco (*).

# Observações

Os itens em VarList são separados por vírgulas. A ocultação de variáveis criadas em programas de nível superior permite que variáveis com o mesmo nome das variáveis privadas sejam manipuladas no programa atual sem afetar os valores das variáveis ocultas. Quando o programa que contém PRIVATE conclui a execução, todas as variáveis e arrays que foram declarados privados ficam novamente disponíveis.

PRIVATE não cria variáveis; simplesmente oculta variáveis declaradas em programas de nível superior do programa atual.

# Exemplo

```foxpro
*** Program example demonstrating PRIVATE ***
SET TALK OFF
val1 = 10
val2 = 15
DO down
? val1, val2  && Displays 10, 100
PROCEDURE down
PRIVATE val1
val1 = 50
val2 = 100
? '   Val1   Val2'
? val1, val2  && Displays 50, 100
RETURN
```
