# Propriedade SelectionNamespaces

Especifica uma declaração XMLNamespace personalizada para expressões XPath. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
XMLAdapter.SelectionNamespaces = sValue
```

# Valor de retorno
 **sValue**
Cadeia de caracteres Unicode que especifica uma declaração de namespace XML personalizada. O valor padrão é uma cadeia de caracteres vazia ("").

# Observações

Aplica-se a: classe XMLAdapter

Para obter mais informações, consulte a descrição da propriedade SelectionNamespaces no SDK do Microsoft Core XML Services (MSXML) 4.0.

Os prefixos de namespace na lista a seguir estão reservados para a classe XMLAdapter e não devem ser usados nesta propriedade:
 - "dataset"
- todos os prefixos que começam com "rowdata"
- "diffgr"
