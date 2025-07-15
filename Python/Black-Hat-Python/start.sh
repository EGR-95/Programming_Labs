#!/bin/bash

docker run -it --rm \
  --net=host \
  --cap-add=NET_ADMIN \
  -v $(pwd):/bhp \
  --name bhp-lab \
  bhp-lab

