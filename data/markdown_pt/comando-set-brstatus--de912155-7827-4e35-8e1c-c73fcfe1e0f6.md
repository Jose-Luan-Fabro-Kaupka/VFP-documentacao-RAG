# Comando SET BRSTATUS

Incluído para compatibilidade com versões anteriores. Use a propriedade StatusBarText em vez disso.

Habilita ou desabilita a exibição da barra de status em uma janela Browse.

```foxpro
SET BRSTATUS ON | OFF
```

# Observações

SET BRSTATUS é incluído para compatibilidade com versões anteriores.

SET BRSTATUS controla a exibição da barra de status quando uma janela Browse é aberta. A barra de status exibe a unidade atual, a tabela ativa, a posição do ponteiro de registro, o número de registros na tabela e o estado das teclas Insert, Num Lock e Caps Lock.

Se a barra de status já estiver exibida quando você abrir uma janela Browse, ela permanece exibida.

ON

 A barra de status é exibida na parte inferior da tela quando uma janela Browse é aberta se SET BRSTATUS estiver ON. Se mais de uma janela Browse foi aberta, a barra de status exibe informações da janela Browse ativa.

 No FoxPro for Windows e no FoxPro for Macintosh, abrir uma janela Browse exibe a barra de status de caracteres se a barra de status estiver desativada.

OFF

 Se SET BRSTATUS estiver OFF, a barra de status não é exibida quando uma janela Browse é aberta. Esta é a configuração padrão.
