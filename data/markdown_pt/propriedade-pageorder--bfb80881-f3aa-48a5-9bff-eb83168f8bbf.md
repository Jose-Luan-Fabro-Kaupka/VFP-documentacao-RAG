# Propriedade PageOrder

Especifica a ordem relativa das páginas em um page frame. Disponível em tempo de design e em tempo de execução.

```foxpro
Page.PageOrder[ = nOrder]
```

#### Parâmetros
 **nOrder**
Especifica a ordem relativa de uma página em um page frame.

# Observações

Aplica-se a: Page Object

Se um page frame contém cinco páginas e você deseja que a terceira página seja exibida por último, defina a propriedade PageOrder da terceira página como 5. A configuração PageOrder da quarta página torna-se 3, a configuração PageOrder da quinta página torna-se 4, e assim por diante.

> **Observação:** As configurações PageOrder não precisam ser sequenciais. Além disso, PageOrder deve ser menor ou igual ao número de páginas em um page frame.
