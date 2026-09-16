# Comando ON SHUTDOWN

Especifica um comando que é executado quando você tenta sair do Visual FoxPro ou do Microsoft Windows.

```foxpro
ON SHUTDOWN [Command]
```

#### Parâmetros

Emita ON SHUTDOWN sem Command para liberar o comando ON SHUTDOWN atual.

# Observações

O comando que você especifica em ON SHUTDOWN é executado se você tentar sair do Visual FoxPro. Se você tentar sair do Microsoft Windows enquanto o Visual FoxPro estiver aberto, o controle é retornado ao Visual FoxPro e o comando que você especifica em ON SHUTDOWN é executado.

O comando ON SHUTDOWN é tipicamente um comando DO que executa uma rotina para exibir uma caixa de diálogo. A caixa de diálogo pergunta se você tem certeza de que deseja sair do aplicativo atual e do Visual FoxPro. Se você deseja sair do aplicativo, a rotina pode fechar arquivos abertos, limpar o ambiente do Visual FoxPro e então executar QUIT. Se você não deseja sair do aplicativo atual, a rotina pode retornar o controle ao aplicativo.
