# Fast Menu Api
# Fast Menu Front

## Sobre<a name = "sobre"></a>
Fast Menu Api é uma Api simples para gerenciar o cardápio de um restaurante.

## Guia de uso<a name = "features"></a>
A seguir segue um resumo de cada funcionalidade do Fast Menu Front e como utilizá-la.

### Restaurante controller
Restaurante controller possui apenas um método GET para obter as informações do cardápio do restaurante especificado (informe id_restaurante = 1, pois é o único restaurante cadastrado na base de dados e a Api ainda não possibilita a criação de novos restaurantes)

### Cardápio controller
Cardápio controller disponibiliza rotas para gerenciar as seções do cardápio especificado (atualmente só temos o cardápio de id_cardapio = 1)

### Cardápio Seção controller
Cardápio Seção controller disponibiliza rotas para gerenciar os ítens da seção especificada do cardápio

## Limitações<a name = "limitacoes"></a>
O projeto Fast Menu Api é apenas um MVP, por isso o conjunto de features implementadas é bastante limitado.
Segue algumas limitações atuais do projeto:
1 - Não é possível criar outras contas, temos apenas a conta de Id = 1 cadastrada na base e essa conta possui o restaurante de Id = 1 cadastrado na base. No futuro a aplicação será multi-tenant.
2 - A Api não necessita de autentição atualmente, ao executar o projeto podemos fazer requests para qualquer endpoint
3 - Não é possível criar novos restaurantes para a conta. No futuro penso que uma conta pode ter vários restaurantes para atender clientes grandes (i.e, Mcdonald's e outras grandes marcas)


## Como executar<a name = "Como executar"></a>
1 - Necessário ter a aplicação Fast Menu Api executando (segue o link com a documentação de como executar a api: https://github.com/matheusmughrabi/fast-menu-api)
2 - Abra o arquivo index.html no diretório ./src/index.html



