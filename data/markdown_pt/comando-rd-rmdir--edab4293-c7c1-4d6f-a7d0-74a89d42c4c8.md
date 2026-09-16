# Comando RD | RMDIR

Remove um diretório ou pasta do disco.

```foxpro
RD cPath | RMDIR cPath
```

#### Parâmetros
 **cPath**
Especifica o nome e o local do diretório ou pasta a ser removido do disco.

# Observações

O Visual FoxPro gera uma mensagem de erro se você tentar remover um diretório ou pasta que não está vazio.

# Exemplo

O exemplo a seguir usa MKDIR para criar um novo diretório chamado `mytstdir`; em seguida, CHDIR é usado para mudar para o novo diretório. GETDIR( ) é usado para exibir a estrutura de diretórios e, depois, RMDIR é usado para remover o diretório recém-criado. GETDIR( ) é usado novamente para exibir a estrutura de diretórios.

```foxpro
SET DEFAULT TO HOME()  && Restore Visual FoxPro directory
MKDIR mytstdir  && Create a new directory
CHDIR mytstdir  && Change to the new directory
= GETDIR()  && Display the Select Directory dialog box
SET DEFAULT TO HOME()  && Restore Visual FoxPro directory
RMDIR mytstdir  && Remove the new directory
= GETDIR()  && Display the Select Directory dialog box
```
