Vagrant.configure("2") do |config|
    # Set the box to Ubuntu 20.04
  config.vm.box = "debian/bullseye64"

  # Set the IP address of the server
  config.vm.network "private_network", ip: "192.168.190.17"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096"
    vb.cpus = "4"
  end
  config.vm.synced_folder "./DockerCompose", "/home/vagrant/wargame1"
 
  # Script to provision the virtual machine
  config.vm.provision "shell", inline: <<-SHELL
    # Update the package repository and install dependencies
    sudo apt update
    sudo apt install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common
	  sudo apt install python3-pip -y
	  pip install Flask
    # Install Ansible
    sudo apt update
    sudo apt install -y software-properties-common
    sudo apt-add-repository --yes --update ppa:ansible/ansible
    sudo apt install -y ansible
    sudo apt-get install gnupg -y
    # Install Docker
    curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
    sudo apt update
    sudo apt install -y docker-ce

    # Install Docker Compose
    sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose


	  git clone https://github.com/Badwargame37/VagrantTestChal2.git


    # Install GCC (GNU Compiler Collection)
    sudo apt install -y gcc

    # Add your user to the Docker group
    sudo usermod -aG docker ${USER}

    # Start Docker service
    sudo systemctl start docker
    sudo systemctl enable docker
sudo usermod -a ${USER} -G docker
    # Optionally, you can set up a Kubernetes cluster using kubeadm here
	mkdir ${HOME}/docker-stack
cd ${HOME}/docker-stack


cd  ${HOME}/docker-stack/
docker network create --driver=bridge --subnet=192.168.191.0/24 pivot_net

docker network create --driver=bridge challenge_net
docker network create --driver=bridge guacamole_net
docker network create --driver=bridge haproxy_net
docker network create --driver=bridge wordpress_internal_net

git clone https://github.com/Badwargame37/wargame-mexico.git


####################gucaomole
mkdir -p ${HOME}/docker-stack/guacamole/init
chmod -R +x ${HOME}/docker-stack/guacamole/init
docker run --rm guacamole/guacamole:1.5.0 /opt/guacamole/bin/initdb.sh --postgres > ${HOME}/docker-stack/guacamole/init/initdb.sql
cp ${HOME}/docker-stack/wargame-mexico/DockerCompose/guacamole/docker-compose.yml  ${HOME}/docker-stack/guacamole/docker-compose.yml

echo "POSTGRES_PASSWORD='PleasePutAStrongPasswordHere123'" >${HOME}/docker-stack/guacamole/.env 
echo "POSTGRES_USER='guacamole_user'" >>${HOME}/docker-stack/guacamole/.env 

####################HA  Proxy
mkdir -p ${HOME}/docker-stack/haproxy
cd ${HOME}/docker-stack/haproxy
cp ${HOME}/docker-stack/wargame-mexico/DockerCompose/haproxy/docker-compose.yml  ${HOME}/docker-stack/haproxy/docker-compose.yml
cp ${HOME}/docker-stack/wargame-mexico/DockerCompose/haproxy/haproxy.cfg  ${HOME}/docker-stack/haproxy/haproxy.cfg
echo 'ENDPOINT="bastion.esd37.com"' >${HOME}/docker-stack/haproxy/.env
chown -R ${USER}:${USER} ${HOME}/docker-stack/


####################wordpress
mkdir -p ${HOME}/docker-stack/wordpress
cp ${HOME}/docker-stack/wargame-mexico/DockerCompose/wordpress  ${HOME}/docker-stack/ -r
g++ -o ${HOME}/docker-stack/wargame-mexico/DockerCompose/Reverse/rbash ${HOME}/docker-stack/wargame-mexico/DockerCompose/Reverse/rbash.cpp

##-------------------------wp------------------
#docker compose -f ${HOME}/docker-stack/haproxy/docker-compose.yml up -d
#docker compose -f ${HOME}/docker-stack/guacamole/docker-compose.yml up -d
#docker compose -f ${HOME}/docker-stack/wordpress/docker-compose.yml up -d
#cp gua${HOME}/docker-stack/wargame-mexico/DockerCompose/Complet ${HOME}/docker-stack/ -r


cd wargame-mexico
docker compose -f ${HOME}/docker-stack/wargame-mexico/DockerCompose/network-config.yml up -d
docker compose -f ${HOME}/docker-stack/haproxy/docker-compose.yml up -d
docker compose -f ${HOME}/docker-stack/guacamole/docker-compose.yml up -d
docker compose -f ${HOME}/docker-stack/wordpress/docker-compose.yml up -d
docker compose -f ${HOME}/docker-stack/wargame-mexico/DockerCompose/Reverse/docker-compose.yml up -d
docker compose -f ${HOME}/docker-stack/wargame-mexico/DockerCompose/pivot/docker-compose.yml up -d
docker-compose -f ${HOME}/docker-stack/wargame-mexico/DockerCompose/pivot/docker-compose.yml down
docker-compose -f ${HOME}/docker-stack/wargame-mexico/DockerCompose/pivot/docker-compose.yml up -d


docker compose -f ${HOME}/docker-stack/haproxy/docker-compose.yml ps
docker compose -f ${HOME}/docker-stack/guacamole/docker-compose.yml ps
docker compose -f ${HOME}/docker-stack/wordpress/docker-compose.yml ps
docker compose -f ${HOME}/docker-stack/wargame-mexico/DockerCompose/Reverse/docker-compose.yml ps
docker compose -f ${HOME}/docker-stack/wargame-mexico/DockerCompose/pivot/docker-compose.yml ps
    echo "All installations completed."
  SHELL
end
