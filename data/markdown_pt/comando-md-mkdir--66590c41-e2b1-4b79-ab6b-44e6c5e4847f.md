# Comando MD | MKDIR

Cria um novo diretório ou subdiretório no disco.

```foxpro
MD cPath | MKDIR cPath
```

#### Parâmetros
 **cPath**
Especifica um diretório ou um caminho (com um designador de unidade e diretórios). Se cPath for um diretório sem designador de unidade, o diretório é criado como um subdiretório do diretório padrão atual do Microsoft Visual FoxPro.

# Observações

O Visual FoxPro gera uma mensagem de erro se você tentar criar um diretório que já existe.

# Exemplo

O exemplo a seguir usa MKDIR para criar um novo diretório chamado `mytstdir`, depois CHDIR é usado para mudar para o novo diretório. GETDIR( ) é usado para exibir a estrutura de diretórios e depois RMDIR é usado para remover o diretório recém-criado. GETDIR( ) é usado para exibir a estrutura de diretórios novamente.

```foxpro
SET DEFAULT TO HOME()  && Restore Visual FoxPro directory
MKDIR mytstdir  && Create a new directory
CHDIR mytstdir  && Change to the new directory
= GETDIR()  && Display the Select Directory dialog box
SET DEFAULT TO HOME()  && Restore Visual FoxPro directory
RMDIR mytstdir  && Remove the new directory
= GETDIR()  && Display the Select Directory dialog box
```
