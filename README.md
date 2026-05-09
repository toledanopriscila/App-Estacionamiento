Sistema de Gestión de Estacionamiento Autónomo Descripción Este proyecto es una API RESTful desarrollada en Flask para gestionar un sistema de estacionamiento, permitiendo controlar vehículos, ingresos, egresos y tarifas. 

Integrantes del Grupo: Priscila Toledano

Requisitos Técnicos Backend: Flask
   
ORM: SQLAlchemy   
Base de Datos: MySQL   
Configuración: Uso de variables de entorno con .env   
Endpoints PrincipalesGET /vehiculos: Registrar o listar vehículos. 
 
GET /ingreso: Registrar entrada.  
GET /egreso: Registrar salida y cálculo de tarifa.  
GET /espacios: Ver lugares disponibles.  
Cómo EjecutarClonar el repositorio.  
Instalar dependencias: pip install -r requirements.txt.  
Configurar el archivo .env.
Ejecutar: python app.py.
