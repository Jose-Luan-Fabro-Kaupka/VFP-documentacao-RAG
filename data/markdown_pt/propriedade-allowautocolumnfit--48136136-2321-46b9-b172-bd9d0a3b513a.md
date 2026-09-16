# Propriedade AllowAutoColumnFit

Especifica como as colunas redimensionam automaticamente para a largura dos dados dentro da grade ou janela browse. Você pode usar AllowAutoColumnFit ao criar uma referência de objeto para a janela browse usando a cláusula NAME no comando BROWSE. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
Grid.AllowAutoColumnFit [ = nValue ]
```

# Valor de retorno
 **nValue**
Tipo de dados numérico. A tabela a seguir lista os valores para nValue . Configuração nValue descrição 0 Permite que todas ou colunas individuais se ajustem automaticamente aos dados. (Padrão) 1 Permite que apenas colunas individuais se ajustem automaticamente a todos os dados. "All data" refere-se apenas a todas as linhas na grade ou janela browse, não a todos os registros na tabela. 2 Desabilita a capacidade das colunas de se ajustarem automaticamente aos dados.

# Observações

Aplica-se a: Grid Control | BROWSE Command

Definir esta propriedade permite redimensionar colunas automaticamente para a largura dos dados quando você clica duas vezes na área entre cabeçalhos de coluna, ou no quadrado imediatamente anterior ao primeiro cabeçalho de coluna no canto superior e esquerdo de uma grade. AllowAutoColumnFit afeta a interação apenas pela interface do usuário.

O ajuste automático das colunas aos dados ocorre nos painéis esquerdo e direito da grade ou browse, mas apenas quando um ou ambos estão visíveis.

Você pode substituir AllowAutoColumnFit usando o método AutoFit, que redimensiona todas ou colunas individuais programaticamente.

Quando uma coluna é redimensionada, o evento Resize dessa coluna é disparado.

Você pode impedir o redimensionamento automático de uma coluna específica definindo a propriedade Resizable dessa coluna como False (.F.).

Eventos de clique no cabeçalho não são chamados porque você clica entre os cabeçalhos de coluna.

Colunas ocultas da grade, que têm sua propriedade Visible definida como False (.F.) e um valor de propriedade Width de 0, não são redimensionadas.
