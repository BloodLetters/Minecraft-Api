# Minecraft-Api
Just another simple python minecraft rest-api

# Install
```
1). pip install -r requirements.txt
2). edit config.json
3). run main.py
4). Check http://localhost:5000/api
```

# Expected Result
```json
// Java
{
  "isonline": true,
  "ip": "serverip",
  "port": 25565,
  "online": 1,
  "max": 100,
  "players": {
    "1": {
      "name":"PlayeName",
      "uuid":"UUID Of Player"}
    },
  "version": "Pufferfish 1.20",
  "protocol":-1
}
```
