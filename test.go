  package main
  import (
      "fmt"
      "log"
      "net/http"
      "os"
  )
  func main() {
      http.HandleFunc("/bar", func(w http.ResponseWriter, r *http.Request) {
          // The insecure user input is coming from the title parameter
          title := r.URL.Query().Get("title")
          // and used to directly open a file.
          // By using ../../../ attackers can access any file in any folder
          // such as the /etc/passwd file, or files containing sensitive data
          f, err := os.Open(title)
          if err != nil {
              fmt.Printf("Error: %v\n", err)
          }
          body := make([]byte, 5)
          if _, err = f.Read(body); err != nil {
              fmt.Printf("Error: %v\n", err)
          }
          fmt.Fprintf(w, "%s", body)
      })
      log.Fatal(http.ListenAndServe(":3000", nil))
  }
