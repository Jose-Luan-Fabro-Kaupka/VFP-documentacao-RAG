# Convenções de nomenclatura de janelas

Ao nomear janelas, use o seguinte formato.

```foxpro
wWindowName
```

# Observações

> **Observação:** Não use um prefixo com definições de classe; use prefixos apenas quando o objeto é instanciado.

# Exemplo

O exemplo a seguir ilustra a nomenclatura de um objeto de janela ao usar o comando DEFINE WINDOW:

```foxpro
DEFINE WINDOW wCustomerInvoices ;
   FROM nFirstRow, nFirstColumn TO nLastRow, nLastColumn
```
