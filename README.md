# tornado_multiple_applications_boilerplate

## Development

Copy tools/.env.sample to .env and replace settings within it.

Then run the server

    pip install -r requirements.txt
    python -m example.server


## Deploy

Build package
    
    python setup.py sdist

Install the package on destination.
Then run it with supervisord(or other process manager) with proper environment variables.

    pip install example-x.x.x.tar.gz
    DEBUG=False DATABASE_URL=your_database_url python -m example.server
