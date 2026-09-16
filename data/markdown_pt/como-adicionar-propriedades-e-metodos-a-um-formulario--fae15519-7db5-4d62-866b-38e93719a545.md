# Como: adicionar propriedades e métodos a um formulário

Você pode adicionar quantas novas propriedades e métodos quiser a um form set ou a um formulário que não faz parte de um form set. Propriedades armazenam um valor; métodos armazenam código procedural a ser executado quando você chama o método. As novas propriedades e métodos têm escopo no formulário e você os referencia da mesma forma que referencia outras propriedades ou métodos do formulário.

# Criando novas propriedades

Se você tiver um form set, propriedades e métodos que adicionar no Form Designer têm escopo no form set. Se você não tiver um form set, as propriedades e métodos têm escopo no formulário.

### Para adicionar uma nova propriedade a um formulário
- No menu Form, escolha New Property.
- Na caixa de diálogo New Property Dialog Box, digite o nome da propriedade. Você também pode incluir uma descrição da propriedade que pode ser exibida na parte inferior da janela Properties.

# Criando uma propriedade de matriz

Uma propriedade de matriz tem escopo no formulário como qualquer outra propriedade, mas pode ser manipulada com os comandos e funções de matriz do Visual FoxPro.

### Para criar uma propriedade de matriz
- Adicione uma nova propriedade ao formulário.
- Na caixa Name da caixa de diálogo New Property Dialog Box, digite o nome da propriedade de matriz e inclua o tamanho e as dimensões da matriz. Por exemplo, para criar uma matriz bidimensional com 10 linhas, você poderia digitar arrayprop[10,2] na caixa Name da caixa de diálogo New Property.

Propriedades de matriz são somente leitura em modo de design, mas você pode gerenciar, redimensionar e atribuir valores aos elementos da propriedade de matriz em tempo de execução. Para um exemplo de uso de uma propriedade de matriz, consulte Como: gerenciar múltiplas instâncias de um formulário.

# Criando novos métodos

Você pode adicionar métodos ao formulário que podem ser chamados da mesma forma que os métodos da classe de formulário podem ser chamados.

### Para criar um novo método para um formulário
- No menu Form, escolha New Method.
- Na caixa de diálogo New Method Dialog Box, digite o nome do método. Você pode opcionalmente incluir uma descrição do método.

Você chama um método definido pelo usuário da mesma forma que chama métodos de classe base, usando a seguinte sintaxe:

```foxpro
        ObjectName.MethodName
```

Seu método também pode aceitar parâmetros e retornar valores. Neste caso, você chama o método em uma instrução de atribuição:

```foxpro
        cVariable = ObjectName.MethodName(cParameter, nParameter)
```

# Incluindo constantes predefinidas

Para usar constantes predefinidas em seus métodos ou eventos (não em propriedades), você pode incluir um arquivo de cabeçalho em um formulário ou form set usando a Diretiva de pré-processador #INCLUDE. Um arquivo de cabeçalho tipicamente contém constantes de tempo de compilação definidas com a diretiva de pré-processador #DEFINE ... #UNDEF.

### Para incluir um arquivo em um formulário
- No menu Form, escolha Include File.
- Na caixa de diálogo Include File Dialog Box, especifique o arquivo na caixa de texto Include File. -ou- Escolha o botão de diálogo para abrir a caixa de diálogo Include e escolha o arquivo.
- Escolha OK.
