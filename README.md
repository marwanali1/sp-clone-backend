# sp-clone
Backend code for music streaming app clone

### Setting up the app locally

Clone the repo: `https://github.com/marwanali1/sp-clone-backend.git`

Change into the repo: `cd sp-clone-backend`

Create a virtual environment and install project dependencies: `pipenv install`

Activate the virtual environment: `pipenv shell`

Run the app: `flask run`

#### Loading database locally
`flask db init`  
`flask db migrate`  
`flask db upgrade`

#### Docker

Create docker image of the app: `docker build -t sp-clone-backend:latest .`  

Run docker container with the image: `docker run -d -p 5000:5000 --rm sp-clone-backend:latest`