# Propriedade ConversionFunc

Especifica uma lista delimitada por vírgulas de pares de campo e nome de função separados por espaços simples. Leitura/gravação em tempo de design e em tempo de execução.

> **Observação:** ConversionFunc se aplica apenas ao usar atualização automática. ConversionFunc não é avaliada em tempo de design.

Use ConversionFunc para especificar funções de conversão nativas do Visual FoxPro ou personalizadas que são aplicadas a um ou mais campos do cursor antes de enviá-los à fonte de dados por meio de uma operação de atualização, inserção ou exclusão. Os valores reais enviados à fonte de dados são os valores retornados pela função associada a cada campo.

```foxpro
CursorAdapter.ConversionFunc [ = 'cFieldName1 cFuncName1 [, cFieldName2 cFuncName2 ]...' ]
```

# Valor de retorno
 **cFieldName**
Especifica um nome de campo.
**cFuncName**
Especifica um nome de função que aceita um valor de campo como primeiro parâmetro. A função ou método especificado deve aceitar o nome do campo associado como único parâmetro. Observação Não inclua parênteses no final do nome da função ou método.

# Observações

Aplica-se a: Classe CursorAdapter

Se o cursor local contém campos de caractere usados como parte da cláusula WHERE para um comando de atualização gerado automaticamente, a fonte de dados pode exigir que os espaços à direita sejam removidos para obter uma correspondência adequada na fonte de dados. O exemplo a seguir ilustra como remover esses espaços:

```foxpro
CursorAdapter.ConversionFunc = "companyname TRIM, contactname TRIM"
```
