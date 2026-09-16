# Propriedade WindowState (Visual FoxPro)

Especifica se uma janela de formulário é exibida como maximizada, minimizada ou normal em tempo de execução. Disponível em tempo de design e em tempo de execução.

```foxpro
 [Object.]WindowState[ = nState]
```

# Valor de retorno
 **nState**
As configurações da propriedade WindowState são as seguintes: Configuração Descrição 0 Normal 1 Minimizada (minimizada para um ícone). Se a janela principal do Visual FoxPro estiver minimizada quando você sair do Visual FoxPro, a janela principal do Visual FoxPro não será exibida antes de sair. Se seu aplicativo exibir uma caixa de diálogo antes de sair, certifique-se de definir _SCREEN.WindowState como 0 antes de exibir a caixa de diálogo. 2 Maximizada (ampliada para preencher a tela)

# Observações

Aplica-se a: Objeto Form | Variável de sistema _SCREEN
