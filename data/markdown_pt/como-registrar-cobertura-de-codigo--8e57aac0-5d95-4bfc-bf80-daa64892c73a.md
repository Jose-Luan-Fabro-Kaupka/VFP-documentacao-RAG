# Como: registrar cobertura de código

Mais adiante no processo de desenvolvimento, você pode querer refinar seu código para desempenho e garantir que testou adequadamente o código registrando informações de cobertura de código.

A cobertura de código fornece informações sobre quais linhas de código foram executadas e quanto tempo levou para executá-las. Essas informações podem ajudar a identificar áreas do código que não estão sendo executadas e, portanto, não estão sendo testadas, bem como áreas do código que você pode querer ajustar para desempenho.

Você pode alternar a cobertura de código ligando e desligando clicando no botão Code Coverage da barra de ferramentas na Debugger Window. Se você alternar a cobertura de código, a Coverage Dialog Box é aberta para que você possa especificar um arquivo para salvar as informações de cobertura.

Você também pode alternar o registro de cobertura ligando e desligando programaticamente usando o comando SET COVERAGE Command. Você pode, por exemplo, incluir o comando a seguir em sua aplicação imediatamente antes de um trecho de código que deseja investigar:

```foxpro
SET COVERAGE TO mylog.log
```

Após a seção de código para a qual deseja registrar cobertura, você pode incluir o comando a seguir para desligar a cobertura de código:

```foxpro
SET COVERAGE TO
```

Quando você especificou um arquivo para as informações de cobertura, alterne para a janela principal do Visual FoxPro e execute seu programa, formulário ou aplicação. Para cada linha de código executada, as seguintes informações são gravadas no arquivo de log:
 - Quanto tempo em segundos a linha levou para executar.
- A classe, se houver, à qual o código pertence.
- O método ou procedimento em que a linha de código está.
- O número da linha de código.
- O arquivo em que o código está.
- O nível da pilha de chamadas em que a linha de código executa.

A maneira mais fácil de extrair informações do arquivo de log é convertê-lo em uma tabela para que você possa definir filtros, executar consultas e relatórios, executar comandos e manipular a tabela de outras formas.

A Coverage Profiler Application cria um cursor a partir dos dados gerados no registro de cobertura e usa esse cursor em uma janela para análise fácil.

# Exemplo

O programa a seguir converte o arquivo de texto criado pelo log de cobertura em uma tabela:

```foxpro
cFileName = GETFILE('DBF')
IF EMPTY(cFileName)
   RETURN
ENDIF
CREATE TABLE (cFileName) ;
   (duration n(7,3), ;
   class c(30), ;
   procedure c(60), ;
   line i, ;
   file c(100))

APPEND FROM GETFILE('log') TYPE DELIMITED
```
