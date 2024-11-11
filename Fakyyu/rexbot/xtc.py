import re
import json
import base64
def convert_link(link):
    # Deteksi tipe link
    if link.startswith("vmess://"):
        return convert_vmess(link)
    elif link.startswith("vless://"):
        return convert_vless(link)
    elif link.startswith("trojan://"):
        return convert_trojan(link)
    else:
        return None

def convert_vmess(link):
    s = str(link[8:]).strip()
    padding = len(s) % 4
    if padding == 1:
        # Handle invalid base64 strings
        return ''
    elif padding == 2:
        s += '=='
    elif padding == 3:
        s += '='
    # Decode link
    decoded = base64.b64decode(s, validate=True).decode()
    
    # Parsing data
    data = json.loads(decoded)
    
    # Buat format Clash
    clash_config =f"""
```yaml
proxies:
  - name: {data["ps"]}
    server: {data["add"]}
    port: {data["port"]}
    type: vmess
    uuid: {data["id"]}
    alterId: 0
    cipher: auto
    udp: true
    skip-cert-verify: false
    tls: {"true" if data.get("tls") == "tls" else "false"}
    servername: {data.get('sni') if data.get("sni") else ""}
    network: {data["net"]}
    ws-opts:
      path: {data.get("path")}
      headers:
        Host: {data.get("sni")}
```
    """
    
    return json.dumps(data, indent=2)

def convert_vless(link):
    # Decode link
    decoded = base64.b64decode(link[8:]).decode()
    
    # Parsing data
    data = decoded.split("?")
    server_info = data[0].split(":")
    query_params = {x.split("=")[0]: x.split("=")[1] for x in data[1].split("&")}
    
    # Buat format Clash
    cek = """
    ```yaml
proxies:
  - name: {data["ps"]}
    server: {data["add"]}
    port: {data["port"]}
    type: vless
    uuid: {data["id"]}
    alterId: 0
    cipher: {data["type"]}
    udp: true
    skip-cert-verify: false
    tls: {"true" if data.get("tls") == "tls" else "false"}
    servername: {data.get('sni') if data.get("sni") else ""}
    network": {data["net"]}
    ws-opts:
    path: {data.get("path")}
    headers:
      Host: {data.get("sni")}
```
    """
    return cek

def convert_trojan(link):
    # Decode link
    link_parts = link.split("://")[1].split("@")
    
    # Parsing data
    password = link_parts[0]
    server_port = link_parts[1].split("?")[0].split(":")
    server = server_port[0]
    port = int(server_port[1])
    sni = link_parts[1].split("sni=")[1].split("&")[0].split('#')[0]
    nama =  link_parts[1].split('#')[1]
    path = link_parts[1].split('%2F')[1].split('&')[0]

    # Buat format Clash
    clash_config =f"""
proxies:
```yaml
  - name: {nama}
    server: {server}
    port: {port}
    type: trojan
    password: {password}
    network: ws
    sni: {sni}
    skip-cert-verify: false
    udp: true
    ws-opts:
    path: /{path}
    headers:
        Host: {server}
```
"""
    return clash_config #json.dumps(clash_config, indent=2)


# def test(link):
#     link_parts = link.split("://")[1].split("@")
#     sni = link_parts[1].split("sni=")[1].split("&")[0].split('#')[0]
#     print(sni)
# print(test(link='trojan://31e5f266-3101-4074-90d8-f38a09d6a864@bugkamu.com:443?path=%2Ftrojan&security=tls&host=dtcm.denkaaravpn.my.id&type=ws&sni=dtcm.denkaaravpn.my.id#trialX-199'))