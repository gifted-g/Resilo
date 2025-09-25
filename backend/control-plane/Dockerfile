FROM golang:1.21-alpine AS build
WORKDIR /src
COPY . .
RUN go build -o /bin/control-plane main.go

FROM alpine:3.18
COPY --from=build /bin/control-plane /bin/control-plane
EXPOSE 8080
ENTRYPOINT ["/bin/control-plane"]
