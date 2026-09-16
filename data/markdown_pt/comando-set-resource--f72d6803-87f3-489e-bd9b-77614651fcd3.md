# Comando SET RESOURCE

Atualiza ou especifica um arquivo de recursos. O arquivo de recursos é uma tabela do Visual FoxPro que contém informações sobre recursos do sistema e definidos pelo usuário, como macros de teclado, preferências, localizações e tamanhos de janelas do sistema, entradas de diário e assim por diante. Há duas versões da sintaxe.

```foxpro
SET RESOURCE ON | OFF
```

```foxpro
SET RESOURCE TO [FileName]
```

#### Parâmetros
 **ON**
Especifica que alterações feitas no ambiente Visual FoxPro são salvas no arquivo de recursos. (Padrão)
**OFF**
Especifica que alterações feitas no ambiente Visual FoxPro não são salvas no arquivo de recursos.
**TO [ FileName ]**
Especifica que alterações feitas no ambiente Visual FoxPro são salvas em um arquivo de recursos ( FileName ) diferente do arquivo de recursos padrão FoxUser.dbf. Emita SET RESOURCE TO sem um nome de arquivo de recursos para abrir o arquivo de recursos padrão FoxUser.dbf. Emitir SET RESOURCE TO executa implicitamente SET RESOURCE ON.
