# Comando DISPLAY STATUS

Exibe o status do ambiente do Visual FoxPro.

```foxpro
DISPLAY STATUS [TO PRINTER [PROMPT] | TO FILE FileName [ADDITIVE]] [NOCONSOLE]
```

#### Parâmetros
 **TO PRINTER [PROMPT]**
Direciona a saída de DISPLAY STATUS para uma impressora. Você pode incluir a cláusula opcional PROMPT para exibir uma caixa de diálogo de impressão antes do início da impressão. Nesta caixa de diálogo, você pode ajustar as configurações da impressora, incluindo o número de cópias e os números de página a imprimir. As configurações da impressora que você pode ajustar dependem do driver de impressora atualmente instalado. Coloque a palavra-chave PROMPT imediatamente após TO PRINTER.
**TO FILE FileName**
Direciona a saída de DISPLAY STATUS para o arquivo especificado com FileName . Se o arquivo já existir e SET SAFETY estiver ON, você será perguntado se deseja sobrescrever o arquivo.
**ADDITIVE**
Anexa ao final do arquivo nomeado. Se você omitir ADDITIVE, o arquivo é sobrescrito com o valor da expressão.
**NOCONSOLE**
Suprime a saída para a janela principal do Visual FoxPro ou para a janela definida pelo usuário ativa.

# Observações

Esta forma de DISPLAY lista informações sobre o ambiente atual do Visual FoxPro. As categorias de informação e as informações em cada categoria são as seguintes.

Informações de tabela e arquivo de índice:
 - Tabelas abertas
- Arquivos memo abertos
- Aliases de tabela
- Páginas de código de tabela
- Relações de tabela
- Índices ativos
- Chaves de arquivo de índice
- O arquivo de índice ou tag de controle
- Arquivos compostos estruturais abertos
- Tags de índice composto abertas
- O status do atributo compartilhado de cada tabela aberta
- Os registros bloqueados atualmente em cada tabela
- A configuração de uso EXCLUSIVE
- A configuração LOCK
- A configuração MULTILOCKS
- O valor SET REFRESH
- O valor SET REPROCESS

Informações de arquivo de baixo nível aberto:
 - Arquivos de baixo nível abertos
- O número do identificador de arquivo para cada arquivo de baixo nível
- A posição do ponteiro de arquivo para cada arquivo de baixo nível
- Atributos de leitura/gravação para cada arquivo de baixo nível

Informações adicionais do ambiente Visual FoxPro:
 - O arquivo de procedimento em uso
- O tipo de processador
- O caminho do Visual FoxPro
- O diretório padrão do Visual FoxPro
- O destino de impressão
- A configuração de margem
- A área de trabalho atual
- Configurações de comandos SET
- Módulos binários atualmente carregados
- Informações DDE no Visual FoxPro
- Página de código atual
- Sequência de ordenação atual
- Página de código do compilador
- Formato de data atual
- Combinação de teclas de macro de teclado
- Como parâmetros UDF são passados
- Opções de textmerge
- Funções de biblioteca compartilhada externa registradas (DLLs)
