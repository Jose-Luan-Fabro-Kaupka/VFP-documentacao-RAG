# Comando SET MULTILOCKS

Determina se você pode bloquear vários registros usando LOCK( ) ou RLOCK( ).

```foxpro
SET MULTILOCKS ON | OFF
```

#### Parâmetros
 **ON**
Permite tentar bloquear um conjunto de registros. Inclua um conjunto de números de registro em LOCK( ) ou RLOCK( ) para tentar bloquear vários registros.
**OFF**
(Padrão) Permite tentar bloquear um único registro com LOCK( ) ou RLOCK( ).

# Observações

Quando uma tabela é aberta para uso compartilhado em uma rede, você pode tentar bloquear mais de um registro em um arquivo de tabela. A configuração SET MULTILOCKS determina se você pode tentar bloquear um único registro ou um conjunto de registros. Os registros podem ser bloqueados com a função LOCK( ) ou RLOCK( ).

> **Observação:** Alternar SET MULTILOCKS de ON para OFF ou de OFF para ON emite implicitamente UNLOCK ALL — todos os bloqueios de registro em todas as áreas de trabalho são liberados.

SET MULTILOCKS tem escopo na sessão de dados atual.

MULTILOCKS deve estar ON antes que o buffer de linha ou de tabela possa ser habilitado com CURSORSETPROP( ). Consulte a função CURSORSETPROP( ) para obter informações adicionais sobre buffer de linha e de tabela.

Se você selecionar a caixa de seleção Enable Data Buffering na caixa de diálogo Propriedades da Área de Trabalho (que é exibida quando você escolhe o botão Propriedades na janela Sessão de Dados), MULTILOCKS é automaticamente definido como ON para a sessão de dados atual. No entanto, desmarcar a caixa de seleção Enable Data Buffering não define MULTILOCKS como OFF para a sessão de dados atual.

Para obter mais informações sobre bloqueio de registros e arquivos e compartilhamento de tabelas em uma rede, consulte a função LOCK( ), a função RLOCK( ) e Programação para acesso compartilhado.
