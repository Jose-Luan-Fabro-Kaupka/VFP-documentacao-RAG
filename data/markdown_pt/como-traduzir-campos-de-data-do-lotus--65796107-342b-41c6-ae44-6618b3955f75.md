# Como: traduzir campos de data do Lotus

Se os campos de data do Lotus foram importados incorretamente, você pode traduzi-los adicionando a data juliana para 1 de janeiro de 1900 (o valor 2415019) ao valor de data no campo.

### Para traduzir campos de data do Lotus
- Importe a planilha para uma tabela do Visual FoxPro.
- Use o Table Designer (Visual FoxPro) para modificar a tabela e adicionar um novo campo de data à tabela.
- Se a data foi importada como um valor numérico, use o comando REPLACE e a função CTOD( ) para copiar a data para o novo campo: REPLACE ALL NewDateField ; WITH CTOD(SYS(10,OldDateField+2415019)) -ou- Se a data foi importada como um valor de caractere, use o seguinte comando para copiar a data para o novo campo: REPLACE ALL NewField ; WITH CTOD(SYS(10,VAL(OldField)+2415019))
- Na tabela, exclua o campo de data original incorreto.
