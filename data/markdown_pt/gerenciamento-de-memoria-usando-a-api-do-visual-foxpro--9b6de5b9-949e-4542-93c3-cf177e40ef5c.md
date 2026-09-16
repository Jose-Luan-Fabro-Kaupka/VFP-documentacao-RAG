# Gerenciamento de memória usando a API do Visual FoxPro

A API do Visual FoxPro fornece acesso direto ao gerenciador de memória dinâmica do Visual FoxPro. Rotinas da API que solicitam alocações de memória retornam identificadores de memória, que identificam a memória. A arquitetura de carregamento de segmentos do Visual FoxPro usa identificadores em vez de ponteiros para que possa gerenciar a memória de forma mais eficiente.

Um identificador de memória é essencialmente um índice em uma matriz de ponteiros. Os ponteiros apontam para blocos de memória que o Visual FoxPro conhece. Quase todas as referências à memória na API são feitas através de identificadores em vez dos ponteiros C mais convencionais.

# Entendendo pilhas

O controle ou biblioteca que você cria não tem sua própria pilha de memória. Em vez disso, ele usa a pilha de memória do programa chamador, ou neste caso, a pilha do Visual FoxPro. No entanto, você não pode controlar o tamanho da pilha do Visual FoxPro nem afetar a quantidade de espaço de pilha disponível para um controle ActiveX ou FLL.

Em circunstâncias normais, essa distinção não é importante. A pilha do Visual FoxPro é geralmente grande o suficiente para manter as variáveis automáticas que você pode precisar alocar em um controle ou biblioteca. Se você ficar sem espaço de pilha, você sempre pode alocar memória adicional no heap dinamicamente.

# Regras para usar identificadores

As seguintes regras se aplicam à alocação e liberação de identificadores de memória:
 - Os usuários devem liberar todos os identificadores que alocam, incluindo identificadores alocados por funções como _Load() .
- _Load() só cria um identificador quando a variável que você está carregando é uma cadeia de caracteres (ou seja, ev_type = 'C' ). Todos os outros tipos de dados armazenam seus valores na estrutura Value em si, enquanto carregar uma cadeia de caracteres coloca um MHANDLE em ev_handle da estrutura Value.
- Em uma biblioteca FLL, o Visual FoxPro assume a responsabilidade de liberar todos os identificadores retornados com _RetVal( ) . Os usuários não devem liberar esses identificadores, mesmo se os alocarem.
- Os usuários não devem liberar identificadores passados a eles em seu ParamBlk . Cuidado Ao escrever uma rotina externa que chama funções, certifique-se de seguir todas as regras e verificar os resultados de retorno. Um ponteiro ou referência de identificador incorreta pode danificar as estruturas de dados internas do Visual FoxPro, causando uma terminação anormal imediata ou problemas atrasados, que podem resultar em perda de dados.
