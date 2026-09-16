# Como: remover registros excluídos

Depois de marcar registros para exclusão, você pode removê-los permanentemente do disco.

### Para remover registros marcados do disco
- Abra a tabela em uma janela de navegação.
- No menu Table, clique em Remove Deleted Records .
- Quando solicitado a confirmar a exclusão, clique em Yes . Os registros marcados são removidos do disco e a janela de navegação é fechada.

### Para remover registros marcados do disco programaticamente
- Use o comando PACK

Para obter mais informações, consulte PACK Command.

> **Dica:** PACK possui duas cláusulas: MEMO e DBF . Chamar PACK sem as cláusulas MEMO ou DBF remove registros marcados para exclusão no arquivo de tabela (.dbf) e no arquivo memo associado (.fpt). Ao chamar o comando PACK, certifique-se de que a tabela foi aberta de forma exclusiva. Para excluir registros apenas no arquivo de tabela e deixar o arquivo memo intacto, use PACK DBF . Para remover espaço não utilizado no arquivo memo sem remover registros marcados para exclusão no arquivo de tabela, use PACK MEMO .
