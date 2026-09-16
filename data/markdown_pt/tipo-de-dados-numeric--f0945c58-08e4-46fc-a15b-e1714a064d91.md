# Tipo de dados Numeric

Para indicar magnitude, use o tipo de dados Numeric. Valores numéricos contêm dígitos de 0 a 9 e, opcionalmente, um sinal e um ponto decimal. O Visual FoxPro suporta valores hexadecimais para dados numéricos. Por exemplo, o valor decimal 255 pode ser representado como 0xFF.

> **Dica:** Para cálculos financeiros precisos, use o tipo de dados Currency em vez de Numeric. Você pode converter valores de Numeric para Currency e vice-versa usando as funções NTOM( ) e MTON( ). Para obter mais informações, consulte Currency Data Type, NTOM( ) Function e MTON( ) Function.

Em campos com tipo de dados Numeric, o comprimento da porção decimal é determinado no momento do design, quando você cria o campo. O comprimento da porção decimal faz parte do comprimento total. Por exemplo, se você especificar um comprimento de 6 para um campo numérico e uma configuração decimal de 4, o campo pode armazenar valores até 9.9999.

Para especificações sobre o tipo de dados Numeric, consulte Visual FoxPro Data and Field Types.

# Precisão numérica

Ao armazenar números de ponto flutuante em campos Numeric, a precisão numérica é limitada a aproximadamente 15 dígitos no Visual FoxPro. Portanto, precisão superior a 15 dígitos pode ser perdida ao converter de números decimais para binários, armazenar números com valores decimais infinitamente repetitivos em binário, executar múltiplas operações repetidas e armazenar valores numéricos em campos Character e em variáveis de memória em formato binário.

Essa limitação baseia-se na forma como processadores baseados em Pentium calculam e armazenam números de ponto flutuante e segue a especificação de ponto flutuante do Institute of Electrical and Electronics Engineers (IEEE) para manipular números de ponto flutuante em formato binário. Esse padrão torna possível que números de ponto flutuante sejam armazenados em uma quantidade razoável de espaço e que cálculos sejam executados mais rapidamente.

Por exemplo, a fração 1/10 pode ser representada como um valor decimal de 0.1. No entanto, ao armazenar 1/10 em binário, o valor decimal não é o mesmo que a fração. Em vez disso, a fração é um decimal binário repetitivo de 0001100110011100110011 e assim por diante. Esse tipo de número não pode ser representado em memória que é finita ou limitada; portanto, o valor decimal é arredondado quando armazenado em binário.

Para valores que exigem maior precisão, consulte Double Field Type.

Para obter mais detalhes sobre como números de ponto flutuante são armazenados e como processadores baseados em Pentium lidam com seu cálculo, consulte o artigo da Microsoft Knowledge Base Q78113, "XL: Floating-Point Arithmetic May Give Inaccurate Results" na MSDN Library em http://msdn.microsoft.com/library/.

O exemplo a seguir ilustra o limite de precisão numérica para números de ponto flutuante para tipos de dados Numeric:

```foxpro
x=1234567890.0987654321
? x
```

O resultado é 1234567890.0987650000.
