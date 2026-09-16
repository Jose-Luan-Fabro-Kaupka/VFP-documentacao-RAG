# Usando campos de chave primária

O poder de um sistema de gerenciamento de banco de dados relacional como o Visual FoxPro vem da capacidade de localizar rapidamente e reunir informações armazenadas em tabelas separadas. Para que o Visual FoxPro funcione com a máxima eficiência, cada tabela do banco de dados deve incluir um campo ou conjunto de campos que identifique exclusivamente cada registro individual armazenado na tabela. Frequentemente, trata-se de um número de identificação exclusivo, como um número de identificação de funcionário ou um número de série. Na terminologia de banco de dados, essas informações são chamadas de chave primária da tabela. O Visual FoxPro usa campos de chave primária para associar rapidamente dados de várias tabelas e reunir os dados para você.

Se você já possui um identificador exclusivo para uma tabela, como um conjunto de números de produto que você desenvolveu para identificar os itens em estoque, pode usar esse identificador como chave primária da tabela. Mas certifique-se de que os valores nesse campo serão sempre diferentes para cada registro — o Visual FoxPro não permite valores duplicados em um campo de chave primária. Por exemplo, não use o nome de alguém como chave primária, porque nomes não são exclusivos. Você pode facilmente ter duas pessoas com o mesmo nome na mesma tabela.

Ao escolher campos de chave primária, considere estes pontos:
 - O Visual FoxPro não permite valores duplicados ou nulos em um campo de chave primária. Por esse motivo, você não deve escolher uma chave primária que possa conter tais valores.
- Você pode usar o valor no campo de chave primária para localizar registros, portanto ele não deve ser muito longo para lembrar ou digitar. Talvez você queira que tenha um certo número de letras ou dígitos, ou que esteja dentro de um determinado intervalo de valores.
- O tamanho da chave primária afeta a velocidade das operações no banco de dados. Ao criar campos de chave primária, use o menor tamanho que acomode os valores que você precisa armazenar no campo.

# Exemplo

A chave primária da tabela Products da Tasmanian Traders contém números de identificação de produto. Como cada número de produto identifica um produto diferente, você não deseja dois produtos com o mesmo número.
 A chave primária da tabela Products é o campo Product_id.

Em alguns casos, você pode querer usar dois ou mais campos que juntos fornecem a chave primária de uma tabela. Por exemplo, a tabela Order_Line_Items no banco de dados Tasmanian Traders usa dois campos como chave primária: Order_id e Product_id. Para obter mais informações, consulte Identifying Relationships.
