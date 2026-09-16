# Propriedade DynamicInputMask

Especifica o formato dinâmico de texto e controles em uma coluna, controlando como os dados são inseridos e exibidos em um objeto Column. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Column.DynamicInputMask[ = cInputMask]
```

# Valor de retorno
 **cInputMask**
Especifica uma expressão de caractere que deve ser avaliada como uma cadeia de caracteres com o seguinte formato: [@cFunction] [cMask] A expressão de caractere é reavaliada em tempo de execução cada vez que o controle Grid é atualizado. Para obter informações adicionais sobre o formato de cFunction e cMask, consulte as propriedades Format e InputMask.

# Observações

Aplica-se a: Column Object

A propriedade DynamicInputMask tem precedência sobre as propriedades Format e InputMask.

Se o controle especificado pela propriedade CurrentControl da coluna for uma caixa de texto, spinner ou combo box, as porções cFunction e cMask da expressão DynamicInputMask são passadas para as propriedades Format e InputMask da caixa de texto, spinner ou combo box.

> **Observação:** O método AutoFit do Grid pode não redimensionar adequadamente para exibir todo o conteúdo de uma coluna se você usar esta propriedade.

# Exemplo

O exemplo a seguir demonstra um formato típico para cInputMask:

```foxpro
Column1.DynamicInputMask = "@R$ ###,###,###.##"
```
