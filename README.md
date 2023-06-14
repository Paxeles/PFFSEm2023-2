# PFFSEm2023-2
EN

Final Project Retro Console, created by Pablo Escalona, Leonardo Campos, and Rodrigo Olvera.

This project aims to emulate a retro video game console.

The objective of this project is to provide a laboratory practice proposal for the Embedded Systems Fundamentals subject.

For this project, the latest version as of June 14, 2023, of Raspberry Pi OS was used, along with a PS4 controller, although it can be any other platform.

The main idea was to have the Raspberry Pi automatically start the "inicio.py" script upon powering on. We tried to achieve this by adding the line "su - axel -c "/home/inicio.py &"" to the rc.local configuration file. However, it resulted in an error upon startup, and the custom image no longer appeared.

The error message displayed is as follows:

[16.203151] rc.local[614]: Traceback (most recent call last):
[16.211714] rc.local[614]: File "/home/inicio.py", line 77, in <module>
[16.218736] rc.local[614]: File ""/home/inicio.py", line 33, in main
[16.221928] rc.local[614]: choice = input("ingrese su opción: ")
[16.229991] rc.local[614]: EOFError: EOF when reading a line.

We were unable to resolve this issue, so the program can only be executed from the command line.

All kinds of feedback are welcome but used at your own responsibility.

Please follow the steps in the manual.



ES
proyecto final consola retro, hecho por Pablo Escalona, Leonardo Campos y Rodrigo Olvera.
Este proyecto trata de emular una consola de videjuegos retro.

El objetivo de este proyecto es dar una propuesta de práctica de laboratorio para la asignatura de Fundamentos de sistemas embebidos.

para este proyecto se utilizó la versión más reciente a la fecha (14 de junio 2023)  de Raspberry Pi OS y 
un mando de PS4, aunque puede ser de cualquier otra plataforma


la idea principal era que al encender la Raspberry iniciara automáticamente se iniciara el script inicio.py, tratamos de hacerlo agregando en el archivo de configuracion rc.local
pero al agregar la linea "su - pi -c "/home/inicio.py &"" nos arrojaba un error al iniciar, además que la imagen personalizada ya no lograba verse.

El error mostrado es el siguiente:


[16.203151] rc.local[614]: Traceback (most recent call last):
[16.211714] rc.local[614]: File "/home/inicio.py", line 77, in <module>
[16.218736] rc.local[614]: File ""/home/inicio.py", line 33, in main
[16.221928] rc.local[614]: choice = input("ingrese su opción: ")
[16.229991] rc.local[614]: EOFError: EOF when reading a line.


Es cual no pudimos resolver, entonces solo se puede ejecutar el programa desde la línea de comandos. 

Se acepta todo tipo de retroalimentacion 
usarla bajo responsabilidad.

seguir pasos del manual.

