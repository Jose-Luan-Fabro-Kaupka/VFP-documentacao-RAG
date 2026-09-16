# Como: retornar um valor de um formulário

Você pode usar formulários em toda a aplicação para permitir que os usuários especifiquem um valor.

### Para retornar um valor de um formulário
- Defina a propriedade WindowType do formulário como 1 para tornar o formulário modal.
- No código associado ao evento Unload do formulário, inclua um comando RETURN com o valor de retorno.
- No programa ou método que executa o formulário, inclua a palavra-chave TO no comando DO FORM. Por exemplo, se FindCustID é um formulário modal que retorna um valor de caractere, a linha de código a seguir armazena o valor de retorno em uma variável chamada cCustID: DO FORM FindCustID TO cCustID

Para obter mais informações, consulte o comando RETURN e o comando DO FORM.

> **Observação:** Se você receber um erro, verifique se WindowType está definido como 1 (Modal).
