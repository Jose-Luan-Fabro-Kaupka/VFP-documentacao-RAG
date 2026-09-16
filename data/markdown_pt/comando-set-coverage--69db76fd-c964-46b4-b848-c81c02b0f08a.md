# Comando SET COVERAGE

Ativa ou desativa a cobertura de código ou especifica um arquivo de texto para o qual as informações de cobertura de código são direcionadas.

```foxpro
SET COVERAGE TO [FileName [ADDITIVE]]
```

#### Parâmetros
 **TO FileName**
Especifica o nome de um arquivo de texto para o qual as informações de cobertura de código são direcionadas. Emita SET COVERAGE TO sem um nome de arquivo para fechar o arquivo de texto. Se o arquivo especificado não existir, o Visual FoxPro cria e abre automaticamente.
**ADDITIVE**
Anexa as informações de cobertura de código ao final do arquivo de texto especificado com FileName. Se você omitir ADDITIVE, as informações de cobertura de código substituem o conteúdo do arquivo de texto.

# Observações

Você pode usar SET COVERAGE em tempo de design e em tempo de execução no Visual FoxPro 9.0. Coverage.app, o aplicativo Coverage Profile incluído com o Visual FoxPro, não pode ser incluído em seus aplicativos de tempo de execução distribuídos. Consulte Recursos e arquivos distribuíveis e restritos do Visual FoxPro para obter mais informações sobre arquivos e aplicativos que podem ser incluídos em seus aplicativos Visual FoxPro distribuídos.

Para obter mais informações sobre opções de cobertura de código, consulte Caixa de diálogo Coverage. Para obter mais informações sobre o Visual FoxPro Coverage Profiler, consulte Aplicativo Coverage Profiler.
