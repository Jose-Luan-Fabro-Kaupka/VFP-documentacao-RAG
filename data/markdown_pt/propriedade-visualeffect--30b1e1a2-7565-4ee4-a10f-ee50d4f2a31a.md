# Propriedade VisualEffect

Permite aplicar comportamentos de SpecialEffect programaticamente a botões de comando do Visual FoxPro. Disponível somente em tempo de execução.

```foxpro
CommandButton.VisualEffect[ = nValue]
```

# Valor de retorno
 **nValue**
Especifica a configuração de formato de um controle conforme a tabela a seguir: Configuração Descrição 0 Nenhum. O efeito visual existente permanece inalterado. 1 Elevado. Produz efeito visual elevado semelhante à passagem do mouse com SpecialEffect=2 (Hot Tracking). 2 Pressionado. Produz efeito visual rebaixado semelhante a manter o mouse pressionado no botão de comando.

# Observações

Aplica-se a: CommandButton Control

Como a configuração Elevado de VisualEffect (1) entra em conflito com a configuração SpecialEffect 3D, o valor 1 de VisualEffect é ignorado se SpecialEffect = 0.
