# Lab2: Tipos de Serviço de Nuvem - Laboratório

1. Entre no portal do Azure.  2qKKKPqV6Q3BQc5X
   
   `https://portal.azure.com` 
   ![image1](images/1.png)

2. Digite "SQL managed instance" em pesquisa, e selecione "Bancode dados SQL",tudo isso na tela principal
   ![image2](images/2.png)

3. Selecione "Criar banco de dados" na tela incial
   ![image3](images/3.png)

4. Selecione "Managed SQL Instance" na tela seguinte
   ![image4](images/4.png)

5. Na página "Create Azure SQL Managed Instance", preencha o nome da instância e seleção a região
   ![image5](images/5.png)

6. Na página "Create Azure SQL Managed Instance", seleção a opção "Configure Managed Instance":
   ![image6](images/6.png)

7. Na página "Create Azure SQL Managed Instance", seleção a guia rede e preencha:
   ![image7](images/7.png)

8. Na página "Create Azure SQL Managed Instance", seleção a guia seguraça e preencha:
   ![image8](images/8.png)

9. Selecione o botão ***criar*** na parte inferior da página
   
10. Em breve a instáncia vai ser criada
   ![image10](images/10.png)

9. Em Conta do administrador, selecione Chave pública SSH.

10. Em Nome de Usuário, insira **azureuser**.

11. Em Origem de chave pública SSH, mantenha o padrão de Gerar novo par de chaves e insira myKey para Nome do par de chaves.

12. Em Regras de porta de entrada:
    Portas de entrada públicas: escolha Permitir portas selecionadas e, em seguida, selecione SSH (22) e HTTP (80) na lista suspensa.
    Segue a imagem resumo com os passos 11,12,13,14
     ![image1](images/4.png)

13. Selecione o botão ***Examinar + criar*** na parte inferior da página

14. Na página Criar uma máquina virtual, você pode ver os detalhes sobre a VM que você está prestes a criar. Quando estiver pronto, selecione Criar.
     ![image1](images/5.png)

15. Quando a janela Gerar novo par de chaves for aberta, selecione Baixar chave privada e criar recurso. O arquivo de chave será baixado como **myKey.pem.** 

16. Depois que a implantação for concluída, selecione Ir para o recurso.
    ![image1](images/6.png)

17. Na página da nova VM, selecione o endereço IP público e copie-o para a área de transferência. neste caso o endereço IP é 52.252.238.212
    ![image1](images/7.png)

18. Conectar-se à máquina virtual:
    
    Mude as permições do arquivo myVM_key.pem
    
    `chmod 400 myVM_key.pem`
    
    Conecte-se via ssh
    
    `ssh -i myVM_key.pem azureuser@52.252.238.212`
    
     ![image1](images/9.png)

19. Instalar servidor Web
    
    `sudo apt-get -y update`
    
    ![image1](images/10.png)
    
    `sudo apt-get -y install nginx`
    
    ![image1](images/11.png)

20. Quando terminar, digite exit para sair da sessão SSH.

21. Use um navegador da Web de sua escolha para exibir a página inicial padrão do NGINX. Digite o endereço IP **52.252.238.212** como o endereço Web.
    ![image1](images/12.png)
