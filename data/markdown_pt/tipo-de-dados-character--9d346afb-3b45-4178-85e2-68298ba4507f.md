# Tipo de dados Character

Para armazenar texto alfanumérico, como letras, números, espaços, símbolos e pontuação, use o tipo de dados Character. Para impedir que dados em campos Character sejam traduzidos entre páginas de código, use o tipo de campo Character (Binary).

> **Dica:** Para criar um campo Character (Binary), use a opção NOCPTRANS nos comandos SQL CREATE TABLE e CREATE CURSOR ou selecione-a na guia Fields no Table Designer.

Campos ou variáveis Character e campos Character (Binary) podem armazenar informações de texto que não são usadas em cálculos matemáticos, como nomes, endereços e números. Por exemplo, números de telefone ou códigos postais, embora incluam principalmente números, na verdade são melhor armazenados como valores de caractere.

Se o valor armazenado em um campo Character for menor que a largura do campo, o Visual FoxPro insere espaçamento adicional no lado direito do valor no campo até a largura máxima do campo. Espaços à direita são truncados. Para armazenar texto alfanumérico em campos sem preenchimento adicional ou truncamento de espaços à direita, use o tipo de campo Varchar em vez disso. Campos com tipo Varchar e Varchar (Binary) têm prioridade sobre o tipo Character em operações UNION e concatenação. Para obter mais informações, consulte Tipo de campo Varchar e Considerações para instruções SQL SELECT.

Para especificações sobre o tipo de dados Character e o tipo de campo Character (Binary), consulte Tipos de dados e campos do Visual FoxPro.
