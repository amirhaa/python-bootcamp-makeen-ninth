from datetime import datetime, timedelta
now = datetime.now()
now.replace(microsecond=0)

with open('q10_file.txt', 'w') as f10:
    f10.write(f'yesterday: "{now - timedelta(days=1)}"\ntoday:     "{now}"\ntomorrow:  "{now - timedelta(days=-1)}"')
