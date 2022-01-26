## Exercício Application Server

### Preparando sua aplicação

1 - Atualize seu CentOS:
```
sudo yum update
```

2 - Adicione o Epel Repository no seu CentOS:
```
sudo yum install epel-release
```

3 - Intale o Nginx:
```
sudo yum install python-pip python-devel gcc nginx
```

4 - Instale o virtualenv e configure uma pasta:
```
sudo pip install virtualenv

# ou qualquer outra pasta que deseja criar seu projeto
cd /Documents/python

mkdir myproject

# acesse sua pasta
cd myproject

# rode
virtualenv myprojectenv

# ative o virtualenv
source myprojectenv/bin/activate
```

5 - Instale o gunicorn e flask
```
pip install gunicorn flask
```

6 - Crie um arquivo dentro do seu projeto

`vi /Documents/python/<nome-da-pasta-do-seu-projeto>/<nome-do-arquivo-do-seu-projeto>.py`

copie e cole o conteúdo abaixo

```
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello World from Nome do Aluno!</h1>"

if __name__ == "__main__":
    application.run(host='0.0.0.0')
```

7 - Teste seu app rodando:

```
python nome-do-arquivo-do-seu-projeto.py
```

Abra o firefox `dentro do seu virtualbox` e busque por http://localhost:5000

Se você viu seu nome, parabéns sua aplicação está rodando com sucesso.

### Configurando o Gunicorn

8 - Crie um arquivo chamado `wsgi.py` dentro da pasta do seu projeto
```
nano /Documents/python/<nome-da-pasta-do-seu-projeto>/wsgi.py
```

Exemplo: `nano /Documents/python/myproject/wsgi.py`

E copie o contúdo abaixo:

```
from <nome-do-arquivo-do-seu-arquivo.py> import application

if __name__ == "__main__":
    application.run()
```

Substitua o <nome-do-arquivo-do-seu-arquivo> pelo nome do seu arquivo.py (criamos esse arquivo no passo `6`)

10 - Vamos agora testar o Gunicorn servindo seu app

```
gunicorn --bind 0.0.0.0:8000 wsgi:app
```

Abra o firefox `dentro do seu virtualbox` e busque por http://localhost:8000 você deve continuar vendo a mensagem de Hello World + seu nome

11 - Desative o ambiente virtual do seu projeto

```
deactivate
```

### Configurando nosso app como serviço

12 - Crie um arquivo de serviço dentro do `etc/systemd/system/`

```
sudo nano /etc/systemd/system/<nome-da-pasta-do-seu-projeto>.service
```

Exemplo: sudo nano /etc/systemd/system/myproject.service

E cole o conteúdo abaixo

```
[Unit]
Description=Gunicorn instance to serve myproject
After=network.target

[Service]
User=user
Group=nginx
WorkingDirectory=/home/user/<nome-da-pasta-do-seu-projeto>
Environment="PATH=/home/user/<nome-da-pasta-do-seu-projeto>/<nome-da-pasta-do-ambiente-virtual-do-seu-projeto>/bin"
ExecStart=/home/user/<nome-da-pasta-do-seu-projeto>/<nome-da-pasta-do-ambiente-virtual-do-seu-projeto>/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target

```

Altere os parâmetros que estão com <nome-da-pasta-do-seu-projeto> + <nome-da-pasta-do-ambiente-virtual-do-seu-projeto> para o nome da pasta do seu projeto e o nome do ambiente virtual que você criou

Exemplo: `Environment="PATH=/home/user/firstproject/firstprojectenv/bin"`

Lembre de usar o `pwd` dentro da pasta do seu projeto para pegar o caminho correto e que o `ambiente virtual` é uma pasta
dentro do seu projeto (criamos no passo `4`)

Se precisar de alguma referência:

[myapplication.service](https://gist.github.com/drsantos20/4ce5e890df209f2129ad239a3a51ec51)


13 - Execute os comandos abaixo para habilitar o gunicorn + nosso app como serviço:
```
sudo systemctl start <nome-do-seu-projeto>
sudo systemctl enable <nome-do-seu-projeto>
```

### Configurando o Nginx

Abra o nginx.conf

```
sudo nano /etc/nginx/nginx.conf
```

Navegue até o `server {}`

e copie toda a instrução do server abaixo e substitua no seu nginx.conf

```
    server {
        listen       80;
        listen       [::]:80 default_server;
	    server_name  firstproject www.firstproject;

	# Logs
        access_log /var/log/nginx/<nome-da-pasta-do-seu-projeto>.access.log;
        error_log /var/log/nginx/<nome-da-pasta-do-seu-projeto>.error.log;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        location / {
            proxy_pass http://unix:/home/adminuser/Documents/python/<nome-da-pasta-do-seu-projeto>/<nome-da-pasta-do-seu-projeto>.sock;
        }

        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }

```

Altere o caminho que está dentro de `location/` e `logs` informando o nome da pasta do seu projeto
exemplo: `proxy_pass http://unix:/home/adminuser/Documents/python/firstproject/firstproject.sock;`

Se precisar de uma referência:

[arquivo-nginx](https://gist.github.com/drsantos20/781d197df16bad65ebffdeafa732695c)

14 - Altere as permissões para o `nginx` acessar a pasta do seu projeto

```
sudo usermod -a -G adminuser nginx
sudo chmod 710 /home/user
```

15 - Verifique se as configurações do `nginx` estão funcionando

```
sudo nginx -t
```

16 - Estando tudo certo no passo `10` agora execute os comandos

```
sudo systemctl start nginx
sudo systemctl enable nginx
```

17 - Adicionando a rota no `/etc/hosts`

Execute o `ifconfig` na sua maquina e copie o ip que está próximo do `inet` (primeiro bloco) no meu caso foi `10.0.2.15`

Pegue esse IP e cole no `/etc/hosts`

Seu arquivo deve estar assim

`sudo nano /etc/hosts`

```
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
10.0.2.15   firstproject
```


18 - Reinicie o Gunicorn e Nginx

```
sudo systemctl restart <nome-do-seu-projeto>
sudo service nginx restart
```

19 - Acesse seu virtualbox, abra o firefox e busque por `http://<nome-do-seu-projeto>`

Se você ver a página do hello world com seu nome, parabéns, você configurou seu primeiro ambiente pronto para produção!