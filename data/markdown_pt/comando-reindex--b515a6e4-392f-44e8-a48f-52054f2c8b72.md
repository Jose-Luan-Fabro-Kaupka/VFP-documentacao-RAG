# Comando REINDEX

Reconstrói arquivos de índice abertos.

REINDEX atualiza todos os arquivos de índice abertos na área de trabalho selecionada.

```foxpro
REINDEX [COMPACT]
```

#### Parâmetros
 **COMPACT**
Converte arquivos de índice simples regulares (.idx) em arquivos .idx compactos.

# Observações

Os arquivos de índice ficam desatualizados quando você abre uma tabela sem abrir seus arquivos de índice correspondentes e faz alterações nos campos-chave dos arquivos de índice. Quando os arquivos de índice ficam desatualizados, você pode atualizá-los reindexando.

O Visual FoxPro reconhece cada tipo de arquivo de índice: arquivos de índice composto (.cdx), arquivos .cdx estruturais e arquivos de índice simples (.idx), e os reindexa adequadamente. Atualiza todas as tags em arquivos .cdx e atualiza arquivos .cdx estruturais, que abrem automaticamente com a tabela.

> **Dica:** Para acelerar o tráfego de rede durante uma operação REINDEX, você pode usar SYS(3050) - Set Buffer Memory Size para definir a memória de buffer com um tamanho grande o suficiente para armazenar a tabela inteira. Durante a primeira passagem, a tabela é paginada localmente e passagens posteriores não tentarão ler dados paginados do computador remoto.

Quaisquer arquivos de índice criados com a palavra-chave UNIQUE do comando INDEX ou com SET UNIQUE ON mantêm seu status UNIQUE quando reindexados.

Para REINDEX arquivos de índice desatualizados, emita estes comandos:

```foxpro
USE TableName INDEX OutdatedIndexNames
REINDEX
```

# Exemplo

No exemplo a seguir, ISEXCLUSIVE( ) verifica se a tabela `customer` foi aberta para uso exclusivo. A tabela não é reindexada, pois a da área de trabalho atual não foi aberta para uso exclusivo.

```foxpro
cExclusive = SET('EXCLUSIVE')
SET EXCLUSIVE OFF
SET PATH TO (HOME(2) + 'Data\')
OPEN DATA testdata  && Opens the test databsase
USE Customer     && Not opened exclusively
USE Employee IN 0 EXCLUSIVE    && Opened exclusively in another work area
IF ISEXCLUSIVE()
 REINDEX  && Can only be done if table opened exclusively
ELSE
  WAIT WINDOW 'The table has to be exclusively opened'
ENDIF
SET EXCLUSIVE &cExclusive
```
