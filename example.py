import docker
import time
client = docker.from_env()

# print(client.containers.list())



for container in client.containers.list():
    for stat in container.stats(decode=True):
     overview= {}
     overview["cpu_usage"]=stat["cpu_stats"]["cpu_usage"]["total_usage"]
     overview["memory_usage"]=stat["memory_stats"]["usage"]
     print (overview)
     time.sleep(30)