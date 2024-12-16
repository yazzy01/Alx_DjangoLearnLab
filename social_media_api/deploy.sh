#!/bin/bash
# deploy.sh

# Activate virtual environment
source /path/to/your/venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Apply migrations
python manage.py migrate

# Restart Gunicorn
sudo systemctl restart gunicorn
