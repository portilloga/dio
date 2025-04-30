# Lab1: Beneficios da nuvem - Laboratório

1. Entre no portal do Azure.
   
   `https://portal.azure.com` 

2. Criar máquina virtual
   
3. Selecione "Criar um recurso" na tela incial
   ![image1](images/1.png)

5. Selecione Máquina virtual. (criar)
   ![image1](images/2.png)

7. Na página Máquinas virtuais, clique em Criar, e em seguida, selecione Máquina virtual. A página Criar uma máquina virtual é aberta.

8. Ecolha Criar grupo de recursos. Digite **myResourceGroup** para o nome.

9. Em Detalhes da instância:
   
   1. insira **myVM** para o Nome da máquina virtual 
   
   2. Escolha ***Ubuntu Server 22.04 LTS – Gen2*** para Imagem.

10. Em region selecione **North Central US**.
    Segue a imagem resumo com os passos 7,8,9,10
     ![image1](images/3.png)

11. Em Conta do administrador, selecione Chave pública SSH.

12. Em Nome de Usuário, insira **azureuser**.

13. Em Origem de chave pública SSH, mantenha o padrão de Gerar novo par de chaves e insira myKey para Nome do par de chaves.

14. Em Regras de porta de entrada:
   Portas de entrada públicas: escolha Permitir portas selecionadas e, em seguida, selecione SSH (22) e HTTP (80) na lista suspensa.
   Segue a imagem resumo com os passos 11,12,13,14
     ![image1](images/4.png)
    
15. Selecione o botão ***Examinar + criar*** na parte inferior da página

16. Na página Criar uma máquina virtual, você pode ver os detalhes sobre a VM que você está prestes a criar. Quando estiver pronto, selecione Criar.
     ![image1](images/5.png)

17. Quando a janela Gerar novo par de chaves for aberta, selecione Baixar chave privada e criar recurso. O arquivo de chave será baixado como **myKey.pem.** 

18. Depois que a implantação for concluída, selecione Ir para o recurso.
    ![image1](images/6.png)
    
19. Na página da nova VM, selecione o endereço IP público e copie-o para a área de transferência. neste caso o endereço IP é 52.252.238.212
    ![image1](images/7.png)
    
20. Conectar-se à máquina virtual:
    
    Mude as permições do arquivo myVM_key.pem
    
    `chmod 400 myVM_key.pem`
    
    Conecte-se via ssh
    
    `ssh -i myVM_key.pem azureuser@52.252.238.212`
    
     ![image1](images/9.png)
    
21. Instalar servidor Web
    
    `sudo apt-get -y update`

    ![image1](images/10.png)
    
    `sudo apt-get -y install nginx`

    ![image1](images/11.png)

22. Quando terminar, digite exit para sair da sessão SSH.

23. Use um navegador da Web de sua escolha para exibir a página inicial padrão do NGINX. Digite o endereço IP **52.252.238.212** como o endereço Web.
    ![image1](images/12.png)
