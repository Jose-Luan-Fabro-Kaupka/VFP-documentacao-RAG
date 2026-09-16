# Páginas de código no Visual FoxPro

Dados armazenados no Visual FoxPro geralmente são marcados com uma página de código, que é uma tabela de caracteres e números correspondentes na memória que o Windows usa para exibir dados corretamente. Por exemplo, se você digitar a letra C em um arquivo de tabela (.dbf), a letra é armazenada no disco rígido como o número 67. Quando você abre o arquivo, o Visual FoxPro determina sua página de código, inspeciona a página de código para encontrar o caractere correspondente ao número 67 e, em seguida, exibe o caractere (C) no monitor.

As páginas de código correspondem aproximadamente a alfabetos diferentes. Por exemplo, o Windows fornece páginas de código para inglês, alemão, idiomas escandinavos e assim por diante. Ao usar páginas de código diferentes, os aplicativos podem exibir corretamente caracteres desses alfabetos diferentes.

# Nesta seção
 **Understanding Code Pages in Visual FoxPro**
Descreve como o Visual FoxPro usa páginas de código para exibir dados. As páginas de código fornecem um conjunto de caracteres específico para um idioma ou plataforma de hardware.
**Code Pages Supported by Visual FoxPro**
Fornece uma lista de páginas de código suportadas pelo Visual FoxPro.
**How to: Specify the Code Page of a .dbf File**
Explica como adicionar, remover e alterar marcas de página de código para um arquivo .dbf.
**How to: Specify the Code Page of a Text File**
Explica como especificar uma página de código para uso com um arquivo de texto.
**How to: Determine the Code Page of a Project File**
Descreve como determinar qual página de código um arquivo em um projeto usa.
**Specification of Code Pages for Variables**
Explica como usar dados armazenados com uma página de código e traduzi-los para outra página de código.
**How to: Prevent Translation of Data in Character or Memo Fields**
Descreve como interromper a tradução automática de página de código. Interromper a tradução automática é ideal quando você pode não querer que os dados sejam traduzidos para outra página de código, porque isso alteraria os dados.

# Seções relacionadas
 **Developing International Applications**
Descreve como desenvolver e planejar aplicativos Visual FoxPro compatíveis e eficazes em mercados internacionais.
**Creating International Applications**
Descreve como criar aplicativos Visual FoxPro compatíveis e eficazes em mercados internacionais.
