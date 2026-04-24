
# Trabajo Práctico: Integración Continua - Grupo 1

## Proyecto: Módulo de Perfiles (Ingeniería de Software III)

Este repositorio contiene la implementación de un módulo de gestión de perfiles de usuario, desarrollado para la cátedra de Ingeniería de Software III (Universidad de la Cuenca del Plata). El foco principal de esta actividad es la **Gestión de la Configuración** y la **Integración Continua (CI)** mediante herramientas de automatización.

### Integrantes y División de Tareas
* *Bagneres Francisco*: Configuración de Pipeline CI (`main-ci.yml `).
* *Hope John*: Revisión de código y soporte de integración.
* *Tabarez Kiara*: Desarrollo de Tests Unitarios (`test_schema.py`).
* *Tomas Mateo*: Diseño de Base de Datos SQL (`Profiles.sql`).

##Instrucciones para Clonar y Ejecutar
Para trabajar con este proyecto de forma local, sigue estos pasos:
### 1. Clonar el repositorio
Abre una terminal y ejecuta el siguiente comando:
```bash
git clone https://github.com/FranBag/TPI_Grupo1_Ingenieria_de_Software_III.git
cd TPI_Grupo1_Ingenieria_de_Software_III
```
### 2. Requisitos previos
Es necesario tener instalado **Python 3.10 o superior** para ejecutar los scripts de validación.
### 3. Ejecutar los tests localmente
Antes de subir cambios a tu rama, puedes validar que el archivo SQL cumple con los requisitos ejecutando:
```bash
python test_schema.py
```

## Configuración de Integración Continua (CI)
Este proyecto utiliza **GitHub Actions** para garantizar la calidad del código en cada contribución.
* **Enlace al archivo de configuración:** .github/workflows/main-ci.yml 
https://github.com/FranBag/TPI_Grupo1_Ingenieria_de_Software_III.git/main/.github/workflows/main-ci.yml

### ¿Cómo funciona la CI en este proyecto?
Nuestro pipeline se dispara automáticamente ante cada `push` o `pull request` hacia la rama `main`. El proceso automatizado es el siguiente:
1. **Validación de Estilo (Linting):** Se utiliza `sqlfluff` para revisar que el archivo `Profiles.sql` cumpla con los estándares de sintaxis y estilo del equipo (por ejemplo, el uso obligatorio de mayúsculas en palabras clave).
2. **Pruebas Unitarias:** Se ejecuta el script `test_schema.py` que realiza 5 comprobaciones automáticas sobre el esquema de la base de datos (existencia de Clave Primaria, campos obligatorios como `birth_date`, tipos de datos correctos, etc.).
3. **Reporte de Estado:** Si alguna prueba falla o el estilo es incorrecto, GitHub marca el proceso con un error (X roja) y bloquea la integración, notificando al equipo para su corrección.

## Estructura del Repositorio
* `Profiles.sql`: Script principal de creación de la tabla de perfiles.
* `test_schema.py`: Script de validación lógica de los 5 tests unitarios.
* `.github/workflows/main-ci.yml`: Definición del pipeline de automatización.
