# Propriedade ShowWindow

Especifica se um formulário ou barra de ferramentas é um formulário de nível superior ou um formulário filho. Disponível em tempo de design; somente leitura em tempo de execução.

```foxpro
Form.ShowWindow[ = nExpr]
```

# Valor de retorno
 **nExpr**
As configurações da propriedade ShowWindow são: Configuração Descrição 0 In Screen (Padrão). O formulário é um formulário filho que é colocado na janela principal do Visual FoxPro. 1 In Top-Level Form. O formulário é um formulário filho do formulário de nível superior ativo, que pode ser a janela principal do Visual FoxPro ou outro formulário de nível superior. Use esta configuração se desejar que o formulário filho seja colocado dentro do formulário de nível superior ativo. Se nExpr estiver definido como 1 quando o formulário de nível superior é a janela principal do Visual FoxPro, o Visual FoxPro redefine automaticamente nExpr para 0. 2 As Top-Level Form. O formulário é um formulário de nível superior no qual formulários filhos podem ser colocados. Observe que um formulário de nível superior é sempre sem modo, independentemente da configuração da propriedade WindowType.

# Observações

Aplica-se a: Objeto Form | Objeto ToolBar

Um formulário filho é um formulário contido em outro formulário. Formulários filhos não podem ser movidos para fora dos limites de seu formulário pai; quando minimizados, aparecem na parte inferior de seu formulário pai. Se um formulário pai é minimizado, os formulários filhos também são minimizados.

Um formulário de nível superior é um formulário independente e sem modo sem um formulário pai, e é usado para criar um aplicativo SDI (single document interface) ou para servir como pai de outros formulários filhos. Formulários de nível superior funcionam no mesmo nível que outros aplicativos Windows, e podem aparecer na frente ou atrás deles. Formulários de nível superior aparecem na barra de tarefas do Windows.

A propriedade Desktop determina o comportamento de um formulário filho. Se a propriedade Desktop estiver definida como true (.T.), o formulário filho não é restrito às bordas de seu formulário pai e pode ser movido para qualquer lugar na área de trabalho do Windows. O formulário filho não aparece na barra de tarefas do Windows.
