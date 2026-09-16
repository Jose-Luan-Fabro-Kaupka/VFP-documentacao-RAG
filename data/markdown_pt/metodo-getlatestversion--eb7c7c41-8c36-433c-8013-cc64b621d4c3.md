# Método GetLatestVersion

Obtém a versão mais recente de um arquivo em um projeto do controle de código-fonte e copia uma versão somente leitura para a unidade local.

```foxpro
Object.GetLatestVersion()
```

# Observações

Aplica-se a: Objeto File (Visual FoxPro)

O método GetLatestVersion não faz check-out do arquivo.

True (.T.) é retornado se o controle de código-fonte puder obter o arquivo com êxito. False (.F.) é retornado se o controle de código-fonte não puder obter o arquivo ou se o projeto não estiver sob controle de código-fonte.
