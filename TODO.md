# ✅ TODO – Proyecto Torneo de Videojuegos

---

## 📁 Base del Proyecto

- [X] **Agregar script `crea_db.py`** para crear la base de datos y tabla de usuarios.
- [X] ✍️ Documentar en `README.md` cómo ejecutar `crea_db.py`.
- [X] Crear tabla games (juegos de la competición)
- [ ] Crear tabla matches o partidas (relaciona usuarios, juegos, resultados, nivel)
- [X] Añadir campo nivel (amateur, normal, expert) en la inscripción o partida
- [ ] Definir y documentar la mecánica del torneo (puntos, tiempos, eliminaciones, etc.)
- [X] Registrar resultados de partidas/juegos 
- [X] Calcular y mostrar ranking general y por juego
- Para el modelo eliminación - ya veremos si lo hago: 
  - Requiere lógica adicional:
      Crear rondas, emparejamientos y marcar eliminados.
      Guardar el estado de cada ronda y quién avanza.
      
---

## 🔐 Autenticación y Seguridad

- [ ] 🔑 Crear **panel de administrador** con un correo y contraseña predefinidos.
- [ ] 🛡️ Proteger rutas para que solo el **admin** pueda acceder a ciertas páginas.
- [ ] 🔐 Mejorar la **seguridad del registro de usuarios**:
  - Validación de email
  - Contraseñas seguras
  - Evitar duplicados
- [ ] 📧 Enviar **correo de confirmación** tras el registro.
- [ ] 💌 Enviar **correo de bienvenida** al nuevo usuario registrado.

---

## 🔁 Flujo de Usuario

- [X] 🔄 Tras registrarse, **redirigir automáticamente al login**.
- [X] 🔓 Crear página de **login** con validaciones y sesiones.
- [X] 🚪 Implementar **logout**.

---

## 🧑‍💻 Paneles de Usuario

- [X] 🧍‍♂️ Crear **Dashboard para usuarios registrados**:
  - Vista de sus juegos o partidas
  - Estadísticas básicas
- [ ] 👑 Crear **Dashboard para administrador**:
  - [ ] 📋 Listar participantes
  - [ ] ➕ Crear participantes
  - [ ] ✏️ Editar participantes
  - [ ] ❌ Eliminar participantes
  - [ ] 🎮 Crear / editar / eliminar juegos

---

## 🛠️ Bonus

- [ ] ⚙️ Añadir sistema de roles (admin / user)
- [ ] 📊 Implementar gráficas con estadísticas del torneo (ranking, puntuaciones, etc.)
