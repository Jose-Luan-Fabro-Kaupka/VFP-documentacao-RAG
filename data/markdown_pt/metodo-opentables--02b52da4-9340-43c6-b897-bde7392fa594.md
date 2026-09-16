# Método OpenTables

Abre por programação as tabelas e exibições associadas ao ambiente de dados.

```foxpro
DataEnvironment.OpenTables
```

#### Parâmetros
 **DataEnvironment**
Especifica o ambiente de dados associado ao formulário, conjunto de formulários ou relatório.

# Observações

Aplica-se a: objeto DataEnvironment

O método OpenTables carrega as tabelas do ambiente de dados quando sua propriedade AutoOpenTables é False (.F.) ou quando o ambiente foi descarregado por meio do método CloseTables. OpenTables atua como um evento, pois é chamado automaticamente quando AutoOpenTables é True (.T.).

Se AutoOpen de um cursor adapter falhar, o método OpenTables do ambiente de dados não relatará erro.
