import yaml

with open('/var/www/cptmorgan.com/movierank/movierank_conf.yml', 'r') as config_fh:
    opts = yaml.load(config_fh)
