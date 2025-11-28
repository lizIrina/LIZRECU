# 🐼 Mundo Panda - Llinin

Aplicación web sobre pandas desplegada automáticamente con CI/CD.

## 🚀 Tecnologías

- **Backend:** Flask (Python)
- **Contenedor:** Docker
- **CI/CD:** GitHub Actions
- **Proxy:** Traefik
- **Registro:** GitHub Container Registry

## 📁 Estructura del Proyecto

```
LIZRECU/
├── .github/workflows/
│   └── cicd.yml
├── aplicacion.py
├── requirements.txt
├── Dockerfile
├── stack.yml
├── .gitignore
└── .dockerignore
```

## 🔧 Configuración de Secrets

En GitHub → Settings → Secrets and variables → Actions:

| Secret | Descripción |
|--------|-------------|
| `GHCR_TOKEN` | Token de GitHub para Container Registry |
| `VPS_HOST` | IP o dominio del servidor |
| `VPS_USER` | Usuario SSH del servidor |
| `VPS_PASSWORD` | Contraseña SSH |
| `VPS_SSH_PORT` | Puerto SSH (ej: 22) |

## 🌐 Despliegue

El pipeline se ejecuta automáticamente en cada push a la rama `morocho`:

1. Build de la imagen Docker
2. Push a GitHub Container Registry
3. Copia del stack.yml al servidor
4. Deploy con Docker Swarm + Traefik

## 🔗 URL de Producción

**https://llinin.byronrm.com**

---

*Proyecto CI/CD - Examen Final* 🌸
