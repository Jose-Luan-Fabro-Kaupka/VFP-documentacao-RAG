# Propriedade RecordSourceType

Especifica como a fonte de dados que preenche o controle Grid é aberta. Disponível em tempo de design e leitura/gravação em tempo de execução.

```foxpro
Grid.RecordSourceType[ = nType]
```

# Valor de retorno
 **nType**
As configurações da propriedade RecordSourceType são: Configuração Descrição 0 Tabela. Abre automaticamente a tabela especificada na configuração da propriedade RecordSource. 1 (Padrão) Alias. Trata a fonte de registros conforme especificado. 2 Prompt. O usuário é solicitado a fornecer a fonte de registros em tempo de execução. Se um banco de dados estiver aberto, o usuário pode escolher uma de suas tabelas como fonte de registros. 3 Consulta (.qpr). A configuração da propriedade RecordSource especifica um arquivo .qpr. 4 Instrução SQL. A instrução SQL é especificada na propriedade RecordSource.

# Observações

Aplica-se a: Controle Grid
