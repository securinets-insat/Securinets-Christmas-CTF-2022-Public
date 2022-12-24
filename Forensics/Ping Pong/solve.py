import pyshark
file=pyshark.FileCapture("task.pcap")
link=""
password=""
for p in file:
    link+=chr(int(p.ip.dst.split('.')[3]))
    password+=chr(int(p.icmp.code))
print("Link",link)
print("Password",password)