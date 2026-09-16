# Variável de Sistema _PDSETUP

Incluída para compatibilidade com versões anteriores. Use o argumento TO FILE ASCII no Comando REPORT FORM.

Carrega ou limpa uma configuração de driver de impressora para relatórios baseados em caracteres.

```foxpro
_PDSETUP = expC
```

# Observações

_PDSETUP carrega uma configuração de driver de impressora ou limpa a configuração atual de driver de impressora. Uma configuração de driver de impressora é uma combinação de configurações que inclui o programa de driver de impressora e informações de impressão, como orientação da página, tamanho e estilo de fonte padrão, margens e assim por diante. Uma configuração de driver de impressora é usada no FoxPro para Windows ao imprimir relatórios baseados em caracteres criados no FoxPro para MS-DOS. No FoxPro para Macintosh, uma configuração de driver de impressora não é necessária para imprimir relatórios baseados em caracteres criados no FoxPro para MS-DOS.

As configurações de driver de impressora são armazenadas no arquivo de recursos FOXUSER.DBF e você pode criá-las interativamente e atribuir nomes a elas na caixa de diálogo Printer Setup Editing.

Você também pode carregar ou limpar uma configuração de driver de impressora com SET PDSETUP. Para carregar uma configuração de driver de impressora, armazene o nome da configuração em _PDSETUP. Você pode limpar a configuração atual de driver de impressora armazenando a cadeia de caracteres nula em _PDSETUP. Armazenar a cadeia de caracteres nula em _PDSETUP também limpa a matriz _PDPARMS da memória.

Se o nome da configuração de driver de impressora que você armazena em _PDSETUP não existir no arquivo de recursos, o aplicativo de interface de configuração de impressora atual é executado. Se você estiver usando GENPD.APP, o aplicativo de interface de configuração de impressora padrão incluído com o FoxPro, a caixa de diálogo Printer Setup Editing aparece para que você possa criar uma configuração com o nome especificado.

Quando o nome da configuração de driver de impressora que você inclui em expC não existe no arquivo de recursos, você pode impedir que o aplicativo de configuração de driver de impressora seja executado precedendo o nome da configuração com um traço (-).

Para carregar uma configuração padrão de driver de impressora ao iniciar o FoxPro para MS-DOS, inclua a seguinte linha no arquivo CONFIG.FP.

PDSETUP = 'setup name' WITH parm list

Certifique-se de colocar o nome da configuração entre aspas.
