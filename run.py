import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "src.main.config.http_server_configs:app",
        host="127.0.0.1",
        port=8001,
        reload=True,
        workers=3
    )
