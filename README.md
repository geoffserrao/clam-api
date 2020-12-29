## Clam-API

### Introduction

clam-api is a fast JSON REST API using fastapi and clamdscan to provide scanning of uploaded files using clamdscan.

The API is in a separate docker container from clamd and uses using TCP port 31330 to stream the file to scan to the scanning daemon. 

### Example

```bash
❯ curl -s -F "file=@eicar.com" 127.0.0.1:8000/scan/ | jq
{
  "eicar.com": "Win.Test.EICAR_HDB-1 FOUND"
}
```
