# INSERT não pode ser emitido quando o buffer de linha ou tabela está habilitado ou quando restrições de integridade estão em vigor (Erro 1588)

Desative o buffer de linha e tabela definindo a propriedade Buffering como 1 com a função CURSORSETPROP( ), ou use o comando APPEND em vez do comando INSERT.
