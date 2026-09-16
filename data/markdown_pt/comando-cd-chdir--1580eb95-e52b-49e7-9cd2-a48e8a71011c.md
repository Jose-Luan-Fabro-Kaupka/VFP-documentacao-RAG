# Comando CD | CHDIR

Altera o diretório padrão do Visual FoxPro para o diretório especificado.

```foxpro
CD cPath | CHDIR cPath
```

#### Parâmetros
 **cPath**
Especifica um dos seguintes: um designador de unidade; um designador de unidade com diretório; um diretório filho; qualquer uma dessas opções usando a notação abreviada do MS-DOS (\ ou ..). Ao usar .. para ir ao diretório pai, inclua um espaço entre CD ou CHDIR e os dois pontos.

# Observações

Use CD ou CHDIR para especificar o diretório padrão do Visual FoxPro. O Visual FoxPro procura arquivos nesse diretório. Se não encontrar um arquivo, procurará no caminho do Visual FoxPro, caso tenha sido especificado. Use SET PATH para definir esse caminho.

Se você criar um arquivo sem especificar onde colocá-lo, ele será criado no diretório padrão do Visual FoxPro.

Você pode localizar diretórios ocultos ou de sistema com CD e CHDIR. Para obter mais informações, consulte Função FILE( ) e Função DIRECTORY( ).

Os comandos CD e CHDIR não têm suporte em servidores DLL de thread única ou múltipla. Eles alteram o diretório padrão de todo o processo, afetando todas as threads. Em servidores DLL, use o comando SET PATH no lugar de SET DEFAULT.

# Exemplo

O exemplo a seguir usa SET DEFAULT para alterar o diretório padrão do Visual FoxPro para o diretório de inicialização. MKDIR cria um diretório chamado `mytestdir`, e CHDIR muda para ele. GETDIR( ) mostra a estrutura na caixa de diálogo Select Directory. Em seguida, SET DEFAULT retorna ao diretório de inicialização, RMDIR remove o novo diretório e GETDIR( ) exibe a estrutura original.

```foxpro
SET DEFAULT TO HOME()
MKDIR mytestdir
CHDIR mytestdir  = GETDIR()
SET DEFAULT TO HOME()
RMDIR mytestdir  = GETDIR()
```
