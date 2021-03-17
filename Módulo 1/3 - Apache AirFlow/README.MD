# Aprendendo a utilizar o Apache Arflow na prática

- Essas atividades nos permitiu conhecer e interagir com a ferrementa de orquestação de pipline de dados, o Apache Airflow. 

- O principal recurso do Airflow é que ele permite que você crie facilmente pipelines de dados programados usando uma estrutura Python flexível, ao mesmo tempo que fornece muitos blocos de construção que permitem juntar as muitas tecnologias diferentes encontradas em cenários tecnológicos modernos. Os pipelines de dados geralmente consistem em várias tarefas ou ações que precisam ser executadas para atingir o resultado desejado em uma ordem específica, e o Arflow nos fornece essa flexibilidade.

- O bom do Airflow é que podemos dividir um grande trabalho, que consiste em uma ou mais etapas, em "tarefas" individuais e, juntos, formar um Directed Acyclic Graph (DAG). Várias tarefas podem ser executadas em paralelo e as tarefas podem executar diferentes tecnologias. Por exemplo, podemos primeiro executar um script Bash e, em seguida, executar um script Python.

- Os arquivos treino01.py, treino02.py, treino03.py, treino04.py são exemplos de DAGS (Gráfico Acíclico Direcionado). 

- O treino01.py verificamos o Básico de Bash Operators e Python Operators, ele echoa uma mensagem "Hello Airflow from Bash" no terminal a cada um minuto.

- O treino02.py extrai dados do Titanic da internet e calcula a idade média de todos a bordo a cada 2 minutos.

- O treino03.py extrai dados do Titanic e calcula idade média para homens ou mulheres.

- O treino04.py extrai dados do ENADE e executa as ações em paralelo aproveitando todo o poder do Airflow, ele calcula a idade centralizada da média, Idade centralizada ao quadrado entre outros e concatena todos os dados tratados num arquivo csv.

- O arquivo "Puckel Arflow.zip" contém toda a estrutura Airflow de teste para ser executada via container de acordo com o docker composer criado. Vale salientar que o mesmo é baseado no projeto https://github.com/puckel/docker-airflow. O docker composer foi alterado para a criação da pasta "data" ondem a mesma será utilizada para armazenamento dos arquivos csv no volume docker.

- O arquivo "GM-Airflow.zip" é uma versão do docker composer do apache airflow 2.0.1 (Versão atualizada mais do que o Puckel Arflow.zip) de minha autoria com inclusão do diretório "data" e as dags para estudo.

O AirFlow tem muito a oferecer na Engenharia de Dados na orquestração de piplines, um longo caminho estará travado a frente para dominar ao máximo esta tecnologia.
