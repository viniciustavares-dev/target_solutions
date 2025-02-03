## Como Executar

Para executar o sistema em seu ambiente de desenvolvimento, siga as instruções abaixo:

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    ```

2.  **Backend:**

    *   Navegue até o diretório do backend:

        ```bash
        cd sistema-gestao-projetos
        ```

    *   Crie um ambiente virtual:

        ```bash
        python3 -m venv venv
        ```

    *   Ative o ambiente virtual:

        ```bash
        source venv/bin/activate
        ```

    *   Instale as dependências:

        ```bash
        pip install -r requirements.txt
        ```

    *   Configure as variáveis de ambiente no arquivo `.env`:

        ```
        KEYCLOAK_REALM_PUBLIC_KEY=-----BEGIN PUBLIC KEY-----\n...\n-----END PUBLIC KEY-----
        KEYCLOAK_AUTH_URL=http://localhost:8080/auth/
        KEYCLOAK_CLIENT_ID=backend-flask
        KEYCLOAK_CLIENT_SECRET=seu-secret
        DATABASE_URL=postgresql://usuario:senha@host:porta/banco_de_dados
        ```

    *   Crie as migrações do banco de dados:

        ```bash
        flask db init
        flask db migrate -m "Initial migration"
        flask db upgrade
        ```

    *   Execute o backend:

        ```bash
        python app.py
        ```

3.  **Frontend:**

    *   Navegue até o diretório do frontend:

        ```bash
        cd frontend
        ```

    *   Instale as dependências:

        ```bash
        npm install
        ```

    *   Configure as variáveis de ambiente no arquivo `.env.local`:

        ```
        NEXT_PUBLIC_KEYCLOAK_REALM=seu-realm
        NEXT_PUBLIC_KEYCLOAK_AUTH_URL=http://localhost:8080/auth/
        NEXT_PUBLIC_KEYCLOAK_CLIENT_ID=backend-flask
        NEXT_PUBLIC_API_URL=http://localhost:5000
        ```

    *   Execute o frontend:

        ```bash
        npm run dev
        ```

## Docker e Kubernetes

Para executar o sistema em um ambiente de produção utilizando Docker e Kubernetes, siga as instruções abaixo:

1.  **Construa as imagens Docker:**

    *   Backend:

        ```bash
        docker build -t backend-image .
        ```

    *   Frontend:

        ```bash
        docker build -t frontend-image .
        ```

2.  **Implante no Kubernetes:**

    *   Crie os arquivos de configuração do Kubernetes (Deployments, Services, etc.) para o backend e o frontend.
    *   Aplique os arquivos no Kubernetes:

        ```bash
        kubectl apply -f backend-deployment.yaml
        kubectl apply -f backend-service.yaml
        kubectl apply -f frontend-deployment.yaml
        kubectl apply -f frontend-service.yaml
        ```
