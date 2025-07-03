# ✅ TODO – Proyecto Torneo de Videojuegos

---

## 📁 Base del Proyecto

- [X] **Agregar script `crea_db.py`** para crear la base de datos y tabla de usuarios.
- [ ] ✍️ Documentar en `README.md` cómo ejecutar `crea_db.py`.

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

- [ ] 🔄 Tras registrarse, **redirigir automáticamente al login**.
- [ ] 🔓 Crear página de **login** con validaciones y sesiones.
- [ ] 🚪 Implementar **logout**.

---

## 🧑‍💻 Paneles de Usuario

- [ ] 🧍‍♂️ Crear **Dashboard para usuarios registrados**:
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
- [ ] 🌐 Añadir internacionalización si se requiere (opcional)
