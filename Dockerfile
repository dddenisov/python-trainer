FROM python:3.9

COPY requirements.txt ./requirements.txt
COPY setup.cfg ./setup.cfg
COPY setup.py ./setup.py
COPY project/app.py ./project/app.py
COPY tests/conftest.py ./tests/conftest.py
COPY tests/test_route.py ./tests/test_route.py
COPY run.sh ./run.sh

RUN pip install -r requirements.txt
RUN pip install -e .

CMD ["/bin/bash", "run.sh"]