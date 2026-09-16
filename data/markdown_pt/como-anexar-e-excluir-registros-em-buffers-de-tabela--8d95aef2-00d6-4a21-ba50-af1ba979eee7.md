# Como: anexar e excluir registros em buffers de tabela

Você pode anexar e excluir registros enquanto o buffer de tabela está habilitado: registros anexados são adicionados ao final do buffer. Para acessar todos os registros no buffer, incluindo os anexados, use a função RECNO( ). A função RECNO( ) retorna números negativos sequenciais nos registros que você anexa a um buffer de tabela. Por exemplo, se você iniciar o buffer de tabela, editar os registros 7, 8 e 9 e depois anexar três registros, o buffer conterá valores RECNO( ) de 7, 8, 9, – 1, – 2 e – 3.

> **Observação:** Tabelas que contêm valores de campo com incremento automático anexam registros com buffer de tabela aproximadamente 35% mais lentamente do que tabelas sem valores de campo com incremento automático, o que pode afetar o desempenho. Ao usar buffer de tabela, o cabeçalho da tabela é bloqueado quando o registro é anexado.
 Buffer após editar e anexar registros

Você pode remover registros anexados do buffer apenas usando a função TABLEREVERT( ). Para qualquer registro anexado, tanto TABLEUPDATE( ) quanto TABLEREVERT( ) excluem o valor RECNO( ) negativo desse registro, mantendo a sequência.
 Buffer após editar, excluir um registro anexado e anexar outro

Ao usar um buffer de tabela, você pode usar o comando GO com o valor RECNO( ) negativo para acessar um registro anexado específico. Por exemplo, usando o exemplo anterior, você pode digitar:

```foxpro
GO 7      && moves to the 1st buffered record
GO -3      && moves to the 6th buffered record (3rd appended)
```

### Para anexar registros a um buffer de tabela
- Use o comando APPEND ou APPEND BLANK depois de habilitar o buffer de tabela.

Registros anexados têm números RECNO( ) negativos sequenciais ascendentes.

### Para remover um registro anexado de um buffer de tabela
- Use o comando GO | GOTO com um valor negativo para posicionar o ponteiro de registro no registro a ser excluído.
- Use o comando DELETE para marcar o registro para exclusão.
- Use a função TABLEREVERT( ) para remover o registro do buffer. Observação A função TABLEREVERT() também afeta o status de linhas excluídas e alteradas.

### Para remover todos os registros anexados de um buffer de tabela
- Use a função TABLEREVERT( ) com um valor true (.T.).

TABLEREVERT( ) remove registros anexados de um buffer de tabela sem gravar os registros na tabela. TABLEUPDATE( ) grava todos os registros atuais em buffer em uma tabela, mesmo se foram marcados para exclusão.
