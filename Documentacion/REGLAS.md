# REGLAS DE TERRASOFT

**Versión:** 1.0  
**Estado:** Activo  
**Proyecto:** Ecosistema Terrasoft  
**Autor:** Mario Eduardo Terrazas Parada  
**Última actualización:** 14/07/2026  

---

# Objetivo

Establecer las reglas oficiales que guían el trabajo, la documentación, la arquitectura, el desarrollo y la gestión del conocimiento dentro de Terrasoft.

Estas reglas aplican a todos los productos actuales y futuros de la empresa.

---

# Regla 1 — Resolver problemas reales

Todo producto de Terrasoft deberá existir para resolver una necesidad real de una persona o empresa.

No se desarrollarán funciones únicamente porque parezcan interesantes.

---

# Regla 2 — Comprender antes de programar

Antes de escribir código se deberá comprender:

- El problema.
- El usuario.
- El proceso del negocio.
- El resultado esperado.

---

# Regla 3 — Diseñar antes de implementar

Toda funcionalidad importante deberá pasar por:

1. Análisis.
2. Diseño.
3. Documentación.
4. Revisión.
5. Implementación.
6. Pruebas.

---

# Regla 4 — La documentación es la fuente oficial

La memoria de una persona o de una inteligencia artificial no reemplaza la documentación.

Si existe una contradicción, la documentación aprobada será la referencia oficial.

---

# Regla 5 — El conocimiento pertenece al proyecto

Las decisiones, aprendizajes, comandos, problemas y soluciones importantes deberán quedar registrados dentro del proyecto.

El conocimiento no deberá depender exclusivamente de Mario, de ChatGPT o de TerrasoftAI.

---

# Regla 6 — Documentación y Knowledge son diferentes

La documentación oficial estará en:

```text
Terrasoft/Documentacion/

El conocimiento preparado para TerrasoftAI estará en:

Terrasoft/TerrasoftAI/Knowledge/

Ambos deberán mantenerse relacionados, pero no serán considerados el mismo contenido.
---

# Regla 7 — La documentación debe evolucionar

Cuando el producto cambie, la documentación correspondiente deberá actualizarse.

No se permitirá que la documentación quede desactualizada respecto al sistema.

Regla 8 — Todo cambio importante deberá rastrearse

Todo cambio relevante deberá conservarse mediante Git.

El historial deberá permitir saber:

Qué cambió.
Quién lo cambió.
Cuándo cambió.
Por qué cambió.
Regla 9 — Los commits deberán ser claros

No se utilizarán mensajes genéricos como:

cambios
update
corrección
nuevo
prueba

Los commits deberán explicar el avance realizado.

Ejemplo:

Sprint 2 - Aprueba DER v1.0 de FerreSys
Regla 10 — No acumular demasiados cambios

Se realizarán commits al terminar bloques coherentes de trabajo.

No se deberá acumular una gran cantidad de cambios sin guardar una versión estable.

Regla 11 — Cada Sprint tendrá registro

Cada Sprint deberá incluir:

Objetivo.
Trabajo realizado.
Decisiones importantes.
Resultado.
Aprendizajes.
Pendientes.
Próximo Sprint.
Regla 12 — Diario y Sprint tienen propósitos diferentes

El Diario responderá:

¿Qué se hizo durante este día?

La documentación de Sprint responderá:

¿Qué se logró durante todo el Sprint?

No se mezclará el detalle diario con el acta oficial del Sprint.

Regla 13 — Cada documento responderá una pregunta principal

Ejemplos:

PRODUCTO.md → ¿Qué es el producto?
MODULOS.md → ¿Qué partes componen el sistema?
CASOS_DE_USO.md → ¿Qué puede hacer cada usuario?
BASE_DATOS.md → ¿Cómo se organizarán los datos?
API.md → ¿Cómo se comunicará el sistema?

Se evitará duplicar contenido innecesariamente.

Regla 14 — Toda decisión arquitectónica deberá justificarse

Una decisión técnica no deberá tomarse únicamente porque una herramienta esté de moda.

Se deberá considerar:

Necesidad.
Complejidad.
Costo.
Seguridad.
Escalabilidad.
Mantenimiento.
Capacidad del equipo.
Regla 15 — No se implementará una tabla sin aprobación previa

Toda tabla deberá existir primero en:

El modelo conceptual.
El diccionario de datos.
El modelo lógico.
El DER.

Después podrá implementarse en PostgreSQL.

Regla 16 — El DER es el documento maestro del modelo de datos

El archivo oficial editable será:

FerreSys/Diagramas/DER.drawio

El archivo:

FerreSys/Diagramas/DER.png

será únicamente una exportación para visualización.

Toda modificación estructural deberá realizarse primero en el archivo editable.

Regla 17 — Cada tabla deberá pertenecer a un módulo

No se crearán tablas sueltas sin responsabilidad definida.

Ejemplos:

Módulo Comercial
CLIENTE
PEDIDO
DETALLE_PEDIDO
Módulo Inventario
PRODUCTO
ALMACEN
INVENTARIO
MOVIMIENTO_INVENTARIO
TIPO_MOVIMIENTO
Módulo Seguridad
ROL
USUARIO
Regla 18 — Mantener integridad y trazabilidad

Las operaciones importantes deberán registrar:

Usuario responsable.
Fecha.
Hora.
Acción.
Motivo.
Información afectada.

No se eliminará información importante sin conservar historial.

Regla 19 — Evitar eliminación física innecesaria

Productos, clientes, usuarios, pedidos y demás registros con historial deberán desactivarse mediante eliminación lógica cuando corresponda.

No se borrarán registros que sean necesarios para auditoría.

Regla 20 — Seguridad desde el diseño

Las contraseñas nunca deberán almacenarse en texto plano.

Los usuarios accederán únicamente a la información permitida por sus roles y permisos.

Las contraseñas, tokens y secretos no deberán subirse a GitHub.

Regla 21 — No guardar credenciales en documentos

No se escribirán contraseñas reales en:

Markdown.
Código fuente.
Scripts SQL.
Capturas.
Commits.
Repositorios públicos.

Las credenciales deberán almacenarse mediante variables de entorno o mecanismos seguros.

Regla 22 — La IA es un asistente, no la autoridad final

TerrasoftAI podrá:

Analizar.
Recomendar.
Documentar.
Detectar errores.
Ayudar a programar.

Las decisiones finales de negocio y arquitectura deberán ser revisadas y aprobadas por una persona responsable.

Regla 23 — La IA no deberá inventar información

Cuando TerrasoftAI no encuentre información suficiente deberá indicarlo claramente.

No deberá presentar suposiciones como si fueran decisiones oficiales del proyecto.

Regla 24 — El MVP deberá ser controlado

La primera versión no intentará implementar todas las ideas.

El MVP deberá concentrarse en resolver los problemas principales del primer cliente.

Toda función futura deberá clasificarse como:

MVP.
Segunda fase.
Futuro.
Regla 25 — Cada módulo deberá resolver una necesidad validada

Una nueva función deberá responder:

¿Qué problema resuelve?
¿Quién la necesita?
¿Cómo se validará?
¿Qué ocurriría si no se desarrolla?
Regla 26 — Simplicidad antes que complejidad

Se elegirá la solución más sencilla que cumpla correctamente el objetivo.

No se agregará complejidad técnica sin una justificación real.

Regla 27 — Calidad antes que velocidad

El objetivo no será avanzar rápidamente creando errores.

Se priorizarán:

Claridad.
Seguridad.
Mantenimiento.
Pruebas.
Documentación.
Regla 28 — El sistema deberá poder crecer

Las decisiones deberán considerar futuras:

Sucursales.
Almacenes.
Usuarios.
Ferreterías.
Integraciones.
Aplicaciones móviles.
Servicios de inteligencia artificial.

La escalabilidad no deberá provocar complejidad innecesaria en el MVP.

Regla 29 — Base de datos normalizada

La información deberá almacenarse evitando duplicaciones y contradicciones.

Las relaciones deberán utilizar claves primarias, claves foráneas y restricciones de integridad.

Regla 30 — Respetar las dependencias

Las tablas y módulos deberán crearse en un orden compatible con sus dependencias.

Ejemplo:

ROL
↓
USUARIO
↓
MOVIMIENTO_INVENTARIO

No se implementará una entidad dependiente antes de su entidad principal.

Regla 31 — Usar nombres consistentes

Se utilizarán nombres claros y coherentes.

Ejemplos:

id_cliente
id_producto
fecha_creacion
fecha_actualizacion

No se mezclarán convenciones diferentes sin una decisión documentada.

Regla 32 — Separar ambientes y responsabilidades

Se mantendrán separados:

Documentación.
Backend.
Frontend.
Base de datos.
Diagramas.
Scripts.
Knowledge.
Backups.

Cada carpeta tendrá una responsabilidad definida.

Regla 33 — Los archivos generados no reemplazan a los editables

Ejemplos:

DER.drawio es el archivo maestro.
DER.png es una exportación.
El código fuente es el archivo maestro.
Los ejecutables son resultados derivados.
Regla 34 — Probar antes de declarar terminado

Una función no se considerará completada solo porque compile o se vea correctamente.

Deberá comprobarse:

Caso exitoso.
Datos inválidos.
Permisos.
Errores.
Integridad de datos.
Comportamiento móvil cuando corresponda.
Regla 35 — Mantener copias de seguridad

Antes de modificar configuraciones sensibles o información importante se deberá crear una copia de seguridad.

Ejemplos:

Base de datos.
Archivos de configuración.
Diagramas.
Documentación crítica.
Regla 36 — No subir Backups innecesarios a Git

Los respaldos pesados, temporales o con información sensible deberán excluirse mediante .gitignore.

Solo se versionarán los archivos que sean necesarios y seguros.

Regla 37 — Toda herramienta deberá documentarse

Cuando se instale una herramienta se registrará:

Nombre.
Versión.
Comando de instalación.
Ruta.
Configuración.
Verificación.
Problemas encontrados.
Regla 38 — El entorno deberá ser reproducible

Otro desarrollador deberá poder preparar una computadora siguiendo INSTALACION.md y COMANDOS.md.

El proyecto no deberá depender de configuraciones desconocidas.

Regla 39 — No afirmar que somos únicos sin investigación

Terrasoft no deberá declarar que un producto no tiene competencia sin una investigación verificable.

La diferenciación deberá demostrarse mediante:

Especialización.
Experiencia de usuario.
Integración.
Resultados.
Validación con clientes.
Regla 40 — El cliente piloto validará el producto

Marito será el primer cliente piloto de FerreSys.

Sus necesidades serán importantes para validar el MVP, pero el sistema deberá evitar depender únicamente de una sola persona o negocio.

Regla 41 — Las normas externas deberán verificarse

Las funciones relacionadas con impuestos, facturación o normativa deberán cumplir los requisitos vigentes de las autoridades correspondientes.

No se considerará factura válida únicamente por generar un PDF.

Regla 42 — Actualizar antes de cerrar la jornada

Cuando exista un avance importante, antes de finalizar se deberá revisar si corresponde actualizar:

Diario.
ROADMAP.
CHANGELOG.
DECISIONES.
Documento del Sprint.
Knowledge.
Git.
Regla 43 — Flujo oficial de trabajo

El flujo general de Terrasoft será:

Idea
↓
Análisis
↓
Validación
↓
Documentación
↓
Arquitectura
↓
Desarrollo
↓
Pruebas
↓
Commit
↓
Push
↓
Actualización de Knowledge
Regla 44 — Mejorar sin miedo a corregir

Una decisión anterior podrá modificarse cuando exista una solución claramente mejor.

El cambio deberá:

Explicarse.
Documentarse.
Actualizar los archivos relacionados.
Registrarse en Git.
Regla 45 — No buscar perfección infinita

Terrasoft trabajará con calidad, pero evitará detener indefinidamente el producto buscando una perfección imposible.

Cuando una solución sea segura, mantenible y suficiente para el objetivo, podrá aprobarse y evolucionar después.

Principio final

En Terrasoft no programamos para descubrir el diseño; diseñamos para que programar sea sencillo.


Después guárdalo:

```powershell
git status
git add .
git commit -m "Documentación - Consolida las reglas oficiales de Terrasoft"
git push
git status

También corrige en tu ROADMAP.md estas dos líneas, porque el DER ya está terminado:

- [x] Completar DER.
- [ ] Diseñar el Modelo Físico PostgreSQL.

Y puedes agregar:

- [x] Crear la base de datos PostgreSQL.