# Propriedade DisplayValue

Especifica o conteúdo da primeira coluna do item selecionado em um controle ListBox ou ComboBox. Disponível em tempo de design e em tempo de execução.

Use a propriedade DisplayValue quando um combo box ou list box tem mais de uma coluna e a propriedade BoundColumn do controle está definida com um valor maior que 1.

```foxpro
 [Form.]Control.DisplayValue[ = Expr]
```

# Valor de retorno
 **Expr**
Especifica uma cadeia de caracteres ou um valor numérico. A tabela a seguir descreve os valores de Expr . Expr Descrição Cadeia de caracteres Especifica o valor da primeira coluna do item selecionado. Para combo boxes, DisplayValue especifica o texto exibido na parte da caixa de texto do combo box quando DisplayValue é uma cadeia de caracteres. No entanto, as propriedades InputMask e MaxLength do ComboBox podem afetar sua exibição. Valor numérico Especifica o índice do item selecionado.

# Observações

Aplica-se a: ComboBox Control | ListBox Control

Quando um combo box ou list box tem apenas uma coluna, a propriedade DisplayValue e a propriedade Value do controle geralmente têm a mesma configuração se ambas contêm cadeias de caracteres. Uma exceção existe quando ambas as propriedades contêm cadeias de caracteres e um valor é digitado no combo box, mas o valor não existe na lista. Neste caso, o valor é uma cadeia vazia (""), e DisplayValue será o valor digitado.
