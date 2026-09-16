# Propriedade XMLPrefix

Contém o prefixo usado para referenciar a propriedade XMLNamespace do objeto correspondente.

O Visual FoxPro desconsidera XMLPrefix , a menos que XMLNamespace do objeto correspondente esteja definido com um valor não vazio. O método ToXML do XMLAdapter desconsidera XMLPrefix do XMLTable .

```foxpro
Object.Prefix
```

# Valor de retorno

Tipo de dados Caractere. XMLPrefix contém uma cadeia de caracteres Unicode ou está vazio ("") quando não preenchido.

> **Observação:** Antes de atribuir um valor de cadeia de caracteres a XMLPrefix , você deve converter o valor para Unicode. Você pode usar a função STRCONV( ) para atender a esse requisito.

# Observações

Aplica-se a: classe XMLAdapter | classe XMLTable
