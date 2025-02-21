FROM parrotsec/core
WORKDIR /app
COPY . .
RUN docker run --name parrot-os parrotsec/core
RUN docker run --name parrot-os -ti parrotsec/core
CMD ["docker", "init"]
