# Função AINSTANCE( )

Coloca instâncias de uma classe em uma matriz de variáveis e retorna o número de instâncias colocadas na matriz.

```foxpro
AINSTANCE(ArrayName, cClassName)
```

#### Parâmetros
 **ArrayName**
Especifica o nome da matriz na qual as instâncias são colocadas. Se a matriz que você especifica não existir, o Visual FoxPro cria a matriz automaticamente. Se a matriz existir e não for grande o suficiente para conter todas as instâncias, o Visual FoxPro aumenta automaticamente o tamanho da matriz para acomodar as instâncias. Se a matriz for maior do que o necessário, o Visual FoxPro trunca a matriz. Se a matriz existir e AINSTANCE( ) retornar 0 porque nenhuma instância foi encontrada, a matriz permanece inalterada. Se a matriz não existir e AINSTANCE( ) retornar 0, a matriz não é criada. Somente instâncias de classe atribuídas a variáveis e elementos de matriz com CREATEOBJECT( ) ou NEWOBJECT( ) são colocadas na matriz.
**cClassName**
Especifica um nome de classe base do Visual FoxPro ou um nome de classe definido pelo usuário. Para uma lista completa das classes base do Visual FoxPro, consulte Base Classes in Visual FoxPro .

# Valor de retorno

Numérico

# Exemplo

No exemplo a seguir, CREATEOBJECT( ) é usado para criar duas instâncias da classe base Form do Visual FoxPro. AINSTANCE( ) é usado para criar uma matriz chamada `gaMyArray` que contém as referências de variável (`goINSTANCE1` e `goINSTANCE2`) para cada instância de formulário. O conteúdo da matriz é então exibido.

```foxpro
CLEAR ALL
goINSTANCE1 = CREATEOBJECT('Form')
goINSTANCE2 = CREATEOBJECT('Form')
CLEAR
? AINSTANCE(gaMyArray, 'Form')  && Returns 2, two form instances
DISPLAY MEMORY LIKE gaMyArray  && Displays the references
```
