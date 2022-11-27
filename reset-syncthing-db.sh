#!/bin/bash

URL="${3:-http://localhost:8384}"
set -ex

curl -k -X POST -H "X-API-Key: $2" "$URL/rest/system/reset?folder=$1"
