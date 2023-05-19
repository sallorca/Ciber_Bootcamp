FROM debian:bullseye

# Instalar paquetes necesarios
RUN apt-get update -y
RUN apt-get install nginx openssh-server tor vim -y

COPY sshd_config /etc/ssh/sshd_config

COPY torrc /etc/tor/torrc
COPY index.html /var/www/html/index.html
COPY nginx.conf /etc/nginx/nginx.conf

COPY service_init.sh .
RUN set -x -e && chmod +x service_init.sh && \
    useradd -m sallorca && \
    echo "sallorca:password" | chpasswd
USER sallorca
RUN set -x -e && mkdir -p /home/sallorca/.ssh && \
        chmod 0700 /home/sallorca/.ssh
COPY --chown=sallorca:sallorca --chmod=0600 authorized_keys /home/sallorca/.ssh
USER root
RUN groupadd sshusers

EXPOSE 4242
EXPOSE 80

CMD sh -c "service nginx start && service ssh start && tor"