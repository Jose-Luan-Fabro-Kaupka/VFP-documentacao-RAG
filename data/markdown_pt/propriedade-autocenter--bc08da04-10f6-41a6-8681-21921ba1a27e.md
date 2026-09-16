# Propriedade AutoCenter

Especifica se o objeto Form é automaticamente centralizado na janela principal do Visual FoxPro ou na área de trabalho na primeira vez que é exibido. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.AutoCenter [ = lExpr]
```

# Valor de retorno
 **lExpr**
Especifica se o objeto Form é centralizado ou posicionado conforme as configurações das propriedades Top e Left. As configurações da propriedade AutoCenter são: Configuração Descrição True (.T.) O objeto Form é centralizado e os valores das propriedades Top e Left são definidos para a nova posição. False (.F.) (Padrão) O objeto Form não é centralizado e é posicionado nas coordenadas especificadas pelas propriedades Top e Left.

# Observações

Aplica-se a: objeto Form | variável de sistema _SCREEN

Formulários são exibidos na janela principal, portanto definir AutoCenter como true (.T.) centraliza o formulário dentro da janela principal.

> **Observação:** Redefinir AutoCenter como false (.F.) depois que foi definido como true (.T.) não retornará o formulário à posição Top e Left original.
