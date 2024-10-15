# Challenge Primary

## Tabla de Contenidos
1. [Prerequisitos](#prerequisitos)
2. [Exportando la Colección de Postman](#exportando-la-colección-de-postman)
3. [Instalando Dependencias](#instalando-dependencias)
4. [Ejecutando Pruebas](#ejecutando-pruebas)
5. [Viendo Reportes](#viendo-reportes)
6. [Agregando a .gitignore](#agregando-a-gitignore)

## Prerequisitos
- Asegúrate de tener **Node.js** y **npm** instalados en tu sistema.
- Clonar el repositorio: git clone https://github.com/yeyu2083/challenge_Primary.git
- Verifica que tu servidor esté en ejecución; de lo contrario, no podrás conectarte a la API, para ello ejecuta el siguiente comando en la terminal python app.py

## Exportando la Colección de Postman
1. Abre Postman.
2. Navega a la pestaña de **Colecciones** en el panel izquierdo.
3. Haz clic derecho sobre la colección `Challenge_Primary` y selecciona **Exportar**.
4. Elige el formato **Collection v2.1** y haz clic en **Exportar**.
5. Guarda el archivo exportado como `Challenge_Primary.postman_collection.json` en el directorio `collections` de tu proyecto.

## Instalando Dependencias
1. Abre una terminal en el directorio de tu proyecto.
2. Ejecuta el siguiente comando para instalar las dependencias necesarias:

   ```bash
   npm install newman newman-reporter-allure

## Problemas con dependencias:
npm install --legacy-peer-deps

## Ejecutar el script de la collection:
./run-newman.sh

## Generar el reporte y ver:
allure serve ./allure-results/
