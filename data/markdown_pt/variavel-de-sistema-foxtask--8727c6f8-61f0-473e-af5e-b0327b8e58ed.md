# Variável de Sistema _FoxTask

Especifica o nome da tabela FOXTASK que suporta o Visual FoxPro Task Manager.

```foxpro
_FoxTask [= cDBFFileName]
```

#### Parâmetros
 **cDBFFileName**
Especifica o nome do arquivo a ser usado pelo Editor do Visual FoxPro e pelo Task List Manager para armazenar atalhos da Tasklist.

# Observações

Por padrão, o arquivo é nomeado foxtask.dbf e armazenado na pasta de aplicativos do usuário do Windows ou no local HOME( ). A tabela a seguir descreve a estrutura de foxtask.dbf

| Nome do Campo | Tipo | Largura | Descrição |
| --- | --- | --- | --- |
| UNIQUEID | C | 10 | Especifica o ID exclusivo do Visual FoxPro |
| TIMESTAMP | N | 10 | Especifica o timestamp do Visual FoxPro |
| FILENAME | M | 4 | Especifica o nome do arquivo |
| CLASS | M | 4 | Especifica o nome da classe (.vcx, .scx) |
| METHOD | M | 4 | Nome do método (.vcx, .scx) |
| LINE | N | 6 | Especifica o número da linha |
| CONTENTS | M | 4 | Especifica o conteúdo da linha |
| TYPE | C | 1 | "S" – para atalho; outros podem ser definidos pelo usuário |
| DUEDATE | D | 8 | Data de vencimento definida pelo usuário |
| PRIORITY | N | 1 | Especifica uma configuração de prioridade definida pelo usuário para o item 0 = baixa1 = média2 = alta |
| STATUS | N | 1 | Estado de conclusão de uma tarefa 0 = não concluída1 = concluída |

Você pode especificar um nome diferente para a tabela da tasklist usando a propriedade FoxTask conforme no exemplo a seguir:

# Exemplo

```foxpro
_FOXTASK = MyTasks.dbf
```
