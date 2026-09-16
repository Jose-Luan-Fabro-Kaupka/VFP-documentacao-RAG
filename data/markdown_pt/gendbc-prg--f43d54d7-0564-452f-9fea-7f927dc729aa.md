# Gendbc.prg

Localizado na pasta Visual FoxPro Tools\Gendbc, esta ferramenta gera um programa que pode recriar um banco de dados. GenDBC.prg suporta autoincremento, sequências de ordenação e chaves primárias filtradas. No Visual FoxPro 9.0, também suporta campos dos tipos Blob, VarChar e VarBinary, e as propriedades AllowSimultaneousFetch, RuleExpression e RuleText para exibições.

Você pode usar este programa para gerar o seguinte:
 - Código que você pode analisar para aprender como um banco de dados é criado usando código de programa
- Código que você pode inserir em seu código de programa, eliminando a necessidade de enviar bancos de dados com seu aplicativo
- Código que você pode inserir em seu código de programa para recriar o banco de dados se os dados de um cliente estiverem corrompidos

```foxpro
DO GENDBC WITH filename
```

#### Parâmetros
 **filename**
Especifica uma cadeia de caracteres contendo o nome de um arquivo de saída. O filename pode conter informações de caminho e uma extensão de arquivo. Se nenhuma extensão for fornecida, a extensão padrão .prg é usada. Observação Este programa funciona apenas no banco de dados atualmente ativo.

# Exemplo

O exemplo a seguir cria um programa chamado `MyData.prg`, que contém código para recriar um banco de dados, `MyDatabase`. O programa`, Main.prg`é criado na pasta C:\VFP e contém código para recriar o banco de dados, `Main`.

```foxpro
OPEN DATABASE MyDatabase
DO gendbc WITH 'MyData.prg'
SET DATABASE TO Main
DO gendbc WITH 'c:\vfp\main'
```
