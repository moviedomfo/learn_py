    docs https://docs.python.org/es/3.13/tutorial/cl
    
 1. Run the FastAPI Server:

    1.1 uvicorn app.main:app --reload
    1.2 Esto lanza uvicorn en una nueva ventana y no te bloquea la consola actual.
        start uvicorn app.main:app --reload

 2. Forzá el cierre desde otra consola con taskkill
    tasklist | findstr uvicorn
    taskkill /PID 22848 /F
