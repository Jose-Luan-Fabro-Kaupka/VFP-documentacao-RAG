# Função STRTOFILE( )

Grava o conteúdo de uma cadeia de caracteres em um arquivo.

> **Observação:** STRTOFILE( ) não grava em arquivos ocultos ao executar o Visual FoxPro no Windows 2000 e posteriores.

```foxpro
STRTOFILE(cExpression, cFileName [, lAdditive | nFlag])
```

#### Parâmetros
 **cExpression**
Especifica a cadeia de caracteres que é gravada no arquivo. cExpression pode ser uma cadeia de caracteres literal, uma expressão que avalia para uma cadeia de caracteres ou uma variável, elemento de matriz ou campo do tipo caractere.
**cFileName**
Especifica o nome do arquivo no qual a cadeia de caracteres é gravada. Inclua um caminho com o nome do arquivo se o arquivo estiver em um diretório diferente do diretório padrão atual. Se o arquivo especificado não existir, o Visual FoxPro cria automaticamente.
**lAdditive (para compatibilidade com versões anteriores)**
Especifica se a cadeia de caracteres é anexada ao final do arquivo. Se lAdditive for true (.T.), a cadeia de caracteres é anexada ao final do arquivo. Se lAdditive for false (.F.) (o padrão), o arquivo é substituído pela cadeia de caracteres. Você é solicitado se deseja substituir um arquivo existente se SET SAFETY estiver definido como ON. Se SET SAFETY estiver definido como OFF, o arquivo é substituído sem aviso.
**nFlag**
A partir do Visual FoxPro 7, você pode usar o parâmetro nFlag em vez de lAdditive, o que também permite escolher gravar marcas de ordem de bytes UTF-8 e Unicode. A tabela a seguir descreve os valores válidos de nFlag. nFlag Bit Descrição 0 (padrão) 0000 O arquivo é substituído pela cadeia de caracteres (anteriormente lAdditive =.f.) 1 0001 A cadeia de caracteres é anexada ao final do arquivo (anteriormente lAdditive =.t.). 2 0010 Grava a Marca de Ordem de Bytes Unicode (BOM) FF FE no início do arquivo. cExpression é assumida como UNICODE, portanto nenhuma tradução é realizada. O arquivo é substituído 4 0100 Grava a Marca de Ordem de Bytes UTF-8 (BOM) EF BB BF no início do arquivo. cExpression é assumida como UTF-8, portanto nenhuma tradução é realizada. O arquivo é substituído.

# Valor de retorno

Numérico; o número de bytes gravados no arquivo.

# Observações

Um valor nFlag de 3 ou 5 não é válido. Você não pode tentar gravar uma nova Marca de Ordem de Bytes se o bit 1 de nFlag, Additive, estiver definido.

Diferentemente das versões anteriores do Visual FoxPro, STRTOFILE( ) abre um arquivo no modo Shared em vez de Exclusive. Isso é útil quando vários servidores tentam gravar simultaneamente no mesmo arquivo. Por causa dessa alteração, você pode não precisar verificar se STRTOFILE( ) retorna 0 (falha ao abrir um arquivo).
