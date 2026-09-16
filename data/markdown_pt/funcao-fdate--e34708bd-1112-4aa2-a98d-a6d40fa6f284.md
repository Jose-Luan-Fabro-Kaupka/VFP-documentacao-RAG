# Função FDATE( )

Retorna a data ou DateTime da última modificação de um arquivo.

```foxpro
FDATE(cFileName [, nType])
```

#### Parâmetros
 **cFileName**
Especifica o nome do arquivo cuja data da última modificação FDATE( ) retorna. cFileName pode incluir um caminho com o nome do arquivo. Se um caminho não for incluído com o nome do arquivo, o Visual FoxPro procura o arquivo no diretório padrão e em quaisquer diretórios ou pastas especificados com SET PATH.
**nType**
Especifica que FDATE( ) retorna a data ou DateTime da última modificação do arquivo especificado com cFileName. Se nType for 0, a data da última modificação é retornada. Incluir 0 é idêntico a omitir nType. Se nType for 1, o DateTime da última modificação é retornado.

# Valor de retorno

Date

# Observações

O valor Date ou DateTime que FDATE( ) retorna é atribuído ao arquivo pelo sistema operacional.

Use LUPDATE( ) para determinar a data da última modificação de uma tabela aberta.

# Exemplo

O exemplo a seguir usa FDATE( ) para exibir o DateTime da última modificação de FoxUser.dbf, o arquivo de recursos do Visual FoxPro.

```foxpro
? FDATE('FOXUSER.DBF', 1)  && Displays the last modification DateTime
```
