#Dockerfile
# #############################################################################
#
# Build image:
# >> docker build -t .
#
# Run container:
# >> docker run -it -p 2517:2517  --name yarn_exporter <images name>
###############################################################################
FROM  centos:centos7
LABEL maintainer="Armadik"

COPY requirements.txt /tmp/
# COPPY yarn_exporter-0.0.1-py3-none-any.whl
COPY dist /tmp/
# if SSL error
COPY pip.conf /etc/

# krb5 packages
RUN yum install -y gcc python3-devel krb5-devel krb5-workstation python3-devel python3-pip && \
        yum clean all

RUN pip3 install --upgrade pip
RUN pip3 install -r /tmp/requirements.txt
RUN pip3 install /tmp/*.whl

EXPOSE 2517

ENTRYPOINT ["python3"]
CMD ["-m", "yarn_exporter"]