mkdir Flask-Docker-App

cd Flask-Docker-App

python3 -m venv venv

. venv/bin/activate

pip3 install Flask

pip3 install pyopenssl

touch app.py Dockerfile

pip3 freeze > requirements.txt

pip3 uninstall pkg-resources==0.0.0

docker build --tag hack-sphere .

sudo docker run --network=host -d -v /var/run/docker.sock:/var/run/docker.sock -p 5000:5000 hack-sphere
