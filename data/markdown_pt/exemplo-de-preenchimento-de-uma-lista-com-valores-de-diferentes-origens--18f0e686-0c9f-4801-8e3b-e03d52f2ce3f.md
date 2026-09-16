# Exemplo de preenchimento de uma lista com valores de diferentes origens

Arquivo: ...\Samples\Solution\Controls\Lists\Multdat1.scx

Este exemplo demonstra como definir RowSourceType de uma caixa de listagem em tempo de execução como um valor, um alias, uma instrução SQL, uma consulta (.qpr), uma matriz, campos de uma tabela, arquivos de um diretório e a estrutura de uma tabela.

A caixa de combinação do formulário contém todos os RowSourceTypes possíveis de uma lista (exceto 9 - popup, incluído para compatibilidade com versões anteriores). O código associado ao evento InteractiveChange define as novas propriedades RowSourceType e RowSource da lista.

Ao alterar RowSourceType e RowSource de uma caixa de listagem em tempo de execução, faça o seguinte:
 - Defina RowSourceType como 0.
- Defina RowSource como a nova origem.
- Defina RowSourceType como o novo tipo.

Se você não seguir essa ordem, as configurações existentes de RowSource e RowSourceType poderão entrar em conflito depois que um novo valor for definido e antes que o valor correspondente seja definido.
