#!/bin/bash

echo "Migrating db"
/opt/sfm-ui/sfm/manage.py migrate --noinput

echo "Collecting static files"
/opt/sfm-ui/sfm/manage.py collectstatic --noinput

if [ $LOAD_FIXTURES = "True" ]; then
    echo "Loading fixtures"
    /opt/sfm-ui/sfm/manage.py loaddata /opt/sfm-setup/fixtures.json
fi

echo "Creating social apps"
/opt/sfm-ui/sfm/manage.py addsocialapp twitter ${TWITTER_CONSUMER_KEY} ${TWITTER_CONSUMER_SECRET}
/opt/sfm-ui/sfm/manage.py addsocialapp tumblr ${TUMBLR_CONSUMER_KEY} ${TUMBLR_CONSUMER_SECRET}
/opt/sfm-ui/sfm/manage.py addsocialapp weibo ${WEIBO_API_KEY} ${WEIBO_API_SECRET}
/opt/sfm-ui/sfm/manage.py addsocialapp instagram ${INSTAGRAM_CONSUMER_KEY} ${INSTAGRAM_CONSUMER_SECRET}
