package main

import (
  "io"
  "log"
  "net/http"
  "time"

  "github.com/go-chi/chi/v5"
  "github.com/go-chi/chi/v5/middleware"
)

func main() {
  r := chi.NewRouter()
  r.Use(middleware.RequestID)
  r.Use(middleware.RealIP)
  r.Use(middleware.Logger)
  r.Use(middleware.Recoverer)

  r.Get("/healthz", func(w http.ResponseWriter, r *http.Request){
    w.WriteHeader(200); w.Write([]byte("ok"))
  })

  r.Get("/api/ci/status", proxyCIStatus)
  r.Post("/api/nodes/register", registerNode)
  r.Get("/api/nodes", listNodes)

  // proxy to local assistant for demo
  r.Post("/api/ai/ask", func(w http.ResponseWriter, r *http.Request){
    resp, err := http.Post("http://localhost:8083/ask", "application/json", r.Body)
    if err != nil {
      log.Println("ai proxy error:", err)
      w.WriteHeader(500); w.Write([]byte(`{"error":"assistant unreachable"}`))
      return
    }
    defer resp.Body.Close()
    w.WriteHeader(resp.StatusCode)
    io.Copy(w, resp.Body)
  })

  srv := &http.Server{
    Addr:         ":8085",
    Handler:      r,
    ReadTimeout:  10*time.Second,
    WriteTimeout: 10*time.Second,
    IdleTimeout:  120*time.Second,
  }

    log.Println("starting control-plane on :8085")
    err := http.ListenAndServe(":8085", nil)

    log.Fatalf("server error: %v", err)
  }


func proxyCIStatus(w http.ResponseWriter, r *http.Request){
  w.Header().Set("Content-Type", "application/json")
  w.Write([]byte(`{"pipelines":[{"id":"p1","name":"deploy-api","runId":"102","status":"success","timestamp":"2025-09-08T10:00:00Z"}]}`))
}

func registerNode(w http.ResponseWriter, r *http.Request){
  w.WriteHeader(201)
  w.Write([]byte(`{"status":"registered"}`))
}

func listNodes(w http.ResponseWriter, r *http.Request){
  w.Write([]byte(`[{"id":"node-01","peerId":"Qm..","uptime":0.997}]`))
}
