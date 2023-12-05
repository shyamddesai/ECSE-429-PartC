coverage run -m unittest
coverage xml

/home/user/Downloads/sonar-scanner-5.0.1.3006-linux/bin/sonar-scanner   -Dsonar.projectKey=Python-project   -Dsonar.sources=.   -Dsonar.host.url=http://localhost:9000   -Dsonar.token=sqp_3ec6fbfe4856732446cc6c50c09b3292dc185a08 -Dsonar.python.coverage.reportPaths=coverage.xml