# Função CREATEOBJECTEX( )

Cria uma instância de um objeto COM registrado (como um servidor Automation do Visual FoxPro) em um computador remoto.

```foxpro
CREATEOBJECTEX(cCLSID | cPROGID, cComputerName [, cIID])
```

#### Parâmetros
 **cCLSID | cPROGID**
Especifica o CLSID (Class Identifier) ou PROGID (Programmatic Identifier) do objeto COM a instanciar. Se você incluir um CLSID, o objeto COM deve estar registrado no servidor remoto que você especifica com cComputerName . Se você incluir um PROGID, o objeto COM deve estar registrado tanto no seu computador local quanto no computador remoto que você especifica com cComputerName . Tentar usar um PROGID sem registrar primeiro o servidor no seu computador local gerará o erro OLE Code 0x800401f3, "Invalid Class String." Para servidores Automation do Visual FoxPro criados na sua máquina local, você pode usar as propriedades CLSID e PROGID do objeto servidor para determinar os valores locais de CLSID e PROGID.
**cComputerName**
Especifica o computador remoto no qual o objeto COM é instanciado. Se cComputerName é a cadeia vazia, o objeto COM é instanciado no computador local ou em uma máquina redirecionada conforme especificado no registro. cComputerName suporta nomes Universal Naming Convention (UNC) como "\\myserver" e "myserver," e nomes Domain System Names (DNS).
**cIID**
Especifica o GUID Interface ID de cCLSID | cPROGID quando você cria uma instância de vinculação antecipada da classe. Se você passar uma cadeia vazia como cIID, o Visual FoxPro tenta acessar a interface padrão (IID) de cCLSID | cPROGID .

# Valor de retorno

Objeto

# Exemplo

```foxpro
      x = CREATEOBJECTEX("excel.application","",;
      "{000208D5-0000-0000-C000-000000000046}")
```

> **Observação:** A seguinte é uma chamada de função válida para um objeto de aplicação excel. Ela retornará a interface padrão do excel.application.

```foxpro
      x = CREATEOBJECTEX("excel.application","","")
```

# Observações

CREATEOBJECTEX( ) retorna uma referência de objeto ao objeto COM se ele for instanciado com sucesso. CREATEOBJECTEX( ) não pode ser usado para instanciar classes do Visual FoxPro, como formulários — use CREATEOBJECT( ) para instanciar classes do Visual FoxPro. Observe que você só pode abreviar CREATEOBJECTEX( ) para um mínimo de 13 caracteres, distinguindo-o da função CREATEOBJECT( ).

Quando você chama certas classes COM com CREATEOBJECT( ), elas retornam "No such interface supported" porque não suportam uma interface IDispatch. Usando o parâmetro cIID, agora você pode acessar essas classes em suas aplicações.

Se você passar uma cadeia vazia ("") como cIID, o Visual FoxPro tenta obter a interface padrão (IID) do CLSID ou PROGID especificado.

Porque suporta vinculação antecipada através de cIID, CREATEOBJECTEX( ) pode ajudar a melhorar o desempenho evitando grande parte da sobrecarga de chamadas IDispatch.

CREATEOBJECTEX( ) suporta a criação de novos objetos de vinculação antecipada. No entanto, também é possível que seu componente Visual FoxPro receba um objeto que você deseja chamar via vinculação antecipada. Você pode usar o suporte GETINTERFACE( ) em objetos COM existentes.

Para informações adicionais sobre o uso do Visual FoxPro para criar servidores Automation, consulte Compartilhando informações e adicionando OLE.
