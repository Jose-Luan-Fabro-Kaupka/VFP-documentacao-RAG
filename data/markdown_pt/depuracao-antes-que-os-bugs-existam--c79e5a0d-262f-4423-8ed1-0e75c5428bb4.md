# Depuração antes que os bugs existam

Boas práticas de codificação, como usar espaço em branco, incluir comentários e seguir convenções de nomenclatura, ajudam a reduzir o número de bugs no seu código. No entanto, uma das melhores maneiras de criar uma aplicação robusta é procurar problemas potenciais antes que ocorram. Para facilitar testes e depuração posteriormente, execute as seguintes etapas no início do processo de desenvolvimento:
 - Criando um ambiente de teste
- Escrevendo código para evitar erros
- Definindo asserts
- Rastreando sequências de eventos

# Criando um ambiente de teste

Embora o ambiente de dados configurado para a aplicação seja importante, o ambiente de sistema no qual você espera que a aplicação seja executada é igualmente importante. Para garantir a portabilidade da sua aplicação e criar um ambiente apropriado para testes e depuração, considere os seguintes itens:
 - Hardware e software.
- Caminhos do sistema e propriedades de arquivos.
- Estrutura de diretórios e localizações de arquivos.

### Hardware e software

Para máxima portabilidade, é recomendável desenvolver aplicações na plataforma mínima comum na qual você espera que sejam executadas. Para estabelecer uma plataforma base, use as seguintes diretrizes:
 - Desenvolva suas aplicações usando o modo de vídeo mínimo comum.
- Determine os requisitos básicos de RAM e espaço de armazenamento em mídia, incluindo drivers necessários ou software executado simultaneamente.
- Considere cenários especiais de memória, arquivo e bloqueio de registros para versões em rede versus versões autônomas de aplicações.

### Caminhos do sistema e propriedades de arquivos

Para garantir que todos os arquivos de programa necessários estejam facilmente acessíveis em cada computador que executa sua aplicação, pode ser necessário uma configuração base de arquivos. Para ajudar a definir uma configuração base, considere as seguintes perguntas:
 - Sua aplicação requer caminhos comuns do sistema?
- Você definiu propriedades de acesso a arquivos apropriadas?
- As permissões de rede estão configuradas corretamente para cada usuário?

### Estrutura de diretórios e localizações de arquivos

Se o seu código-fonte referencia caminhos ou nomes de arquivo absolutos, esses caminhos e arquivos exatos devem existir quando sua aplicação for instalada em qualquer outro computador. Evite esse cenário executando as seguintes tarefas:
 - Use arquivos de configuração do Visual FoxPro. Para informações adicionais sobre o uso de arquivos de configuração, consulte Customizing the Visual FoxPro Environment.
- Crie um diretório ou estrutura de diretórios separada para manter arquivos-fonte separados dos arquivos de aplicação gerados. Assim, você pode testar as referências da aplicação concluída e saber exatamente quais arquivos distribuir.
- Use caminhos relativos.

# Escrevendo código para evitar erros

Você pode ajudar a reduzir erros antecipando onde eles podem ocorrer e escrevendo código que evite esses erros.

A tabela a seguir ilustra como evitar condições de erro de exemplo.

| Condição de erro | Como evitar o erro |
| --- | --- |
| O comando SKIP move o ponteiro de registro em uma tabela para o próximo registro. No entanto, se o ponteiro de registro passou do último registro na tabela, chamar o comando SKIP gera um erro. | Verifique o fim do arquivo: IF !EOF() SKIP IF EOF() GO BOTTOM ENDIF ENDIF |
| A linha de código a seguir exibe a caixa de diálogo Open para que um usuário possa abrir uma tabela em uma nova área de trabalho: USE GETFILE('DBF') IN 0 O usuário pode escolher Cancel na caixa de diálogo Open ou digitar o nome de um arquivo que não existe. O usuário também pode digitar o nome de um arquivo que não é uma tabela do Visual FoxPro. | Certifique-se de que o arquivo existe antes que o usuário tente usá-lo: cNewTable = GETFILE('DBF') IF FILE(cNewTable) USE (cNewTable) IN 0 ENDIF Se o usuário digitar o nome de um arquivo que não é uma tabela do Visual FoxPro e a mensagem de erro 15, "Not a table", ocorrer, você pode exibir uma mensagem solicitando que o usuário abra outro arquivo, por exemplo, "Please open another file. This file is not a table." |

# Definindo asserts

Asserts exibem caixas de mensagem quando uma expressão lógica é avaliada como False (.F.). Você pode incluir asserts no seu código para verificar suposições sobre o ambiente de execução do código. Você pode usar o comando ASSERT para definir asserts. Para obter mais informações, consulte o comando ASSERT.

# Rastreando sequências de eventos

Ao rastrear sequências de eventos em relação a outros eventos, você pode determinar o local mais eficiente para adicionar código aos eventos. Para obter mais informações, consulte Como: rastrear sequências de eventos.
