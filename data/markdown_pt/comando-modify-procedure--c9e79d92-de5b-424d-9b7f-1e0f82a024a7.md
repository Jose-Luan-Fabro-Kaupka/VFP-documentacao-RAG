# Comando MODIFY PROCEDURE

Abre o editor de texto do Visual FoxPro, tornando possível criar novas stored procedures para o banco de dados atual ou modificar stored procedures existentes no banco de dados atual.

```foxpro
MODIFY PROCEDURE [NOWAIT]
```

#### Parâmetros
 **NOWAIT**
Continua a execução do programa depois que o editor de procedures do banco de dados atual é aberto. O programa não aguarda o fechamento do editor, mas continua a execução na linha do programa imediatamente após a linha que contém MODIFY PROCEDURE NOWAIT. Sem a cláusula NOWAIT, MODIFY PROCEDURE abre um editor de procedures e a execução do programa pausa até você fechar o editor.

# Observações

Um banco de dados deve estar aberto antes que você possa criar ou modificar stored procedures. Stored procedures normalmente são especificadas em triggers Delete, Insert ou Update criados para um banco de dados com CREATE TRIGGER.

Stored procedures no banco de dados atual podem ser executadas como outras procedures do Visual FoxPro em um arquivo de procedures ou programa aberto. Consulte o Comando PROCEDURE para uma descrição da ordem e do local em que o Visual FoxPro procura procedures.

# Exemplo

O exemplo a seguir abre o banco de dados `testdata` e usa MODIFY PROCEDURE para abrir o editor de texto do Visual FoxPro, tornando possível criar novas stored procedures ou modificar stored procedures existentes.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
MODIFY PROCEDURE  && Opens the Visual FoxPro text editor
```
