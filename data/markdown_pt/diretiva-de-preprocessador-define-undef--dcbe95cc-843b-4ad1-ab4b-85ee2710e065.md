# Diretiva de preprocessador #DEFINE ... #UNDEF

Cria e libera constantes de tempo de compilação.

Você pode usar as diretivas de preprocessador #DEFINE e #UNDEF para criar constantes de tempo de compilação em programas. Ao criar constantes com #DEFINE em vez de usar variáveis, você pode reduzir o consumo de memória, aumentar o desempenho e simplificar programas.

Para criar uma constante com #DEFINE, especifique o nome da constante com ConstantName e seu valor com eExpression. Quando o programa é compilado, a substituição de texto é executada e a expressão de valor da constante é substituída pelo nome da constante onde quer que apareça no programa. Você pode interromper a substituição da constante emitindo #UNDEF.

```foxpro
#DEFINE ConstantName eExpression...
#UNDEF ConstantName
```

#### Parâmetros
 **ConstantName**
Especifica um nome de constante de tempo de compilação. O nome da constante deve ser um nome Microsoft Visual FoxPro legítimo que comece com uma letra ou sublinhado e consista em até 254 letras, dígitos ou sublinhados. Para melhorar a legibilidade do programa e simplificar a depuração, capitalize os nomes das constantes e use uma convenção de nomenclatura padrão para elas. Cuidado Não use palavras-chave Visual FoxPro para nomes de constantes. Para interromper a substituição de texto de uma constante criada com #DEFINE, emita #UNDEF ConstantName .
**eExpression**
Especifica o valor da constante de tempo de compilação. eExpression pode ser um nome ou uma expressão que avalia para um valor de caractere, numérico, moeda, data, datetime ou lógico. Cuidado Não use variáveis de sistema para eExpression . Variáveis de sistema não são avaliadas até o tempo de execução.

# Observações

O Visual FoxPro executa substituição somente no código que segue a instrução #DEFINE que cria a constante e que precede a instrução #UNDEF dessa constante. A constante está disponível somente para o programa que cria a constante.

Se você colocar #DEFINE dentro de um procedimento de evento ou método em um formulário, a constante de tempo de compilação #DEFINE estará disponível dentro do procedimento de evento ou método. Além disso, ela também pode estar disponível em outros eventos ou métodos, já que esses trechos de código são todos gravados juntos no mesmo campo Memo dentro do arquivo de formulário ou biblioteca de classes. Você não deve depender desse comportamento, pois a ordem em que os métodos são gravados pode mudar em uma gravação subsequente. Para tornar as constantes de tempo de compilação #DEFINE disponíveis a todos os procedimentos de evento e método em um formulário ou classe, escolha o item de menu Include File no menu Form (ou Class) e especifique um arquivo de cabeçalho contendo as constantes de tempo de compilação #DEFINE.

> **Observação:** Constantes de tempo de compilação não são reconhecidas quando colocadas entre aspas.

Você pode redefinir um #DEFINE somente se não alterar o valor. Se você alterar o #DEFINE para um valor diferente, o Visual FoxPro gera um erro.

# Exemplo

O programa a seguir cria uma constante de tempo de compilação chamada `MAXITEMS`. Esta constante é usada em um loop FOR ... NEXT para exibir os números de 1 a 10.

```foxpro
#DEFINE MAXITEMS 10
CLEAR
FOR gnCount = 1 TO MAXITEMS
   ? gnCount
NEXT
```
