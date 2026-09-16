# Objeto Page

Cria uma página em um controle PageFrame.

Você pode usar páginas para criar formulários ou caixas de diálogo com guias. Um page frame contém um conjunto de páginas. Para informações adicionais sobre como criar páginas e page frames, consulte "Adding Page Frames to a Form" em Controls for Extending Forms.

```foxpro
Page
```

# Observações

Você pode referenciar uma página em um page frame pelo nome, como no exemplo a seguir:

```foxpro
myFrame.MyPage1
```

Você também pode referenciar uma página pelo seu número de índice usando a propriedade Pages do PageFrame. Isso é consistente com as coleções de controles em outros contêineres do Visual FoxPro.

```foxpro
myFrame.Pages(2).Enabled = .T.
```

Este índice não necessariamente é igual à propriedade PageOrder. Você pode ter três páginas com PageOrders de 2, 3 e 5. Você pode referenciar essas páginas da seguinte forma:

```foxpro
myFrame.Pages(1)
myFrame.Pages(2)
myFrame.Pages(3)
```

Somente a página ativa é atualizada quando ocorre o método Refresh do Form para o formulário no qual a página está localizada.
