# Propriedade FillColor (Visual FoxPro)

Especifica a cor usada para preencher formas desenhadas em um objeto por rotinas gráficas. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.FillColor[ = nColor ]
Object.FillColor[ = RGB(nRedValue, nGreenValue, nBlueValue) ]
```

# Valor de retorno
 **nColor**
Especifica um único número para representar a cor. Por padrão, FillColor é definida como 0 (preto). Para obter mais informações sobre configurações de cores, consulte o tópico das propriedades BackColor, ForeColor.
**nRedValue, nGreenValue, nBlueValue**
Especifica três intensidades de cor separadas que compõem a cor de preenchimento; deve ser usado com a função RGB( ) para consolidar os três componentes de cor em um único número, que é o valor da propriedade FillColor. Observação: na janela Properties, você pode clicar duas vezes em qualquer uma das propriedades de cor para exibir a caixa de diálogo Color. Você pode escolher ou definir cores nessa caixa de diálogo. As intensidades de vermelho, verde e azul correspondentes à cor escolhida tornam-se as configurações dessas propriedades depois que você fecha a caixa de diálogo Color.

# Observações

Aplica-se a: Objeto Form | Variável de sistema _SCREEN | Controle Shape

Quando a propriedade FillStyle está definida com seu valor padrão, 1 (Transparent), a configuração de FillColor é ignorada.

Somente uma forma fechada, como um círculo, caixa ou elipse, pode ser preenchida.

Objetos Shape usam a propriedade BackColor para especificar a cor de preenchimento.
