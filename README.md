# Roteiro do Desenvolvimento do Scanner de Portas

## 1. Desenvolvimento inicial do código
- Escrevemos um script básico em Python para escanear portas TCP em um endereço IP.
- Utilizamos o módulo `socket` para tentar se conectar a portas dentro de um intervalo fornecido.

## 2. Adição de multi-threading
- Para tornar o escaneamento mais rápido, implementamos threads usando o módulo `threading`.
- O código foi ajustado para criar múltiplas threads, cada uma escaneando uma porção das portas, permitindo que o escaneamento ocorresse em paralelo.

## 3. Melhoria da interface
- Transformamos o script em algo mais “user-friendly”, removendo a dependência de argumentos de linha de comando.
- Agora, o código solicita diretamente ao usuário o endereço IP, o intervalo de portas, e o número de threads, mostrando mensagens claras e fornecendo valores padrão.

## 4. Flexibilidade no escaneamento
- Adicionamos lógica para lidar com casos em que o usuário não insere valores para start e end, aplicando valores padrão.
- O usuário pode personalizar o número de threads e o intervalo de portas de forma interativa, tornando o script mais acessível.

## 5. Exibição dos resultados
- As portas abertas são exibidas durante o escaneamento, tornando o processo mais dinâmico e informativo.
- Uma lista consolidada de portas abertas é mostrada ao final, permitindo que o usuário veja claramente quais portas foram identificadas.

---

**Resumo:**  
O código começou como um simples scanner de portas TCP, ganhou melhorias de desempenho com threads e foi aprimorado para que qualquer pessoa pudesse usá-lo de forma intuitiva, sem precisar conhecer comandos ou opções de linha de comando.
