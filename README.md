# Robot-Movil
Creación de un robot móvil de navegación y mapeo autoónomo
## Materiales
 - Raspberry Pi 4 con Ubuntu 22.04.03 LTS (Jammy Jellyfish)
 - Arduino Uno
 - Modúlo L928n (Control Driver)
 - Rplidar
 - Carcaza y 4 llantas
## Instalación de ROS2 (Humble Hawksbill)
Para la raspberry se instala ros 2.
### Establecer configuración regional
```
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings

```
## Fuentes de configuración
Habilitamos el repositorio de ubuntu universe
```
sudo apt install software-properties-common
sudo add-apt-repository universe
```
Se agrega la clave GPG ros2 con apt
```
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```
Agregamos el repositorio a las listas fuente
```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```
## Instalar paquetes de Ros2
Se actualiza los repositorios
```
sudo apt update
```
Instalamos la nueva versiones
```
sudo apt upgrade
```
Instalamos la version de escritorio
```
sudo apt install ros-humble-desktop
```
#Conectando el sensor Rplidar
