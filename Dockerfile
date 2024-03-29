FROM ubuntu:20.04

### add a non-root user
RUN apt update -y && apt install sudo && apt-get upgrade -y
ARG USERNAME=sigma_chan && GROUPNAME=user && UID=1000 && GID=1000 
ARG PASSWD=$USERNAME && HOME=/home/$USERNAME

RUN groupadd -g $GID $GROUPNAME && \
    useradd -m -s /bin/bash -u $UID -g $GID -G sudo $USERNAME && \
    echo $USERNAME:$PASSWD | chpasswd && \
    echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER $USERNAME
WORKDIR $HOME

### install python
RUN sudo apt install --no-install-recommends -y python3.8 python3-pip python3.8-dev

### install mysql client
RUN sudo apt install --no-install-recommends -y default-libmysqlclient-dev

### install poetry
RUN sudo apt install --no-install-recommends -y curl && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
ENV PATH $HOME/.poetry/bin:$PATH


### install python modules
COPY . $HOME
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

### Add uvicorn path
ENV PATH $HOME/.local/bin:$PATH

### something server

#CMD ["uvicorn", "time_series:app", "--reload", "--host", "0.0.0.0", "--port", "80"]