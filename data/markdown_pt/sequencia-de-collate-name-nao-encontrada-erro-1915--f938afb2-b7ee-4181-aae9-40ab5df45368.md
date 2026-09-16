# Sequência de collate "name" não encontrada (Erro 1915)

Este erro ocorre ao tentar usar uma sequência de collate que não é suportada pela code page atual. A sequência de collate atribuída com o comando SET COLLATE ou a cláusula COLLATE nos comandos CREATE TABLE - SQL, ALTER TABLE - SQL ou INDEX deve ser uma sequência de collate válida do Visual FoxPro.

Você deve especificar uma code page compatível no arquivo de configuração do Visual FoxPro. Por exemplo, você pode ver o erro "Collating sequence "CZECH" is not found" ao emitir o comando:

```foxpro
SET COLLATE TO "CZECH"
```

Para habilitar suporte à sequência de collate CZECH, adicione a seguinte linha de código ao arquivo Config.fpw e reinicie o Visual FoxPro:

```foxpro
CODEPAGE = 1250
```

Para obter mais informações sobre sequências de collate, consulte SET COLLATE Command para sequências de collate válidas e Optimizing International Applications.
