# workshop_docker_ao_vivo

```
git clone ...
cd ...
```

docker build ...

docker run ...

[ "poetry", "run", "streamlit", "app.py", "--server.port=8501", "--server.address=0.0.0.0" ]


docker build -t minha-primeira-imagem .


docker run -d -p 8501:8501 --name my-first-container minha-primeira-imagem


netstat -ano | findstr :8501 my-first-container
