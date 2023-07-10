FROM    python:3.10.6-bullseye AS builder
WORKDIR /usr/src/app
ENV     PATH="/usr/src/app/venv/bin:$PATH"
RUN     pip3 install --target=/usr/src/app/dependencies "git+https://github.com/aocana-data/monstry.git@monstry.v01#egg=monstry"



FROM    python:3.10-slim-bullseye
WORKDIR /usr/src/app

COPY --from=builder /usr/src/app/dependencies ./dependencies
ENV PYTHONPATH="${PYTHONPATH}:/usr/src/app/dependencies"

