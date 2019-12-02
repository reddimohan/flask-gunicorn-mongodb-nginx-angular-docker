# import multiprocessing

pidfile = 'flask_app.pid'
workers = 2
# workers = multiprocessing.cpu_count() * 2 + 1
bind = '0.0.0.0:5000'
accesslog = './logs/access.log'
errorlog = './logs/error.log'
# user = 'ubuntu'
# group = 'ubuntu'
