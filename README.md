# Signature background removal service

## Routes:
- /apisignature/process
- /apisignature/process_view
- /apisignature/view

## How to use:

### Process
- Returns base64 processed signature
```shell
curl http://host:port/process -X POST -F image=@/path/to/image
```

### Process and View
- Returns url to view processed signature
```shell
curl http://host:port/process_view -X POST -F image=@/path/to/image
```