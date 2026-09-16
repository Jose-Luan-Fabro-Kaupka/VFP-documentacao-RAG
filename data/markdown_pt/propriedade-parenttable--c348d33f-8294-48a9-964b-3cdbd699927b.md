# Propriedade ParentTable

Contém uma referência de objeto a um objeto XMLTable pai que existe e contém o objeto XMLTable. Somente leitura.

```foxpro
XMLTable.ParentTable
```

# Valor de retorno

Referência de objeto. ParentTable contém um dos seguintes:
 - Uma referência de objeto ao objeto XMLTable pai quando ele contém o objeto XMLTable
- Null (.NULL.) nas seguintes condições: Você cria o objeto XMLTable por si só, sem estar contido por um objeto XMLAdapter nem como filho de outro objeto XMLTable. Quando o objeto XMLTable está contido por um objeto XMLAdapter. A propriedade XMLAdapter contém uma referência de objeto ao objeto XMLAdapter que contém o objeto XMLTable.

# Observações

Aplica-se a: XMLTable Class
