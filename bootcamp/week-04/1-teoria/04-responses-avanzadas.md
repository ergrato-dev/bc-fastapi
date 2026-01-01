# 🚀 Responses Avanzadas

## 🎯 Objetivos de Aprendizaje

Al finalizar este tema, serás capaz de:

- ✅ Usar diferentes tipos de Response
- ✅ Implementar redirecciones
- ✅ Streaming de datos grandes
- ✅ Respuestas con archivos
- ✅ Personalizar headers de respuesta

---

## 📚 Contenido

### 1. Tipos de Response en FastAPI

FastAPI soporta múltiples tipos de respuesta:

```python
from fastapi import FastAPI
from fastapi.responses import (
    JSONResponse,      # JSON (default)
    HTMLResponse,      # HTML
    PlainTextResponse, # Texto plano
    RedirectResponse,  # Redirección
    StreamingResponse, # Streaming
    FileResponse,      # Archivos
    Response           # Respuesta base
)

app = FastAPI()
```

---

### 2. JSONResponse

La respuesta por defecto, pero puedes personalizarla:

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# FastAPI usa JSONResponse automáticamente
@app.get("/items")
async def get_items():
    return {"items": [1, 2, 3]}

# JSONResponse explícito para más control
@app.get("/custom-json")
async def custom_json():
    content = {"message": "Custom response"}
    return JSONResponse(
        content=content,
        status_code=200,
        headers={
            "X-Custom-Header": "custom-value",
            "Cache-Control": "max-age=3600"
        }
    )

# JSONResponse con encoding especial
@app.get("/unicode")
async def unicode_response():
    data = {"greeting": "¡Hola! 你好 مرحبا"}
    return JSONResponse(
        content=data,
        media_type="application/json; charset=utf-8"
    )
```

---

### 3. HTMLResponse

Para respuestas HTML:

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>FastAPI HTML</title>
        </head>
        <body>
            <h1>Welcome to FastAPI!</h1>
            <p>This is an HTML response.</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# Con status code personalizado
@app.get("/error-page", response_class=HTMLResponse)
async def error_page():
    return HTMLResponse(
        content="<h1>404 - Page Not Found</h1>",
        status_code=404
    )
```

---

### 4. PlainTextResponse

Para texto plano:

```python
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/text", response_class=PlainTextResponse)
async def text_response():
    return "This is plain text response"

@app.get("/robots.txt", response_class=PlainTextResponse)
async def robots():
    return """User-agent: *
Allow: /
Disallow: /admin/
"""

@app.get("/health")
async def health_check():
    return PlainTextResponse(
        content="OK",
        status_code=200,
        media_type="text/plain"
    )
```

---

### 5. RedirectResponse

Para redirecciones HTTP:

```python
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

# Redirección temporal (307)
@app.get("/old-path")
async def redirect_temp():
    return RedirectResponse(url="/new-path")

# Redirección permanente (301)
@app.get("/legacy")
async def redirect_permanent():
    return RedirectResponse(
        url="/modern",
        status_code=301  # Moved Permanently
    )

# Redirección después de POST (303 See Other)
@app.post("/submit")
async def submit_form(data: dict):
    # Procesar datos...
    return RedirectResponse(
        url="/success",
        status_code=303  # See Other - GET después de POST
    )

# Redirección externa
@app.get("/docs-redirect")
async def redirect_external():
    return RedirectResponse(
        url="https://fastapi.tiangolo.com/",
        status_code=302
    )
```

#### Códigos de Redirección

| Código | Nombre | Uso |
|--------|--------|-----|
| 301 | Moved Permanently | URL cambió permanentemente |
| 302 | Found | Redirección temporal |
| 303 | See Other | Redirigir a GET después de POST |
| 307 | Temporary Redirect | Mantiene método HTTP |
| 308 | Permanent Redirect | Permanente, mantiene método |

---

### 6. StreamingResponse

Para datos grandes o generados en tiempo real:

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

# Generador simple
def generate_numbers():
    for i in range(100):
        yield f"Number: {i}\n"

@app.get("/stream-numbers")
async def stream_numbers():
    return StreamingResponse(
        generate_numbers(),
        media_type="text/plain"
    )

# Generador async
async def async_generator():
    for i in range(10):
        await asyncio.sleep(0.5)  # Simular procesamiento
        yield f"data: {{'count': {i}}}\n\n"

@app.get("/sse")
async def server_sent_events():
    """Server-Sent Events para actualizaciones en tiempo real"""
    return StreamingResponse(
        async_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive"
        }
    )

# Streaming de archivo grande
async def file_streamer(filepath: str, chunk_size: int = 8192):
    async with aiofiles.open(filepath, "rb") as f:
        while chunk := await f.read(chunk_size):
            yield chunk

@app.get("/download-large")
async def download_large_file():
    return StreamingResponse(
        file_streamer("/path/to/large/file.zip"),
        media_type="application/zip",
        headers={
            "Content-Disposition": "attachment; filename=large_file.zip"
        }
    )
```

---

### 7. FileResponse

Para servir archivos:

```python
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

app = FastAPI()

FILES_DIR = Path("./files")

@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = FILES_DIR / filename
    
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(
        path=file_path,
        filename=filename,  # Nombre sugerido para descarga
        media_type="application/octet-stream"
    )

# Imagen con tipo específico
@app.get("/images/{image_name}")
async def get_image(image_name: str):
    image_path = FILES_DIR / "images" / image_name
    
    if not image_path.exists():
        raise HTTPException(status_code=404, detail="Image not found")
    
    # Determinar media type
    suffix = image_path.suffix.lower()
    media_types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp"
    }
    
    return FileResponse(
        path=image_path,
        media_type=media_types.get(suffix, "application/octet-stream")
    )

# PDF
@app.get("/reports/{report_id}")
async def get_report(report_id: int):
    report_path = FILES_DIR / f"report_{report_id}.pdf"
    
    if not report_path.exists():
        raise HTTPException(status_code=404, detail="Report not found")
    
    return FileResponse(
        path=report_path,
        filename=f"report_{report_id}.pdf",
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"inline; filename=report_{report_id}.pdf"
            # "inline" muestra en navegador, "attachment" fuerza descarga
        }
    )
```

---

### 8. Response Base

Para control total de la respuesta:

```python
from fastapi import FastAPI, Response

app = FastAPI()

# Respuesta personalizada
@app.get("/custom")
async def custom_response():
    return Response(
        content="Custom content",
        status_code=200,
        media_type="text/plain",
        headers={"X-Custom": "value"}
    )

# XML Response
@app.get("/xml")
async def xml_response():
    xml_content = """<?xml version="1.0"?>
    <root>
        <item id="1">
            <name>Item 1</name>
        </item>
    </root>
    """
    return Response(
        content=xml_content,
        media_type="application/xml"
    )

# CSV Response
@app.get("/csv")
async def csv_response():
    csv_content = """id,name,price
1,Item 1,10.00
2,Item 2,20.00
3,Item 3,30.00
"""
    return Response(
        content=csv_content,
        media_type="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=data.csv"
        }
    )
```

---

### 9. Modificar Response en el Endpoint

Usando el parámetro `Response`:

```python
from fastapi import FastAPI, Response, Cookie

app = FastAPI()

# Agregar headers
@app.get("/with-headers")
async def add_headers(response: Response):
    response.headers["X-Request-ID"] = "abc123"
    response.headers["X-Process-Time"] = "0.05"
    return {"message": "Headers added"}

# Establecer cookies
@app.post("/login")
async def login(response: Response, username: str):
    # Validar usuario...
    response.set_cookie(
        key="session_id",
        value="abc123xyz",
        httponly=True,      # No accesible desde JavaScript
        secure=True,        # Solo HTTPS
        samesite="lax",     # Protección CSRF
        max_age=3600        # 1 hora
    )
    return {"message": f"Welcome {username}"}

# Eliminar cookies
@app.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key="session_id")
    return {"message": "Logged out"}

# Leer cookies
@app.get("/profile")
async def profile(session_id: str = Cookie(None)):
    if not session_id:
        return {"message": "Not logged in"}
    return {"session": session_id}
```

---

### 10. Background Tasks con Response

Ejecutar tareas después de enviar la respuesta:

```python
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse
import time

app = FastAPI()

def send_email(email: str, message: str):
    """Tarea que se ejecuta en background"""
    time.sleep(5)  # Simular envío de email
    print(f"Email sent to {email}: {message}")

def log_operation(operation: str, user_id: int):
    """Loggear operación"""
    print(f"Operation: {operation} by user {user_id}")

@app.post("/register")
async def register(
    email: str,
    background_tasks: BackgroundTasks
):
    # Agregar tareas al background
    background_tasks.add_task(
        send_email,
        email=email,
        message="Welcome to our platform!"
    )
    background_tasks.add_task(
        log_operation,
        operation="user_registered",
        user_id=1
    )
    
    # La respuesta se envía inmediatamente
    # Las tareas se ejecutan después
    return {"message": "Registration successful, check your email"}

# Con JSONResponse y background tasks
@app.post("/order")
async def create_order(
    order_data: dict,
    background_tasks: BackgroundTasks
):
    # Crear orden...
    order_id = 123
    
    # Programar confirmación por email
    background_tasks.add_task(
        send_email,
        email=order_data.get("email"),
        message=f"Order {order_id} confirmed"
    )
    
    return JSONResponse(
        content={"order_id": order_id, "status": "created"},
        status_code=201
    )
```

---

### 11. Response Class por Defecto

Establecer tipo de respuesta por defecto para el router:

```python
from fastapi import FastAPI, APIRouter
from fastapi.responses import ORJSONResponse, UJSONResponse

# App con response class por defecto
app = FastAPI(default_response_class=ORJSONResponse)

# Todos los endpoints usarán ORJSONResponse
@app.get("/fast-json")
async def fast_json():
    return {"data": [1, 2, 3] * 1000}  # Serialización más rápida

# Router con response class específica
html_router = APIRouter(
    prefix="/pages",
    default_response_class=HTMLResponse
)

@html_router.get("/about")
async def about_page():
    return "<h1>About Us</h1>"

app.include_router(html_router)
```

---

## 🎯 Resumen

| Response | Uso | Media Type |
|----------|-----|------------|
| `JSONResponse` | Datos JSON (default) | application/json |
| `HTMLResponse` | Páginas HTML | text/html |
| `PlainTextResponse` | Texto plano | text/plain |
| `RedirectResponse` | Redirecciones | - |
| `StreamingResponse` | Datos grandes/streaming | variable |
| `FileResponse` | Servir archivos | variable |
| `Response` | Control total | variable |
| `ORJSONResponse` | JSON rápido | application/json |

### Mejores Prácticas

1. ✅ Usa `response_class` en el decorador para documentación
2. ✅ `StreamingResponse` para archivos grandes
3. ✅ `BackgroundTasks` para operaciones lentas
4. ✅ Headers apropiados para caché y seguridad
5. ✅ `Content-Disposition` para descargas

---

## 📚 Recursos Adicionales

- [FastAPI Custom Response](https://fastapi.tiangolo.com/advanced/custom-response/)
- [FastAPI Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/)
- [Starlette Responses](https://www.starlette.io/responses/)

---

[← Anterior: Manejo de Errores](03-manejo-errores.md) | [Siguiente: Documentación OpenAPI →](05-documentacion-openapi.md)
