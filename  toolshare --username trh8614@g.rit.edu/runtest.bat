echo "Running toolshare Tester Simulator"
echo "SWEN-261"
echo "Bradely Conn"

echo "Testing toolmanager and userextra apps"
py manage.py test
python manage.py test
python3 manage.py test

echo "Testing registration app (third party)"
py manage.py test registration.forms
python manage.py test registration.forms
python3 manage.py test registration.forms

echo "Closing in 10 seconds."
timeout /t 10