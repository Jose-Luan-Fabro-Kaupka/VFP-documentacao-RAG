# Restaurando o ambiente interativo do Visual FoxPro

Se desejar encerrar todas as operações de programa e retornar o Visual FoxPro ao seu estado interativo, emita os seguintes comandos em ordem na janela Command ou no programa chamado imediatamente antes de sair do Visual FoxPro.

```foxpro
CLEAR ALL
CLOSE ALL
CLEAR PROGRAM
```

CLEAR ALL remove todos os objetos da memória, o que, por sua vez, fecha todas as sessões de dados privadas e cursors.

CLOSE ALL, após CLEAR ALL ser concluído com sucesso, fecha todos os bancos de dados, tabelas e cursors na sessão de dados 1, a sessão de dados padrão do Visual FoxPro.

CLEAR PROGRAM limpa o buffer de programa compilado dos programas executados mais recentemente. CLEAR PROGRAM força o Visual FoxPro a ler os programas do disco, em vez do buffer de programa.

Limpando durante transações Se transações estiverem em andamento, use o Comando END TRANSACTION para cada nível de transação antes de emitir CLEAR ALL, CLOSE ALL e CLEAR PROGRAM.

Limpando durante atualizações em buffer Se atualizações em buffer estiverem em andamento, use TABLEUPDATE( ) Function ou TABLEREVERT( ) Function para cada cursor com atualizações em buffer antes de emitir CLEAR ALL, CLOSE ALL e CLEAR PROGRAM.
