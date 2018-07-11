import re
matches = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', input(), re.IGNORECASE)
if matches:
    for i in matches:
        print(i)
else:
    print('-1')



