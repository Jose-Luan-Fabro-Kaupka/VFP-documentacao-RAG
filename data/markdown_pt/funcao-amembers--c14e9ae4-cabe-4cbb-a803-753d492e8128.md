# Função AMEMBERS( )

Coloca os nomes de propriedades, procedimentos e objetos membros de um objeto em uma matriz de variáveis.

```foxpro
AMEMBERS(ArrayName, oObjectName | cClassName [, nArrayContentsID] [, cFlags])
```

#### Parâmetros
 **ArrayName**
Especifica a matriz na qual os nomes das propriedades membro de oObjectName são colocados. Se você especificar o nome de uma matriz que não existe, a matriz é criada automaticamente. Se a matriz não for grande o suficiente para conter todos os nomes, o Visual FoxPro aumenta automaticamente o tamanho da matriz.
**oObjectName**
Especifica o objeto cujas propriedades membro são colocadas na matriz de variáveis especificada com ArrayName. oObjectName pode ser qualquer expressão que avalie para um objeto, como uma referência de objeto, uma variável de objeto ou um elemento de matriz de objetos.
**cClassName**
Especifica a classe Visual FoxPro cujas propriedades membro são colocadas na matriz de variáveis especificada com ArrayName.
**nArrayContentsID , 0 | 1 | 2 | 3**
Descrição 0 Especifica que a matriz contém uma única coluna de nomes de propriedades. Omitir o parâmetro nArrayContentsID é o mesmo que passar 0. 1 Especifica que a matriz contém os nomes das propriedades do objeto ou classe, bem como os métodos e objetos membros. A matriz resultante é bidimensional, com a segunda coluna especificando que tipo de membro está listado na primeira coluna. Os valores possíveis para a segunda coluna são Property, Event, Method ou Object. 2 Especifica que a matriz contém os nomes de objetos que são membros de um objeto nativo do Visual FoxPro especificado com oObjectName. A matriz resultante é unidimensional. Esta opção fornece um método para determinar os nomes de objetos filhos em um container, como todos os objetos Form em um form set ou controles em um formulário. 3 Especifica que a matriz contém informações sobre um ou mais objetos. Você pode passar uma referência de objeto para um objeto nativo do Visual FoxPro ou para um objeto COM. Observação Um valor de 3 para este parâmetro não é suportado em aplicativos .app ou .exe. A matriz retornada quando você especifica este parâmetro consiste em quatro colunas conforme descrito na tabela a seguir: Coluna Descrição 1 Nome do evento ou método 2 Tipo de propriedade (por exemplo, PROPERTYPUT, PROPERTYGET, PROPERTYPUTREF, METHOD) 3 Assinatura da função (parâmetros e seus tipos, e o tipo de retorno da função). Esta informação é semelhante ao texto Quick Info fornecido na expansão IntelliSense de um método. 4 Cadeia de ajuda Se você omitir nArrayContentsID, AMEMBERS( ) retorna uma matriz de uma coluna de propriedades.
**cFlags**
Especifica a filtragem aplicada à matriz retornada pela função AMEMBERS( ). cFlags não funcionará quando AMEMBERS( ) receber um objeto COM (o valor de ArrayContentsID é 3). Algumas flags são mutuamente exclusivas; portanto, se você usar mais de um cFlag, use-os nos seguintes agrupamentos: [P | H | G] [N | U] [C] [I | B] [R] As tabelas a seguir descrevem os valores válidos para cFlags. Valor Flags de filtro P Propriedades, métodos ou eventos Protected H Propriedades, métodos ou eventos Hidden G Propriedades, métodos ou eventos Public N Propriedades, métodos ou eventos nativos (intrínsecos) U Propriedades, métodos ou eventos definidos pelo usuário (extrínsecos) C Propriedades alteradas (mas não propriedades de matriz alteradas) I Propriedades, métodos ou eventos herdados B Propriedades, métodos ou eventos base (usando o método AddProperty) R Propriedades somente leitura

A configuração padrão para a filtragem especificada por cFlags é OR lógico entre flags. Você pode alterar isso usando o cFlags especial "+".

| Valor | Flags especiais |
| --- | --- |
| # | Adiciona uma nova coluna à matriz de saída com o valor cFlags correspondente. |
| + | Executa AND lógico entre flags de filtro. |

# Valor de retorno

Numérico

# Observações

AMEMBERS( ) retorna o número de objetos, propriedades e procedimentos do objeto, ou 0 se a matriz não puder ser criada. Se você omitir os parâmetros opcionais de flag 1, 2 ou 3, uma matriz unidimensional é criada contendo as propriedades de oObjectName.

Você pode passar referências de objetos COM para a função AMEMBERS( ), mas ao fazer isso, também deve passar um valor de 3 no terceiro parâmetro (flag), como no exemplo a seguir.

```foxpro
oExcel = CREATEOBJECT("excel.application")
= AMEMBERS(gaPropArray, oExcel, 3)
```

# Exemplo

O exemplo a seguir usa CREATEOBJECT( ) para criar um objeto Form chamado `goForm1`. AMEMBERS( ) é usado para criar uma matriz chamada `gaPropArray` contendo as propriedades disponíveis para o formulário; as propriedades são então exibidas.

```foxpro
CLEAR
goForm1 = CREATEOBJECT("Form")  && Creates a Form
= AMEMBERS(gaPropArray, goForm1, 1)  && Array containing Form properties
DISPLAY MEMORY LIKE gaPropArray  && Display the Form properties
```
