# Otimizando aplicativos em ambientes multiusuário

Ao escrever aplicativos para um ambiente multiusuário, prestar atenção ao desempenho é particularmente importante porque as ineficiências podem se multiplicar. Quando vários usuários acessam dados, seu aplicativo deve lidar com questões de simultaneidade e acesso à rede.

Você pode usar as seguintes sugestões para melhorar o desempenho e lidar com essas questões:
 - Usar indexação e classificação de tabelas adequadamente.
- Ajustar o intervalo para tentativas de bloqueio.
- Usar processamento de transações de forma eficiente.

Você também pode se beneficiar das sugestões para trabalhar com dados armazenados em servidores remotos. Para obter detalhes, consulte Optimizing Access to Remote Data.

# Indexando e classificando tabelas adequadamente

Quando os dados em uma tabela são relativamente estáticos, processar tabelas classificadas sequencialmente sem definir uma ordem melhora o desempenho. No entanto, isso não significa que tabelas classificadas não possam ou não devam tirar proveito de arquivos de índice; por exemplo, o comando SEEK requer um índice e localiza registros rapidamente. No entanto, depois de encontrar um registro usando o comando SEEK, você pode desativar a ordenação.

# Ajustando o intervalo para tentativas de bloqueio

Se seu aplicativo tentar bloquear um registro ou tabela e não for bem-sucedido, você pode especificar que o Visual FoxPro repita a tentativa automaticamente após um pequeno intervalo. No entanto, cada tentativa de bloqueio resulta em tráfego de rede, adicionando congestionamento a qualquer tráfego de rede existente e resultando em desempenho geral reduzido para todos os usuários. Para ajudar a evitar este cenário, você pode chamar a função SYS(3051) - Set Lock Retry Interval para ajustar o intervalo entre tentativas de bloqueio. Usar um intervalo maior, que resulta em menos tentativas por segundo, reduz o tráfego de rede e aumenta o desempenho.

Para obter mais informações, consulte SYS(3051) - Set Lock Retry Interval.

# Usando processamento de transações de forma eficiente

Ao usar processamento de transações, projete transações para que minimizem seu impacto sobre outros usuários. As transações devem começar e terminar o mais próximo possível da atualização real dos dados. Uma transação ideal contém somente instruções de atualização de dados.

Quando você anexa registros a uma tabela, o Visual FoxPro bloqueia o cabeçalho da tabela. O cabeçalho permanece bloqueado durante a duração da transação, impedindo que outros usuários também anexem registros. Enquanto uma transação permanece aberta, quaisquer bloqueios definidos durante a transação permanecem bloqueados até que a transação seja confirmada ou revertida. Mesmo se você chamar um comando UNLOCK explícito, os bloqueios permanecem até que você chame o comando END TRANSACTION ou ROLLBACK Command. Para obter mais informações, consulte UNLOCK Command, END TRANSACTION Command e ROLLBACK Command.

Por exemplo, suponha que você adicione processamento de transações a atualizações de tabela feitas a partir de um formulário. Em vez de abrir uma transação, executar o formulário e depois confirmar a transação quando o formulário é fechado, coloque instruções de processamento de transações no código do evento Click de um botão de comando Save, conforme mostrado nas seguintes linhas de código de exemplo:

```foxpro
BEGIN TRANSACTION
UPDATE Products SET reorder_amt = 0 WHERE discontinued = .T.
END TRANSACTION
```
