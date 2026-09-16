# Comando SET FORMAT

Incluído para compatibilidade com versões anteriores. Use a propriedade Format em vez disso.

Abre um arquivo de formato.

```foxpro
SET FORMAT TO [file | ?]
```

#### Parâmetros
 file | ?

 Especifique o arquivo de formato a abrir com file. SET FORMAT TO ? exibe uma lista de arquivos de formato disponíveis. Arquivos de formato têm extensão .FMT ou .PRX.

 Emita SET FORMAT TO sem file para fechar um arquivo de formato na área de trabalho atual.

# Observações

SET FORMAT está incluído para compatibilidade com versões anteriores. Use um READ de várias janelas em vez disso.

SET FORMAT abre um arquivo de formato para uso com APPEND, BROWSE, INSERT e READ.

Arquivos de formato podem conter código de inicialização antes dos comandos @ ... SAY. Código de limpeza pode seguir os comandos @ ... SAY. O código de inicialização é executado imediatamente após APPEND, CHANGE, EDIT, INSERT ou READ ser emitido. O código de limpeza é executado imediatamente após APPEND, CHANGE, EDIT, INSERT ou READ concluir a execução.
