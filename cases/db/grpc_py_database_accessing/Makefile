
proto:
	python3 -m grpc_tools.protoc -I ./api/proto/ --python_out=./api/grpc/ --pyi_out=./api/grpc/ --grpc_python_out=./api/grpc/ ./api/proto/database.proto

run:
	python3 client.py -host=0.0.0.0:8080

git:
	git add .
	git commit -m "$(COMMIT)"
	git push