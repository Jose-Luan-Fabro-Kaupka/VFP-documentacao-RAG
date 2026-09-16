# Comando DISPLAY STRUCTURE

Exibe a estrutura de um arquivo de tabela. O nome de cada campo na tabela é exibido com seu tipo e largura.

```foxpro
DISPLAY STRUCTURE [IN nWorkArea | cTableAlias]
   [TO PRINTER [PROMPT] | TO FILE FileName [ADDITIVE]] [NOCONSOLE]
```

#### Parâmetros
 **IN nWorkArea | cTableAlias**
Exibe a estrutura da tabela em uma área de trabalho diferente das áreas de trabalho atuais. nWorkArea especifica o número da área de trabalho e cTableAlias especifica o alias da tabela.
**TO PRINTER [PROMPT]**
Direciona a saída de DISPLAY STRUCTURE para uma impressora. Você pode incluir a cláusula opcional PROMPT para exibir uma caixa de diálogo antes do início da impressão. Nessa caixa de diálogo, você pode ajustar as configurações da impressora, incluindo o número de cópias e os números de página a imprimir. As configurações da impressora que você pode ajustar dependem do driver de impressora instalado no momento. Coloque a palavra-chave PROMPT imediatamente após TO PRINTER.
**TO FILE FileName**
Direciona a saída de DISPLAY STRUCTURE para o arquivo especificado com FileName . Se o arquivo já existir e SET SAFETY estiver ON, você será perguntado se deseja substituir o arquivo.
**ADDITIVE**
Anexa ao final do arquivo nomeado. Se você omitir ADDITIVE , o arquivo será substituído pelo valor da expressão.
**NOCONSOLE**
Suprime a saída para a janela principal do Visual FoxPro ou para a janela definida pelo usuário ativa.

# Observações

DISPLAY STRUCTURE também exibe o seguinte:
 - A largura total de todos os campos.
- O número de casas decimais no campo se o campo for do tipo Numeric , Double ou Float .
- Suporte a valores nulos para cada campo.
- Se o campo for um campo de autoincremento, os valores Next e Step nas duas últimas colunas.
- O número atual de registros na tabela e a data da última atualização.
- O tamanho do bloco do campo memo se a tabela tiver um campo memo associado.
- A página de código da tabela.
- Se a tabela estiver associada a um índice composto estrutural, e se uma tag, ou entrada de índice, no índice composto estrutural tiver o mesmo nome de um campo na tabela, DISPLAY STRUCTURE exibe a ordem da tag, ascendente ou descendente, e a sequência de ordenação da tag ao lado do nome do campo. Para obter mais informações sobre índices compostos estruturais e tags, consulte Comando INDEX .

Se SET FIELDS for usado para limitar o acesso a campos na tabela, um sinal de maior que (>) aparece ao lado dos nomes dos campos que podem ser acessados.

# Exemplo

No exemplo a seguir, a tabela `customer` no banco de dados `testdata` é aberta. DISPLAY STRUCTURE é usado para exibir a estrutura da tabela.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer  && Opens Customer table
CLEAR
DISPLAY STRUCTURE
```
