failed_attempts = []
with open ("sample.log.save","r")as file:
    for line in file:
        if line.startswith("Failed login"):
            parts=line.split()
            ip_address=parts[3]
            failed_attempts.append(ip_address)

def count_ip(failed_attempts):
  unique_ips=set(failed_attempts)
  results=[]
  for ip_address in unique_ips:
    result=failed_attempts.count(ip_address)
    results.append((ip_address, result))
  return results
result = count_ip(failed_attempts)
print("===== Failed Login Report =====")
for ip, count in result:
   print(f"ip:{ip}")
   print(f"Failed Attempts:{count}")
   if count>=3:
    print("ALERT: Suspicious IP detected")


      

           
