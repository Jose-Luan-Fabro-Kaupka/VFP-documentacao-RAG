# Propriedade Count (Visual FoxPro)

Contém o número de itens em uma coleção, por exemplo, objetos de projeto, arquivo ou servidor em uma coleção de projetos, arquivos ou servidores. Somente leitura em tempo de design e em tempo de execução.

```foxpro
Object.Count
```

# Valor de retorno

Numérico

# Observações

Aplica-se a: Files Collection (Visual FoxPro) | Projects Collection (Visual FoxPro) | Servers Collection | Collection Class

Para uma coleção de projetos, a propriedade Count contém zero se não existirem instâncias do Project Manager. Para uma coleção de arquivos ou servidores, a propriedade Count contém zero se não existirem arquivos ou servidores na coleção de arquivos ou servidores.

Você pode usar a propriedade Count para acessar o número de itens em uma coleção. No entanto, não é possível alterar Count manualmente, exceto usando os métodos Add e Remove da coleção. Os objetos Collection fornecem seus próprios métodos Add e Remove.

Você deve usar Count para determinar o número de itens em uma coleção ao iterar pelos itens da coleção usando FOR...ENDFOR ou ao referenciar itens individuais com o método Item.

Count suporta o método Access. Como Count é somente leitura, não suporta o método Assign.
