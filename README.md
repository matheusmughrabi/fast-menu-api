# Fast Menu Api

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
1. Não é possível criar outras contas, temos apenas a conta de Id = 1 cadastrada na base e essa conta possui o restaurante de Id = 1 cadastrado na base. No futuro a aplicação será multi-tenant.
2. A Api não necessita de autentição atualmente, ao executar o projeto podemos fazer requests para qualquer endpoint
3. Não é possível criar novos restaurantes para a conta. No futuro penso que uma conta pode ter vários restaurantes para atender clientes grandes (i.e, Mcdonald's e outras grandes marcas)

## Requisitos e Como executar<a name = "Como executar"></a>
### Requisitos
1. git instalado
2. python instalado
3. [Opcional] Algum gerenciador de pacotes python como virtualenv para facilitar a criação de um ambiente virtual ([virtualenv](https://virtualenv.pypa.io/en/latest/installation.html))

### Como executar
1. Git clone https://github.com/matheusmughrabi/fast-menu-api.git
2. Abra o terminal no diretório relativo a raiz do projeto: .\src\FastMenu.Api
3. [Opcional] Crie o ambiente virtual
4. [Opcional] Ative o ambiente virtual
5. Execute o comando pip install -r requirements.txt
6. Execute o comando flask run --host 0.0.0.0 --port 5000 IMPORTANTE EXECUTAR COM A PORTA 5000 POIS O PROJETO FAST MENU FRONT ESTÁ APONTANDO PARA ESTA PORTA

### Observações
1. Utilizei o banco de dados sqlite, então não é necessário ter nenhuma infraestrutura adicional instalada



