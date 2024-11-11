ip = ["192.168.168.1", "192.168.168.2", "192.168.168.3"]
bug = ["google.com", "facebook.com", "amazon.com"]

# # Membuat template data
data = "proxies:\n"
for i in range(len(ip)):
    data += f"""  - name: {ip[i]}
    ip: {ip[i]}
    bug: {bug[i]}\n"""
    print(data)
#     data =+ f"""  - name: {data["ps"]}
#     server: {data["add"]}
#     port: {data["port"]}
#     type: vmess
#     uuid: {data["id"]}
#     alterId: 0
#     cipher: {data["type"]}
#     udp: true
#     skip-cert-verify: false
#     tls: {"true" if data.get("tls") == "tls" else "false"}
#     servername: {data.get('sni') if data.get("sni") else ""}
#     network": {data["net"]}
#     ws-opts:
#     path: {data.get("path")}
#     headers:
#       Host: {data.get("sni")}
# """
# print(data)

# for x in range(len)
import xtc
link='vmess://eyJ2IjogIjIiLCAicHMiOiAidHJpYWxYLTc2IiwgImFkZCI6ICJpa2R6LmRlbmthYXJhdnBuLm15LmlkIiwgInBvcnQiOiAiNDQzIiwgImlkIjogImUxYzkwM2FkLTNkNTItNDlhNi04ZTgyLTI1ZjAwNTMzM2ExZCIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAicGF0aCI6ICJ2bWVzcyIsICJ0eXBlIjogIm5vbmUiLCAiaG9zdCI6ICJpa2R6LmRlbmthYXJhdnBuLm15LmlkIiwgInRscyI6ICJ0bHMifQ'
print(xtc.convert_link(link))
