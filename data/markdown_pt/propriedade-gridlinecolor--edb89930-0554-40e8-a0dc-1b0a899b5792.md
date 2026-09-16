# Propriedade GridLineColor

Especifica a cor das linhas que separam as células em um controle Grid. Disponível em tempo de design; leitura/gravação em tempo de execução. Há duas versões da sintaxe.

```foxpro
Grid.GridLineColor[ = nColor]
```

```foxpro
Grid.GridLineColor = RGB(nRedValue, nGreenValue, nBlueValue)
```

# Valor de retorno
 **nColor**
Especifica um único número para representar a cor. Por padrão, GridLineColor é definido como 0 (Preto).
**nRedValue, nGreenValue, nBlueValue**
Especifica três intensidades de cor separadas que compõem a cor das linhas do Grid; devem ser usadas com a função RGB( ) para consolidar os três componentes de cor em um único número, que é o valor da propriedade GridLineColor. Na janela Properties, você pode clicar duas vezes em qualquer uma das propriedades de cor para exibir a caixa de diálogo Color. Você pode escolher ou definir cores nessa caixa de diálogo. As intensidades de vermelho, verde e azul correspondentes à cor escolhida tornam-se as configurações dessas propriedades depois que você fecha a caixa de diálogo Color.

# Observações

Aplica-se a: Grid Control
