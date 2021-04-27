# Zuri Random Blog

The Zuri Random Blog is an open blog where everyone can create an account, login and start posting articles on the blog or commenting on other people's articles.

## Getting Started

To get started, you need python, django and the other dependencies in the requirements.txt file installed on your machine. To install all the dependencies after cloning the repo, you can run 

> pip install

Once the dependencies are installed, you need to make migrations by running

> python manage.py makemigrations
> python manage.py migrate

After running the migrations, you can then run the server by running

> python manage.py runserver

To see the app in production, visit [Zuri Random Blog Site](https://zurirandomblog.herokuapp.com/)
