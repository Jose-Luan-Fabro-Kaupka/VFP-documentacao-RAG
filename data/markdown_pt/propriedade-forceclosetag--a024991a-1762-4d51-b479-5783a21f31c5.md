# Propriedade ForceCloseTag

Especifica se deve substituir tags de elemento vazio únicas por um conjunto de tags de abertura e fechamento de elemento vazio. Você pode usar ForceCloseTag se pesquisar tags de abertura e fechamento ao analisar XML ou se desejar aumentar a legibilidade.

ForceCloseTag se aplica ao executar o método ToXML do XMLAdapter, que cria XML consistente com sua configuração.

```foxpro
XMLAdapter.ForceCloseTag [= lValue]
```

# Valor de retorno
 **lValue**
Tipo de dados lógico. A tabela a seguir lista os valores para lValue . lValue Descrição False (.F.) Não substitui tags de elemento vazio únicas por um conjunto de tags de abertura e fechamento de elemento vazio. (Padrão) True (.T.) Substitui tags de elemento vazio únicas por um conjunto de tags de abertura e fechamento de elemento vazio.

# Observações

Aplica-se a: Classe XMLAdapter

# Exemplo

O exemplo a seguir contém uma tag de elemento vazio, `<col1/>`:

```foxpro
<?xml version = "1.0" encoding="Windows-1252" standalone="yes"?>
<VFPData>
   <etest>
      <col1>One</col1>
   </etest>
   <etest>
      <col1/>
   </etest>
</VFPData>
```

Definir ForceCloseTag como True (.T.) substitui a tag de elemento vazio única por um conjunto válido de tags de abertura e fechamento de elemento vazio, `<col1></col1>`.

```foxpro
<?xml version = "1.0" encoding="Windows-1252" standalone="yes"?>
<VFPData>
   <etest>
      <col1>One</col1>
   </etest>
   <etest>
      <col1></col1>
   </etest>
</VFPData>
```
