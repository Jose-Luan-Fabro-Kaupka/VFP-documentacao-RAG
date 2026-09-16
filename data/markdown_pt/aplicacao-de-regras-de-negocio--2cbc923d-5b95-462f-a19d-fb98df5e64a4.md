# Aplicação de regras de negócio

Quando você tem ou usa regras de negócio para entrada de dados, há várias maneiras de aplicar essas regras no seu banco de dados:
 - Crie e use regras de validação para controlar os dados inseridos em campos e registros de tabelas de banco de dados. Para obter mais informações, consulte Trabalhando com regras de validação .
- Evite valores duplicados em campos usando índices candidatos ou primários. Para obter mais informações, consulte Evitando valores duplicados em campos .
- Mantenha relacionamentos entre tabelas estabelecendo regras de integridade referencial usando triggers e stored procedures que são invocados quando registros em tabelas de banco de dados são modificados. Para obter mais informações, consulte Como: construir integridade referencial entre tabelas .

Ao desenvolver restrições para o seu banco de dados, considere o nível em que deseja aplicar uma regra de negócio e a ação que ativa a restrição. As restrições são ativadas na ordem em que aparecem em uma tabela. A primeira violação de qualquer restrição interrompe a operação.

A tabela a seguir resume a ordem em que o Visual FoxPro aplica restrições de validação de dados, o nível em que se aplicam e quando essas restrições são ativadas.

| Nível | Mecanismo de aplicação | Ativado quando |
| --- | --- | --- |
| Formulário | Cláusula VALID | O ponteiro de registro sai do registro. |
| Tabela | Triggers | Valores são alterados em tabelas com uma operação INSERT , UPDATE ou DELETE . |
| Campo ou coluna | Validação NULL | Sai de um campo ou coluna em uma janela de navegação ou altera o valor do campo com uma operação INSERT ou REPLACE . |
| Campo ou coluna | Regras de validação em nível de campo | Sai de um campo ou coluna em uma janela de navegação ou altera o valor do campo com uma operação INSERT ou REPLACE . |
| Registro | Regras de validação em nível de registro | Um registro é atualizado. |
| Registro | Índice candidato/primário | Um registro é atualizado. |

> **Observação:** Quando um trigger é chamado, o Alias é sempre o do cursor sendo atualizado, independentemente do Alias selecionado no código que causou a execução do trigger.
