# Função SEEK( )

Pesquisa em uma tabela indexada a primeira ocorrência de um registro cuja chave de índice corresponde a uma expressão especificada. Emitir SEEK( ) é equivalente a emitir SEEK e FOUND( ) em sequência.

> **Observação:** O Visual FoxPro não oferece suporte a operações seek para índices binários.

```foxpro
SEEK(eExpression [, nWorkArea | cTableAlias
   [, nIndexNumber | cIDXIndexFileName | cTagName]])
```

#### Parâmetros
 **eExpression**
Especifica a expressão de chave de índice que você deseja que SEEK( ) pesquise.
**nWorkArea**
Especifica o número da área de trabalho da tabela que é pesquisada pela chave de índice.
**cTableAlias**
Especifica o alias da tabela que é pesquisada. Se você omitir nWorkArea e cTableAlias , a tabela na área de trabalho atualmente selecionada é pesquisada.
**nIndexNumber**
Especifica o número do arquivo de índice ou tag usado para pesquisar a chave de índice. nIndexNumber refere-se aos arquivos de índice conforme listados em USE ou SET INDEX. Arquivos .idx abertos são numerados primeiro na ordem em que aparecem em USE ou SET INDEX. As tags no arquivo estrutural .cdx (se existir) são então numeradas na ordem em que foram criadas. Por fim, as tags em quaisquer arquivos .cdx independentes abertos são numeradas na ordem em que foram criadas. Para obter mais informações sobre numeração de índices, consulte Comando SET ORDER .
**cIDXIndexFileName**
Especifica um arquivo .idx usado para pesquisar a chave de índice.
**cTagName**
Especifica uma tag de um arquivo .cdx usada para pesquisar a chave de índice. O nome da tag pode ser de um arquivo .cdx estrutural ou de qualquer arquivo .cdx independente aberto. Observação O arquivo .idx tem precedência se existirem nomes duplicados de arquivo .idx e tag.

# Valor de retorno

Lógico. SEEK( ) retorna True (.T.) se uma correspondência é encontrada e o ponteiro de registro se move para o registro correspondente. Caso contrário, SEEK( ) retorna False (.F.) se nenhuma correspondência é encontrada, e o ponteiro de registro se move para o final do arquivo se SET NEAR estiver OFF ou para o registro correspondente mais próximo se SET NEAR estiver ON.

# Observações

Você pode usar SEEK( ) em uma tabela com uma ordem de índice definida ou, se nenhuma ordem de índice estiver definida na tabela, definir o índice controlador com o 3º parâmetro, nIndexNumber, cIDXIndexFileName ou cTagName. A correspondência deve ser exata, a menos que SET EXACT esteja definido como OFF.

Se você omitir os argumentos nIndexNumber, IDXIndexFileName e cTagName, SEEK( ) usa o índice controlador mestre ou a tag de índice para pesquisar a chave de índice.

A configuração SET KEY é ignorada se SEEK( ) usar um índice não ativo.

# Exemplo

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer ORDER cust_id  && Opens Customer table
? SEEK('CHOPS')  && Returns .T., record found
```
