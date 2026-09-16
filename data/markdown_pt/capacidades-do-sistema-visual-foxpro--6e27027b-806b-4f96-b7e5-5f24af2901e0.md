# Capacidades do sistema Visual FoxPro

Diferentes partes do Visual FoxPro possuem limites de capacidade do sistema. As tabelas a seguir listam esses limites.

> **Observação:** Algumas capacidades podem ser limitadas pela memória disponível e espaço em disco.

# Arquivos de tabela e índice

| Recurso | Capacidade |
| --- | --- |
| Número máximo de registros por arquivo de tabela. | 1 bilhão |
| Tamanho máximo de um arquivo de tabela. | 2 gigabytes |
| Tamanho máximo de um arquivo FPT. | 2 gigabytes |
| Número máximo de caracteres por registro. | 65.500 |
| Número máximo de campos por registro 1 . | 255 |
| Número máximo de tabelas abertas ao mesmo tempo 2 . | 65.535 |
| Número máximo de caracteres por campo de tabela. | 254 |
| Número máximo de bytes por chave de índice em um índice não compacto 3 . | 100 |
| Número máximo de bytes por chave de índice em um índice compacto 3 . | 240 |
| Número máximo de arquivos de índice abertos por tabela 2 . | Limitado pela memória disponível |
| Número máximo de índices abertos em todas as áreas de trabalho 2 . | Limitado pela memória disponível |
| Número máximo de relações. | Limitado pela memória disponível |
| Comprimento máximo de expressões relacionais. | Limitado pela memória disponível |

# Campos

| Recurso | Capacidade |
| --- | --- |
| Tamanho máximo de campos de caractere. | 254 |
| Tamanho máximo de campos numéricos e float. | 20 |
| Número máximo de caracteres em nomes de campos em uma tabela livre. | 10 |
| Número máximo de caracteres em nomes de campos para uma tabela contida em um banco de dados. | 128 |
| Valor mínimo de um inteiro. | -2.147.483.647 |
| Valor máximo de um inteiro. | 2.147.483.647 |
| Dígitos de precisão em computações numéricas. O Visual FoxPro pode manipular números até 9007199254740992 (2^53) em computações exatas. | 16 |
| Diversos: 64 bits = 8 bytes Maior número = 10 ^ 308 = 2 ^ 1023 -> 10 bits por expoente + 1 para sinal do expoente mais 1 para sinal do número => 12 bits Deixando 52 bits para a mantissa + 1 para bit normalizado implícito -> 53 bits LOG10(2^53) = 15,95 dígitos decimais de precisão | |

# Variáveis e matrizes

| Recurso | Capacidade |
| --- | --- |
| Número padrão de variáveis. | 16.384 |
| Número máximo de variáveis. | 65.000 |
| Número máximo de matrizes. | 65.000 |
| Número máximo de elementos por matriz. | Normal: 2 gigabytes Matriz de membros: 2 gigabytes Matriz de objetos membros: 65.000 |

# Arquivos de programa e procedimento

| Recurso | Capacidade |
| --- | --- |
| Número máximo de linhas em arquivos de programa-fonte. | Limitado pela memória disponível |
| Tamanho máximo de módulos de programa compilados 4 . | Limitado pela memória disponível |
| Número máximo de procedimentos por arquivo. | 65.535 |
| Número máximo de chamadas DO aninhadas. Dica Você pode alterar o nível padrão de aninhamento usando um arquivo de configuração que inclua a configuração STACKSIZE. Para obter mais informações, consulte Special Terms for Configuration Files . | 128 (Padrão) |
| Número máximo de níveis de aninhamento READ. | 5 |
| Número máximo de comandos de programação estruturada aninhados. | 384 |
| Número máximo de parâmetros passados. | 26 |
| Número máximo de transações. | 5 |
| Número máximo de níveis de compilador para #INCLUDE . | 4 |

# Relatórios

| Recurso | Capacidade |
| --- | --- |
| Número máximo de objetos em uma definição de relatório. | Limitado pela memória disponível |
| Altura máxima de uma única banda de relatório. | 20 polegadas | 50,8 cm | 1920 pixels |
| Número máximo de níveis de agrupamento de dados. | 74 |
| Comprimento máximo de nomes de variáveis de relatório de caractere ou uma expressão de relatório. | 255 |
| Número máximo de bandas Detail. | 20 |
| Número máximo de páginas em um relatório em tempo de execução. | 65534 Na visualização assistida por objetos, limitado pelos recursos GDI+ disponíveis |

# Diversos

| Recurso | Capacidade |
| --- | --- |
| Número máximo de janelas abertas (todos os tipos) 2 . | Limitado pela memória disponível |
| Número máximo de janelas Browse abertas. | 255 |
| Número máximo de caracteres por cadeia de caracteres ou variável de memória. | 16.777.184 |
| Número máximo de caracteres por linha de comando. | 8.192 |
| Número máximo de caracteres por controle de label em um relatório. | 252 |
| Número máximo de caracteres por linha substituída por macro. | 8.192 |
| Número máximo de arquivos abertos. | Limite do sistema operacional |
| Máximo de pressionamentos de tecla em macro de teclado. | 1.024 |
| Máximo de campos que podem ser selecionados por uma instrução SQL SELECT. | 255 |
| Comprimento máximo de um literal de cadeia de caracteres. | 255 |
| Tamanho máximo de arquivo acessível via funções de arquivo de baixo nível | 2 gigabytes |

1 Se um ou mais campos permitem valores nulos, o limite é reduzido em um para 254 campos.

2 Limitado pela memória e handles de arquivo disponíveis. Arquivos .cdx usam apenas um handle de arquivo.

3 Se a sequência de ordenação estiver definida como MACHINE, cada caractere usa um byte. Se a sequência de ordenação não estiver definida como MACHINE, cada caractere usa dois bytes. Se o campo indexado suporta valores nulos, um byte adicional é usado na chave de índice. Observe que índices não-machine são sempre compactos.

4 Um módulo de programa é um procedimento. Um programa ou aplicação pode conter um número ilimitado de módulos de programa.
