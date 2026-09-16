# Comando SET OLEOBJECT

Especifica se o Visual FoxPro pesquisa o registro quando um objeto não pode ser localizado.

```foxpro
SET OLEOBJECT ON | OFF
```

#### Parâmetros
 **ON**
(Padrão) Especifica que o Visual FoxPro pesquisa o registro quando um objeto não pode ser localizado.
**OFF**
Especifica que o Visual FoxPro não pesquisa o registro quando um objeto não pode ser localizado.

# Observações

Quando um objeto é criado com CREATEOBJECT( ) ou GETOBJECT( ), o Visual FoxPro pesquisa o objeto nos seguintes locais e na seguinte ordem:
 - As classes base do Visual FoxPro.
- Definições de classe na memória na ordem em que são carregadas.
- Definições de classe no programa atual.
- Definições de classe nas bibliotecas de classes .vcx abertas com SET CLASSLIB.
- Definições de classe em arquivos de procedimento abertos com SET PROCEDURE.
- Definições de classe na cadeia de execução de programas do Visual FoxPro (Para obter detalhes, consulte Comando DO).
- O registro.

Quando o Visual FoxPro pesquisa um objeto, o registro é pesquisado por último. O Visual FoxPro carrega o suporte a objetos COM antes de pesquisar o registro, aumentando a quantidade de memória necessária pelo Visual FoxPro e reduzindo a quantidade de memória disponível para outros aplicativos.

Se você está desenvolvendo um aplicativo que não requer suporte COM, emita SET OLEOBJECT OFF para impedir que o Visual FoxPro pesquise o registro quando um objeto não pode ser localizado.

SET OLEOBJECT não afeta objetos COM em Forms ou campos General. O Visual FoxPro sempre carrega o suporte a objetos COM quando um Form contendo um objeto COM é aberto para modificação ou é instanciado, ou quando uma tabela com um campo general é aberta.

Como GETOBJECT( ) ativa um objeto COM, o Visual FoxPro gera um erro quando GETOBJECT( ) é emitido e SET OLEOBJECT está OFF.
