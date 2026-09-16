# Propriedade XMLAdapter

Contém uma referência a um objeto XMLAdapter somente quando a coleção Tables desse XMLAdapter contém o objeto XMLTable.

```foxpro
XMLTable.XMLAdapter
```

# Valor de retorno

Referência de objeto. XMLAdapter contém um dos seguintes:
 - Uma referência a um objeto XMLAdapter cuja coleção Tables contém o objeto XMLTable
- Nulo (.NULL.) nas seguintes condições: o objeto XMLTable é criado isoladamente, não estando contido em um objeto XMLAdapter nem como filho de outro objeto XMLTable. Quando o objeto XMLTable está contido em outro objeto XMLTable. A propriedade ParentTable contém uma referência ao objeto XMLTable pai.

# Observações

Aplica-se a: Classe XMLTable
