# This Dockerfile creates a containerized FastAPI application for serving ML predictions.

# BASE IMAGE

FROM python:3.13.5-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /src
ENV PATH="/src/.venv/bin:$PATH"
COPY "pyproject.toml" "uv.lock" ".python-version" ./
RUN uv sync --locked
COPY "pipeline_v1.bin" "pred.py" "test.py" ./
EXPOSE 9696
ENTRYPOINT ["uvicorn", "pred:app", "--host", "0.0.0.0", "--port", "9696"]
