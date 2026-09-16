# Passando matrizes para Automation Servers

Versões anteriores do Visual FoxPro passavam matrizes para objetos COM, como servidores Automation criados no Visual FoxPro, Visual Basic ou Visual C++, por valor. Ou seja, os elementos da matriz permaneciam inalterados após uma chamada de método, e as alterações do objeto COM não se propagavam para os elementos no cliente. Esta restrição impedia passar grandes quantidades de dados entre o Visual FoxPro e objetos COM.

Por padrão, uma matriz passada para um objeto COM é assumida como uma matriz baseada em um, significando que o primeiro elemento, linha ou coluna da matriz é referenciado com 1, por exemplo, `MyArray[1]`, e é passada por valor. No entanto, alguns objetos COM exigem que a matriz seja passada como uma matriz baseada em zero, significando que o primeiro elemento, linha ou coluna da matriz é referenciado com 0, por exemplo, `MyArray[0]`, e por referência.

Você pode especificar como passar uma matriz para um Automation server usando a função COMARRAY( ). Para obter mais informações, consulte COMARRAY( ) Function.
