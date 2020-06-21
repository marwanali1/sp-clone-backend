FROM python:3.7

COPY . /sp-clone-backend

ENV PATH /sp-clone-backend/.bin:$PATH

WORKDIR /sp-clone-backend

RUN pip3 install pipenv
RUN pipenv install

CMD ["pipenv", "run", "flask", "run", "-h", "0.0.0.0", "-p", "5000"]