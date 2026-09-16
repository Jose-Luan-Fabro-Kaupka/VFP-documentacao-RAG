# Comando SET CLEAR

Incluído para compatibilidade com versões anteriores. Use o método Refresh (Visual FoxPro) em vez disso.

Determina se a emissão de SET FORMAT e QUIT limpa a tela.

```foxpro
SET CLEAR ON | OFF
```

# Observações

SET CLEAR determina se a janela principal do FoxPro é limpa quando SET FORMAT é emitido.

ON

 Se SET CLEAR estiver ON, a janela principal do FoxPro não é limpa quando você abre um arquivo de formato com SET FORMAT. Esta é a configuração padrão.

OFF

 A janela principal do FoxPro é limpa se SET CLEAR estiver OFF.

 No FoxPro para MS-DOS, se SET CLEAR estiver OFF, a janela principal do FoxPro não é limpa quando você sai do FoxPro. Você pode exibir uma tela de encerramento ao sair do FoxPro.
