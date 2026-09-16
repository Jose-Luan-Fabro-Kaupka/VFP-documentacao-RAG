# Comando SET CONSOLE

Ativa ou desativa a saída para a janela principal do Visual FoxPro ou para a janela ativa definida pelo usuário a partir de programas.

```foxpro
SET CONSOLE ON | OFF
```

#### Parâmetros
**ON**
Envia toda a saída para a janela principal do Visual FoxPro ou para a janela ativa definida pelo usuário. (Padrão)
**OFF**
Suprime a saída para a janela principal do Visual FoxPro ou para a janela ativa definida pelo usuário.

# Observações

SET CONSOLE é definido como ON quando você usa o Visual FoxPro interativamente e não pode ser alterado para OFF na janela Command. Você pode alterar a configuração para OFF somente a partir de um programa.

SET CONSOLE afeta algumas caixas de diálogo interativas do Visual FoxPro. Por exemplo, se SET CONSOLE estiver definido como OFF e você emitir BROWSE quando nenhuma tabela estiver aberta, o Visual FoxPro exibirá uma mensagem de erro. Se SET CONSOLE estiver definido como ON nas mesmas circunstâncias, o Visual FoxPro exibirá a caixa de diálogo Open.

SET CONSOLE não afeta a saída de @ ... SAY. A saída de @ ... SAY é controlada pela configuração SET DEVICE.

> **Observação:** Um erro sempre define SET CONSOLE como ON.
