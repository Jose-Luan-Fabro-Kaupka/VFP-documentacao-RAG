# Operação inválida para exibição offline enquanto usada online (Erro 2008)

Algumas operações não são válidas quando uma exibição offline está sendo usada online.
 - Você tentou alterar o modo de buffer da exibição. Por definição, exibições offline usadas online estão no modo de buffer de tabela. Não chame CURSORSETPROP( ) para alterar o modo de buffer.
- Você tentou criar um índice. Não use SET ORDER TO ou INDEX em exibições offline enquanto estiver usando online.
