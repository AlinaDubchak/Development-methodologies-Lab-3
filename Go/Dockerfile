FROM golang:latest

WORKDIR /app

# Dependancies
COPY go.mod go.sum ./

RUN go mod download

# Code
COPY . .

RUN go build -o build/fizzbuzz

EXPOSE 8080

CMD ["./build/fizzbuzz", "serve"]
