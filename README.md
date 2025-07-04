# 🎮 Torneo de Videojuegos

**Autor:**  
Carolina Rodríguez  
Curso: Proyecto Final Python - Propuesta C

![Foto del autor](coloca_aquí_tu_foto.jpg) <!-- Puedes cambiar por un link externo si lo subes a GitHub -->

---

## 📑 Índice

1. [Descripción general del proyecto](#descripción-general-del-proyecto)  
2. [Objetivos y alcance](#objetivos-y-alcance)  
3. [Stack tecnológico y alternativas evaluadas](#stack-tecnológico-y-alternativas-evaluadas)  
4. [Modelo de datos](#modelo-de-datos)  
5. [Requisitos de la aplicación](#requisitos-de-la-aplicación)  
6. [Manual de instalación](#manual-de-instalación)  
7. [Conclusiones](#conclusiones)  
8. [Evolutivos del proyecto](#evolutivos-del-proyecto)  

---

## 🧾 Descripción general del proyecto

Aplicación web desarrollada en **Python** con **Flask** para la gestión de un torneo de videojuegos. Permite:

- El registro y control de acceso de participantes y administradores  
- La gestión de juegos y usuarios  
- La visualización de resultados mediante gráficas  

El objetivo es facilitar la organización y seguimiento de torneos de forma sencilla y segura.

---

## 🎯 Objetivos y alcance

### Objetivos

- Permitir el registro y login seguro de participantes y administradores  
- Gestionar la información de los participantes y los juegos del torneo  
- Visualizar resultados y estadísticas mediante gráficas  
- Garantizar la seguridad y privacidad de los datos  

### Alcance

**Incluye:**  
- Registro/login  
- Gestión de usuarios y juegos  
- Visualización de resultados  
- Panel de administración

**No incluye:**  
- Integración con plataformas externas  
- Pagos online  
- Soporte multilenguaje  

---

## 🧰 Stack tecnológico y alternativas evaluadas

### Stack tecnológico

- **Lenguaje:** Python 3  
- **Framework:** Flask  
- **Base de datos:** SQLite (por simplicidad y portabilidad)  
- **Frontend:** HTML + Bootstrap (tema de [Bootswatch](https://bootswatch.com))  
- **Librerías:** Jinja2, Chart.js o Matplotlib (para gráficas)  

### Alternativas evaluadas

| Alternativa       | Evaluación |
|-------------------|------------|
| Django            | Muy robusto, pero excesivo para este proyecto pequeño |
| PostgreSQL/MySQL  | Más potentes, pero SQLite es suficiente para el alcance |
| Tkinter           | Solo válido para apps de escritorio, no web |

---

## 🗂 Modelo de datos

### Explicación

Se utiliza SQLite para almacenar usuarios, juegos y resultados. Es una base de datos ligera, fácil de integrar con Flask y suficiente para el alcance del proyecto.

### Esquema de tablas (ejemplo)

- **Usuario:** `id`, `nombre`, `email`, `contraseña`, `rol` (participante/admin), `nivel`  
- **Juego:** `id`, `nombre`, `descripción`  
- **Participación:** `id`, `usuario_id`, `juego_id`, `puntuación`, `tiempo`

<!-- Puedes insertar aquí un diagrama visual generado con diagrams.net -->

---

## ✅ Requisitos de la aplicación

### Requisitos funcionales

- Registro de usuarios y login seguro  
- Panel de administración para gestionar participantes y juegos  
- Visualización de estadísticas y resultados en gráficas  
- Control de acceso según rol (participante o administrador)

### Requisitos no funcionales

- Seguridad en el almacenamiento de contraseñas (hashing)  
- Interfaz intuitiva y responsive  
- Facilidad de despliegue y mantenimiento

<!-- Puedes incluir aquí capturas de pantalla de las páginas principales -->

---

## 🛠 Manual de instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Estivbi/torneo_videojuegos.git
cd torneo_videojuegos
```
### 2. Crear y activar un entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Crear las tablas de la base de datos (usuarios, juegos y partidas)

```bash
python crea_db.py
``` 

### 5. Ejecutar la aplicación

```bash
python app.py
``` 