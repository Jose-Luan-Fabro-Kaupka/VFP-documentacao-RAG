# Comando COMPILE

Compila um ou mais arquivos-fonte especificados e cria um arquivo-objeto para cada um. Há duas versões da sintaxe.

```foxpro
COMPILE [DATABASE | FORM | CLASSLIB | LABEL | REPORT] cFileName | cFileSkeleton | ? [ALL]
```

```foxpro
COMPILE cFileName | cFileSkeleton | ? [ENCRYPT] [NODEBUG] [AS nCodePage]
```

#### Parâmetros
 **DATABASE**
Compila um ou mais arquivos de banco de dados (.dbc) especificados por cFileName ou cFileSkeleton. Compila o código-fonte dos procedimentos armazenados salvos com o banco e o armazena em um campo memo adicional. Pode ser usado fora do Database Designer. Observação: COMPILE DATABASE compacta os campos memo do arquivo .dct para remover espaço não usado; registros marcados para exclusão não são removidos.
**FORM**
Compila arquivos de definição de formulário (.scx). Compila o código-fonte do ambiente de dados salvo no formulário e o armazena em um campo memo adicional. Formulários são compilados automaticamente ao serem salvos no Form Designer. O código-fonte fica em campos memo da tabela Form; COMPILE FORM o converte em código-objeto, executado por DO FORM.
**CLASSLIB**
Compila bibliotecas de classes visuais (.vcx). O código-fonte é armazenado em campos memo da tabela da biblioteca; CLASSLIB o compila e armazena em um campo memo adicional.
**LABEL**
Compila arquivos de definição de etiqueta (.lbx), incluindo o código-fonte do ambiente de dados salvo no arquivo.
**REPORT**
Compila arquivos de definição de relatório (.frx), incluindo o código-fonte do ambiente de dados salvo no arquivo.
**cFileName**
Especifica o arquivo de destino a compilar. Com uma opção, aceita: DATABASE, nome do banco com procedimentos armazenados; FORM, nome do formulário; CLASSLIB, nome da biblioteca; LABEL, nome da etiqueta; REPORT, nome do relatório. Sem essas opções, aceita arquivos Program (.prg), Form (.spr), Menu (.mpr), Query (.qpr) e Format (.fmt).
**cFileSkeleton**
Especifica um conjunto ou subconjunto de arquivos por um padrão que pode conter curingas * ou ?. Por exemplo: COMPILE DATABASE A* compila bancos iniciados por A; COMPILE *.PRG compila todos os programas .prg da pasta atual.
**?**
Exibe a caixa de diálogo Compile para procurar e escolher um arquivo.
**ALL**
Em relatórios (.frx) e etiquetas (.lbx) multiplataforma antigos, compila todos os registros de todas as plataformas. Disponível somente com REPORT e LABEL. Se omitido, compila apenas os registros da plataforma atual.
**ENCRYPT**
Criptografa programas compilados e não está disponível com DATABASE, FORM, CLASSLIB, LABEL ou REPORT. Impede acesso aos programas-fonte originais; inclua-o em programas destinados à distribuição para proteção adicional.
**NODEBUG**
Reduz o arquivo compilado em dois bytes por linha de origem e não está disponível com DATABASE, FORM, CLASSLIB, LABEL ou REPORT. Esses bytes referenciam a linha correspondente. A remoção não afeta o desempenho, reduz o tamanho e economiza espaço. Com NODEBUG, não é possível acompanhar a execução em Trace nem obter por MESSAGE(1) o código-fonte da linha que causou um erro.
**AS nCodePage**
Especifica a página de código da compilação. Não está disponível com DATABASE, FORM, CLASSLIB, LABEL ou REPORT e substitui a página global definida por SET CPCOMPILE.

# Observações

O Visual FoxPro executa somente arquivos-objeto. Se um fonte ainda não foi compilado, ele é compilado automaticamente ao executar o programa. O fonte permanece inalterado e um objeto separado, com o mesmo nome raiz e outra extensão, é criado.

| Tipo de arquivo | Extensão de origem | Extensão compilada |
| --- | --- | --- |
| Arquivo de programa | PRG | FXP |
| Código de menu | MPR | MPX |
| Consulta | QPR | QPX |
| Formato | FMT | PRX |

O compilador detecta erros de sintaxe. Se SET LOGERRORS estiver ON, as mensagens serão salvas em um arquivo de texto com o mesmo nome raiz e extensão .err. Se estiver OFF, esse arquivo não será criado.

Se um formulário tiver um cabeçalho #INCLUDE (.h) movido do diretório original, ocorrerá um erro de compilação listado no arquivo .err. O formulário poderá ser executado, mas, se for modificado, não poderá ser salvo até que o caminho seja corrigido.

### Para corrigir o caminho de um arquivo de cabeçalho (.h) movido
- Abra o formulário com MODIFY FORM.
- No menu Form, escolha Include File.
- Na caixa Include File, procure ou digite o novo caminho.

Para obter mais informações, consulte Diretiva #INCLUDE, Comando MODIFY FORM e Caixa de diálogo Include File.

# Exemplos

O exemplo usa CLOSE DATABASES para fechar todos os bancos abertos e COMPILE DATABASE para compilar os procedimentos armazenados do banco de exemplo TestData.dbc.

```foxpro
CLOSE DATABASES
COMPILE DATABASE (HOME(2) + 'Data\TestData')
```
