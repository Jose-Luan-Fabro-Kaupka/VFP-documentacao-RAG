# Comando SET DOHISTORY

Determina se os comandos de um programa são colocados na janela Debug Output.

```foxpro
SET DOHISTORY ON | OFF
```

#### Parâmetros
 **ON**
Coloca comandos de um programa na janela Debug Output conforme o programa é executado.
 **OFF**
(Padrão) Não coloca comandos de um programa na janela Debug Output.

# Observações

Use SET DOHISTORY apenas como auxílio de depuração para isolar bugs particularmente persistentes.
 SET DOHISTORY ON não tem efeito quando o programa está sendo executado no ambiente de biblioteca de tempo de execução ou quando a janela Debug Output não existe no IDE.
 Comandos executados diretamente da janela Command não são colocados na janela Debug Output.
 Scripts executados via função EXECSCRIPT( ) se comportam como código de programa padrão e são colocados na janela Debug Output.
