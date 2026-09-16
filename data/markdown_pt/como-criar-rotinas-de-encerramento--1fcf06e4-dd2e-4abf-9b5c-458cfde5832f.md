# Como: criar rotinas de encerramento

Você pode criar rotinas de encerramento personalizadas para quando o usuário quiser sair do aplicativo, do Visual FoxPro ou do Microsoft Windows.

### Para criar uma rotina de encerramento
- Use o comando ON SHUTDOWN e inclua um comando ou procedimento a executar.

O comando ON SHUTDOWN normalmente usa DO para chamar um procedimento ou programa quando o usuário tenta sair do aplicativo. Por exemplo, a linha a seguir especifica uma rotina chamada My_QuitRoutine:

```foxpro
ON SHUTDOWN DO My_QuitRoutine
```

A rotina geralmente inclui uma caixa de diálogo que pergunta se o usuário deseja sair do aplicativo atual. Se desejar, a rotina pode fechar arquivos abertos, limpar o ambiente e chamar QUIT. Caso contrário, pode devolver o controle ao aplicativo.

Para obter mais informações, consulte o comando ON SHUTDOWN.
