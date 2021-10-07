FROM python:3.9.5

# set up location of code
WORKDIR /code
ENV PYTHONPATH=/code/src

# install python requirements
ADD ./containers/pipelinerunner/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Install cron
RUN apt-get update && apt-get -y install cron

# Copy crontab file to the cron.d directory
COPY scheduler/crontab /etc/cron.d/crontab

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/crontab

# Apply cron job
RUN crontab /etc/cron.d/crontab

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log