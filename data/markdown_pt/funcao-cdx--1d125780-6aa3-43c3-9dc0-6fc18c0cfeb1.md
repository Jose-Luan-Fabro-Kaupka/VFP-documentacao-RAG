# Função CDX( )

Retorna os nomes do arquivo de índice composto (.cdx) aberto que possui o número de posição de índice especificado.

```foxpro
CDX(nIndexNumber [, nWorkArea | cTableAlias])
```

#### Parâmetros
 **nIndexNumber**
Para uma tabela com índice composto estrutural e outros índices compostos: 1 retorna o arquivo estrutural; 2 retorna o primeiro índice especificado em INDEX de USE ou SET INDEX; 3 retorna o segundo e assim por diante; um número maior que o total retorna a cadeia vazia. Sem índice estrutural, 1 retorna o primeiro índice composto, 2 o segundo e assim por diante.
**nWorkArea**
Especifica o número da área de trabalho da tabela cujos nomes de índices compostos abertos devem ser retornados.
**cTableAlias**
Especifica o alias dessa tabela. Se nWorkArea e cTableAlias forem omitidos, retorna os nomes da tabela na área atualmente selecionada.

# Valor de retorno

Character

# Observações

CDX( ) é idêntica a MDX( ).

Um índice .cdx composto consiste em um arquivo físico com várias tags de índice, cada uma representando uma ordem para a tabela associada.

Há índices compostos padrão e estruturais. Um .cdx padrão pode ter nome diferente da tabela, residir em outro diretório e existir em vários arquivos. Ele é aberto pela cláusula INDEX de USE ou por SET INDEX.

Um .cdx estrutural deve ter o mesmo nome e diretório da tabela. Uma tabela pode ter somente um, aberto e atualizado automaticamente com USE.

CDX( ) ignora arquivos .idx especificados em USE ou SET INDEX.

Use TAG( ) para retornar tags individuais de um .cdx e NDX( ) para retornar nomes de arquivos .idx abertos.

Com SET FULLPATH ON, CDX( ) retorna caminho e nome; com OFF, unidade e nome.

# Exemplo

O exemplo abre a tabela `customer` no banco `testdata`. FOR ... ENDFOR cria um loop que exibe o nome de cada índice estrutural.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'data\testdata')
USE customer     && Open customer table
CLEAR
FOR nCount = 1 TO TAGCOUNT()
   IF !EMPTY(TAG(nCount))  && Checks for tags in the index
   ? CDX(nCount)     && Display structural index names
   ELSE
      EXIT  && Exit the loop when no more tags are found
   ENDIF
ENDFOR
```
