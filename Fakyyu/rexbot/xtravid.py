import xtc
with open ( "./bug/xlvid.txt"  ,  "r" )  as  f:
    bugxtravid = f.read().split("\n")
link = "vmess://eyJhZGQiOiJ3YXJuYS5kYW16ejI1Lm15LmlkIiwiYWlkIjoiMCIsImhvc3QiOiJ3YXJuYS5kYW16ejI1Lm15LmlkIiwiaWQiOiIzMzAxMzAzOC1kM2JiLTVmMjgtYmY0OC04OTQxZTYwZjVlODEiLCJuZXQiOiJ3cyIsInBhdGgiOiIvdm1lc3MiLCJwb3J0IjoiNDQzIiwicHMiOiJGcmVlIDdEIiwic2N5Ijoibm9uZSIsInNuaSI6Indhcm5hLmRhbXp6MjUubXkuaWQiLCJ0bHMiOiJ0bHMiLCJ0eXBlIjoiIiwidiI6IjIifQ=="
import json
def xtravid(link):
    if link.startswith("vmess://"):
        basextravid = json.loads(xtc.convert_vmess(link))
        # Membuat template basextravid
        templatextravid = "proxies:\n"
        for i in range(len(bugxtravid)):
            templatextravid += f"""  - name: {basextravid["ps"]}
    server: {bugxtravid[i]}
    port: {basextravid["port"]}
    type: vmess
    uuid: {basextravid["id"]}
    alterId: 0
    cipher: {basextravid["type"]}
    udp: true
    xudp: true
    skip-cert-verify: false
    tls: true
    servername: {basextravid.get('sni') if basextravid.get("sni") else ""}
    network: {basextravid["net"]}
    ws-opts:
      path: {basextravid.get("path")}
      headers:
        Host: {basextravid.get("sni")}\n"""
        return( "```yaml\n" + templatextravid + "```")
    elif  link.startswith("ss://"):
        pass
    else:
        pass

# print(xtravid(link))
# print()