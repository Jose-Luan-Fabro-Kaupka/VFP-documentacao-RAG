# Função ASORT( )

Classifica elementos em uma matriz em ordem crescente ou decrescente.

```foxpro
ASORT(ArrayName [, nStartElement [, nNumberSorted [, nSortOrder [, nFlags]]])
```

#### Parâmetros
 **ArrayName**
Especifica o nome da matriz a ser classificada.
**nStartElement**
Especifica o elemento inicial da classificação. Se você omitir nStartElement , a matriz é classificada a partir do primeiro elemento da matriz por padrão. If the array is one-dimensional, the sort includes nStartElement . If the array is two-dimensional, the starting element nStartElement determines both the row where the sort begins and the column that determines the sort order of the rows. Note You can refer to an element in a two-dimensional array in one of two ways. The first method uses two subscripts to specify the row and column position of the element in the array; the other method uses an element number. This function and others that manipulate two-dimensional arrays require element numbers (in ASORT() the numeric expressions nStartElement and nNumberSorted ). You can use AELEMENT( ) to return the element number from row and column subscripts in a two-dimensional array. The following example illustrates that the starting element nStartElement determines how the rows in a two-dimensional array are sorted. A small array named gaArray is created and sorted twice. The first sort begins with the first element of gaArray ; the rows are sorted based on the values contained in the first column of the array. The second sort begins with the fourth element of gaArray ; the rows are sorted based on the values contained in the second column. The first sort begins with the first row. The second sort begins with the second row. You can use DISPLAY MEMORY to display the contents of the array; in these examples tables are used to graphically display the results of the sorts. These commands create the array named gaArray : DIMENSION gaArray(3,2) gaArray(1) = 'G' gaArray(2) = 'A' gaArray(3) = 'C' gaArray(4) = 'Z' gaArray(5) = 'B' gaArray(6) = 'N' gaArray looks like this: Column 1 Column 2 Row 1 G A Row 2 C Z Row 3 B N The array is then sorted by ASORT( ) starting with the first element (1,1) in the array. The elements in the first column are placed in ascending order by rearranging the rows of the array. =ASORT(gaArray,1) Note the new order of the rows: Column 1 Column 2 Row 1 B N Row 2 C Z Row 3 G A The array is then sorted starting with the fourth element (2,2) in the array. The elements in the second column are placed in order by rearranging the array rows. =ASORT(gaArray,4) Note the difference in the order of the rows: Column 1 Column 2 Row 1 B N Row 2 G A Row 3 C Z
**nNumberSorted**
Especifica o número de elementos classificados em uma matriz unidimensional ou o número de linhas classificadas em uma matriz bidimensional. For example, if the array is one-dimensional and nStartElement is 2, indicating that the sort starts with the second array element, and nNumberSorted is 3, indicating that the sort should include three elements, the second, third and fourth array elements are sorted. If nNumberSorted is –1 or is omitted, all array elements from the starting element nStartElement through the last element in the array are sorted. If the array is two-dimensional, nNumberSorted designates the number of rows to sort, beginning with the row containing the starting element nStartElement . For example, if nStartElement is 2 and nNumberSorted is 3, the row containing the second array element and the following two rows are sorted. If nNumberSorted is –1 or is omitted, all array rows beginning with the row containing the starting element nStartElement through the last array row are sorted.
**nSortOrder**
Especifica a ordem de classificação (crescente ou decrescente) para os elementos na matriz. Por padrão, os elementos da matriz são classificados em ordem crescente. If nSortOrder is 0 or is omitted, the array elements are sorted in ascending order. If nSortOrder is any positive value, the array elements are sorted in descending order.
**nFlags**
Especifica critérios de pesquisa que diferenciam maiúsculas de minúsculas a serem aplicados à função de classificação. Valid values are 0 (the default) and 1. ASORT( ) uses the current collate sequence (see SET COLLATE Command ) to determine the sort order. Certain collate sequences (such as "GENERAL") are not case-sensitive, and specifying nFlags = 0 will not cause a case-sensitive sorting. The nFlags parameter is only useful when the current collate sequence is case-sensitive (such as "MACHINE"), and you wish to do a non-case-sensitive sort. The number you specify in nFlags provides a bit-value that determines the case sensitivity of a sort according to the following table: nFlag Bit Description 0 000 Case-sensitive sort 1 001 Case insensitive sort

> **Observação:**

# Valor de retorno

Numeric

# Observações

Todos os elementos incluídos na classificação devem ser do mesmo tipo de dados. Matrizes unidimensionais são classificadas por seus elementos; matrizes bidimensionais são classificadas por suas linhas. Quando uma matriz bidimensional é classificada, a ordem das linhas na matriz é alterada para que os elementos em uma coluna da matriz fiquem em ordem crescente ou decrescente.

Se a classificação for bem-sucedida, 1 é retornado; caso contrário, –1 é retornado.

# Exemplo

O exemplo a seguir copia o campo `contact` da tabela `customer` para uma matriz chamada `gaContact`. Os primeiros 20 contatos na matriz são exibidos, a matriz é classificada e os contatos são exibidos novamente em ordem classificada.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE Customer  && Open customer table
COUNT TO gnCount  && Number of contacts
DIMENSION gaContact(gnCount,1)  && Create a contact array
COPY TO ARRAY gaContact FIELD contact     && Fill the array
CLEAR
? 'Contact names:'
?
FOR nCount = 1 TO 20
   ? gaContact(nCount)  && Display first 20 contacts
ENDFOR
= ASORT(gaContact)     && Sort the array
?
? 'Sorted Contact names:'
?
FOR nCount = 1 TO 20
   ? gaContact(nCount)  && Display first 20 contacts, sorted
ENDFOR
```
