# Função ACOPY( )

Copia elementos de um array para outro array.

```foxpro
ACOPY(SourceArrayName, DestinationArrayName
[, nFirstSourceElement [, nNumberElements [, nFirstDestElement ]]])
```

#### Parâmetros
 **SourceArrayName , DestinationArrayName**
Especifica o array de origem SourceArrayName do qual os elementos são copiados um a um para o array de destino DestinationArrayName . Os elementos no array de origem substituem os elementos no array de destino. Os arrays podem ser unidimensionais ou bidimensionais. Se o array de destino não existir, o Visual FoxPro cria automaticamente. Nesse caso, o tamanho do array de destino será o mesmo do array de origem. Observação Você pode referenciar um elemento em um array variável bidimensional de duas maneiras: A primeira usa dois subscritos para especificar a posição de linha e coluna do elemento no array; a outra usa um número de elemento único. Esta função e outras que manipulam arrays bidimensionais requerem números de elemento únicos (aqui, nFirstSourceElement e nFirstDestElement ). Use AELEMENT( ) para retornar o número de elemento apropriado para um array bidimensional a partir de seus subscritos de linha e coluna.
**nFirstSourceElement**
Especifica o número do primeiro elemento no array de origem a ser copiado; inclusivo (o número do elemento nFirstSourceElement é incluído na cópia). Se nFirstSourceElement não for incluído, a cópia começa com o primeiro elemento no array de origem.
**nNumberElements**
Especifica o número de elementos copiados do array de origem. Se nNumberElements for –1, todos os elementos do array de origem começando com o elemento nFirstSourceElement são copiados.
**nFirstDestElement**
Especifica o primeiro elemento no array de destino a ser substituído.

# Valor de retorno

Numérico. ACOPY( ) retorna o número de elementos copiados para o array de destino.

# Observações

Copiar um array de membro para um array não membro existente com certas dimensões usando a função ACOPY( ) pode gerar o erro "Subscript is outside defined range." Você pode evitar esse erro alterando a dimensão do array de destino para um único elemento antes de chamar ACOPY( ). Para obter mais informações, consulte Comando DIMENSION.

# Exemplo

O exemplo a seguir cria um array a partir de registros selecionados na tabela `customer` e depois usa ACOPY( ) para criar um novo array.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'data\testdata')
USE customer     && Open customer table
SELECT DISTINCT company ;
   FROM customer ;
   ORDER BY company ;
   WHERE country = 'Germany';
   INTO ARRAY gaCompanies
= ACOPY(gaCompanies, gaCompaniesTemp)  && Make a copy of the array
CLEAR
DISPLAY MEMORY LIKE gaCompaniesTemp
```
