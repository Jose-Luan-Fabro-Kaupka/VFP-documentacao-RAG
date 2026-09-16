# Variável de sistema _GENPD

Incluída para compatibilidade com versões anteriores. Use o argumento TO FILE ASCII no comando REPORT FORM .

Especifica um programa de interface de driver de impressora para relatórios baseados em caractere criados no FoxPro para MS-DOS.

```foxpro
_GENPD = expC
```

# Observações

_GENPD contém o nome do programa de interface de driver de impressora atual. Por padrão, este programa é o aplicativo fornecido com o FoxPro, GENPD.APP.

No FoxPro para Windows, GENPD.APP é usado somente para imprimir relatórios baseados em caractere criados no FoxPro para MS-DOS.

No FoxPro para Macintosh, um programa de interface de driver de impressora não é necessário para imprimir relatórios baseados em caractere criados no FoxPro para MS-DOS.

No FoxPro para MS-DOS, o programa cujo nome está armazenado em _GENPD é executado quando você faz um dos seguintes:

 - Escolhe a caixa de seleção Printer Driver Setup na caixa de diálogo Printer Setup.
- Escolhe a caixa de seleção Set Printer Driver na caixa de diálogo Page Layout do Report Writer ou na caixa de diálogo Label Environment do Label Designer.
- Emite SET PDSETUP.
- Armazena um nome de configuração de driver de impressora em _PDSETUP.
- Especifica uma configuração de impressora padrão antes de iniciar o FoxPro.
- O FoxPro passa 0 ao programa se você executar o programa escolhendo a caixa de seleção Printer Driver Setup na caixa de diálogo Printer Setup, emitir SET PDSETUP ou armazenar um nome de configuração de driver de impressora em _PDSETUP.
- O FoxPro passa 2 ao programa se você escolher a caixa de seleção Set Printer Driver na caixa de diálogo Layout do Report Writer ou na caixa de diálogo Label Environment do Label Designer.

Para evitar recursão, é uma boa ideia testar o parâmetro numérico passado ao programa de configuração de driver de impressora. Por exemplo, você poderia armazenar um nome de programa de driver de impressora em _PDRIVER que executa automaticamente o procedimento PDONLOAD no programa de driver de impressora. Seu procedimento PDONLOAD executa seu aplicativo de interface de configuração de impressora e passa um valor de 1.

O aplicativo de interface de configuração de impressora testa o valor numérico. Se o valor for 1, um nome de programa de driver de impressora não deve ser armazenado em _PDRIVER no programa. Se, neste caso, um nome de programa de driver de impressora for armazenado em _PDRIVER, PDONLOAD é executado automaticamente novamente e seu programa de configuração de driver de impressora é executado novamente em um loop infinito.

O segundo parâmetro que o FoxPro passa ao programa de configuração de driver de impressora é o nome da configuração de driver de impressora especificada em SET PDSETUP ou armazenada em _PDSETUP. Se você executar o programa de configuração de driver de impressora escolhendo a caixa de seleção Printer Driver Setup na caixa de diálogo Printer Setup, o FoxPro passa um ponto de interrogação (?) como segundo parâmetro ao programa especificado em _GENPD.
