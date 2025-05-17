# Instructions to run:

1. Clone git repo with:
```
git clone git@github.com:sanilb19/fetch-receipt-processor.git
```



2. In the cloned repo, run
```
echo "PORT=8000" > .env
```
_you may set any available port number here, 8000 as default_



3. With Docker and Make installed, run 
```
make build
```
or manually:

```
docker build -t receipt-app
```




4. Run the container with
```
make run
```
or manually:
```
docker run -d -p $(PORT):$(PORT) -e PORT=$(PORT) --name receipt-container receipt-app
```



5. Navigate to http://localhost:8000 (using the same port number as chosen in step 2) to see the swagger API UI

  

6. (optional) run ```make test``` or ```pytest /tests``` in local terminal to run basic end-to-end tests

7. Run ``` make clean ``` to destroy the container and service





