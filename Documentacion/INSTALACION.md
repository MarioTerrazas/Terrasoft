--

- Instalar Git.
- Instalar Node.js.
- Instalar Python.
- Instalar GitHub CLI.
- Instalar Ollama.
- Configurar PATH cuando sea necesario.
- ## PostgreSQL 17

Instalación mediante Winget:

```powershell
winget install --id PostgreSQL.PostgreSQL.17 --exact
```

Ruta de instalación:

```text
C:\Program Files\PostgreSQL\17
```

Agregar al PATH:

```text
C:\Program Files\PostgreSQL\17\bin
```

Verificación:

```powershell
psql --version
```