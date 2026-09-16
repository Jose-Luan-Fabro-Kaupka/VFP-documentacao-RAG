# Foundation Class Registry Access

Esta classe fornece acesso a informações no Registro do Windows.

| Categoria | Utilitários do sistema |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Utilities |
| Classe | registry |
| Classe base | Custom |
| Biblioteca de classes | registry.vcx |
| Classe pai | registry |
| Exemplo | ...\Samples\Solution\WinAPI\regfox.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item da Galeria de componentes, selecione Adicionar ao projeto ou Adicionar ao formulário. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca a classe no formulário. Você pode então especificar os valores de propriedade apropriados e fornecer os objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Diretrizes para usar Foundation Classes do Visual FoxPro para obter mais informações sobre o uso de foundation classes.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Método CloseKey | Fecha uma chave do registro. Sintaxe: CloseKey( ) Retorno: nenhum Argumentos: nenhum |
| Método DeleteKey | Exclui uma chave do registro. Sintaxe: DeleteKey(nUserKey, cKeyPath) Retorno: nenhum Argumentos: nUserKey especifica a chave de usuário do Registro. cKeyPath especifica o caminho da chave de usuário do Registro. |
| Método DeleteKeyValue | Exclui um valor de uma chave do registro. Sintaxe: DeleteKeyValue(cOptName, cKeyPath, nUserKey) Retorno: nenhum Argumentos: cOptName especifica o nome da opção da chave do Registro. cKeyPath especifica o caminho para a chave do Registro. nUserKey especifica a chave de usuário. |
| Método EnumKeys | Enumera por uma chave do registro. Sintaxe: EnumKeys(@aKeyNames) Retorno: nenhum Argumentos: aKeyNames especifica as chaves do Registro a enumerar. |
| Método EnumKeyValues | Enumera pelos valores de uma chave do registro. Sintaxe: EnumKeyValues(@aKeyValues) Retorno: nenhum Argumentos: aKeyValues especifica os valores da chave de usuário do Registro a enumerar. |
| Método EnumOptions | Enumera por todas as entradas de uma chave e preenche um array com valores. Sintaxe: EnumOptions(@aRegOpts, cOptPath, nUserKey, lEnumKeys) Retorno: nenhum Argumentos: aRegOpts especifica a opção da chave do Registro. cOptPath especifica o caminho para a opção da chave do Registro. nUserKey especifica o ID da chave de usuário. lEnumKeys especifica se deve enumerar outras opções, se existirem. |
| Método GetKeyValue | Retorna o valor de uma chave. Sintaxe: GetKeyValue(cValueName, cKeyValue) Retorno: nenhum Argumentos: cValueName especifica o nome do valor a recuperar. cKeyValue especifica o valor de cValueName . |
| Método GetRegKey | Retorna uma configuração de chave do registro. Sintaxe: GetRegKey(cOptName, cOptVal, cKeyPath, nUserKey) Retorno: nenhum Argumentos: cOptName especifica o nome da opção da chave do Registro. cOptVal especifica o valor a aplicar à opção. cKeyPath especifica o caminho da chave do Registro. nUserKey especifica a chave de usuário. |
| Método IsKey | Retorna se uma chave especificada existe. Sintaxe: IsKey(cKeyName, nRegKey) Retorno: nenhum Argumentos: cKeyName especifica o nome da chave de usuário a verificar, se existir. nRegKey especifica o ID da chave do Registro |
| Método OpenKey | Abre uma chave do registro. Sintaxe: Open(cLookUpKey, nRegKey, lCreateKey) Retorno: nenhum Argumentos: cLookUpKey especifica o nome da chave de usuário a pesquisar. nRegKey especifica o ID da chave do Registro. lCreateKey especifica se deve criar uma nova chave do Registro se a especificada não existir. |
| Método SetKeyValue | Define o valor de uma chave do registro. Sintaxe: SetKeyValue(cValueName, cValue) Retorno: nenhum Argumentos: cValueName especifica o nome do valor a definir. cValue especifica o valor a aplicar a cValueName . |
| Método SetRegKey | Define a configuração da chave do registro. Sintaxe: SetRegKey(cOptName, cOptVal, cKeyPath, nUserKey) Retorno: nenhum Argumentos: cOptName especifica o nome da opção da chave do Registro. cOptVal especifica o valor a aplicar à opção. cKeyPath especifica o caminho da chave do Registro. nUserKey especifica o ID da chave de usuário. |
| Propriedade cAppPathKey | Interna à classe. |
| Propriedade cIniDllFile | Interna à classe. |
| Propriedade cODBCDllFile | Interna à classe. |
| Propriedade cRegDllFile | Interna à classe. |
| Propriedade cVfpOptPath | Interna à classe. |
| Propriedade lCreateKey | Interna à classe. |
| Propriedade lHadError | Interna à classe. |
| Propriedade lLoaddedDlls | Interna à classe. |
| Propriedade lLoadedInis | Interna à classe. |
| Propriedade lLoadedOdbcs | Interna à classe. |
| Propriedade nCurrentKey | Interna à classe. |
| Propriedade nCurrentOS | Interna à classe. |
| Propriedade nUserKey | Interna à classe. |
| Método LoadRegFuncs | Interna à classe. |
