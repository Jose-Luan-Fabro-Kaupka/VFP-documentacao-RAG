# Comando LOCAL

Cria variáveis locais e matrizes de variáveis. Há duas versões da sintaxe.

```foxpro
LOCAL Var1 [ AS type [ OF ClassLib ] ] | [ ArrayName1( nRows1 [, nColumns1 ] ) [ AS type [ OF ClassLib ] ] ]
    [, Var2 [ AS type [ OF ClassLib ] ] | [, ArrayName2( nRows2 [, nColumns2 ] ) [ AS type [ OF ClassLib ] ] ]
```

```foxpro
LOCAL [ ARRAY ] ArrayName1( nRows1 [, nColumns1 ] ) [ AS type [OF ClassLib ] ]
    [, ArrayName2( nRows2 [, nColumns2 ] ) [ AS type [ OF ClassLib ] ] ]
```

#### Parâmetros
 **LOCAL VarList**
Especifica uma ou mais variáveis locais a criar. Use vírgulas para separar vários itens em VarList . As letras simples de A a J e M são reservadas e não podem ser usadas como nomes de variáveis.
**[ ARRAY ] ArrayName1 ( nRows1 [, nColumns1 ] ) [, ArrayName2 ( nRows2 [, nColumns2 ] ) ] ...**
Especifica uma ou mais matrizes locais a criar. Para mais informações sobre matrizes, consulte o comando DIMENSION .
**[ AS type [ OF ClassLib ] ]**
Especifica o tipo de dados da variável ou matriz e a biblioteca de classes que contém a descrição de tipo de type na qual esta variável ou matriz se baseia. Quando você especifica um nome de classe válido, o Visual FoxPro usa a biblioteca de tipos, se você especificar uma Propriedade ProgID (Visual FoxPro) , ou instancia um objeto para obter uma lista de propriedades, métodos e eventos. Se o nome de classe especificado não for encontrado, o Visual FoxPro exibe uma caixa de listagem de classes disponíveis. Você pode usar a cláusula AS para implementar tipagem forte. A funcionalidade IntelliSense está disponível para referências de objetos e variáveis somente quando são fortemente tipadas. Para mais informações, consulte Como: implementar tipagem forte para código de classes, objetos e variáveis .

# Observações

Você pode usar e modificar variáveis locais e matrizes de variáveis somente no procedimento ou função em que foram criadas e não podem ser acessadas por programas de nível superior ou inferior. Após a conclusão da execução do procedimento ou função que contém as variáveis e matrizes locais, elas são liberadas.

Variáveis e matrizes criadas com LOCAL são inicializadas como False (.F.).

Você deve declarar quaisquer variáveis ou matrizes que deseja locais antes de atribuir valores a elas. Se você atribuir um valor a uma variável ou matriz em um programa e depois declará-la como local usando LOCAL, o Visual FoxPro gera um erro de sintaxe.

Você pode passar variáveis locais por referência.

Você não pode abreviar LOCAL porque LOCAL e LOCATE têm as mesmas quatro primeiras letras.
