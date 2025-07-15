FROM python:3.11-slim

# Install dev + network tools
RUN apt update && apt install -y \
    git vim curl \
    iputils-ping net-tools tcpdump nmap \
    build-essential libpcap-dev \
    && apt clean

# Install Python hacking libraries
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /bhp
CMD ["bash"]

