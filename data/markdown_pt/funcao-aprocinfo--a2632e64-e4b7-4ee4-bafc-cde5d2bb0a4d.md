# Função APROCINFO( )

Cria uma matriz contendo elementos da linguagem Visual FoxPro contidos em um arquivo de programa.

```foxpro
APROCINFO(ArrayName, cFileName [, nType])
```

#### Parâmetros
 **ArrayName**
Especifica o nome da matriz a ser criada.
**cFileName**
Especifica o nome do arquivo do programa que esta função percorre.
**nType**
Especifica o tipo de informação retornada em cArrayName. A tabela a seguir especifica valores nType válidos e descreve a informação retornada por cada valor nType. nType Descrição Detalhes da matriz 0 (padrão Popula a matriz com todas as informações do documento. Coluna1 – conteúdo Doc View Coluna2 – linha Coluna3 – tipo Coluna4 – indentação A indentação é usada com diretivas de pré-processador para mostrar níveis aninhados de instruções do tipo #IF. 1 Popula a matriz apenas com as definições de classe no documento. Coluna1 – nome da classe Coluna2 – linha Coluna3 – parentclass Coluna4 - is OLEpublic 2 Popula a matriz apenas com informações de procedimento de classe (definição de classe excluída) Coluna1 – conteúdo Doc View Coluna2 – linha 3 Popula a matriz com #define e outras diretivas de pré-processador no documento. Coluna1 – conteúdo Doc View Coluna2 – linha Coluna3 – tipo A tabela a seguir descreve os valores "type" retornados na Coluna3 para valores nType de 0 e 3. nType Descrição Define diretiva de pré-processador #DEFINE Directive Outras diretivas de pré-processador, como #IF Class Linha de definição de classe Procedure Procedure, Method ou Event

# Valor de retorno

Numeric. APROCINFO( ) retorna o número de linhas adicionadas à matriz.

# Observações

O Visual FoxPro cria automaticamente a matriz que você especifica se ela ainda não existir. O Visual FoxPro aumenta ou trunca automaticamente o tamanho da matriz para acomodar as informações retornadas. Esta função suporta apenas arquivos de programa (PRG).
