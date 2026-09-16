# Otimizando tabelas e índices

Você pode acelerar o acesso a dados em tabelas usando índices e usando buffering de forma eficiente. Além disso, você pode usar a tecnologia Rushmore Query Optimization para otimizar suas consultas.

# Usando índices

Para acelerar o acesso a dados em uma tabela, use um índice. Adicionar um índice a uma tabela acelera pesquisas, especialmente se você puder usar a tecnologia Rushmore para otimizar sua pesquisa. A indexação também permite trabalhar com dados em uma ordem específica, como visualizar uma tabela de clientes em ordem por sobrenome.

Se os registros em uma tabela têm chaves exclusivas, crie um índice primário ou candidato no campo. Esses tipos de índice permitem que o Visual FoxPro valide a chave em um nível baixo, resultando no melhor desempenho.

Além de indexar campos usados para pesquisa e classificação, você também deve indexar quaisquer campos envolvidos em um join. Se você unir duas tabelas em campos que não estão indexados, a operação de join pode levar centenas de vezes mais tempo.

Um recurso importante do Visual FoxPro é que você pode criar um índice em qualquer expressão. (Em alguns produtos de banco de dados, você só pode indexar campos.) Essa capacidade permite usar índices para otimizar pesquisa, classificação ou join em combinações de campos, ou em expressões derivadas de campos. Por exemplo, você pode indexar um campo de nome baseado em uma expressão que usa a função SOUNDEX( ). Dessa forma, sua aplicação pode fornecer acesso extremamente rápido a nomes que soam parecidos.

Ao adicionar índices às suas tabelas, você deve equilibrar o benefício obtido nos tempos de recuperação com a perda de desempenho ao atualizar a tabela. À medida que você adiciona mais índices à sua tabela, atualizações e inserções na tabela ficam mais lentas porque o Visual FoxPro precisa atualizar cada índice.

Por fim, evite usar índices em campos que contêm apenas alguns valores discretos, como um campo lógico. Nesses casos, o índice contém apenas um pequeno número de entradas, e a sobrecarga de manter o índice provavelmente supera o benefício que ele fornece na pesquisa.

Para detalhes sobre como indexar de forma eficaz ao usar a tecnologia Rushmore, consulte Using Rushmore Query Optimization to Speed Data Access.

# Otimizando joins

Quando você cria joins usando o comando SELECT - SQL, as seguintes situações podem degradar o desempenho e produzir resultados inesperados:
 - Unir tabelas em dados que não são chave primária ou exclusiva em uma das tabelas.
- Unir tabelas contendo campos vazios.

Para evitar essas situações, crie joins baseados na relação entre chaves primárias em uma tabela e chaves estrangeiras na outra. Se você criar um join baseado em dados que não são exclusivos, o resultado final pode ser o produto de duas tabelas. Por exemplo, a seguinte instrução SELECT - SQL cria um join, que pode produzir um resultado muito grande:

```foxpro
SELECT *;
 FROM  tastrade!customer INNER JOIN tastrade!orders ;
 ON  Customer.postal_code = Orders.postal_code
```

No exemplo, o código postal identifica exclusivamente uma localização dentro de uma cidade, mas tem pouco valor se sua intenção é corresponder linhas de cliente e suas linhas de pedido. O código postal não identifica necessariamente exclusivamente um cliente ou um pedido. Em vez disso, crie um join usando uma instrução como a seguinte:

```foxpro
SELECT *;
 FROM  tastrade!customer INNER JOIN tastrade!orders ;
 ON  Customer.customer_id = Orders.customer_id
```

Neste exemplo, o campo `customer_id` identifica exclusivamente um cliente específico e os pedidos pertencentes a esse cliente e, portanto, cria um conjunto de resultados que combina a linha do cliente com cada linha de pedido.

Além disso, use cautela ao unir tabelas com campos vazios porque o Visual FoxPro corresponderá campos vazios. No entanto, o Visual FoxPro não corresponde campos contendo null. Ao criar um join, qualifique as expressões de campo na condição de join testando uma cadeia de caracteres vazia.

Por exemplo, se você acha que o campo customer id na tabela Orders pode estar vazio, use uma instrução como a seguinte para filtrar registros de pedido sem número de cliente:

```foxpro
SELECT *;
 FROM  tastrade!customer INNER JOIN tastrade!orders ;
 ON  Customer.customer_id = Orders.customer_id;
 WHERE tastrade!orders <> ""
```

> **Dica:** Você também pode testar uma cadeia de caracteres vazia usando a função EMPTY( ), mas incluir uma chamada de função na expressão de filtro não é tão rápido quanto comparar com um valor constante.

# Usando o Project Manager

Quando você usa o Project Manager, pode combinar um número ilimitado de programas e procedimentos em um único arquivo .app ou .exe. Isso pode aumentar muito a velocidade de execução do programa por alguns motivos.

Primeiro, o Visual FoxPro abre um arquivo de programa e o mantém aberto. Depois, quando você emite um comando DO em um programa contido no arquivo, o Visual FoxPro não precisa abrir um arquivo adicional.

Segundo, uma aplicação de apenas um ou dois arquivos reduz o número de arquivos necessários no diretório de trabalho. A velocidade de todas as operações de arquivo aumenta à medida que o sistema operacional tem menos entradas de diretório para examinar ao abrir, renomear ou excluir arquivos.

Para informações sobre como usar o Project Manager para criar aplicações, consulte Compiling an Application.

# Dicas gerais de otimização de tabelas e índices

Para criar as tabelas e índices mais rápidos possíveis, siga as recomendações listadas abaixo.
 - Se o buffering de registro ou tabela não estiver habilitado, use INSERT - SQL em vez de APPEND BLANK seguido de REPLACE, particularmente com uma tabela indexada em um ambiente multiusuário, porque os índices só precisam ser atualizados uma vez.
- Se você precisar anexar um grande número de registros a uma tabela indexada, pode ser mais rápido remover o índice, anexar os registros e depois recriar o índice.
- Em instruções SQL, evite chamadas de função se possível, especialmente em instruções que retornarão mais de um registro, porque a instrução deve ser reavaliada (e as funções chamadas novamente) para cada registro. Se você estiver criando uma instrução SQL com dados variáveis, use expressões de nome ou substituição de macro em vez da função EVALUATE( ). Uma estratégia melhor ainda é construir a instrução inteira dinamicamente, não apenas cláusulas individuais. Para mais informações, consulte Using Macros and Creating Name Expressions.
- Se você geralmente usa uma determinada ordem de índice, pode melhorar o desempenho classificando periodicamente a tabela nessa ordem.
- Use arquivos .cdx em vez de .idx em ambientes multiusuários porque você pode atualizar um arquivo .cdx mais rapidamente do que pode atualizar vários arquivos .idx.
