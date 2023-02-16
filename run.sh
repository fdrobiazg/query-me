docker build -t query-me:v1 .
docker run --rm -d --network host query-me:v1