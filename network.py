import subprocess

# Ifconfig -> ipconfig: Get network interface configuration (Windows)
def get_ifconfig():
    result = subprocess.run(['ipconfig'], stdout=subprocess.PIPE)
    print(result.stdout.decode())


# Ping: Send a ping request to a host
def ping_host(host):
    result = subprocess.run(['ping', '-n', '4', host], stdout=subprocess.PIPE)
    print(result.stdout.decode())


# Netstat: Display active network connections
def get_netstat():
    result = subprocess.run(['netstat', '-an'], stdout=subprocess.PIPE)
    print(result.stdout.decode())


# Traceroute -> tracert: Trace the route to a host (Windows)
def trace_route(host):
    result = subprocess.run(['tracert', host], stdout=subprocess.PIPE)
    print(result.stdout.decode())


# Example usage:
if __name__ == "__main__":
    get_ifconfig()
    ping_host("google.com")
    get_netstat()
    trace_route("google.com")
