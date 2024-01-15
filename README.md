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
