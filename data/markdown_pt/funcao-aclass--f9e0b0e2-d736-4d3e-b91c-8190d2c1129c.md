# Função ACLASS( )

Coloca o nome da classe de um objeto e os nomes de suas classes ancestrais em uma matriz de variáveis.

```foxpro
ACLASS(ArrayName, oExpression)
```

#### Parâmetros
 **ArrayName**
Especifica o nome da matriz na qual os nomes de classe são colocados. Se você especificar o nome de uma matriz que não existe, o Microsoft Visual FoxPro cria automaticamente a matriz. Se você especificar o nome de uma matriz existente que não é grande o suficiente para conter todos os nomes de pai, o Visual FoxPro aumenta automaticamente o tamanho da matriz. Se a matriz for maior do que o necessário, o tamanho da matriz é truncado. Se você especificar o nome de uma matriz bidimensional existente, a matriz é redimensionada para uma matriz unidimensional.
**oExpression**
Especifica um objeto cujo nome de classe e nomes de classes ancestrais são colocados na matriz. oExpression pode ser qualquer expressão de objeto, como uma referência de objeto, uma variável de objeto ou um elemento de matriz de objetos.

# Valor de retorno

Numeric

# Observações

ACLASS( ) cria uma matriz unidimensional contendo o nome da classe do objeto especificado e os nomes de suas classes ancestrais. O primeiro elemento da matriz contém o nome da classe do objeto, o segundo elemento contém o nome da classe pai do objeto, o terceiro elemento contém o nome da classe avô do objeto, e assim por diante.

ACLASS( ) retorna o número de nomes de classe na matriz. ACLASS( ) retorna 0 se a matriz não puder ser criada.

# Exemplo

O exemplo a seguir cria duas classes personalizadas chamadas FormChild e FormGrandChild a partir da classe base Form do Visual FoxPro. ACLASS( ) é usada para criar uma matriz chamada `gaNewarray` contendo os nomes de classe, que são então exibidos.

```foxpro
CLEAR
frmMyForm = CREATEOBJECT("FormGrandChild")
FOR nCount = 1 TO ACLASS(gaNewarray, frmMyForm)    && Creates an array
   ? gaNewarray(nCount)  && Displays the names of the classes
ENDFOR
RELEASE frmMyForm
DEFINE CLASS FormChild AS FORM
ENDDEFINE
DEFINE CLASS FormGrandChild AS FormChild
ENDDEFINE
```
