# Dados XML no Visual FoxPro

Você pode trabalhar com dados XML no Visual FoxPro importando ou exportando documentos XML usando as funções do Visual FoxPro ou objetos XMLAdapter. As seções a seguir apresentam documentos XML válidos, ou "bem formados", e esquemas XML, que ajudam a explicar os requisitos para trabalhar com dados XML no Visual FoxPro:
 - Documentos XML bem formados
- Suporte a esquemas XML

# Documentos XML bem formados

Documentos XML são válidos quando são "bem formados". O Visual FoxPro produz documentos XML que são bem formados. Um documento bem formado está em conformidade com as regras básicas do XML:
 - Cada documento XML deve ter um elemento raiz exclusivo, que é um elemento que abrange todo o documento.
- Todas as tags de início e fim correspondem. As tags XML diferenciam maiúsculas de minúsculas.
- Para cada tag de início, existe uma tag de fim correspondente. Uma tag abreviada especial pode denotar elementos vazios.
- Os elementos não se sobrepõem. Em outras palavras, as tags de início e fim devem estar adequadamente aninhadas dentro de outros elementos.
- Certos caracteres reservados fazem parte da sintaxe XML e não são interpretados como são se usados na porção de dados de um elemento. A tabela a seguir lista sequências de caracteres especiais, ou entidades, usadas para substituir esses caracteres reservados. Caractere Tipo de dados Codificação de entidade & (e comercial) < (sinal de menor) > (sinal de maior) " (aspas) ' (apóstrofo) String String String String String Substituir por & Substituir por < Substituir por > Substituir por " Substituir por ' Para outros tipos de dados, a tabela a seguir lista regras para codificação de entidades. Tipo de dados Caractere e codificação de entidade Data Deve seguir o formato ISO 8601 Números A pontuação deve usar regras do inglês dos EUA. Por exemplo, você deve usar um ponto como separador decimal. Números podem incluir expoentes. Boolean False = 0, True = 1. (SQL XML retorna 0 e 1) BLOB Use codificação MIME Base64

O exemplo a seguir mostra um documento XML bem formado:

```foxpro
<?xml version="1.0"?>
<Data>
<ORDER>
 <CUSTOMER>Mary Baker</CUSTOMER>
  <ITEM>Coho Winery's Chablis</ITEM>
 <PRICE>$10.00</PRICE>
 <QUANTITY>1 Bottle</QUANTITY>
 </ORDER>
</Data>
```

> **Dica:** Você pode usar espaço em branco em todo o documento para melhorar a legibilidade.

No exemplo, o código ilustra certas partes do documento XML:
 - <?xml version="1.0"?> Declara o documento XML e fornece o número da versão. Esta declaração é opcional, mas recomendada em qualquer documento XML.
- <ORDER> Especifica o elemento raiz que abrange todo o documento.
- <CUSTOMER> ... </CUSTOMER> Especifica um conjunto de tags de início e fim, que descreve um elemento de dados, neste caso, o nome do cliente. Observação Cada conjunto de tags tem tags de início e fim, diferencia maiúsculas de minúsculas e está adequadamente aninhado. Quando os dados são importados pelo aplicativo receptor, a entidade &apos é transformada em um apóstrofo ('). O apóstrofo tem um propósito especial em um documento XML e pode ser mal interpretado se usado diretamente no texto. Os dados convertidos são exibidos como Coho Winery's Chablis .

# Suporte a esquemas XML

Esquemas XML podem ajudar a definir as regras e a estrutura para documentos XML. O Visual FoxPro pode interpretar arquivos XML com ou sem esquemas. No entanto, o Visual FoxPro oferece suporte a XML Schema Definition (XSD), que é uma infraestrutura básica para descrever o tipo e a estrutura de documentos XML. Uma definição de esquema XML serve a vários propósitos:
 - Descreve a estrutura dos dados em um formato comum que clientes, outros navegadores Web e qualquer número de programas de software habilitados para XML podem reconhecer.
- Define as regras de um documento de dados XML, incluindo nomes de elementos e tipos de dados, quais elementos podem aparecer em combinação e quais atributos estão disponíveis para cada elemento.
- Fornece um modelo para um documento de dados XML definindo a disposição de tags e texto em todos os documentos que referenciam o esquema.

Ao usar um esquema XML, você pode garantir que qualquer documento XML usado para importar ou exportar dados contenha dados específicos e esteja em conformidade com uma estrutura definida. Quando você especifica um esquema ao exportar XML do Visual FoxPro, os documentos XML exportados são considerados XML válido. Isso significa que, além de serem bem formados, os documentos estão em conformidade com um esquema definido. Você também pode fornecer um esquema a outras empresas e aplicativos para que possam estruturar os dados XML que fornecem a você, bem como fornecer seu esquema a você.

Em particular, o Visual FoxPro oferece suporte ao formato de esquema XSD do W3C. O formato de esquema XSD é baseado na Recomendação do W3C da especificação XSD Schema. Para obter mais informações, consulte http://www.w3.org/TR/2001/REC-xmlschema-0-20010502/ e documentos relacionados.
