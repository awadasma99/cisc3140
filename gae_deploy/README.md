To deploy manually to Google App Engine: `gcloud app deploy app.yaml`

the `cloudbuild.yml` file is for automating deploy with Cloud Build after pushing to Github, assuming all the other dependencies have been set up.

Note that GAE looks for a main.py file, so if that's where you deploy to you'll have to ensure your architecture supports that.

Don't forget to include a `requirements.txt` file since it tells GAE which python libraries to install for you.
